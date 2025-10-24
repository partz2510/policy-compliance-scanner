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
```

## 🧠 Usage

Place your config files in the configs/ folder, then run:
```bash
python scanner.py
```

## 🧾 Example Output
![Security Policy Compliance Scanner](https://github.com/partz2510/policy-compliance-scanner/blob/main/screenshot/policy%20compliance%20scanner.png?raw=true)


## 🔮 Future Improvements

1. Add more compliance rules (e.g., encryption checks)

2. Assign severity levels (Low / Medium / High)

3. Add --path argument for scanning custom folders

## ✨ Author

Parthiban Ganesan
💼 Cybersecurity & Cloud Enthusiast
