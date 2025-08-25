import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in environment.")
    sys.exit(1)

# Check if prompt is provided
if len(sys.argv) < 2:
    print("Error: No prompt provided.")
    print("Usage: uv run main.py \"<your prompt here>\" [--verbose]")
    sys.exit(1)

# Extract arguments
args = sys.argv[1:]
verbose = False

if "--verbose" in args:
    verbose = True
    args.remove("--verbose")

user_prompt = " ".join(args)

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Build conversation messages
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

# Send to Gemini
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

# Print response
print(response.text)

# Print token usage with verbose output
if verbose:
    usage = response.usage_metadata
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
