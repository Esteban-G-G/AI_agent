import sys
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in environment.")
    sys.exit(1)

# Check if prompt is provided
if len(sys.argv) < 2:
    print("Error: No prompt provided.")
    print("Usage: uv run main.py \"<your prompt here>\"")
    sys.exit(1)

# Combine all arguments (to allow spaces in prompt)
prompt = " ".join(sys.argv[1:])

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=prompt
)

# Print response
print(response.text)

# Print token usage
usage = response.usage_metadata
print(f"\nPrompt tokens: {usage.prompt_token_count}")
print(f"Response tokens: {usage.candidates_token_count}")
