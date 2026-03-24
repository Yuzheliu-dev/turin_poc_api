Follow-up Q&A
=============

.. http:post:: /api/followup

   Ask follow-up questions about scan results. Supports multi-turn conversations
   (up to 6 rounds).

   **Processing time:** 5--15 seconds per question.

Request
-------

.. list-table::
   :header-rows: 1
   :widths: 15 10 10 65

   * - Field
     - Type
     - Required
     - Description
   * - ``code``
     - string
     - Yes
     - The source code being discussed
   * - ``language``
     - string
     - Yes
     - ``"c"``, ``"cpp"``, ``"cxx"``, or ``"java"``
   * - ``findings``
     - string
     - No
     - Scan findings for context
   * - ``question``
     - string
     - Yes
     - The follow-up question to ask
   * - ``history``
     - array
     - No
     - Previous conversation turns (max 6 rounds)

**history item:**

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Field
     - Type
     - Description
   * - ``role``
     - string
     - ``"user"`` or ``"assistant"``
   * - ``content``
     - string
     - The message content

**Example request body:**

.. code-block:: json

   {
     "code": "#include <stdio.h>\nint main() {\n  char buf[10];\n  gets(buf);\n  return 0;\n}",
     "language": "c",
     "findings": "Buffer overflow via gets() at line 4",
     "question": "Is this vulnerability exploitable remotely?",
     "history": [
       { "role": "user", "content": "What is the severity?" },
       { "role": "assistant", "content": "This is a critical severity issue..." }
     ]
   }

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
     - ``"success"`` or ``"failed"``
   * - ``answer``
     - string
     - The AI-generated answer to the question
   * - ``vulnerable_lines``
     - array
     - Relevant line ranges referenced in the answer

**Example response:**

.. code-block:: json

   {
     "status": "success",
     "answer": "Yes, this vulnerability can be exploitable remotely if the program reads input from a network socket...",
     "vulnerable_lines": [{ "start": 4, "end": 4 }]
   }
