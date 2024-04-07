from google.oauth2 import service_account
from googleapiclient.discovery import build

# Authenticate and create the Google Drive service
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'C:/Users/Arvin/OneDrive/Desktop/CC_project/Archive/app/cc-project-418504-060a962e75fc.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

def get_file_metadata(file_id):
    try:
        # Request to get the file metadata
        file_metadata = service.files().get(fileId=file_id, fields='id, name, mimeType, size, owners, createdTime, modifiedTime').execute()

        # Print the metadata
        print(f"File ID: {file_metadata.get('id')}")
        print(f"Name: {file_metadata.get('name')}")
        print(f"MIME Type: {file_metadata.get('mimeType')}")
        print(f"Size: {file_metadata.get('size', 'N/A')} bytes")
        print(f"Owners: {[owner['emailAddress'] for owner in file_metadata.get('owners', [])]}")
        print(f"Created Time: {file_metadata.get('createdTime')}")
        print(f"Modified Time: {file_metadata.get('modifiedTime')}")
        print("--------------------------------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # List of file IDs to retrieve metadata for; replace these with your actual file IDs
    file_ids = [
        '11cyG4f1egCiRf9URf7QKUS65i9F0sCM-',
        '1cNfz5qxkFaexhl9ckfp3F-jy-Gasr3Xy',
        '1Sae5RWGDM8Tr3PzIx7ULFloxLRg1Hsyg'
        # Add more file IDs as needed
    ]

    for file_id in file_ids:
        get_file_metadata(file_id)



# File ID: 11cyG4f1egCiRf9URf7QKUS65i9F0sCM-
# Successfully uploaded hello.py
# File ID: 1cNfz5qxkFaexhl9ckfp3F-jy-Gasr3Xy
# Successfully uploaded OOADJ-6B_Lab-10_MVC_PES1UG21CS112.pdf
# File ID: 1Sae5RWGDM8Tr3PzIx7ULFloxLRg1Hsyg
# Successfully uploaded Screenshot (27).png
        


# output:
# File ID: 11cyG4f1egCiRf9URf7QKUS65i9F0sCM-
# Name: hello.py
# MIME Type: text/x-python
# Size: 20 bytes
# Owners: ['google-drive-backup-project@cc-project-418504.iam.gserviceaccount.com']
# Created Time: 2024-04-01T09:56:56.047Z
# Modified Time: 2024-04-01T09:56:56.047Z
# --------------------------------------------------
# File ID: 1cNfz5qxkFaexhl9ckfp3F-jy-Gasr3Xy
# Name: OOADJ-6B_Lab-10_MVC_PES1UG21CS112.pdf
# MIME Type: application/pdf
# Size: 568777 bytes
# Owners: ['google-drive-backup-project@cc-project-418504.iam.gserviceaccount.com']
# Created Time: 2024-04-01T09:56:58.114Z
# Modified Time: 2024-04-01T09:56:58.114Z
# --------------------------------------------------
# File ID: 1Sae5RWGDM8Tr3PzIx7ULFloxLRg1Hsyg
# Name: Screenshot (27).png
# MIME Type: image/png
# Size: 2402480 bytes
# Owners: ['google-drive-backup-project@cc-project-418504.iam.gserviceaccount.com']
# Created Time: 2024-04-01T09:57:00.020Z
# Modified Time: 2024-04-01T09:57:00.020Z
# --------------------------------------------------