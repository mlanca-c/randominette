# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    randominette.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayalla, sotto & dutesier                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/13 18:14:29 by dareias-          #+#    #+#              #
#    Updated: 2022/01/18 12:37:18 by dareias-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import json
import random
import sys
from decouple import config
import time

#
# Some important key assumptions that will hopefully not need to be hardcoded in later versions:
# Right now, we know we only need to make two calls with a page size of 100 to get a list of all active logins at 42 Lisboa, but not all campus have 200 computers
# 
#
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
    ret = requests.get(f'https://api.intra.42.fr/v2/campus/{campus}/locations?sort=-end_at,host&filter[active]=true&range[host]=c{cluster}, c{cluster + 1}r00s00', headers=headers, json=params)
    users_in_campus = ret.json()
    # Check if we have all elements or if there are more pages
    if 'Link' in ret.headers:
        page['number'] = page['number'] + 1
        time.sleep(my_time)
        second_page =  requests.get(f'https://api.intra.42.fr/v2/campus/{campus}/locations?sort=-end_at,host&filter[active]=true&range[host]=c{cluster}, c{cluster + 1}r00s00', headers=headers, json=params).json()
        users_in_campus = users_in_campus + second_page
    # Get ammount of active users
    i = 0
    for student in users_in_campus:
        i = i + 1
    print(f"There are currently {i} active users in cluster {cluster} at campus {campus}")
    # Pick a random user
    if i:
        chosen_one = random.randrange(0, i - 1)
        print("The Chosen One is: ")
        print(users_in_campus[chosen_one]['user']['login'])
        print(users_in_campus[chosen_one]['user']['location'])

if __name__ == '__main__':
    main()
