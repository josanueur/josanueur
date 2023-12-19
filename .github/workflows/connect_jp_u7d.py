import paramiko
import pandas as pd
from urllib.parse import urlparse

# Read credentials from environment variables
hostname = "mcg6g464mb0k40pqs74w2t1xksp1.ftp.marketingcloudops.com"
username = "534006085_6"
password = "2023.Esencial"

# SFTP URL
sftp_url = f"sftp://{username}:{password}@{hostname}/Import/Reportes/Metricas.csv"

# Parse the SFTP URL
url_parts = urlparse(sftp_url)
remote_path = url_parts.path

# Local path where you want to save the downloaded file
local_path = "./Metricas.csv"  # Change this to your desired local path and filename

# Create an SFTP client
transport = paramiko.Transport((hostname, 22))
transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Download the file
sftp.get(remote_path, local_path)

# Read the CSV file into a DataFrame
df = pd.read_csv(local_path, encoding='utf-16le')

# Display the DataFrame as a table
#print("Content of the downloaded file:")
print(df)

# Close the SFTP connection
sftp.close()
transport.close()

print(f"File '{remote_path}' downloaded to '{local_path}'")
