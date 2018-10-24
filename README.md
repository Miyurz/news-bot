# news-bot
My own news-bot that sends me news of my interest

Requirements:
- pyenv
- python 3.5+ or anaconda (switch with pyenv)
- pip install -r requirements.txt


To do:
- Check for best tts engine. Right now using pyspeak


- FAQ
1. pip install pycurl may fail on Mac. Do:
   - export PYCURL_SSL_LIBRARY=openssl
   - export LDFLAGS=-L/usr/local/opt/openssl/lib;export CPPFLAGS=-I/usr/local/opt/openssl/include;
   - pip install pycurl
