from netmiko import ConnectHandler
from datetime import datetime
import paramiko


def upload_to_sftp(local_file):

    choice = input("\nDo you want to upload the backup to an SFTP server? (yes/no): ").lower()

    if choice != "yes":
        print("Skipping SFTP upload.")
        return

    sftp_server = input("Enter SFTP server IP: ")
    sftp_user = input("Enter SFTP username: ")
    sftp_password = input("Enter SFTP password: ")
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

    device = {
        "device_type": "cisco_ios",
        "host": host,
        "username": username,
        "password": password
    }

    connection = ConnectHandler(**device)

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

    host = input("Enter switch hostname or IP: ")
    username = input("Username: ")
    password = input("Password: ")
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

    print(f"\nBackup saved: {backup}")

    upload_to_sftp(backup)
