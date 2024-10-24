import requests

BASE_URL = ""

def create_resource(resource_data):
    """POST-request"""
    response = requests.post(BASE_URL, json=resource_data)
    if response.status_code == 201:
        print("Resource created:", response.json())
    else:
        print("Error creating resource:", response.status_code, response.text)

def get_resources():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Resources:", response.json())
    else:
        print("Error fetching resources:", response.status_code, response.text)

def get_resource_by_id(resource_id):
    """Fetches a specific resource by ID."""
    response = requests.get(f"{BASE_URL}/{resource_id}")
    if response.status_code == 200:
        print("Resource:", response.json())
    else:
        print("Error fetching resource:", response.status_code, response.text)

def update_resource(resource_id, update_data):
    """Updates an existing resource in the API."""
    response = requests.put(f"{BASE_URL}/{resource_id}", json=update_data)
    if response.status_code == 200:
        print("Resource updated:", response.json())
    else:
        print("Error updating resource:", response.status_code, response.text)

def delete_resource(resource_id):
    """Deletes a resource by id."""
    response = requests.delete(f"{BASE_URL}/{resource_id}")
    if response.status_code == 200:
        print("Resource deleted")
    else:
        print("Error deleting resource:", response.status_code, response.text)
