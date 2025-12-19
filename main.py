from simulator.encryptor import encrypt_folder
from detector.behaviour_monitor import monitor_folder
from config import TEST_FOLDER, KEY_PATH
from threading import Thread
import time

print("⚠️ WARNING: This is a ransomware SIMULATION.")
print("Only files inside 'test_folder' will be encrypted.")

choice = input("Type YES to continue: ")

if choice == "YES":
    # Start monitoring in a separate thread
    monitor_thread = Thread(target=monitor_folder, args=(TEST_FOLDER,), daemon=True)
    monitor_thread.start()

    # Start encryption simulator
    encrypt_folder(TEST_FOLDER, KEY_PATH)
    print("✔ Simulation complete.")

    # Keep monitoring for a few seconds after encryption
    time.sleep(5)
    print("Monitoring finished.")
else:
    print("❌ Operation cancelled.")
