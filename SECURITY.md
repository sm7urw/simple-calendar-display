cat << 'EOF' > SECURITY.md
# Security Policy

## Supported Versions

Currently, only the latest version of **Simple Calendar Display** is supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| Main    | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

I take the security of this project seriously. If you find any security-related issues or vulnerabilities, please **do not** open a public issue. Instead, please report them directly to me.

You can reach me by:
* Opening a private discussion on GitHub (if available)
* Or by contacting me via my GitHub profile details.

I will do my best to acknowledge your report within 48 hours and provide a fix as soon as possible.

## Best Practices for Users
Since this project displays data from a private iCal-link:
1. Never share your `update_calendar.py` or `.env` files if they contain your private iCal URL.
2. Ensure your Raspberry Pi is kept up to date with `sudo apt update && sudo apt upgrade`.
3. If running on a public network, ensure your port 8080 is protected by a firewall or only accessible via VPN/Tailscale.
EOF
