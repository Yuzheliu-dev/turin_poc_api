Processing Times
================

Estimated response times by input type and mode.

.. list-table::
   :header-rows: 1
   :widths: 35 30 35

   * - Input Type
     - Basic Mode
     - Pro Mode
   * - Code snippet (< 1 KB)
     - 2--10 seconds
     - --
   * - Single file
     - 5--30 seconds
     - --
   * - Multiple files (up to 10)
     - 30 seconds -- 3 minutes
     - --
   * - Project archive (.zip)
     - 3--10 minutes
     - 1--5 hours
   * - Fix generation
     - 10--30 seconds per file
     - --
   * - Follow-up Q&A
     - 5--15 seconds per question
     - --

Key Takeaways
-------------

- **Basic mode** responds in seconds to minutes, making it ideal for CI/CD pipelines and
  developer workflows.
- **Pro mode** is available only for project-level scans and provides deeper analysis. It
  may take hours on large projects.
- Both modes call LLM APIs. Processing time depends on code size and complexity.
- **Fix generation** and **follow-up Q&A** respond within seconds regardless of mode.

Async Recommendations
---------------------

For **Pro mode** scans on large projects:

- Implement client-side polling with exponential backoff.
- Set reasonable timeouts (e.g., 6 hours for very large codebases).
- Consider running Pro scans as scheduled jobs rather than blocking CI/CD pipelines.
