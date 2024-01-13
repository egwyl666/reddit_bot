import praw
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry  # Direct import from urllib3

# Setting up a proxy for requests
proxies = {
    'http': 'socks5://log:pass@ip:port',
    'https': 'socks5://log:pass@ip:port'
}

# Creating a requests session with proxy settings
session = requests.Session()
session.proxies.update(proxies)

# Configuring retries for the session
retries = Retry(total=5, backoff_factor=0.1)
session.mount('http://', HTTPAdapter(max_retries=retries))
session.mount('https://', HTTPAdapter(max_retries=retries))

# Using a custom session in praw
mybot = praw.Reddit("bot1", requestor_kwargs={'session': session})
