To fully work with the Reddit bot, you will first need to fill out praw.ini.

After that, execute these commands in the terminal in sequence:

python -m venv myenv

pip install -r requirements.txt

or manually install what is in requirements.txt

After all this, fill in these lines in request.py with your own in this format:

socks5://log:pass@ip:port
