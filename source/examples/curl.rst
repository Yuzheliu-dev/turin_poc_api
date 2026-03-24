cURL Examples
=============

All examples assume ``RAVEN_API_KEY`` is set as an environment variable.

Scan a Code Snippet
-------------------

.. code-block:: bash

   curl -X POST https://api.raven.ai4secure.com/api/scan/snippet \
     -H "Content-Type: application/json" \
     -H "X-API-Key: $RAVEN_API_KEY" \
     -d '{
       "code": "#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}",
       "language": "c"
     }'

Scan Uploaded Files
-------------------

.. code-block:: bash

   curl -X POST https://api.raven.ai4secure.com/api/scan/files \
     -H "X-API-Key: $RAVEN_API_KEY" \
     -F "files=@buffer.c" \
     -F "files=@utils.c" \
     -F "language=c"

Scan a Project Archive
----------------------

**Basic mode:**

.. code-block:: bash

   curl -X POST https://api.raven.ai4secure.com/api/scan/project \
     -H "X-API-Key: $RAVEN_API_KEY" \
     -F "archive=@my-project.zip" \
     -F "mode=basic"

**Pro mode:**

.. code-block:: bash

   curl -X POST https://api.raven.ai4secure.com/api/scan/project \
     -H "X-API-Key: $RAVEN_API_KEY" \
     -F "archive=@my-project.zip" \
     -F "mode=pro"

Generate a Fix
--------------

.. code-block:: bash

   curl -X POST https://api.raven.ai4secure.com/api/fix \
     -H "Content-Type: application/json" \
     -H "X-API-Key: $RAVEN_API_KEY" \
     -d '{
       "code": "#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}",
       "language": "c",
       "findings": "Buffer overflow via gets() at line 4",
       "vuln_pairs": [
         { "line": 4, "reason": "Use of unsafe gets() function", "category": "CWE-120" }
       ]
     }'

Follow-up Question
------------------

.. code-block:: bash

   curl -X POST https://api.raven.ai4secure.com/api/followup \
     -H "Content-Type: application/json" \
     -H "X-API-Key: $RAVEN_API_KEY" \
     -d '{
       "code": "#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}",
       "language": "c",
       "findings": "Buffer overflow via gets() at line 4",
       "question": "Is this vulnerability exploitable remotely?",
       "history": []
     }'

Health Check
------------

.. code-block:: bash

   curl https://api.raven.ai4secure.com/api/healthz
