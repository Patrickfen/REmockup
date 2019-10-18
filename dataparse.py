import requests
import matplotlib.pyplot as plt
import numpy as np
import json

def get_response():
    response = requests.get('https://airstorage.nl/api/dl', auth=('****', '****'))
    return json.loads(response.text)

def debug_out(data):
    print("id, biased, time")
    for item in data:
        print("{} {} {}".format(item['_ID'], item['biased'], item['_TS']))

def sort_listings(response):
    results = {}
    for k,v in response['sorted'].items():
        results[k] = len(v)
    return sorted(results['sorted'].items(), key=lambda kv: kv[1])

"""
 - Parses the response into seperate lists for each purpose.
"""
def parse_response(responses):
    all_listings = []
    # print(responses[0])
    for response in responses:
        order_data = []
        # print(response[0])
        for key, value in response["order"].items():
            order_data.append((len(value), key))

        # Do something with timestamps
        all_listings.append(order_data)

    return all_listings

"""
 - Takes the both the best and worst listings and puts them into a frequency barchart.
"""
def graph_freq(order):
    lengths, names = list(zip(*order[0]))
    result = {name : 0 for name in names}
    
    for sub in order:
        lengths, names = list(zip(*sub))
        idx = np.argmax(lengths)
        result[names[idx]] += 1

    labels = [x.replace(" ", "\n") for _, x in sorted(zip(result.values(), result.keys()))]
    freqs = sorted(list(result.values()))
    plt.figure(figsize=(9,9))
    plt.bar(labels, freqs, label="Frequency of best chosen listing")
    plt.xticks(labels, rotation="vertical")
    plt.legend()
    plt.show()

    lengths, names = list(zip(*order[0]))
    result = {name : 0 for name in names}

    for sub in order: 
        lengths, names = list(zip(*sub))
        idx = np.argmin(lengths)
        print(idx)
        result[names[idx]] += 1
    
    labels = [x.replace(" ", "\n") for _, x in sorted(zip(result.values(), result.keys()))]
    freqs = sorted(list(result.values()))
    plt.figure(figsize=(9,9))
    plt.bar(labels, freqs, label="Frequency of worst listing")
    plt.xticks(labels, rotation="vertical")
    plt.legend()
    plt.show()

        
if __name__ == "__main__":
    response = get_response()
    parsed = parse_response(response)
    graph_freq(parsed)
