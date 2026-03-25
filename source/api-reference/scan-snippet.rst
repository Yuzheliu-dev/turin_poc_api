Scan Snippet
============

.. http:post:: /api/scan/snippet

   Scan a code snippet for vulnerabilities using **SAST** mode.

   **Processing time:** 2--10 seconds.

Request
-------

Send a JSON body with the source code and language.

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
     - Source code to scan (max 200 KB)
   * - ``language``
     - string
     - Yes
     - ``"c"``, ``"cpp"``, ``"cxx"``, ``"java"``, ``"python"``, ``"go"``, ``"javascript"``, ``"typescript"``, or ``"auto"``

**Example request body:**

.. code-block:: json

   {
     "code": "#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}",
     "language": "c"
   }

Response
--------

.. list-table::
   :header-rows: 1
   :widths: 20 12 68

   * - Field
     - Type
     - Description
   * - ``request_id``
     - string
     - Unique identifier for this scan request (UUID)
   * - ``elapsed_ms``
     - integer
     - Processing time in milliseconds
   * - ``status``
     - string
     - ``"completed"`` or ``"failed"``
   * - ``verdict``
     - string
     - ``"vulnerable"`` or ``"safe"``
   * - ``vulnerable_lines``
     - array
     - List of objects with ``start`` and ``end`` line numbers
   * - ``importance``
     - string
     - Severity: ``"critical"``, ``"high"``, ``"medium"``, or ``"low"``

**Example response:**

.. code-block:: json

   {
     "request_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
     "elapsed_ms": 4523,
     "status": "completed",
     "verdict": "vulnerable",
     "vulnerable_lines": [{ "start": 4, "end": 4 }],
     "importance": "high"
   }
