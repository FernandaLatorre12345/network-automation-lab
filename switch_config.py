from netmiko import ConnectHandler
from datetime import datetime


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
    print(hostname_check)
    print(vlan_check)

    config = connection.send_command("show running-config")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"backup_{timestamp}.txt"

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

