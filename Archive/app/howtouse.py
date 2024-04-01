import googleapiclient.discovery

def upload_file(file_path, file_name):
    """Uploads a file to Google Drive.

    Args:
        file_path: The path to the file to upload.
        file_name: The name of the file to upload.
    """

    # Create a service account credentials object.
    credentials = service_account.Credentials.from_service_account_file(
        'C:/Users/Arvin/OneDrive/Desktop/CC_project/Archive/app/cc-project-418504-060a962e75fc.json')

    # Create a Google Drive API service object.
    service = googleapiclient.discovery.build(
        'drive', 'v3', credentials=credentials)

    # Create a file metadata object.
    file_metadata = {
        'name': file_name
    }

    # Create a media object.
    media = googleapiclient.http.MediaFileUpload(
        file_path, mimetype='text/plain')

    # Upload the file.
    file = service.files().create(body=file_metadata, media_body=media,
        fields='id').execute()

    print(f'File ID: {file.get("id")}')

if __name__ == '__main__':
    # Set the file path and file name.
    file_path = 'C:/Users/Arvin/OneDrive/Desktop/dummy/hello.py'
    file_name = 'hello.py'

    # Upload the file.
    upload_file(file_path, file_name)
