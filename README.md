# RCE Payload Generator

This repository contains a Python-based payload generator designed for generating over **207,000 Remote Code Execution (RCE)** payloads, useful for penetration testing, vulnerability assessments, and security research.

The payloads are crafted to test common injection points in web applications, such as URL parameters, form inputs, and other user-controlled input vectors. This tool is focused on shell command injection, Java, Python, and PowerShell invocations, among others, to simulate potential attack vectors that an attacker might use in real-world exploitation scenarios.

### Contents

- **`generate_payloads.py`**: Python script for generating the payloads.
- **`rce.txt`**: Generated payloads saved in a text file (over 207,000 unique payloads).

### Features

- **Customizable Payloads**: The script supports different types of payloads including:
  - Basic enumeration commands (e.g., `whoami`, `id`, `ls -la`).
  - Advanced discovery commands (e.g., `find / -name '*.conf'`).
  - OS command execution via various injection points (e.g., `bash -c`, `powershell -Command`).
  - HTTP-based exploits (e.g., `curl`, `wget`, `powershell` commands).
  - Language-specific injection payloads (Java, Python, etc.).
  
- **Flexible Encoding**: Payloads are encoded in various formats to bypass security filters and firewalls:
  - URL encoding (`%` encoding for special characters).
  - Special character encoding to avoid detection by simple filters.
  - Escaped characters for payload obfuscation.

- **Combination of Prefixes and Suffixes**: The script generates payloads by applying various shell prefixes and suffixes to simulate different attack scenarios, such as chaining commands, adding comments, or redirecting output.

### Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/inpentest/rce
   cd rce
   ```

2. **Generate Payloads**:

Run the Python script to generate the payloads:

```bash
python generate_payloads.py
This will create a file named rce.txt containing all the generated payloads.
```

3. **Inspect Payloads**:

You can view the generated payloads directly in the rce.txt file. These payloads can be tested against vulnerable applications to verify RCE vulnerabilities.

4. **Customize Parameters**:

Modify the parameters, prefixes, payloads, and suffixes lists in the Python script to adjust the types of payloads generated based on your testing requirements.

### Important Note
This tool is intended for ethical penetration testing and security research only. Ensure you have explicit permission to test the target systems before using the generated payloads. Unauthorized use of these payloads may be illegal and unethical.

### License
This repository is licensed under the MIT License. See LICENSE for more information.
