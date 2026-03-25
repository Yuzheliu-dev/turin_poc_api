Scan Project
============

.. http:post:: /api/scan/project

   Upload and scan a project archive (.zip). RAVEN automatically selects key source files
   for analysis. Supports both **SAST** and **DAST** modes.

   **Processing time:** SAST: 3--10 minutes. DAST: 1--5 hours (large projects).

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
   * - ``archive``
     - file
     - Yes
     - Project archive (.zip, max 25 MB)
   * - ``mode``
     - string
     - No
     - ``"sast"`` or ``"dast"`` (default: ``"sast"``)

**Example (cURL):**

.. code-block:: bash

   curl -X POST $RAVEN_BASE_URL/api/scan/project \
     -H "X-API-Key: $RAVEN_API_KEY" \
     -F "archive=@my-project.zip" \
     -F "mode=sast"

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
   * - ``project``
     - string
     - Name of the uploaded archive
   * - ``mode``
     - string
     - The scan mode used (``"sast"`` or ``"dast"``)
   * - ``results``
     - array
     - Array of per-file scan results (same structure as :doc:`scan-files`)
   * - ``selection_meta``
     - object
     - Metadata about file selection

**selection_meta object:**

.. list-table::
   :header-rows: 1
   :widths: 25 12 63

   * - Field
     - Type
     - Description
   * - ``candidate_count``
     - integer
     - Total source files found in the archive
   * - ``selected_count``
     - integer
     - Number of files selected for scanning (max 30)

**Example response:**

.. code-block:: json

   {
     "status": "completed",
     "project": "my-project.zip",
     "mode": "sast",
     "results": [
       {
         "filename": "src/parser.c",
         "verdict": "vulnerable",
         "vulnerable_lines": [{ "start": 33, "end": 45 }],
         "importance": "critical"
       }
     ],
     "selection_meta": {
       "candidate_count": 87,
       "selected_count": 15
     }
   }

.. note::

   **DAST mode** performs deeper semantic analysis and may take 1--5 hours for large
   projects. For DAST scans, consider implementing asynchronous polling on the client side.
