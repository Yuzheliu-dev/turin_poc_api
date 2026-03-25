Platform Integration
====================

RAVEN can be integrated into web platforms, development tools, and existing workflows
via its REST API.

Web Platform Integration
------------------------

Embed RAVEN scanning into your web-based code review or project management platform:

1. **On-demand scan:** Call ``/api/scan/snippet`` or ``/api/scan/files`` when a user
   submits code for review. Display results inline with the source code.

2. **Project-level scan:** Upload a project archive via ``/api/scan/project`` to run
   a full SAST or DAST scan. Poll for results and display a summary dashboard.

3. **Auto-fix suggestions:** When vulnerabilities are found, call ``/api/fix`` to
   generate fix suggestions. Present the diff to the user for one-click application.

4. **Interactive Q&A:** Use ``/api/followup`` to let users ask questions about scan
   findings directly within the platform UI.

GitHub Integration
------------------

Integrate RAVEN into GitHub workflows:

1. **Pull request checks:** Use GitHub Actions to run RAVEN scans on every PR.
   See :doc:`cicd` for workflow examples.

2. **Status checks:** Report scan results as GitHub commit statuses or check runs.
   Block merges when critical or high-severity vulnerabilities are detected.

3. **PR comments:** Post scan results as PR comments with inline annotations
   pointing to vulnerable lines.

What RAVEN Provides
-------------------

- REST API-based vulnerability detection (SAST / DAST modes), fix generation, and
  interactive Q&A
- Rule-based scanning via ``/api/scan/rules`` for fast, deterministic results
- Support for code snippets, files, and project-level input
- Cloud deployment -- access via API Key, no local tooling required
