import requests

# Define the Datadog API endpoint and headers
url = "https://api.datadoghq.com/api/v1/hosts"
headers = {
    "Accept": "application/json",
    "DD-API-KEY": "d2679b0e8de59578fe8f0620fcd5f355",
    "DD-APPLICATION-KEY": "7cfd3b5baee80add3ac664f80625161bbebd4296"
}

# Make the GET request to the Datadog API
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Check if the host exists in the response
    host_exists = any(host["name"] == "395172-web-01" for host in data["host_list"])
    if host_exists:
        print("The host '395172-web-01' exists in Datadog.")
    else:
        print("The host '395172-web-01' does not exist in Datadog.")
else:
    print(f"Error: Failed to retrieve data from Datadog. Status code: {response.status_code}") 
