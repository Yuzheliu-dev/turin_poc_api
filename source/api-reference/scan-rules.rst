Scan Rules (Rule-Based Only)
============================

.. http:post:: /api/scan/rules

   Run a rule-based static analysis scan **without** LLM reasoning.
   Returns raw findings from the built-in rule engine. This is useful when you need fast,
   deterministic results or want to feed rule-based findings into your own pipeline.

   **Processing time:** 2--30 seconds depending on input size and rule set.

Request
-------

Send a ``multipart/form-data`` or JSON request.

**Option A — Scan a code snippet (JSON):**

.. list-table::
   :header-rows: 1
   :widths: 15 10 10 65

   * - Field
     - Type
     - Required
     - Description
   * - ``code``
     - string
     - Yes (if no ``files``/``archive``)
     - Source code to scan
   * - ``language``
     - string
     - No
     - Language hint (default: ``"auto"``)
   * - ``rules``
     - string
     - No
     - Rule set to use: ``"auto"``, ``"security"``, ``"owasp-top-10"``, etc. (default: ``"auto"``)

**Option B — Scan files or a project archive (multipart):**

.. list-table::
   :header-rows: 1
   :widths: 15 10 10 65

   * - Field
     - Type
     - Required
     - Description
   * - ``files``
     - file[]
     - Yes (if no ``code``/``archive``)
     - Source files to scan
   * - ``archive``
     - file
     - Yes (if no ``code``/``files``)
     - Project archive (.zip, max 25 MB)
   * - ``rules``
     - string
     - No
     - Rule set (default: ``"auto"``)

**Example request (snippet):**

.. code-block:: json

   {
     "code": "#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}",
     "language": "c",
     "rules": "auto"
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
     - ``"completed"`` or ``"failed"``
   * - ``findings``
     - array
     - List of rule-based findings

**findings item:**

.. list-table::
   :header-rows: 1
   :widths: 20 12 68

   * - Field
     - Type
     - Description
   * - ``rule_id``
     - string
     - Rule identifier (e.g., ``"CWE-120"``, ``"insecure-use-gets-fn"``)
   * - ``message``
     - string
     - Description of the finding
   * - ``severity``
     - string
     - ``"ERROR"``, ``"WARNING"``, or ``"INFO"``
   * - ``file``
     - string
     - File path (or ``"<snippet>"`` for code snippets)
   * - ``line_start``
     - integer
     - Start line number
   * - ``line_end``
     - integer
     - End line number

**Example response:**

.. code-block:: json

   {
     "status": "completed",
     "findings": [
       {
         "rule_id": "insecure-use-gets-fn",
         "message": "Use of insecure function gets(). Use fgets() instead.",
         "severity": "ERROR",
         "file": "<snippet>",
         "line_start": 4,
         "line_end": 4
       }
     ]
   }

.. note::

   This endpoint does **not** call any LLM API. Results are purely rule-based and
   deterministic. For LLM-assisted analysis with triage and explanation, use the
   ``/api/scan/snippet``, ``/api/scan/files``, or ``/api/scan/project`` endpoints instead.
