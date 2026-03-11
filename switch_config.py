from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
from datetime import datetime
import paramiko
import getpass


def upload_to_sftp(local_file):
    """
    Optionally uploads the generated backup file to a remote SFTP server.
    The user is prompted for SFTP credentials and destination directory.
    """

    choice = input("\nDo you want to upload the backup to an SFTP server? (yes/no): ").lower()

    if choice not in ["yes", "y"]:
        print("Skipping SFTP upload.")
        return

    sftp_server = input("Enter SFTP server IP: ")
    sftp_user = input("Enter SFTP username: ")
    sftp_password = getpass.getpass("Enter SFTP password: ")
    remote_dir = input("Enter remote directory (default /backups): ")

    if remote_dir == "":
        remote_dir = "/backups"

    try:
        transport = paramiko.Transport((sftp_server, 22))
        transport.connect(username=sftp_user, password=sftp_password)

        sftp = paramiko.SFTPClient.from_transport(transport)

        remote_path = f"{remote_dir}/{local_file}"

        sftp.put(local_file, remote_path)

        sftp.close()
        transport.close()

        print(f"Backup successfully uploaded to SFTP: {remote_path}")

    except Exception as e:
        print(f"SFTP upload failed: {e}")


def configure_switch(host, username, password, vlan_id, vlan_name, new_hostname):
    """
    Connects to a network switch via SSH using Netmiko.
    Applies hostname and VLAN configuration, validates the changes,
    and generates a local backup of the running configuration.
    """

    device = {
        "device_type": "cisco_ios",
        "host": host,
        "username": username,
        "password": password
    }

    try:
        connection = ConnectHandler(**device)
        print("Connected to device.")

    except NetmikoTimeoutException:
        print("ERROR: Device unreachable or SSH not responding.")
        return None

    except NetmikoAuthenticationException:
        print("ERROR: Authentication failed. Check username/password.")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

    commands = [
        f"hostname {new_hostname}",
        f"vlan {vlan_id}",
        f"name {vlan_name}"
    ]

    connection.send_config_set(commands)
    connection.save_config()

    print("Configuration applied successfully")

    hostname_check = connection.send_command("show running-config | include hostname")
    vlan_check = connection.send_command("show vlan brief")

    print("\nValidation:")

    alerts = []

    if new_hostname not in hostname_check:
        alerts.append("Hostname configuration mismatch")

    if vlan_name not in vlan_check:
        alerts.append(f"VLAN {vlan_id} ({vlan_name}) not found")

    if alerts:
        print("ALERT: configuration mismatch detected")
        for alert in alerts:
            print(f"- {alert}")
    else:
        print("Configuration validation successful")
        print(hostname_check.strip())
        print(f"VLAN {vlan_id} {vlan_name} present")

    config = connection.send_command("show running-config")

    hostname_output = connection.send_command("show running-config | include hostname")
    hostname = hostname_output.split()[1]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{hostname}_backup_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write(config)

    connection.disconnect()

    return filename


if __name__ == "__main__":

    """
    Main execution block.
    Collects user input and executes the automation workflow.
    """

    host = input("Enter switch hostname or IP: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    new_hostname = input("New hostname: ")
    vlan_id = input("VLAN ID: ")
    vlan_name = input("VLAN Name: ")

    backup = configure_switch(
        host,
        username,
        password,
        vlan_id,
        vlan_name,
        new_hostname
    )

    if backup:
        print(f"\nBackup saved: {backup}")
        upload_to_sftp(backup)
    else:
        print("Automation failed. No backup generated.")

