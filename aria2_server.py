import os
import subprocess
import requests

def start_aria2_server():
    # نصب aria2
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "aria2"])

    # راه‌اندازی سرور
    os.makedirs("aria2", exist_ok=True)
    with open("aria2/aria2.conf", "w") as conf_file:
        conf_file.write("dir=./downloads\n")
        conf_file.write("file-allocation=none\n")
        conf_file.write("rpc-enable=true\n")
        conf_file.write("rpc-listen-port=6800\n")
        conf_file.write("rpc-secret=your_secret_token\n")

    subprocess.Popen(["aria2c", "--conf-path=aria2/aria2.conf", "--enable-rpc"])
    print("Aria2 server is running on port 6800 with token: your_secret_token")

if __name__ == "__main__":
    start_aria2_server()
