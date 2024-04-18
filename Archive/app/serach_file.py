from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'PATH TO CREDENTIALS.json'

# Scopes required by the application
SCOPES = ['https://www.googleapis.com/auth/drive']

def search_file():
    """Searches for JPEG files in the Drive."""

    # Authenticate using the service account file
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        # Create the Drive API service
        service = build('drive', 'v3', credentials=credentials)

        # List to hold the files found
        files = []
        page_token = None

        # Loop through all available pages of results
        while True:
            response = service.files().list(
                q="mimeType='text/plain'",
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageToken=page_token
            ).execute()

            # Extend the files list with the current page of files
            files.extend(response.get('files', []))

            # Print the names and IDs for the current page of files
            for file in files:
                print(f'Found file: {file.get("name")} ({file.get("id")})')

            # Update the page token for the next iteration
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

    except HttpError as error:
        print(f'An error occurred: {error}')
        files = None

    return files

if __name__ == '__main__':
    # Call the search_file function to search for JPEG files in the Drive
    search_file()
