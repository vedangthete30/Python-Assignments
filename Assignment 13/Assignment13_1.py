import os
import hashlib
import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import time

# Function to calculate checksum (SHA-256)
def get_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # Read in 64k chunks
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

# Function to find duplicate files
def find_duplicate_files(directory):
    duplicates = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            checksum = get_checksum(file_path)
            if checksum in duplicates:
                duplicates[checksum].append(file_path)
            else:
                duplicates[checksum] = [file_path]
    return duplicates

# Function to delete duplicate files and create a log
def delete_duplicate_files(duplicates):
    log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "_log.txt"
    with open(log_filename, 'w') as log_file:
        for checksum, file_paths in duplicates.items():
            if len(file_paths) > 1:
                log_file.write("Duplicate Files:\n")
                for file_path in file_paths:
                    log_file.write(file_path + "\n")
                log_file.write("\n")
                for file_path in file_paths[1:]:
                    os.remove(file_path)
                    log_file.write("Deleted: " + file_path + "\n")

# Function to send an email with statistics and log file as an attachment
def send_email(receiver_email, log_filename, statistics):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465  
    sender_email = 'vthete3@gmail.com'
    sender_password = 'sqhl jwkr otcs esax'
    
    # Create an email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Duplicate File Removal Report'
    
    # Add the statistics to the email body
    body = f"Duplicate File Removal Report\n\n{statistics}"
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach the log file
    with open(log_filename, 'rb') as log_file:
        attachment = MIMEText(log_file.read())
        attachment.add_header('Content-Disposition', f'attachment; filename="{log_filename}"')
        msg.attach(attachment)
    
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print("Email sending failed:", str(e))
    finally:
        server.quit()

# Function to collect and format statistics
def collect_statistics(start_time, duplicates):
    end_time = datetime.now()
    total_files = sum(len(files) for files in duplicates.values())
    total_duplicates = sum(1 for files in duplicates.values() if len(files) > 1)
    return f"Start Time: {start_time}\nEnd Time: {end_time}\nTotal Files Scanned: {total_files}\nTotal Duplicate Files Found: {total_duplicates}"

# Main script
def main():
    parser = argparse.ArgumentParser(description='Duplicate File Removal Script')
    parser.add_argument('directory', help='Absolute path of the directory containing duplicate files')
    parser.add_argument('interval', type=int, help='Time interval in minutes')
    parser.add_argument('receiver_email', help='Email address of the receiver')
    args = parser.parse_args()

    start_time = datetime.now()
    while True:
        duplicates = find_duplicate_files(args.directory)
        delete_duplicate_files(duplicates)
        statistics = collect_statistics(start_time, duplicates)
        send_email(args.receiver_email, log_filename, statistics)

        # Sleep for the specified time interval in seconds
        time.sleep(args.interval * 10)

if __name__ == "__main__":
    main()
