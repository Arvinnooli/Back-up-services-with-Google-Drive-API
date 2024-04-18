# Back-up services with Kubernetes using Google Drive API

## Overview
Creating a backup service that periodically backs up the contents of a folder to Google Drive using Docker and Kubernetes involves several steps.

## Files Description

- **backupscript.py**: Python script responsible for backing up specific data to Google Drive. Utilizes Google Drive API to securely store files remotely.
  
- **download.py**: you can add the file id you wish to download and run the python script
  
- **search_file.py**: you can search the type of file you wish to check availability, for example the current code runs it for all types of .txt (text) file
- **view_metadata.py**: You can view the metadata of the folder uploaded

- **requirements.txt**: Contains a list of Python packages that the project depends on. Run `pip install -r requirements.txt` to install these dependencies.

- **Dockerfile**: Defines the Docker container specifications including the base image, dependencies, and the main script to execute. Used to build a Docker image for running the backup script.

- **backup-cronjob.yaml**: Kubernetes CronJob configuration file that schedules regular backups using the Docker container. Defines the job frequency, container image, and environment setup.

- **service_account_credentials.json**: (only format includes no content due to security reasons) Service account credentials file used for authentication with the Google Cloud API.

## Setup and Deployment

1. **Build Docker Image**: Run `docker build -t backup-server .` to create the Docker image from the Dockerfile.
2. **Run Locally**: Execute `docker run --name backup-container backup-server` to start the backup process manually.
3. **Deploy on Kubernetes**: Apply the CronJob configuration with `kubectl apply -f backup-cronjob.yaml` to schedule automatic backups.


Additionally, you can also run all the python script locally (if you don't want to use docker and Kubernetes)


