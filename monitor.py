"""Print a system health snapshot."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import psutil

def snapshot() -> dict:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(str(Path.home().anchor or "/"))
    processes = []
    for proc in psutil.process_iter(["pid", "name", "memory_info"]):
        try:
            info = proc.info
            mem = info["memory_info"].rss if info.get("memory_info") else 0
            processes.append({"pid": info["pid"], "name": info.get("name") or "unknown",
                              "memory_mb": round(mem / (1024 * 1024), 1)})
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    processes.sort(key=lambda item: item["memory_mb"], reverse=True)
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "cpu_percent": cpu, "logical_cpus": psutil.cpu_count(),
        "memory": {"total_gb": round(memory.total / 1e9, 2), "used_percent": memory.percent},
        "disk": {"mount": str(Path.home().anchor), "total_gb": round(disk.total / 1e9, 2),
                 "used_percent": disk.percent},
        "top_processes": processes[:10]
    }

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="Save snapshot to a JSON file")
    args = parser.parse_args()
    data = snapshot()
    print(json.dumps(data, indent=2))
    if args.json:
        args.json.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(f"Saved {args.json}")

if __name__ == "__main__":
    main()
