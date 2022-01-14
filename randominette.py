# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    randominette.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayalla, sotto & dutesier                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/13 18:14:29 by dareias-          #+#    #+#              #
#    Updated: 2022/01/14 08:01:29 by dareias-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import json
#from oauthlib.oauth2 import WebApplicationClient

def main():
    client_id = '4750c51e351446aa3ca5c0e7059ccc066b9dfffc21e8ddce787a76971c56f984'

    client_secret = input("Enter Secret: ")
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
    print(access_token.text)
    access_token_j = access_token.json() 
    token = access_token_j["access_token"]
    print(token)
    params = {
            "Authorization": f"Bearer {token}",
            "filter": "[id]=28"
            }
    print(params)
    users_in_campus = requests.get("https://api.intra.42.fr/v2/campus_users", params=params)
    print(users_in_campus.headers)
    print(users_in_campus.text)

if __name__ == '__main__':
    main()
#curl -X POST --data "grant_type=client_credentials&client_id=4750c51e351446aa3ca5c0e7059ccc066b9dfffc21e8ddce787a76971c56f984&client_secret=d885c04ae7c0857ee61b339ddf10c8b08ff424b802b51762fcd3dfb136d31e98" https://api.intra.42.fr/oauth/token
