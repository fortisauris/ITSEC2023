import subprocess

def scan_wifi():
    cmd = "nmcli dev wifi list"
    networks = subprocess.check_output(cmd, shell=True)
    networks = networks.decode("utf-8")
    return networks

if __name__ == '__main__':
    print(scan_wifi())