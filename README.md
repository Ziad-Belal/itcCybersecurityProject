--> ProjectStructure : 
itcCybersecurityProject/
│
├── main.py
├── config.py
│
├── simulator/
│   ├── encryptor.py
│   └── decryptor.py
│
├── detector/
│   └── behavior_monitor.py
│
├── recovery/
│   └── restore.py
│
├── test_folder/        ← ONLY this folder is touched
│
└── keys/
    └── key.bin

--> Project Architecture: 
User Test Folder
      ↓
Encryption Simulator (AES)
      ↓
Behavior Monitor
      ↓
Detection Engine
      ↓
Alert System
      ↓
Recovery Module

