CI/CD Integration
=================

RAVEN can be integrated into CI/CD pipelines to automatically scan code for vulnerabilities
before merging or deploying.

GitHub Actions
--------------

Add a RAVEN security scan step to your GitHub Actions workflow:

.. code-block:: yaml

   name: Security Scan
   on:
     pull_request:
       branches: [main]

   jobs:
     raven-scan:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4

         - name: Create project archive
           run: zip -r project.zip src/ -x "*.git*"

         - name: Run RAVEN scan
           env:
             RAVEN_API_KEY: ${{ secrets.RAVEN_API_KEY }}
           run: |
             RESPONSE=$(curl -s -w "\n%{http_code}" \
               -X POST $RAVEN_BASE_URL/api/scan/project \
               -H "X-API-Key: $RAVEN_API_KEY" \
               -F "archive=@project.zip" \
               -F "mode=basic")

             HTTP_CODE=$(echo "$RESPONSE" | tail -1)
             BODY=$(echo "$RESPONSE" | head -n -1)

             if [ "$HTTP_CODE" != "200" ]; then
               echo "RAVEN API returned HTTP $HTTP_CODE"
               exit 1
             fi

             # Check for critical/high severity findings
             CRITICAL=$(echo "$BODY" | jq '[.results[] | select(.importance == "critical" or .importance == "high")] | length')
             if [ "$CRITICAL" -gt 0 ]; then
               echo "Found $CRITICAL critical/high vulnerabilities"
               echo "$BODY" | jq '.results[] | select(.importance == "critical" or .importance == "high")'
               exit 1
             fi

             echo "No critical/high vulnerabilities found"

GitLab CI
---------

.. code-block:: yaml

   raven-scan:
     stage: test
     image: curlimages/curl:latest
     script:
       - apk add --no-cache jq zip
       - zip -r project.zip src/ -x "*.git*"
       - |
         RESPONSE=$(curl -s \
           -X POST $RAVEN_BASE_URL/api/scan/project \
           -H "X-API-Key: $RAVEN_API_KEY" \
           -F "archive=@project.zip" \
           -F "mode=basic")
         CRITICAL=$(echo "$RESPONSE" | jq '[.results[] | select(.importance == "critical" or .importance == "high")] | length')
         if [ "$CRITICAL" -gt 0 ]; then
           echo "Blocked: $CRITICAL critical/high vulnerabilities found"
           exit 1
         fi
     rules:
       - if: $CI_MERGE_REQUEST_ID

Best Practices
--------------

- **Block on critical/high only.** Allow medium and low findings to pass but report them.
- **Use Basic mode in CI/CD.** It completes in minutes, suitable for PR checks.
- **Reserve Pro mode** for scheduled nightly scans or release gates where longer processing
  is acceptable.
- **Cache results** by commit hash to avoid re-scanning unchanged code.
- **Store the API key** as a CI/CD secret, never in the repository.
