import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Replace with your connection string
connection_string = os.getenv('AzureStorageString')

# File to be uploaded
local_file_name = "movie.json"
upload_file_path = os.path.join(os.getcwd(), local_file_name)

# Create a BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get the container client
container_client = blob_service_client.get_container_client("test")

# Create a blob client for the file
blob_client = container_client.get_blob_client(local_file_name)

# Upload the file
with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)
    print(f"File {local_file_name} uploaded to blob container 'test'.")
