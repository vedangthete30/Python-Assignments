import os
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import sys

def get_process_info():
    process_info_list = []
    try:
        for process in psutil.process_iter(attrs=['name', 'pid']):
            try:
                process_attrs = process.as_dict(attrs=['name', 'pid'])
                process_info_list.append(process_attrs)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    except Exception as e:
        print(f"An error occurred while retrieving process information: {str(e)}")
    return process_info_list

def create_and_write_log(directory, process_info):
    log_file_name = os.path.join(directory, 'process_info.log')
    try:
        with open(log_file_name, 'w') as log_file:
            log_file.write("Currently running processes:\n")
            for process in process_info:
                log_file.write(f"Process Name: {process['name']}, PID: {process['pid']}\n")
    except Exception as e:
        print(f"An error occurred while writing to the log file: {str(e)}")
    return log_file_name

def send_email(sender_email, sender_password, receiver_email, log_file):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Process Information Log"
        
        # Attach the log file
        with open(log_file, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(log_file))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(log_file)}"'
            msg.attach(part)
        
        # Send the email
        smtp_server = "smtp.gmail.com"  # Replace with your SMTP server address
        smtp_port = 587  # Replace with your SMTP server port (e.g., 587 for TLS)
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python process_info_email.py <directory> <receiver_email>")
        sys.exit(1)

    directory = sys.argv[1]
    receiver_email = sys.argv[2]

    process_info = get_process_info()

    if not process_info:
        print("No running processes found.")
        sys.exit(1)

    log_file = create_and_write_log(directory, process_info)

    # Email the log file
    sender_email = "vthete3@gmail.com"  # Replace with your sender email
    sender_password = "gcnn jdei thuq raf"  # Replace with your sender email password
    send_email(sender_email, sender_password, receiver_email, log_file)

if __name__ == "__main__":
    main()