Health Check
============

.. http:get:: /api/healthz

   Check if the RAVEN API is running and healthy. This endpoint does **not** require
   authentication.

   **Processing time:** Instant.

Request
-------

No request body or parameters required.

.. code-block:: bash

   curl $RAVEN_BASE_URL/api/healthz

Response
--------

.. list-table::
   :header-rows: 1
   :widths: 20 12 68

   * - Field
     - Type
     - Description
   * - ``ok``
     - boolean
     - ``true`` if the service is healthy
   * - ``timestamp``
     - string
     - ISO 8601 timestamp of the health check

**Example response:**

.. code-block:: json

   {
     "ok": true,
     "timestamp": "2026-03-24T12:00:00Z"
   }
