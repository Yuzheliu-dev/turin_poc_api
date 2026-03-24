Error Codes
===========

RAVEN uses standard HTTP status codes to indicate the result of API requests.

HTTP Status Codes
-----------------

.. list-table::
   :header-rows: 1
   :widths: 15 25 60

   * - Code
     - Status
     - Description
   * - ``200``
     - OK
     - Request completed successfully
   * - ``400``
     - Bad Request
     - Input format is incorrect or parameters are invalid
   * - ``401``
     - Unauthorized
     - Missing or invalid API key
   * - ``413``
     - Payload Too Large
     - Request body exceeds the size limit
   * - ``422``
     - Unprocessable Entity
     - Required fields are missing or contain invalid values
   * - ``429``
     - Too Many Requests
     - Rate limit exceeded or async queue is full
   * - ``500``
     - Internal Server Error
     - An unexpected error occurred on the server

Error Response Format
---------------------

Error responses include a JSON body with details:

.. code-block:: json

   {
     "status": "error",
     "error": {
       "code": 422,
       "message": "Field 'language' is required",
       "details": "Supported values: c, cpp, cxx, java"
     }
   }

Common Error Scenarios
----------------------

**Missing required field:**

.. code-block:: json

   {
     "status": "error",
     "error": {
       "code": 422,
       "message": "Field 'code' is required"
     }
   }

**Unsupported language:**

.. code-block:: json

   {
     "status": "error",
     "error": {
       "code": 400,
       "message": "Unsupported language: 'rust'. Supported: c, cpp, cxx, java"
     }
   }

**Code snippet too large:**

.. code-block:: json

   {
     "status": "error",
     "error": {
       "code": 413,
       "message": "Code snippet exceeds maximum size of 200 KB"
     }
   }

**Rate limit exceeded:**

.. code-block:: json

   {
     "status": "error",
     "error": {
       "code": 429,
       "message": "Rate limit exceeded. Retry after 60 seconds."
     }
   }
