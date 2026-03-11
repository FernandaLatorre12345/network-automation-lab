from netmiko import ConnectHandler
from getpass import getpass

host = input("Switch IP or hostname: ")
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

connection.save_config()

print("Configuration applied successfully")

connection.disconnect()
