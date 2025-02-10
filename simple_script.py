import datetime
import platform

def main():
    """
    A simple script to demonstrate Jenkins build triggers.
    This script prints system and time information.
    """
    current_time = datetime.datetime.now()
    print(f"Jenkins Build Trigger Test")
    print(f"Script executed at: {current_time}")
    print(f"Running on: {platform.system()} {platform.release()}")
    print(f"Python version: {platform.python_version()}")

if __name__ == "__main__":
    main()