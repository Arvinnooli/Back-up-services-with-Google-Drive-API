from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

# Authenticate and create the Google Drive service
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'C:/Users/Arvin/OneDrive/Desktop/CC_project/client_secret_282779927583-iltfr8q3mim2g8or89qfimdm3kp1mpaq.apps.googleusercontent.com.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

# Function to upload a single file
def upload_file(filename, filepath, mimetype):
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath, mimetype=mimetype)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File ID: {file.get('id')}")

# Function to list files in a directory
def list_files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Function to backup a directory to Google Drive
def backup_directory(local_directory):
    files = list_files_in_directory(local_directory)
    for filename in files:
        filepath = os.path.join(local_directory, filename)
        mimetype = 'application/octet-stream'  # Adjust as needed for specific file types
        try:
            upload_file(filename, filepath, mimetype)
            print(f'Successfully uploaded {filename}')
        except Exception as e:
            print(f'Failed to upload {filename}: {str(e)}')
            # Implement retry logic here if needed

if __name__ == '__main__':
    # Replace 'your_local_directory_path' with the path to the directory you wish to back up
    backup_directory('your_local_directory_path')
