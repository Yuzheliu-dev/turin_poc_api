JavaScript Examples
===================

All examples use the built-in ``fetch`` API (Node.js 18+ or any modern browser).

Setup
-----

Set the following environment variables before running:

.. code-block:: bash

   export RAVEN_API_KEY="your-api-key"
   export RAVEN_BASE_URL="https://<BASE_URL_TBD>"   # update when finalized

.. code-block:: javascript

   const API_KEY = process.env.RAVEN_API_KEY;
   const BASE_URL = process.env.RAVEN_BASE_URL;

   const headers = {
     "Content-Type": "application/json",
     "X-API-Key": API_KEY,
   };

Scan a Code Snippet
-------------------

.. code-block:: javascript

   const response = await fetch(`${BASE_URL}/api/scan/snippet`, {
     method: "POST",
     headers,
     body: JSON.stringify({
       code: '#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}',
       language: "c",
     }),
   });
   const result = await response.json();
   console.log(`Verdict: ${result.verdict}, Importance: ${result.importance}`);

Scan Uploaded Files
-------------------

.. code-block:: javascript

   const formData = new FormData();
   formData.append("files", new Blob([await fs.promises.readFile("buffer.c")]), "buffer.c");
   formData.append("files", new Blob([await fs.promises.readFile("utils.c")]), "utils.c");
   formData.append("language", "c");

   const response = await fetch(`${BASE_URL}/api/scan/files`, {
     method: "POST",
     headers: { "X-API-Key": API_KEY },
     body: formData,
   });
   const data = await response.json();
   data.results.forEach((r) => console.log(`${r.filename}: ${r.verdict}`));

Scan a Project Archive
----------------------

.. code-block:: javascript

   const formData = new FormData();
   formData.append(
     "archive",
     new Blob([await fs.promises.readFile("my-project.zip")]),
     "my-project.zip"
   );
   formData.append("mode", "basic");

   const response = await fetch(`${BASE_URL}/api/scan/project`, {
     method: "POST",
     headers: { "X-API-Key": API_KEY },
     body: formData,
   });
   const data = await response.json();
   console.log(`Scanned ${data.selection_meta.selected_count} files`);

Generate a Fix
--------------

.. code-block:: javascript

   const response = await fetch(`${BASE_URL}/api/fix`, {
     method: "POST",
     headers,
     body: JSON.stringify({
       code: '#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}',
       language: "c",
       findings: "Buffer overflow via gets() at line 4",
       vuln_pairs: [
         { line: 4, reason: "Use of unsafe gets() function", category: "CWE-120" },
       ],
     }),
   });
   const fix = await response.json();
   console.log(fix.fix_markdown);
   console.log("--- Fixed code ---");
   console.log(fix.fixed_code);

Follow-up Question
------------------

.. code-block:: javascript

   const response = await fetch(`${BASE_URL}/api/followup`, {
     method: "POST",
     headers,
     body: JSON.stringify({
       code: '#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}',
       language: "c",
       findings: "Buffer overflow via gets() at line 4",
       question: "Is this vulnerability exploitable remotely?",
       history: [],
     }),
   });
   const data = await response.json();
   console.log(data.answer);

Health Check
------------

.. code-block:: javascript

   const response = await fetch(`${BASE_URL}/api/healthz`);
   console.log(await response.json());
