Scan Modes
==========

RAVEN offers two scan modes, both powered by large language models.

Basic Mode
----------

- **Speed:** Seconds to minutes
- **Availability:** All scan endpoints (snippet, files, project)
- **Best for:** CI/CD pipelines, developer workflows, quick feedback

Basic mode provides fast LLM-driven vulnerability detection. It analyzes code with
sufficient context to identify common vulnerability patterns and is suitable for
iterative development.

Pro Mode
--------

- **Speed:** Minutes to hours
- **Availability:** Project-level scans only (``/api/scan/project``)
- **Best for:** Release gates, security audits, deep analysis

Pro mode uses deeper semantic analysis with a larger context window and stronger
reasoning capabilities. It can detect complex, multi-file vulnerability patterns that
Basic mode might miss.

Comparison
----------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Feature
     - Basic
     - Pro
   * - Analysis depth
     - Pattern-level
     - Semantic-level
   * - Context scope
     - Single file
     - Cross-file
   * - Snippet scan
     - Yes
     - No
   * - File scan
     - Yes
     - No
   * - Project scan
     - Yes
     - Yes
   * - Typical speed
     - Seconds to minutes
     - Minutes to hours
   * - CI/CD suitability
     - Excellent
     - Scheduled/nightly only

When to Use Each
----------------

- Use **Basic** for pull request checks, real-time IDE feedback, and any workflow that
  needs results in under 10 minutes.
- Use **Pro** for pre-release security audits, compliance scans, and deep analysis of
  critical codebases where thoroughness is more important than speed.

.. note::

   Both modes call external LLM APIs (Anthropic, Google, OpenAI). The system automatically
   selects the best model for each task.
