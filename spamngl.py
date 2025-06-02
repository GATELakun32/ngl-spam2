import requests
import random
import string
import threading
import time
import os

# === CONFIGURATION ===
THREADS = 10  # Number of concurrent threads
MAX_RETRIES = 3  # How many times to retry failed requests
USER_AGENT_FILE = 'user-agents.txt'
PROXY_FILE = 'proxies.txt'

title = """
 ____  __.  _____ __________                         .__   
|    |/ _| /  _  \\______    \           ____    ____ |  |  
|      <  /  /_\  \|       _/  ______  /    \  / ___\|  |  
|    |  \/    |    \    |   \ /_____/ |   |  \/ /_/  >  |__
|____|__ \____|__  /____|_  /         |___|  /\___  /|____/
        \/       \/       \/               \//_____/       
"""

# === LOAD DATA ===
def load_list_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] File not found: {filename}")
        return []

user_agents = load_list_from_file(USER_AGENT_FILE)
proxies_list = load_list_from_file(PROXY_FILE)

# === DEVICE ID GENERATOR ===
def generate_device_id():
    parts = [8, 4, 4, 4, 12]
    return '-'.join(''.join(random.choices(string.ascii_lowercase + string.digits, k=p)) for p in parts)

# === SENDER FUNCTION ===
def send_message(username, message, use_proxy, delay, log_file):
    attempt = 0
    while attempt < MAX_RETRIES:
        headers = {
            'Host': 'ngl.link',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': random.choice(user_agents) if user_agents else 'Mozilla/5.0',
            'origin': 'https://ngl.link',
            'referer': f'https://ngl.link/{username}',
        }

        data = {
            'username': username,
            'question': message,
            'deviceId': generate_device_id(),
            'gameSlug': '',
            'referrer': '',
        }

        proxies = {}
        if use_proxy and proxies_list:
            proxy = random.choice(proxies_list)
            proxies = {'http': proxy, 'https': proxy}

        try:
            res = requests.post('https://ngl.link/api/submit', headers=headers, data=data, proxies=proxies, timeout=10)
            if res.status_code == 200:
                print(f"[+] Sent successfully to {username}")
                with open(log_file, 'a') as log:
                    log.write(f"SENT to {username}: {message}\n")
                break
            else:
                print(f"[-] Failed with status {res.status_code}")
        except Exception as e:
            print(f"[!] Error: {e}")
        attempt += 1
        time.sleep(delay)

# === MAIN FUNCTION ===
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(title)
    print("🔥 NGL SPAMMER by:KARTO 🔥\n")

    print("══════════════════════════════════")
    username = input("Masukkan NGL Username Target: @").strip()
    print("══════════════════════════════════")
    message = input("Masukkan Pesan yang akan dikirim: ").strip()
    print("══════════════════════════════════")
    count = int(input("Berapa pesan yang akan dikirim: "))
    print("══════════════════════════════════")
    delay = float(input("Jeda antar percobaan (dalam detik): "))
    print("══════════════════════════════════")
    use_proxy_input = input("Gunakan proxy? (y/n): ").strip().lower()
    use_proxy = use_proxy_input == 'y'
    print("══════════════════════════════════")
    log_file = 'spam_log.txt'

    threads = []
    for _ in range(count):
        t = threading.Thread(target=send_message, args=(username, message, use_proxy, delay, log_file))
        threads.append(t)
        t.start()
        if len(threads) >= THREADS:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    print("\n✅ Finished sending messages.")

if __name__ == "__main__":
    main()
