from dotenv import load_dotenv
import requests
from os import getenv
import re

load_dotenv()


def main():
    URL = getenv("URL")
    r = requests.get(URL)
    matched = re.findall(getenv("PATTERN"), r.text, re.M)
    if not len(matched):
        requests.post(getenv("POST_URL"))


        
    

if __name__ == "__main__":
    main()