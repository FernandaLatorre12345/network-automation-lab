# Network Automation Lab

This project demonstrates basic network automation using Python and Netmiko.

The script connects to a Cisco switch via SSH and automatically applies configuration commands such as VLAN configuration and hostname modification.

## Features

- SSH connection to a Cisco switch
- Automated VLAN configuration
- Hostname modification
- Automatic configuration saving

## Technologies Used

- Python
- Netmiko
- SSH
- Git

## Lab Environment

The script was tested using the Cisco DevNet Catalyst 9000 Always-On Sandbox environment.

## Automation Workflow

1. The user runs the Python script.
2. The script prompts for device credentials.
3. An SSH connection is established using Netmiko.
4. Configuration commands are sent to the device.
5. VLAN configuration and hostname changes are applied.
6. The configuration is saved on the device.

## How to Run

Execute the script using:

py switch_config.py

The script will request:

- Device hostname or IP
- Username
- Password

## Purpose

This project demonstrates how network engineers can automate repetitive configuration tasks using Python and network automation libraries.

This project demonstrates how network engineers can automate repetitive configuration tasks using Python and network automation libraries.
