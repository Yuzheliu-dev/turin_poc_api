Artemis Integration
===================

RAVEN is designed as a security layer within the Artemis code optimization pipeline.

Integration Modes
-----------------

1. Post-Optimization Scan
^^^^^^^^^^^^^^^^^^^^^^^^^

After Artemis completes code optimization, automatically invoke RAVEN's **Basic** mode to
verify that no vulnerabilities were introduced. This adds only seconds of latency and
provides immediate security assurance.

2. CI/CD Security Gate
^^^^^^^^^^^^^^^^^^^^^^

Add a RAVEN quality gate to Artemis-managed CI/CD pipelines. Block merges when critical
or high-severity vulnerabilities are detected. See :doc:`cicd` for pipeline examples.

3. Interactive Remediation Loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When vulnerabilities are found, RAVEN generates fix suggestions. Artemis can then further
optimize the fixed code, forming a "secure and performant" feedback loop:

.. code-block:: text

   Original Code
     -> Artemis optimizes
     -> RAVEN scans (finds vulnerability)
     -> RAVEN generates fix
     -> Artemis optimizes the fix
     -> RAVEN verifies (safe)
     -> Deploy

4. IDE Integration
^^^^^^^^^^^^^^^^^^

Through the Artemis Navigator (VS Code extension), provide real-time security feedback
during development.

What RAVEN Provides
-------------------

- REST API-based vulnerability detection (Basic / Pro modes), fix generation, and
  interactive Q&A
- Support for code snippets, files, and project-level input
- Cloud deployment -- access via API Key, no local tooling required

What TurinTech Needs to Provide
--------------------------------

- **Hook points:** Locations in the Artemis pipeline where security scans can be inserted
- **API documentation:** Artemis Navigator extension interface documentation (for IDE-level integration)
- **Test samples:** Before/after code pairs from Artemis optimization, for verifying that security is not degraded
- **PoC scope agreement:** Evaluation criteria and timeline
