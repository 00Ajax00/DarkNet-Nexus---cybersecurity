# crawler/tor_manager.py
import os
import time
import requests
import stem.process
from stem.control import Controller
from stem import Signal
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class TorManager:
    TOR_CONTROL_PORT = 9051
    TOR_SOCKS_PORT = 9050
    TOR_PASSWORD = "your_tor_password"  # Set this in torrc file

    def __init__(self):
        self.session = self._configure_tor_session()

    def _configure_tor_session(self):
        """Configures a session to route traffic through the Tor network."""
        session = requests.Session()
        session.proxies = {
            'http': f'socks5h://127.0.0.1:{self.TOR_SOCKS_PORT}',
            'https': f'socks5h://127.0.0.1:{self.TOR_SOCKS_PORT}'
        }

        # Retry logic for robustness
        retry = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def start_tor_process(self):
        """Starts the Tor process if it's not already running."""
        if not self._is_tor_running():
            print("[*] Starting Tor process...")
            return stem.process.launch_tor_with_config(
                config={
                    'SocksPort': str(self.TOR_SOCKS_PORT),
                    'ControlPort': str(self.TOR_CONTROL_PORT),
                    'HashedControlPassword': self.TOR_PASSWORD
                }
            )

    def _is_tor_running(self):
        """Checks if the Tor process is already running."""
        try:
            with Controller.from_port(port=self.TOR_CONTROL_PORT) as controller:
                controller.authenticate(password=self.TOR_PASSWORD)
                return True
        except Exception:
            return False

    def renew_ip(self):
        """Requests a new identity from Tor to change IP."""
        with Controller.from_port(port=self.TOR_CONTROL_PORT) as controller:
            controller.authenticate(password=self.TOR_PASSWORD)
            controller.signal(Signal.NEWNYM)
            time.sleep(10)  # Wait for Tor to establish a new circuit
            print("[*] Tor IP address changed.")

    def get_current_ip(self):
        """Fetches the current IP address seen by the web."""
        response = self.session.get("http://check.torproject.org/api/ip")
        if response.status_code == 200:
            return response.json().get("IP")
        return "Unable to retrieve IP"

    def request(self, url):
        """Makes a request through the Tor network."""
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"[*] Request error: {e}")
            return None

if __name__ == "__main__":
    tor_manager = TorManager()
    
    print("[*] Checking Tor IP...")
    print(f"Your current Tor IP: {tor_manager.get_current_ip()}")

    test_url = "http://check.torproject.org"
    print("[*] Fetching test page...")
    print(tor_manager.request(test_url))

    print("[*] Renewing IP...")
    tor_manager.renew_ip()
    print(f"New Tor IP: {tor_manager.get_current_ip()}")
