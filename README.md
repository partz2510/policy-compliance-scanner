# 🧩 Security Policy Compliance Scanner (Python)

A lightweight Python tool that scans configuration files (JSON / YAML) for risky or non-compliant settings such as open ports, weak password policies, and public resource access.  
Designed to simulate a mini-GRC (Governance, Risk & Compliance) control audit for both cloud and on-prem environments.

---

## 🚀 Features
✅ Detects risky settings such as:
- Public Access Enabled
- Open Admin Ports (22 / 3389)
- Weak Password Policy  
✅ Supports `.json` and `.yaml` configs  
✅ Colorized CLI report using **rich**  
✅ Exports structured summary to `scan_report.json`  

---

## ⚙️ Setup
```bash
git clone https://github.com/<your-username>/policy-compliance-scanner.git
cd policy-compliance-scanner
python -m venv .venv
.\.venv\Scripts\Activate.ps1    # Windows
# or
source .venv/bin/activate       # macOS/Linux
pip install -r requirements.txt
