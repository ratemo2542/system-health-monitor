# System Health Monitor

A lightweight terminal snapshot of CPU, memory, disk usage, and system uptime.

## Requirements
- Python 3.10+
- psutil

## Install and run
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python main.py
```

Optionally pass a disk path: `python main.py --path /` (Windows example: `--path C:\\`).

## Notes
Metrics are read from the local machine. Some process or disk details may be unavailable due to operating-system permissions.
