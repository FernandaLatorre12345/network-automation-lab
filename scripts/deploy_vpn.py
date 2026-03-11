# deploy_vpn.py
# Main script that orchestrates the VPN deployment workflow

from fortigate_vpn import configure_fortigate
from paloalto_vpn import configure_paloalto
from vpn_test import test_connectivity

def main():

    vpn_config = {
        "fortigate_wan": "200.1.1.1",
        "paloalto_wan": "200.2.2.2",
        "local_network": "10.1.1.0/24",
        "remote_network": "10.2.2.0/24",
        "psk": "MySecurePSK"
    }

    print("Starting VPN automation workflow")

    configure_fortigate(vpn_config)
    configure_paloalto(vpn_config)

    test_connectivity("10.2.2.10")

    print("Automation workflow finished")

if __name__ == "__main__":
    main()