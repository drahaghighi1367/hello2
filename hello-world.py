import requests
import pyzipper

# Print a Hello World message
print("Hello, World!")

# Send a GET request to a public test API (JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/posts/1"  # A test endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("API Request Successful!")
    # Save the response as a text file
    file_name = "api_response.txt"
    with open(file_name, 'w') as f:
        f.write(str(response.json()))  # Save the response JSON as text

    print(f"Response saved to {file_name}")

    # Now let's create a zip file with password protection
    zip_file_name = "api_response.zip"
    password = b"your_password"  # Password for the zip file (must be bytes)
    
    with pyzipper.AESZipFile(zip_file_name, mode="w", encryption=pyzipper.WZ_AES) as zipf:
        # Set the password for encryption
        zipf.setpassword(password)
        
        # Add the .txt file to the zip
        zipf.write(file_name)

    print(f"Zipped file created: {zip_file_name}")
else:
    print(f"Failed to get data from API. Status code: {response.status_code}")
