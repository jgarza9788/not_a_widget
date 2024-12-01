import subprocess

def get_cpu_usage():
    """Get CPU usage percentage using bash commands."""
    try:
        result = subprocess.run(
            "top -bn1 | grep 'Cpu(s)' | awk '{print 100 - $8}'",
            shell=True,
            capture_output=True,
            text=True,
        )
        return float(result.stdout.strip())
    except Exception as e:
        print(f"Error getting CPU usage: {e}")
        return None

def get_memory_usage():
    """Get Memory usage percentage using bash commands."""
    try:
        result = subprocess.run(
            "free | grep Mem | awk '{print $3/$2 * 100.0}'",
            shell=True,
            capture_output=True,
            text=True,
        )
        return float(result.stdout.strip())
    except Exception as e:
        print(f"Error getting Memory usage: {e}")
        return None

def get_gpu_usage():
    """Get GPU usage percentage using bash commands via nvidia-smi."""
    try:
        result = subprocess.run(
            "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits | awk '{print $1}'",
            shell=True,
            capture_output=True,
            text=True,
        )
        return float(result.stdout.strip())
    except Exception as e:
        print(f"Error getting GPU usage: {e}")
        return None

def main():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    gpu_usage = get_gpu_usage()

    print(f"CPU Usage: {cpu_usage:.2f} %")
    print(f"Memory Usage: {memory_usage:.2f} %")
    print(f"GPU Usage: {gpu_usage:.2f} %" if gpu_usage is not None else "GPU Usage: Not available")

if __name__ == "__main__":
    main()
