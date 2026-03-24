Configuration Limits
====================

The following limits apply to RAVEN API requests.

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Parameter
     - Limit
   * - Maximum code snippet size
     - 200 KB
   * - Maximum request body size
     - 2 MB
   * - Maximum project archive size
     - 25 MB
   * - Maximum files in archive
     - 5,000
   * - Maximum files scanned per project
     - 30
   * - Follow-up conversation history
     - 6 rounds (most recent)

.. note::

   If your project archive exceeds the limits, consider splitting it into smaller archives
   or using the file upload endpoint (``/api/scan/files``) for individual files.
