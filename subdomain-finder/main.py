import requests

target = "google.com"

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
with open("wordlist.txt","r") as key_list:
    for word in key_list:
        word = word.strip()
        url = "https://" + word + "." + target
        response = make_request(url)
        print(url ,response)
