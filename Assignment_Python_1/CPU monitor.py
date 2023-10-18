import psutil
def get_cpu_usage():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        return cpu_usage
    except Exception as e:
        print(f"Error: {e}")
        return None
def main(threshold=85):
    print(f"Monitoring CPU usage (Threshold: {threshold}%)...")

    while True:
        cpu_usage = get_cpu_usage()
        if cpu_usage is not None:
            print(f"CPU Usage: {cpu_usage}%")
            if cpu_usage > threshold:
                print(f"Alert: CPU usage exceeds {threshold}%!")
def main(threshold=90):
    print(f"Monitoring CPU usage (Threshold: {threshold}%)...")
    while True:
        cpu_usage = get_cpu_usage()
        if cpu_usage is not None:
            print(f"CPU Usage: {cpu_usage}%")
            if cpu_usage > threshold:
                print(f"Alert: CPU usage exceeds {threshold}%!")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")