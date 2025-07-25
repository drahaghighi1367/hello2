import requests
import pyzipper

# Hardcoded API Key (only for testing)
GEMINI_API_KEY = "your_hardcoded_api_key_here"

# Mock function to simulate GenAI API response
def generate():
    # In reality, you would call the GenAI API, but let's mock it
    # response = requests.get(f"https://genai.googleapis.com/api/{GEMINI_API_KEY}")
    # For now, let's use a placeholder response instead.
    
    response_text = """
    User: Hello
    Model: Hi there! How can I assist you today?
    """
    
    # Save the response as a text file
    file_name = "api_response.txt"
    with open(file_name, 'w') as f:
        f.write(response_text)  # Save the mock response

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
