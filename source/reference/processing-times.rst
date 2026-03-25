Processing Times
================

Estimated response times by input type and mode.

.. list-table::
   :header-rows: 1
   :widths: 35 30 35

   * - Input Type
     - SAST Mode
     - DAST Mode
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
   * - Rule-based only (``/api/scan/rules``)
     - 2--30 seconds
     - --
   * - Fix generation
     - 10--30 seconds per file
     - --
   * - Follow-up Q&A
     - 5--15 seconds per question
     - --

Benchmark Environment
---------------------

The response times above were measured on Google Cloud Run instances configured with
2 vCPUs / 2 GB memory in the us-central1 region, with a container concurrency of 40,
a maximum of 5 instances, and Claude claude-opus-4-6 as the backend model via Anthropic Vertex AI.

**Expected improvements with higher-spec configurations:**

With higher-spec instances (4+ vCPUs / 8 GB+ memory) and increased parallelism
(max instances scaled to 20+, concurrency raised to 80+), processing times are expected
to improve by approximately 40--60% for project-level scans and batch file analysis,
while snippet scan and follow-up Q&A latency — dominated by LLM inference — would remain
largely unchanged.

.. list-table::
   :header-rows: 1
   :widths: 35 30 35

   * - Input Type
     - Current (2 vCPU / 2 GB)
     - Estimated (4+ vCPU / 8 GB+, 20+ instances)
   * - Project archive (SAST)
     - 3--10 minutes
     - 1--4 minutes
   * - Project archive (DAST)
     - 1--5 hours
     - 30 min -- 2 hours
   * - Multiple files (up to 10)
     - 30 sec -- 3 min
     - 15 sec -- 1 min
   * - Code snippet
     - 2--10 seconds
     - 2--10 seconds (LLM-bound)
   * - Fix generation
     - 10--30 seconds
     - 10--30 seconds (LLM-bound)

Key Takeaways
-------------

- **SAST mode** responds in seconds to minutes, making it ideal for CI/CD pipelines and
  developer workflows.
- **DAST mode** is available only for project-level scans and provides deeper analysis. It
  may take hours on large projects.
- Both modes call LLM APIs. Processing time depends on code size and complexity.
- **Fix generation** and **follow-up Q&A** respond within seconds regardless of mode.

Async Recommendations
---------------------

For **DAST mode** scans on large projects:

- Implement client-side polling with exponential backoff.
- Set reasonable timeouts (e.g., 6 hours for very large codebases).
- Consider running DAST scans as scheduled jobs rather than blocking CI/CD pipelines.
