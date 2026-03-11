# fortigate_vpn.py
# Conceptual example of FortiGate VPN configuration using API

import requests

def configure_fortigate(config):

    print("Configuring FortiGate VPN")

    phase1_config = {
        "remote_gateway": config["paloalto_wan"],
        "psk": config["psk"]
    }

    phase2_config = {
        "local_network": config["local_network"],
        "remote_network": config["remote_network"]
    }

    print("Phase1 parameters:", phase1_config)
    print("Phase2 parameters:", phase2_config)

    # Example API endpoint (conceptual)
    url = f"https://{config['fortigate_wan']}/api/v2/cmdb/vpn.ipsec"

    try:
        response = requests.get(url, verify=False, timeout=3)
        print("FortiGate API reachable:", response.status_code)

    except Exception:
        print("FortiGate API not reachable (expected in demo environment)")