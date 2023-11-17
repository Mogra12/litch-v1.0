from requests import get
import json
import pprint


def whois():
    API_KEY = "68bc4792f39b4f4397bb67f7fa59f14d"

    ip_domain = input("IP/Domain: ")
    url = f"https://api.whoisfreaks.com/v1.0/whois?apiKey={API_KEY}&whois=live&domainName={ip_domain}"
    response = get(url)
    data = response.json()
    object = json.dumps(data, indent=4)  
    create_file = input('Wish create an archive?[Y][N]: ').upper()

    if create_file == 'Y':
        with open('domain_lookup.json','w') as source:
            source.write(object)
            print('File created!')
    elif create_file == 'N':
        pprint.pprint(data)
    else:
        print('ERROR')
        