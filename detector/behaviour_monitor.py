import os
import math
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep

def file_entropy(file_path):
    """Calculate Shannon entropy of a file"""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        if not data:
            return 0
        entropy = 0
        for x in range(256):
            p_x = data.count(bytes([x])) / len(data)
            if p_x > 0:
                entropy -= p_x * math.log2(p_x)
        return entropy
    except Exception as e:
        return 0

class RansomwareHandler(FileSystemEventHandler):
    def __init__(self, entropy_threshold=7.5):
        self.entropy_threshold = entropy_threshold

    def on_modified(self, event):
        if not event.is_directory:
            entropy = file_entropy(event.src_path)
            if entropy > self.entropy_threshold:
                print(f"⚠️ Suspicious activity detected: {event.src_path} (entropy={entropy:.2f})")

def monitor_folder(folder_path):
    event_handler = RansomwareHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    print(f"Monitoring folder '{folder_path}' for ransomware-like behavior...")

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
