import paramiko
import re
import requests
import tkinter as tk
from tkinter import scrolledtext

def get_isp(ip):
    if ip.startswith("10.20"):
        return "INTERNAL"
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        isp = data.get('org', 'Unknown ISP')
        return isp
    except:
        return "Unknown ISP"

def update_info(output_text):
    ssh_host = 'server1.example.com'
    ssh_port = 22
    ssh_username = 'root'
    ssh_password = 'password'

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    try:
        client.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)

        stdin, stdout, stderr = client.exec_command('echo {} | sudo -S wg show'.format(ssh_password))

        output = stdout.read().decode()
        client.close()

        allowed_ips_info = re.findall(r'allowed ips: ([\d.]+/\d+)', output)
        endpoint_info = re.findall(r'endpoint: ([\d.]+):', output)

        # Combine IP and ISP information
        ip_isp_info = []
        for allowed_ips, endpoint_ip in zip(allowed_ips_info, endpoint_info):
            isp = get_isp(endpoint_ip)
            ip_isp_info.append((allowed_ips.split('/')[0], endpoint_ip, isp))

        # Sort IP information by IP address in ascending order
        sorted_ip_isp_info = sorted(ip_isp_info, key=lambda x: [int(i) for i in x[0].split('.')])

        output_text.delete('1.0', tk.END)  # Clear existing content

        # Display sorted information
        for ip, endpoint_ip, isp in sorted_ip_isp_info:
            # Append updated output to the scrolled text widget
            output_text.insert(tk.END, f"IP: {ip}, Endpoint: {endpoint_ip}, ISP: {isp}\n")

    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials.")
    except paramiko.SSHException as e:
        print("Error:", str(e))

def main():
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Wireguard IP Info GUI")

    # Create a scrolled text widget to display output
    output_text = scrolledtext.ScrolledText(window, width=80, height=20)
    output_text.grid(row=0, column=0, padx=10, pady=10)

    # Create a button to update the info
    update_button = tk.Button(window, text="Update Info", command=lambda: update_info(output_text))
    update_button.grid(row=1, column=0, padx=10, pady=5)

    window.mainloop()

if __name__ == '__main__':
    main()
