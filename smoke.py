import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
  api_key=os.getenv("INFERENCE_API_KEY"),
  base_url=os.getenv("INFERENCE_BASE_URL")
)

response = client.chat.completions.create(
  model=os.getenv("INFERENCE_MODEL"),
  reasoning_effort="low",
  messages=[
      {"role": "user", "content": "Reply 'Setup works' and nothing else."},
  ]
)

print(response.choices[0].message.content)