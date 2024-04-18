from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# Set up the credentials and Drive API client
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = ''PATH TO CREDENTIALS.json''  # Update this to your service account file path

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

def download_file(file_id, destination):
    """Downloads a file from Google Drive given its file ID."""
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    
    # Create a downloader object and download the file
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    try:
        while not done:
            status, done = downloader.next_chunk()
            print("Download progress: {0:.2f}%".format(status.progress() * 100))
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    # Write the downloaded bytes to a file
    with open(destination, 'wb') as f:
        f.write(fh.getbuffer())
    print(f"File has been downloaded to: {destination}")

if __name__ == '__main__':
    file_id = 'FILE ID'  # obtained after u run backupscript.py
    destination_path = ''PATH TO LOCAL DIRECTORY WHERE YOU WANT FILE TO BE DOWNLOADED'  # Replace with your desired local file path
    download_file(file_id, destination_path)
