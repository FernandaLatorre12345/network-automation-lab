from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

# Request credentials from user
host = input("Enter switch hostname or IP: ")
username = input("Username: ")
password = getpass("Password: ")

device = {
    "device_type": "cisco_ios",
    "host": host,
    "username": username,
    "password": password
}

print("Connecting to device...")

connection = ConnectHandler(**device)

# Configuration commands
commands = [
    "hostname SWITCH_AUTOMATIZADO",
    "vlan 10",
    "name VLAN_DATOS",
    "vlan 20",
    "name VLAN_VOZ",
    "vlan 50",
    "name VLAN_SEGURIDAD"
]

connection.send_config_set(commands)

# Save configuration
connection.save_config()

print("Configuration applied and saved.")

# Validation
print("Validating configuration...")

hostname_check = connection.send_command("show running-config | include hostname")
vlan_check = connection.send_command("show vlan brief")

print(hostname_check)
print(vlan_check)

# Backup running configuration
print("Creating backup...")

config = connection.send_command("show running-config")

timestamp = datetime.now().strftime("%Y%m%d_%H%M")
filename = f"backup_{timestamp}.txt"

with open(filename, "w") as file:
    file.write(config)

print(f"Backup saved as {filename}")

connection.disconnect()

print("Automation completed successfully.")
