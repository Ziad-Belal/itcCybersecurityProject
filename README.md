






# 🛡️ Ransomware Behavior Simulation & Defense Framework

A **Python-based cybersecurity project** that simulates ransomware behavior in a **controlled and ethical environment**, detects suspicious file activity in real time, and provides safe recovery mechanisms.

> ⚠️ This project does **NOT** create real ransomware.  
> It is strictly designed for **educational, defensive, and research purposes**.

---

## 📌 Project Overview

Ransomware is one of the most dangerous modern cyber threats.  
This project demonstrates how ransomware operates **at a behavioral level**, and how such attacks can be **detected and mitigated** without causing real harm.

The system:
- Simulates file encryption **only inside a controlled test folder**
- Monitors ransomware-like behavior in real time
- Detects suspicious encryption patterns using entropy analysis
- Alerts the user during the simulation
- Allows secure recovery and decryption of files

---

## 🎯 Objectives

- Understand ransomware behavior without creating malware
- Demonstrate secure cryptographic file handling
- Detect suspicious activity using behavioral indicators
- Apply defensive cybersecurity principles
- Build a competition-safe and ethical project

---

## 🧱 Project Architecture

```

ransomware_sim/
│
├── main.py                 # Entry point
├── config.py               # Global configuration
│
├── simulator/
│   ├── encryptor.py        # Controlled encryption simulator (AES)
│   └── decryptor.py        # Safe recovery & decryption
│
├── detector/
│   └── behavior_monitor.py # Ransomware behavior detection
│
├── recovery/
│   └── restore.py          # (Reserved for future enhancements)
│
├── test_folder/            # Controlled test environment
│
├── keys/                   # Encryption keys (ignored by Git)
│
├── requirements.txt
└── README.md

````

---

## 🔐 Security Design Principles

✔ Explicit user consent before encryption  
✔ Test folder isolation  
✔ No persistence or auto-execution  
✔ No privilege escalation  
✔ No network propagation  
✔ Defensive and educational intent  

---

## 🧪 Detection Methodology

The detection engine monitors the file system for ransomware-like behavior, including:

- Rapid file modifications
- High-entropy file content (encrypted data)
- Abnormal file change patterns

**Entropy-based detection** is used to identify encrypted files, a common indicator of ransomware activity.

---

## 🔄 Recovery & Decryption

- Files encrypted during the simulation can be safely restored
- AES encryption keys are stored locally and securely
- Integrity is preserved throughout the recovery process

---

## ⚙️ Installation (Ubuntu)

### 1️⃣ Prerequisites

```bash
sudo apt update
sudo apt install python3-full python3-venv -y
````

### 2️⃣ Clone Repository

```bash
git clone <repository-url>
cd ransomware_sim
```

### 3️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Place test files inside `test_folder/`
2. Run the project:

```bash
python3 main.py
```

3. Confirm the simulation when prompted
4. Observe real-time detection alerts
5. Restore files using the decryption option

---

## ⚠️ Important Notes

* This project **must NOT** be run with `sudo`
* Only files inside `test_folder/` are affected
* Encryption keys are excluded from version control
* Intended strictly for **cybersecurity education and competitions**

---

## 🏆 Competition Relevance

This project demonstrates:

* Ethical ransomware research
* Defensive cybersecurity engineering
* Secure cryptographic implementation
* Real-time behavior monitoring
* Linux-based Python development

---

## 📚 Technologies Used

* Python 3
* cryptography (AES – Fernet)
* watchdog
* psutil
* Linux file system monitoring

---

## 👥 Team Collaboration

* Virtual environments used for dependency isolation
* `.gitignore` prevents sensitive data leakage
* `requirements.txt` ensures reproducibility

---

## 📜 Disclaimer

This software is intended **solely for educational and research purposes**.
The authors take no responsibility for misuse of this project.

---

## ✅ Status

**Project completed and competition-ready.**

```

---

## 🏁 Final Advice (VERY IMPORTANT)

If a judge reads **only your README**, they will immediately see:
- Ethics
- Defensive intent
- Professional structure
- Cybersecurity understanding

This README alone already puts you **above many teams**.

---

If you want, next I can:
- Prepare **presentation slides**
- Write a **2-minute judge explanation script**
- Add a **GUI dashboard** for extra points

Just tell me 👍
```
