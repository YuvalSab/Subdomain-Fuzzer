import requests

url = input("Enter The Target Domain: ")
with open("wordlist.txt") as f:
    wordlist = [line.strip() for line in f]

for subdomain in wordlist:
    subdomain_url = f"https://{subdomain}.{url}"
    try:
        response = requests.get(subdomain_url)
        if response.status_code == 200 or 302 or 403:
            print(f"Subdomain Found: https://{subdomain + '.' + url}")
    except requests.exceptions.ConnectionError:
        pass
