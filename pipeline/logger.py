import pickle
from datetime import datetime
from pathlib import Path

class PKLLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

    def log(self, data, filename_prefix="pipeline"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = self.log_dir / f"{filename_prefix}_{timestamp}.pkl"
        with open(file_path, "wb") as f:
            pickle.dump(data, f)
        print(f"[LOGGED] Data saved to {file_path}")
