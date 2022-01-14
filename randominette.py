# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    randominette.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayalla, sotto & dutesier                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/13 18:14:29 by dareias-          #+#    #+#              #
#    Updated: 2022/01/14 11:58:56 by dareias-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import json
from decouple import config
import time
#from oauthlib.oauth2 import WebApplicationClient

def main():
    mode = input("Mode (t for testing): ")
    if mode == "t" :
        client_id = config('42-UID-T')
        client_secret = config('42-SECRET-T')
        my_time = int(input("Time between requests: "))
    else :
        client_id = config('42-UID')
        client_secret = config('42-SECRET')
        my_time = 2
    authorization_base_url = "https://api.intra.42.fr/oauth/authorize"
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
    print("Response from POST request")
    print(access_token.text)
    access_token_j = access_token.json() 
    token = access_token_j["access_token"]
    print("Our token:")
    print(token)
    params = {
            "Authorization": f"Bearer {token}",
            }
    print("Our params:")
    print(params)
    time.sleep(my_time)
    users_in_campus = requests.get("https://api.intra.42.fr/v2/campus/38/locations", params=params)
    print("Response from GET request")
    print(users_in_campus.headers)
    print(users_in_campus.text)

if __name__ == '__main__':
    main()
#curl -X POST --data "grant_type=client_credentials&client_id=4750c51e351446aa3ca5c0e7059ccc066b9dfffc21e8ddce787a76971c56f984&client_secret=d885c04ae7c0857ee61b339ddf10c8b08ff424b802b51762fcd3dfb136d31e98" https://api.intra.42.fr/oauth/token
