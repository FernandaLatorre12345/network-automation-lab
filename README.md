# Network Automation Lab

This project demonstrates basic network automation using Python and Netmiko.

The script connects to a network device via SSH and automatically applies configuration tasks such as VLAN configuration and hostname modification. It also validates the applied configuration and creates a backup of the running configuration.

## Features

- SSH connection to a network device
- Automated VLAN configuration
- Hostname modification
- Automatic configuration saving
- Configuration validation
- Backup of running configuration

## Technologies Used

- Python
- Netmiko
- SSH
- Git

## Installation

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Compatibility

This script uses Netmiko for SSH communication and can be adapted to work with any network device supported by Netmiko, including:

- Cisco IOS
- Cisco IOS-XE
- Cisco NX-OS
- Arista EOS
- Juniper JunOS
- Palo Alto PAN-OS
- Fortinet FortiOS

The current implementation targets Cisco IOS-based devices.

## Lab Environment

The script was tested using the Cisco DevNet Catalyst 9000 Always-On Sandbox environment.

This environment provides access to a virtual Cisco IOS-XE device for testing network automation scripts and programmability features.

## Automation Workflow

User Input → SSH Connection → Configuration Commands → Validation → Backup

1. The user runs the Python script.
2. The script requests device credentials from the user.
3. An SSH connection is established using Netmiko.
4. Configuration commands are sent to the device.
5. VLAN configuration and hostname changes are applied.
6. The configuration is saved on the device.
7. The script validates the configuration using show commands.
8. A backup of the running configuration is generated.

## How to Run

Execute the script using:

```bash
py switch_config.py
```

The script will request:

- Device hostname or IP address
- Username
- Password

## Security Note

Device credentials are not stored in the script.

The script requests credentials at runtime to avoid exposing sensitive information in the repository.

## Project Structure

network-automation-lab  
│  
├── README.md  
├── switch_config.py  
└── requirements.txt  

## Purpose

This project demonstrates how network engineers can automate repetitive configuration tasks using Python and network automation libraries.
