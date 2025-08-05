#!/usr/bin/env python3
import subprocess
import time
import os


seen_ttys = set()

def get_logged_in_users():
    try:
        output = subprocess.check_output(["who"]).decode()
        for line in output.strip().splitlines():
            parts = line.split()
            if len(parts) >= 5:
                username = parts[0]
                tty = parts[1]
                ip = parts[4]

                
                if tty in seen_ttys:
                    continue

                
                seen_ttys.add(tty)
                print("=== New SSH Session Detected ===")
                print("User: {}\nTTY:  {}\nFrom: {}\n".format(username, tty, ip))

                
                print("Active processes:")
                try:
                    ps_out = subprocess.check_output(["ps", "-t", tty, "-o", "pid,cmd"]).decode()
                    print(ps_out)
                except subprocess.CalledProcessError:
                    print("  Unable to fetch processes.\n")

                print("-" * 40)

    except Exception as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    while True:
        get_logged_in_users()
        time.sleep(5)  
