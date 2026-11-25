"""Display a one-shot snapshot of local system health."""
import argparse, platform, time
from datetime import timedelta
import psutil

def snapshot(disk_path=None):
    boot = psutil.boot_time()
    disk_path = disk_path or ("C:\\" if platform.system() == "Windows" else "/")
    vm = psutil.virtual_memory()
    disk = psutil.disk_usage(disk_path)
    return {
        "platform": f"{platform.system()} {platform.release()}",
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": vm.percent,
        "memory_used_gb": vm.used / (1024**3),
        "memory_total_gb": vm.total / (1024**3),
        "disk_percent": disk.percent,
        "disk_used_gb": disk.used / (1024**3),
        "disk_total_gb": disk.total / (1024**3),
        "uptime": str(timedelta(seconds=int(time.time()-boot))),
    }

def main():
    parser = argparse.ArgumentParser(description="Show local system health metrics.")
    parser.add_argument("--path", help="disk mount/path to inspect")
    args = parser.parse_args()
    try:
        data = snapshot(args.path)
    except (OSError, PermissionError) as exc:
        parser.error(f"Could not inspect disk: {exc}")
    print("SYSTEM HEALTH")
    print("=" * 42)
    print(f"System:       {data['platform']}")
    print(f"Uptime:       {data['uptime']}")
    print(f"CPU usage:    {data['cpu_percent']:.1f}%")
    print(f"Memory:       {data['memory_percent']:.1f}% ({data['memory_used_gb']:.2f}/{data['memory_total_gb']:.2f} GB)")
    print(f"Disk:         {data['disk_percent']:.1f}% ({data['disk_used_gb']:.2f}/{data['disk_total_gb']:.2f} GB)")

if __name__ == "__main__":
    main()
