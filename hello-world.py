import requests
import json
import pyzipper
import os

# API URL for a test endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"  # A test endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("API Request Successful!")
    
    # Get the response JSON data
    data = response.json()

    # Save the response to a .txt file
    file_name = "api_response.txt"
    with open(file_name, 'w') as file:
        file.write(json.dumps(data, indent=4))  # Save the response as pretty JSON
    print(f"Response saved to {file_name}")

    # Zip the .txt file and password protect it
    zip_file_name = "api_response.zip"
    zip_password = "your_secret_password"  # Set your password here

    with pyzipper.AESZipFile(zip_file_name, 'w', compression=pyzipper.ZIP_DEFLATED) as zipf:
        zipf.setpassword(zip_password.encode())  # Set the password for encryption
        zipf.write(file_name)  # Add the .txt file to the zip
    print(f"File {file_name} zipped and password protected as {zip_file_name}")

    # Clean up: remove the original .txt file (optional)
    os.remove(file_name)
    print(f"Original {file_name} deleted after zipping.")
else:
    print(f"Failed to get data from API. Status code: {response.status_code}")
