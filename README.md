## Wireguard-IP-Info: Secure Tunnel Monitor and ISP Lookup

The **Wireguard-IP-Info** Python script leverages the power of `paramiko`, `re`, and `requests` libraries to create a tool for monitoring secure WireGuard tunnels while simultaneously conducting ISP lookups for endpoint IP addresses. This comprehensive script offers the following capabilities:

1. Establishes a secure SSH connection to a remote server, using specified credentials.
2. Executes remote commands to retrieve detailed information about active WireGuard tunnels.
3. Parses the command output to extract crucial data such as allowed IP ranges and endpoint IPs.
4. Utilizes the `ipinfo.io` API to look up Internet Service Provider (ISP) information based on endpoint IPs.
5. Presents comprehensive details for each active WireGuard tunnel, including allowed IP ranges and associated ISPs.

### Features:

- **SSH Connection**: Connect securely to a remote server via SSH to gather WireGuard tunnel information.
- **ISP Lookup**: Utilize the `ipinfo.io` API to determine the ISPs associated with endpoint IP addresses.
- **Tunnel Details**: Display in-depth information for each active WireGuard tunnel, including IP ranges and ISPs.

### Usage:

#### Command Line Interface (CLI) Version:

1. Make sure to have the `paramiko` library installed using `pip install paramiko`.
2. Modify the `ssh_host`, `ssh_port`, `ssh_username`, and `ssh_password` variables in the script with your server's credentials.
3. Execute the script, and it will establish an SSH connection, retrieve tunnel data, and provide detailed insights for each tunnel.

```bash
main.py
```

#### Graphical User Interface (GUI) Version:

1. Ensure you have the required libraries installed, including `paramiko`, `requests`, and `tkinter`.
2. Modify the `ssh_host`, `ssh_port`, `ssh_username`, and `ssh_password` variables in the script with your server's credentials.
3. Execute the script, and it will open a GUI window where you can click a button to update the information displayed.

```bash
gui.py
```

Remember to handle sensitive information like SSH credentials and passwords with care. Always ensure proper permissions and adhere to security best practices.

Feel free to adapt and distribute this script to suit your requirements. If you encounter any challenges or have ideas for enhancements, don't hesitate to get in touch!
