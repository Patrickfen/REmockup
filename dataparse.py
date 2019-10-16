import requests

def get_response():
    response = requests.get('https://airstorage.nl/api/dl', auth=('****', '****'))
    return response.json()

def debug_out(data):
    print("id, biased, time")
    for item in data:
        print("{} {} {}".format(item['_ID'], item['biased'], item['_TS']))

def sort_listings(response):
    results = {}
    for k,v in response['sorted'].items():
        results[k] = len(v)
    return sorted(results['sorted'].items(), key=lambda kv: kv[1])
