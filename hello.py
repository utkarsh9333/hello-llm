"""
Hello LLM — first Python + Claude API project.
Takes a prompt from the command line and prints Claude's response.
"""

import os
import sys
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()  # Load environment variables from .env file

client=Anthropic()

def ask_claude(prompt: str) -> str:
    """Send a prompt to Claude and return the text response."""
    message = client.messages.create(
        model="claude-haiku-4-5",  
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # message.content is a list of content blocks. For simple text responses, the first block has the text.
    return message.content[0].text


def main():
    # Get the prompt from command line arguments, or use a default for the first run.
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = "In one sentence, what is a software bug?"
    
    print(f"\n🤖 Asking Claude: {prompt}\n")
    
    try:
        response = ask_claude(prompt)
        print(f"💬 Claude says:\n{response}\n")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Check that your API key is set correctly in .env")


if __name__ == "__main__":
    main()