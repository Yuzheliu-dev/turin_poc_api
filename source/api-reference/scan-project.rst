Scan Project
============

.. http:post:: /api/scan/project

   Upload and scan a project archive (.zip). RAVEN automatically selects key source files
   for analysis. Supports both **Basic** and **Pro** modes.

   **Processing time:** Basic: 3--10 minutes. Pro: 1--5 hours (large projects).

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
     - ``"basic"`` or ``"pro"`` (default: ``"basic"``)

**Example (cURL):**

.. code-block:: bash

   curl -X POST $RAVEN_BASE_URL/api/scan/project \
     -H "X-API-Key: $RAVEN_API_KEY" \
     -F "archive=@my-project.zip" \
     -F "mode=basic"

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
     - The scan mode used (``"basic"`` or ``"pro"``)
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
     "mode": "basic",
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

   **Pro mode** performs deeper semantic analysis and may take 1--5 hours for large
   projects. For Pro scans, consider implementing asynchronous polling on the client side.
