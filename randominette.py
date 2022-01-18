# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    randominette.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayalla, sotto & dutesier                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/13 18:14:29 by dareias-          #+#    #+#              #
#    Updated: 2022/01/18 17:26:30 by dareias-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import json
import random
import sys
import pprint
from decouple import config
import time

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
    # Get Campus ID and Cluster from user
        campus = int(input("Campus ID (38 for Lisbon): "))
        cluster = int(input("Cluster: "))
        my_time = int(input("Time between requests: "))
    else :
        campus = 38
        cluster = 1
        my_time = 1
    client_id = config('42-UID')
    client_secret = config('42-SECRET')
    # Get authorization token
    token_url = "https://api.intra.42.fr/oauth/token"
    data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
            }
    access_token = requests.post(
            token_url,
            data,
            )
    ret = access_token.json()
    # Set pagination
    page = {
            "number": 1,
            "size": 50
            }
    # Pass our authorization token as a header
    headers = {
            "Authorization": f"{ret['token_type']} {ret['access_token']}",
            }
    # Pass our pagination definitions as a dict 
    params = {
            "page": page
            }
    time.sleep(my_time)
    url = f'https://api.intra.42.fr/v2/campus/{campus}/locations?sort=-end_at,host&filter[active]=true&range[host]=c{cluster}, c{cluster + 1}r00s00'
    #print(url)
    ret = requests.get(url, headers=headers, json=params)
    users_in_campus = ret.json()
    #pprint.pprint(users_in_campus)
    i = 0
    if len(users_in_campus) == 0:
        return (print(f"There are currently {i} active users in cluster {cluster} at campus {campus}"))

    # Check if we have all elements or if there are more pages
    if 'Link' in ret.headers and len(users_in_campus)==page['size'] :
        while True:
            time.sleep(my_time)
            page['number'] = page['number'] + 1
            ret =  requests.get(url, headers=headers, json=params)
            second_page = ret.json()
            users_in_campus = users_in_campus + second_page
            if len(second_page) != page['size']:
                break 
            #pprint.pprint(users_in_campus)
    # Get ammount of active users
    for student in users_in_campus:
        i = i + 1
    print(f"There are currently {i} active users in cluster {cluster} at campus {campus}")
    if i == 0:
        return
    # Pick a random user
    if i > 1:
        chosen_one = random.randrange(0, i - 1)
    if i == 1:
        chosen_one = 0
    print("The Chosen One is: ")
    print(users_in_campus[chosen_one]['user']['login'])
    print(users_in_campus[chosen_one]['user']['location'])

if __name__ == '__main__':
    main()
