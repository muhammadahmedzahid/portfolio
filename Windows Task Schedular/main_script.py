import subprocess
import time
import threading


def run_script(script_path):
    while True:
        try:
            print(f"Starting {script_path}...")
            process = subprocess.Popen(["python", script_path],creationflags=subprocess.CREATE_NEW_CONSOLE)
            process.wait()  # Wait for the process to finish
            print(f"{script_path} stopped, restarting in 5 seconds...")
            time.sleep(5)  # Sleep for a few seconds before restarting
        except Exception as e:
            print(f"An error occurred with {script_path}: {e}")
            time.sleep(5)  # Sleep before attempting to restart


def restart_scripts(script_paths):
    threads = []
    for script_path in script_paths:
        thread = threading.Thread(target=run_script, args=(script_path,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    script_paths = [
        f"C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\Restarting Cron Job\\script_01.py",
        f"C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\Restarting Cron Job\\script_02.py"
    ]
    restart_scripts(script_paths)
