Authentication
==============

All RAVEN API endpoints (except ``/api/healthz``) require authentication via an API key.

Obtaining an API Key
--------------------

Contact the AI4Secure team to receive your API key. Each key is associated with a specific
organization and rate limit tier.

Using Your API Key
------------------

Include your API key in the ``X-API-Key`` header of every request:

.. code-block:: text

   X-API-Key: YOUR_API_KEY

Example
^^^^^^^

.. code-block:: bash

   curl -X POST $RAVEN_BASE_URL/api/scan/snippet \
     -H "Content-Type: application/json" \
     -H "X-API-Key: YOUR_API_KEY" \
     -d '{"code": "int main() { char buf[10]; gets(buf); }", "language": "c"}'

If the key is missing or invalid, the API returns ``401 Unauthorized``.

Rate Limiting
-------------

Requests are rate-limited per API key. When you exceed the limit, the API returns
``429 Too Many Requests``.

Rate limit information is included in response headers:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Header
     - Description
   * - ``X-RateLimit-Limit``
     - Maximum requests allowed per window
   * - ``X-RateLimit-Remaining``
     - Remaining requests in the current window
   * - ``X-RateLimit-Reset``
     - Unix timestamp when the window resets

Security Best Practices
-----------------------

- **Use environment variables** to store your API key. Never hard-code it in source files.

  .. code-block:: bash

     export RAVEN_API_KEY="your-key-here"

- **Do not commit** your API key to version control. Add it to ``.gitignore`` or use a
  secrets manager.
- **Rotate keys regularly** and revoke any compromised keys immediately.
- **Use HTTPS only.** All API traffic must be encrypted in transit.
