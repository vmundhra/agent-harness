import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("INFERENCE_MODEL")

client = OpenAI(
  api_key=os.getenv("INFERENCE_API_KEY"),
  base_url=os.getenv("INFERENCE_BASE_URL")
)

SYSTEM_PROMPT = """
You are a coding assistant running in a terminal, helping a developer with software engineering tasks.

Be concise. Prefer short, direct answers over long ones. When the user asks for code, return the code with minimal explanation unless they ask for more.

When returning code, use fenced code blocks and specify the language.

You do not currently have access to any tools — you cannot read files, run commands, or modify anything on the user's system. If the user asks you to do something that would require a tool, say so plainly and suggest they describe the relevant content directly.
"""

def run():
    """Run the agent's conversation loop until the user quits."""

    # The conversation history. This is the entire memory of the agent.
    # Every turn, we append to it and send the whole thing to the model.
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("Agent ready. Type 'quit' or 'exit' to leave.\n")

    while True:

        # 1. Get input from the user
        user_input = input("you > ").strip()

        # 2. Allow the user to leave cleanly
        if user_input in {"quit", "exit"}:
            print("Goodbye.")
            break

        # Skip empty lines without making a model call
        if not user_input:
            continue

        # 3. Append the user's message to the history
        messages.append({
            "role": "user",
            "content": user_input
        })

        # 4. Call the model with the full conversation so far
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            extra_body={"thinking": {"type": "disabled"}}, # for kimi models
        )

        # 5. Extract the assistant's reply
        assistant_message = response.choices[0].message.content

        # 6. Append the assistant's reply to the history
        messages.append({"role": "assistant", "content": assistant_message})

        # 7. Show the user
        print(f"\nagent > {assistant_message}\n")


if __name__ == "__main__":
    run()