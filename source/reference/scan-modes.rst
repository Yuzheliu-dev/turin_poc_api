Scan Modes
==========

RAVEN offers two scan modes.

SAST Mode
---------

- **Speed:** Seconds to minutes
- **Availability:** All scan endpoints (snippet, files, project)
- **Best for:** CI/CD pipelines, developer workflows, quick feedback

SAST mode combines rule-based static analysis with LLM-assisted triage and explanation.
The rule engines perform fast pattern matching across a wide range of languages, while
the LLM layer reduces false positives and provides human-readable vulnerability
descriptions.

DAST Mode
---------

- **Speed:** Minutes to hours
- **Availability:** Project-level scans only (``/api/scan/project``)
- **Best for:** Release gates, security audits, deep analysis

DAST mode uses LLM-powered deep semantic analysis with a larger context window and stronger
reasoning capabilities. It can detect complex, multi-file vulnerability patterns that
SAST mode might miss. Currently supports C/C++ only.

Comparison
----------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Feature
     - SAST
     - DAST
   * - Analysis engine
     - Rule-based + LLM triage
     - LLM-only (deep reasoning)
   * - Analysis depth
     - Pattern-level
     - Semantic-level
   * - Context scope
     - Single file
     - Cross-file
   * - Language support
     - 10+ languages
     - C/C++
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

- Use **SAST** for pull request checks, real-time IDE feedback, and any workflow that
  needs results in under 10 minutes.
- Use **DAST** for pre-release security audits, compliance scans, and deep analysis of
  critical codebases where thoroughness is more important than speed.

.. note::

   Both modes call external LLM APIs (Anthropic, Google, OpenAI) for triage and analysis.
   The system automatically selects the best model for each task.
