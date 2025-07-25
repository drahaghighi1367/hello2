import os
import requests
import pyzipper
from google import genai
from google.genai import types

# Hardcoded API Key for testing
API_KEY = "AIzaSyC-5F2pFV06h2Q3tQ7wsQeP-_KssV9eqYM"  # Replace with your actual API key

def generate():
    client = genai.Client(
        api_key=API_KEY,
    )

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="Hello, I need help with my project."),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        tools=tools,
    )

    # Generate the content using the model and print the response
    result_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        result_text += chunk.text

    # Save the response to a text file
    file_name = "api_response.txt"
    with open(file_name, 'w') as f:
        f.write(result_text)  # Save the generated text to the file

    print(f"Response saved to {file_name}")

    # Now create a password-protected zip file
    zip_file_name = "api_response.zip"
    password = b"your_password"  # Set your password here (must be bytes)

    with pyzipper.AESZipFile(zip_file_name, mode="w", encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(password)  # Set the password for the zip file
        zipf.write(file_name)  # Add the .txt file to the zip

    print(f"Zipped file created: {zip_file_name}")


if __name__ == "__main__":
    generate()
