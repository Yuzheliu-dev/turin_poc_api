Overview
========

**RAVEN** (Reasoning Agent for Vulnerability ExaminatioN) is an AI-driven platform for
automated code vulnerability detection and remediation. It analyzes source code to identify
security vulnerabilities, generates actionable fix suggestions, and supports interactive Q&A
on scan results.

Supported Languages
-------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Language
     - Status
   * - C
     - Supported
   * - C++
     - Supported
   * - Java
     - Supported
   * - Python, Go, TypeScript
     - On roadmap

Scan Modes
----------

RAVEN offers two scan modes:

.. list-table::
   :header-rows: 1
   :widths: 15 45 20 20

   * - Mode
     - Description
     - Speed
     - Availability
   * - **Basic** (``"basic"``)
     - LLM-powered fast vulnerability detection, suitable for code snippets, files, and general project scans
     - Seconds to minutes
     - All scan endpoints
   * - **Pro** (``"pro"``)
     - LLM-powered deep semantic analysis with larger context and stronger reasoning capabilities
     - Minutes to hours
     - Project-level scans only

Both modes use large language models (LLMs) for analysis. The key differences are analysis
depth, context scope, and processing time.

Endpoint Summary
----------------

.. list-table::
   :header-rows: 1
   :widths: 22 8 30 15 25

   * - Endpoint
     - Method
     - Description
     - Uses AI
     - Typical Response Time
   * - ``/api/scan/snippet``
     - POST
     - Scan a code snippet (Basic)
     - Yes (LLM)
     - 2--10 seconds
   * - ``/api/scan/files``
     - POST
     - Scan uploaded source files (Basic)
     - Yes (LLM)
     - 5--30 seconds per file
   * - ``/api/scan/project``
     - POST
     - Scan a project archive (.zip)
     - Yes (LLM)
     - Basic: 3--10 min; Pro: 1--5 hours
   * - ``/api/fix``
     - POST
     - Generate vulnerability fix suggestions
     - Yes (LLM)
     - 10--30 seconds per file
   * - ``/api/followup``
     - POST
     - Follow-up Q&A on scan results
     - Yes (LLM)
     - 5--15 seconds per question
   * - ``/api/healthz``
     - GET
     - Health check
     - No
     - Instant

Deployment
----------

RAVEN is deployed as a cloud REST API, authenticated via API Key. See
:doc:`authentication` for details on how to authenticate your requests.

**AI API Usage:** RAVEN's core analysis capabilities call large language models, including
models from Anthropic, Google, and OpenAI. The system automatically selects the appropriate
model based on the task. Callers do not need to provide their own API keys.
