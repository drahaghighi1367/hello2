import requests
import pyzipper
from google import genai
from google.genai import types

# Hardcode the Gemini API Key
GEMINI_API_KEY = "your_hardcoded_api_key_here"

# Generate content using Google GenAI API
def generate():
    client = genai.Client(api_key=GEMINI_API_KEY)

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content(role="user", parts=[types.Part.from_text(text="hi")]),
        types.Content(role="model", parts=[types.Part.from_text(text="Hello! How can I help you today?")]),
        types.Content(role="user", parts=[types.Part.from_text(text="INSERT_INPUT_HERE")]),
    ]
    tools = [types.Tool(googleSearch=types.GoogleSearch())]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0),
        tools=tools,
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text += chunk.text

    # Save the response as a text file
    file_name = "api_response.txt"
    with open(file_name, 'w') as f:
        f.write(response_text)  # Save the response text

    print(f"Response saved to {file_name}")

    # Now create a password-protected zip file
    zip_file_name = "api_response.zip"
    password = b"your_password"  # Password for the zip file (must be bytes)
    
    with pyzipper.AESZipFile(zip_file_name, mode="w", encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(password)  # Set the password for encryption
        zipf.write(file_name)  # Add the .txt file to the zip

    print(f"Zipped file created: {zip_file_name}")

if __name__ == "__main__":
    generate()
