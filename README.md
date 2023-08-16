## Secure Shell (SSH) Tunnel Monitor and ISP Lookup

This Python script utilizes the `paramiko`, `re`, and `requests` libraries to establish an SSH connection to a remote server and retrieve information about WireGuard (wg) tunnels, including IP address details and associated Internet Service Providers (ISPs). The script provides the following functionality:

1. Establishes an SSH connection to a remote server using specified credentials.
2. Executes a command remotely to retrieve information about active WireGuard tunnels.
3. Parses the output to extract allowed IP addresses and endpoint IP information.
4. Utilizes the `ipinfo.io` API to look up ISP information based on endpoint IPs.
5. Displays details of each tunnel, including the allowed IP range, endpoint IP, and associated ISP.

### Features:

- Securely connects to a remote server via SSH and retrieves WireGuard tunnel information.
- Looks up ISPs for endpoint IPs using the `ipinfo.io` API.
- Presents the details of each active WireGuard tunnel, including IP ranges and ISPs.

### Usage:

1. Ensure the `paramiko` library is installed (`pip install paramiko`) before running the script.
2. Modify the script's `ssh_host`, `ssh_port`, `ssh_username`, and `ssh_password` variables with your server's credentials.
3. Run the script, and it will establish an SSH connection, retrieve tunnel information, and display details for each tunnel.

Please exercise caution when handling sensitive information like SSH credentials and passwords. Ensure you have the necessary permissions and are complying with any relevant security practices.

Feel free to customize and distribute this script according to your requirements. If you encounter any issues or have suggestions for improvement, please let us know!
