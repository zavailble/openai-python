import os
import openai
openai.api_key = "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"
openai.organization = "org-a6q5O46t5UeIPYYfPro8qUHB"
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
prompt = """
"""

response = openai.Completion.create(
              model="text-davinci-001",
              prompt=prompt,
              max_tokens=100,
              temperature=0
            )

print(response)