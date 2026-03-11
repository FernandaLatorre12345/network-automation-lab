# vpn_test.py
# Simple connectivity validation script

import subprocess

def test_connectivity(target_ip):

    print(f"Testing connectivity to {target_ip}")

    try:

        result = subprocess.run(
            ["ping", "-c", "2", target_ip],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("VPN connectivity test successful")

        else:
            print("VPN connectivity test failed")

    except Exception:
        print("Connectivity test could not be executed")