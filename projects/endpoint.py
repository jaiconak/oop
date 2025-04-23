import requests

resp = requests.get("http://google.com")
if resp.status_code == 200 :
    print ("Its up and running!")
else:
    print("Website is down")


websites = ['http://google.com', 'http://netflix.com', 'http://amazon.com']

for links in websites:
    resp = requests.get(links)
    if resp.status_code == 200:
        print(f"Link is up: {links}")
    else:
        print(f"Link is down:{links}")