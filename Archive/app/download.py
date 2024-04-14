from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# Set up the credentials and Drive API client
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/etc/credentials/cc-project-418504-060a962e75fc.json'  # Update this to your service account file path

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
    file_id = 'your_file_id_here'  # Replace with your actual file ID
    destination_path = 'C:/Users/Arvin/OneDrive/Desktop/CC_project/Archive/backup_download'  # Replace with your desired local file path
    download_file(file_id, destination_path)
