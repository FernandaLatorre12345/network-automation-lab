from netmiko import ConnectHandler

switch = {
    "device_type": "cisco_ios",
    "host": "devnetsandboxiosxec9k.cisco.com",
    "username": "fernandalatorre.09",
    "password": "h_mVg95j_t4UVIq"
}

print("Conectando al switch...")

connection = ConnectHandler(**switch)

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

connection.send_command("write memory")

print("Configuración aplicada y guardada")

connection.disconnect()