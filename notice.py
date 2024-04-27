import sys
sys.dont_write_bytecode = True


import time
import http.client as httplib
from telegram_bot_sender import tele_bot

# Function to check if laptop is connected to Internet


def have_internet() -> bool:
    conn = httplib.HTTPSConnection("8.8.8.8", timeout=5)
    try:
        conn.request("HEAD", "/")
        return True
    except Exception:
        return False
    finally:
        conn.close()


# Main function
def main():
    # Wait until laptop is connected to WiFi
    while not have_internet():
        print("Waiting for WiFi connection...")
        time.sleep(1)  # Check every 10 seconds
    print("Connected to WiFi and Internet!")
    msg = "Laptop turned ON"
    class_instance = tele_bot()
    class_instance.sen(msg)


if __name__ == "__main__":
    main()
