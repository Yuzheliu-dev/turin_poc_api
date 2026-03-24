Fix
===

.. http:post:: /api/fix

   Generate AI-driven fix suggestions for detected vulnerabilities. Returns both a
   human-readable fix description and structured output (fixed code + repair metadata).

   **Processing time:** 10--30 seconds per file.

Request
-------

.. list-table::
   :header-rows: 1
   :widths: 15 10 10 65

   * - Field
     - Type
     - Required
     - Description
   * - ``code``
     - string
     - Yes
     - Original source code
   * - ``language``
     - string
     - Yes
     - ``"c"``, ``"cpp"``, ``"cxx"``, or ``"java"``
   * - ``findings``
     - string
     - No
     - Scan findings (plain text or structured JSON)
   * - ``vuln_pairs``
     - array
     - No
     - Structured vulnerability location data from a prior scan

**vuln_pairs item:**

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Field
     - Type
     - Description
   * - ``line``
     - integer
     - Line number of the vulnerability
   * - ``reason``
     - string
     - Description of the vulnerability
   * - ``category``
     - string
     - CWE category (e.g., ``"CWE-120"``)

**Example request body:**

.. code-block:: json

   {
     "code": "#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}",
     "language": "c",
     "findings": "Buffer overflow via gets() at line 4",
     "vuln_pairs": [
       { "line": 4, "reason": "Use of unsafe gets() function", "category": "CWE-120" }
     ]
   }

Response
--------

.. list-table::
   :header-rows: 1
   :widths: 20 12 68

   * - Field
     - Type
     - Description
   * - ``status``
     - string
     - ``"success"`` or ``"failed"``
   * - ``fix_markdown``
     - string
     - Human-readable fix explanation in Markdown format
   * - ``fixed_code``
     - string
     - The complete fixed source code, ready to replace the original file
   * - ``repair_pairs``
     - array
     - Per-line repair metadata (line number + fix reason)
   * - ``model``
     - string
     - Internal model identifier used for generating the fix

**repair_pairs item:**

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Field
     - Type
     - Description
   * - ``line``
     - integer
     - Line number that was modified
   * - ``reason``
     - string
     - Explanation of the fix applied

**Example response:**

.. code-block:: json

   {
     "status": "success",
     "fix_markdown": "## Fix for Buffer Overflow\n\nReplace `gets()` with `fgets()` which accepts a size limit...",
     "fixed_code": "#include <stdio.h>\nint main() {\n  char buf[10];\n  fgets(buf, sizeof(buf), stdin);\n  return 0;\n}",
     "repair_pairs": [
       { "line": 4, "reason": "Replaced gets() with fgets() to prevent buffer overflow" }
     ],
     "model": "raven-fix-v1"
   }
