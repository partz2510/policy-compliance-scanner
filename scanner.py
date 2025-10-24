import os, re, json, yaml
from rich.console import Console
from rich.table import Table

console = Console()

# Simple compliance rules
RISK_RULES = {
    "Public Access Enabled": re.compile(r'"?PublicAccess"?:\s*true', re.IGNORECASE),
    "Open Admin Port (22/3389)": re.compile(r'"?Port"?:\s*(22|3389)', re.IGNORECASE),
    "Weak Password Policy": re.compile(r'"?PasswordPolicy"?:\s*"?weak"?', re.IGNORECASE),
}

def scan_file(path):
    """Return list of rule names matched in the file."""
    with open(path, "r") as f:
        text = f.read()
    findings = [name for name, pat in RISK_RULES.items() if pat.search(text)]
    return findings

def main():
    console.print("[bold cyan]🔍 Security Policy Compliance Scanner[/bold cyan]\n")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("File", width=25)
    table.add_column("Findings", width=50)

    results = {}
    for file in os.listdir("configs"):
        path = os.path.join("configs", file)
        if not os.path.isfile(path):
            continue
        findings = scan_file(path)
        results[file] = findings
        table.add_row(file, ", ".join(findings) if findings else "[green]Compliant[/green]")

    console.print(table)
    with open("scan_report.json", "w") as f:
        json.dump(results, f, indent=2)
    console.print("\n[bold green]Report saved as scan_report.json[/bold green]")

if __name__ == "__main__":
    main()
