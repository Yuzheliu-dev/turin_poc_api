API Reference
=============

Base URL
--------

All API requests should be sent to:

.. code-block:: text

   https://api.raven.ai4secure.com

Content Types
-------------

- **JSON endpoints** (``/api/scan/snippet``, ``/api/fix``, ``/api/followup``):
  Use ``Content-Type: application/json``.
- **File upload endpoints** (``/api/scan/files``, ``/api/scan/project``):
  Use ``Content-Type: multipart/form-data``.

Authentication
--------------

All endpoints except ``/api/healthz`` require the ``X-API-Key`` header.
See :doc:`/authentication` for details.

Endpoints
---------

.. toctree::
   :maxdepth: 1

   scan-snippet
   scan-files
   scan-project
   fix
   followup
   healthz
