Python Examples
===============

All examples use the ``requests`` library. Install it with:

.. code-block:: bash

   pip install requests

Setup
-----

Set the following environment variables before running:

.. code-block:: bash

   export RAVEN_API_KEY="your-api-key"
   export RAVEN_BASE_URL="https://<BASE_URL_TBD>"   # update when finalized

.. code-block:: python

   import os
   import requests

   API_KEY = os.environ["RAVEN_API_KEY"]
   BASE_URL = os.environ["RAVEN_BASE_URL"]
   HEADERS = {
       "X-API-Key": API_KEY,
       "Content-Type": "application/json",
   }

Scan a Code Snippet
-------------------

.. code-block:: python

   response = requests.post(
       f"{BASE_URL}/api/scan/snippet",
       headers=HEADERS,
       json={
           "code": '#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}',
           "language": "c",
       },
   )
   result = response.json()
   print(f"Verdict: {result['verdict']}, Importance: {result['importance']}")

Scan Uploaded Files
-------------------

.. code-block:: python

   with open("buffer.c", "rb") as f1, open("utils.c", "rb") as f2:
       response = requests.post(
           f"{BASE_URL}/api/scan/files",
           headers={"X-API-Key": API_KEY},
           files=[("files", f1), ("files", f2)],
           data={"language": "c"},
       )
   for result in response.json()["results"]:
       print(f"{result['filename']}: {result['verdict']}")

Scan a Project Archive
----------------------

.. code-block:: python

   with open("my-project.zip", "rb") as archive:
       response = requests.post(
           f"{BASE_URL}/api/scan/project",
           headers={"X-API-Key": API_KEY},
           files={"archive": archive},
           data={"mode": "sast"},
       )
   data = response.json()
   print(f"Scanned {data['selection_meta']['selected_count']} files")
   for result in data["results"]:
       if result["verdict"] == "vulnerable":
           print(f"  {result['filename']}: {result['importance']}")

Generate a Fix
--------------

.. code-block:: python

   response = requests.post(
       f"{BASE_URL}/api/fix",
       headers=HEADERS,
       json={
           "code": '#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}',
           "language": "c",
           "findings": "Buffer overflow via gets() at line 4",
           "vuln_pairs": [
               {"line": 4, "reason": "Use of unsafe gets() function", "category": "CWE-120"}
           ],
       },
   )
   fix = response.json()
   print(fix["fix_markdown"])
   print("--- Fixed code ---")
   print(fix["fixed_code"])

Follow-up Question
------------------

.. code-block:: python

   response = requests.post(
       f"{BASE_URL}/api/followup",
       headers=HEADERS,
       json={
           "code": '#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}',
           "language": "c",
           "findings": "Buffer overflow via gets() at line 4",
           "question": "Is this vulnerability exploitable remotely?",
           "history": [],
       },
   )
   print(response.json()["answer"])

Health Check
------------

.. code-block:: python

   response = requests.get(f"{BASE_URL}/api/healthz")
   print(response.json())
