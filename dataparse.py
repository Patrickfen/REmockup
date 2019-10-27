import requests
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import json
import matplotlib.colors as pltcolors
import collections

colors = ["yellow", "greenyellow", "limegreen", "mediumseagreen",
          "mediumaquamarine", "mediumturquoise", "deepskyblue", "steelblue",
          "darkblue", "darkmagenta"]

colorsrgb = list(map (pltcolors.to_rgba, colors))

def get_response():
    response = requests.get('https://airstorage.nl/api/dl', auth=('requirements', 'engineering'))
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
    listings = []
    biased_listings = []
    for response in responses:
        order_data = []
        if response["biased"] == True:
            destination = biased_listings
        else: 
            destination = listings
    
        for key, value in response["order"].items():
            order_data.append((len(value), key))
        destination.append(order_data)
        
    return (listings, biased_listings)

def get_seconds(prev, curr):
    DT_FMT = "%d/%m/%Y %H:%M:%S"
    if not prev: return 0
    dt_prev = datetime.strptime(prev, DT_FMT)
    dt_curr = datetime.strptime(curr, DT_FMT)
    dt_diff = dt_curr - dt_prev
    return dt_diff.total_seconds()

def parse2(responses):
    '''
        {
            biased:[
                {
                    id:1
                    list:[
                        {
                            name:name1,
                            score: highest,
                            time:...
                        },
                        ...,
                        {
                            name:name3,
                            score: lowest,
                            time:...
                        }
                    ]
                },
                ..user2,
                ..user3
            ]
            unbiased:[
                ..same as biased..
            ]
        }
    '''
    results = {'biased':[], 'unbiased':[]}
    # Loop all responses, which are all different users
    for user in responses:
        # loop vaiable to compare time + result object
        prev_ts = None
        user_result = {
            'list':[],
            'id':user['_ID'],
            'ts':user['_TS']
        }
        # Loop each listing of a user
        for (name, better_than, time) in zip(user['order'].keys(), user['order'].values(), user['timestamps']):
            user_result['list'].append({
                'name':name,
                'score':len(better_than),
                'time':get_seconds(prev_ts, time)
            })
            prev_ts = time
        # Sort this user's list of choices by score
        user_result['list'].sort(key=lambda x: x['score'])
        # Add this user to the correct list
        results['biased' if user['biased'] else 'unbiased'].append(user_result)
    return results


def get_freqs(order, biased_order):
    lengths, all_names = list(zip(*order[0]))
    result = {name : 0 for name in all_names}
    biased_result = {name : 0 for name in all_names}
    
    for sub in order:
        lengths, names = list(zip(*sub))
        idx = np.argmax(lengths)
        result[names[idx]] += 1
    
    for sub in biased_order:
        lengths, names = list(zip(*sub))
        idx = np.argmax(lengths)
        biased_result[names[idx]] += 1

    merged_result = [(key, value, biased_result[key]) for key, value in sorted(result.items(), key=(lambda x: x[0]))]
    biased_freqs = []
    freqs = []
    labels = []
    for item in merged_result:
        freqs.append(item[1])
        biased_freqs.append(item[2])
        labels.append("\n".join(item[0].split(" ")[:3]))
    

    biased_freqs = list(map (lambda x: x / sum(biased_freqs), biased_freqs))
    freqs = list(map (lambda x: x / sum(freqs), freqs))
    return (labels, freqs, biased_freqs)

def get_freqs_worst(order, biased_order):
    lengths, all_names = list(zip(*order[0]))
    print(all_names)
    result = {name : 0 for name in all_names}
    biased_result = {name : 0 for name in all_names}
    
    for sub in order:
        lengths, names = list(zip(*sub))
        idx = np.argmin(lengths)
        result[names[idx]] += 1
    
    for sub in biased_order:
        lengths, names = list(zip(*sub))
        idx = np.argmin(lengths)
        biased_result[names[idx]] += 1

    merged_result = [(key, value, biased_result[key]) for key, value in sorted(result.items(), key=(lambda x: x[0]))]
    biased_freqs = []
    freqs = []
    labels = []
    for item in merged_result:
        freqs.append(item[1])
        biased_freqs.append(item[2])
        labels.append("\n".join(item[0].split(" ")[:3]))
    
    biased_freqs = list(map (lambda x: x / sum(biased_freqs), biased_freqs))
    freqs = list(map (lambda x: x / sum(freqs), freqs))
    return (labels, freqs, biased_freqs)

