import requests

# Print a Hello World message
print("Hello, World!")

# Send a GET request to a public test API (JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/posts/1"  # A test endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("API Request Successful!")
    # Print the response JSON
    print("Response from API:", response.json())
else:
    print(f"Failed to get data from API. Status code: {response.status_code}")
