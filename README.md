# Network Automation Lab

This project demonstrates basic network automation using Python and Netmiko.

The solution automates VLAN configuration on network devices and includes a simple graphical interface for user input. The script connects to a device via SSH, applies configuration changes, validates them, and generates a backup of the running configuration.

## Features

* SSH connection to a network device
* Automated VLAN configuration
* Hostname modification
* Automatic configuration saving
* Configuration validation
* Backup of running configuration
* Optional SFTP backup upload
* Simple graphical frontend for user input

## Technologies Used

* Python
* Netmiko
* Paramiko (SFTP transfer)
* Tkinter
* SSH
* Git

## Compatibility

This script uses Netmiko for SSH communication and can be adapted to work with any network device supported by Netmiko, including:

* Cisco IOS
* Cisco IOS-XE
* Cisco NX-OS
* Arista EOS
* Juniper JunOS
* Palo Alto PAN-OS
* Fortinet FortiOS

The current implementation targets Cisco IOS-based devices.

## Lab Environment

The automation was tested using the Cisco DevNet Catalyst 9000 Always-On Sandbox environment.

This sandbox provides access to a virtual Cisco IOS-XE switch that allows testing of automation and network programmability features.

## Automation Workflow

User Input → Frontend → Automation Script → Network Device

1. The user launches the graphical interface.
2. The user enters device credentials and VLAN information.
3. The frontend sends the information to the automation script.
4. The script establishes an SSH connection using Netmiko.
5. Configuration commands are applied to the device.
6. The configuration is saved to the device.
7. Validation commands confirm the configuration.
8. A backup of the running configuration is created locally.
9. Optionally, the backup can be uploaded to an SFTP server.

## Installation

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## How to Run

Run the graphical interface:

```bash
py frontend.py
```

Alternatively, the automation script can be executed directly from the command line:

```bash
py switch_config.py
```

The script will request:

* Device hostname or IP address
* Username
* Password
* New hostname
* VLAN ID
* VLAN Name

## Security Note

Device credentials are not stored in the script.

Credentials are requested at runtime to prevent exposing sensitive information in the repository.

## Project Structure

```
network-automation-lab
│
├── README.md
├── switch_config.py
├── frontend.py
├── requirements.txt
├── vpn_automation_plan.md
└── screenshots/
```

## Purpose

This project demonstrates how network engineers can automate repetitive configuration tasks using Python and network automation libraries.