"""
 - Takes the both the best and worst listings and puts them into a frequency barchart.
"""
def graph_freq(order, biased_order, title):
    labels, freqs, biased_freqs = get_freqs(order, biased_order)
    # biased_labels, biased_freqs = get_freqs(biased_order)

    ind = np.arange(len(freqs))
    width = 0.2
    plt.figure(figsize=(9,9))
    fig, ax = plt.subplots(figsize=(9,9))
    rects1 = ax.bar(ind - width/2, freqs, width,
                label='Unbiased')
    rects2 = ax.bar(ind + width/2, biased_freqs, width,
                label='Biased')

    plt.xticks(ind, labels, rotation='vertical', weight="8")
    plt.title(title.format("Best"))
    plt.legend()
    plt.ylabel("Frequency chosen as best normalised to the number of participants")
    plt.xlabel("Listings")

    plt.ylim(0, 0.9)
    plt.subplots_adjust(bottom=0.15)

    plt.savefig("./graphs/best_both.png")

    
    labels, freqs, biased_freqs = get_freqs_worst(order, biased_order)

    ind = np.arange(len(freqs))
    width = 0.2
    plt.figure(figsize=(9,9))
    fig, ax = plt.subplots(figsize=(9,9))
    rects1 = ax.bar(ind - width/2, freqs, width,
                label='Unbiased')
    rects2 = ax.bar(ind + width/2, biased_freqs, width,
                label='Biased')

    plt.ylim(0, 0.9)
    plt.xticks(ind, labels, rotation='vertical', weight="8")
    plt.ylabel("Frequency chosen as worst normalised to the number of participants")
    plt.xlabel("Listings")
    plt.legend()
    plt.subplots_adjust(bottom=0.15)
    plt.title(title.format("Worst"))
    plt.savefig("./graphs/worst_both.png")


'''
shows the time of each choice that each user had to make.
'''
def graph_time(responses, name, title, color, both=True):
    if not both:
        plt.figure()
    plt.xlabel("Listing rounds")
    plt.ylabel("Time in seconds")
    plt.title(title)
    
    times = []
    for user in responses:
        user_time = [listing["time"] for listing in user["list"]]
        times.append(user_time)
        # plt.plot(np.arange(0, len(times)), times, label=user["id"])

    rounds = [[] for _ in range(10)]
    for user in times:
        for idx, time in enumerate(user):
            if time < 150:
                rounds[idx].append(time)

    average = [np.mean(r) for r in rounds]
    minimum = [np.amin(r) for r in rounds]
    maximum = [np.amax(r) for r in rounds]
    stddev = [np.std(r) + np.mean(r) for r in rounds]
    minstddev = []
    for r in rounds: 
        temp = np.mean(r) - np.std(r)
        if temp < 0:
            temp = 0
        minstddev.append(temp)

    plt.plot(np.arange(0, len(average)), average, label="averages {}".format(name))
    if not both:
        plt.plot(np.arange(0, len(minimum)), minimum, label="minimum")
        plt.plot(np.arange(0, len(maximum)), maximum, label="maximum")
    ax = plt.gca()

    ax.fill_between(np.arange(0,10), stddev, minstddev, facecolor=(color[0], color[1], color[2], 0.5), 
            interpolate=True, label="standard deviation {}".format(name))

    if not both:
        plt.legend()
        plt.savefig("./graphs/times_{}.png".format(name))

def graph_time_both(objects):
    plt.figure()

    graph_time(
        objects["biased"], 
        "biased", 
        "Biased Amount of Time spent on each listing", 
        pltcolors.to_rgba(colors[6])
    )  
    graph_time(
        objects["unbiased"], 
        "unbiased", 
        "Biased Amount of Time spent on each listing",
        pltcolors.to_rgba(colors[0])
    )
    plt.legend()
    plt.savefig("./graphs/times_{}.png".format("both"))
    # plt.figure()

def get_googleform_times(objects):
    res = []
    for item in objects['biased'] + objects['unbiased']:
        res.append({'id':item['id'], 'ts':item['ts']})
    return res
        
def create_samplePlot(biased, listings):
    plt.figure()
    plt.bar(np.arange(0,2), [len(listings), len(biased)])
    plt.xticks(np.arange(0,2), ["Non-Biased", "Biased",])
    plt.title("Distribution Biased vs Non Biased")
    plt.ylabel("Frequency")
    plt.savefig("./graphs/sample.png")


if __name__ == "__main__":
    response = get_response()
    # print(response)
    biased, listings = parse_response(response)
    graph_freq(listings, biased, "{} Non biased vs Biased listings")
    # graph_freq(biased, "Biased", "Biased {} listing, n = {}")


    print("==parse2==")
    objects = parse2(response)
    graph_time_both(objects)

    print("==crossref google==")
    print(get_googleform_times(objects))

    create_samplePlot(biased, listings)
