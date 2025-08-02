""" Simple logger to trace memory steps """
import os

class MemoryLogger:
    def __init__(self, log_path='logs/agent_log.txt'):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        with open(self.log_path, 'w') as f:
            f.write("🔍 Agent Log
")

    def log(self, text: str):
        with open(self.log_path, 'a') as f:
            f.write(f"{text}\n")
