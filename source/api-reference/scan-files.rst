Scan Files
==========

.. http:post:: /api/scan/files

   Upload and scan multiple source files using **Basic** mode.

   **Processing time:** 5--30 seconds per file (files are scanned concurrently).

Request
-------

Send a ``multipart/form-data`` request with the following fields:

.. list-table::
   :header-rows: 1
   :widths: 15 12 10 63

   * - Field
     - Type
     - Required
     - Description
   * - ``files``
     - file[]
     - Yes
     - One or more source files to scan
   * - ``language``
     - string
     - No
     - ``"c"``, ``"cpp"``, ``"cxx"``, ``"java"``, or ``"auto"`` (default: ``"auto"``)

**Example (cURL):**

.. code-block:: bash

   curl -X POST $RAVEN_BASE_URL/api/scan/files \
     -H "X-API-Key: $RAVEN_API_KEY" \
     -F "files=@buffer.c" \
     -F "files=@utils.c" \
     -F "language=c"

Response
--------

Returns a per-file results array. Each element has the same structure as the
:doc:`scan-snippet` response.

.. list-table::
   :header-rows: 1
   :widths: 20 12 68

   * - Field
     - Type
     - Description
   * - ``status``
     - string
     - ``"completed"`` or ``"failed"``
   * - ``results``
     - array
     - Array of per-file scan results

Each result object:

.. list-table::
   :header-rows: 1
   :widths: 20 12 68

   * - Field
     - Type
     - Description
   * - ``filename``
     - string
     - Name of the scanned file
   * - ``verdict``
     - string
     - ``"vulnerable"`` or ``"safe"``
   * - ``vulnerable_lines``
     - array
     - List of objects with ``start`` and ``end`` line numbers
   * - ``importance``
     - string
     - ``"critical"``, ``"high"``, ``"medium"``, or ``"low"``

**Example response:**

.. code-block:: json

   {
     "status": "completed",
     "results": [
       {
         "filename": "buffer.c",
         "verdict": "vulnerable",
         "vulnerable_lines": [{ "start": 12, "end": 12 }],
         "importance": "high"
       },
       {
         "filename": "utils.c",
         "verdict": "safe",
         "vulnerable_lines": [],
         "importance": "low"
       }
     ]
   }
