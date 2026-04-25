import os
from openai import OpenAI
# Use environment variable for security
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "hi"}],
        max_tokens=10
    )
    print("SUCCESS", response.choices[0].message.content)
except Exception as e:
    print("ERROR:", e)
