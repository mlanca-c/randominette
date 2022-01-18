# randominette :electric_plug:
*"Push your work my little piscinner"* - Drop, probably.
## Purpose
The purpose of this project is to create a python script that uses 42's API to return a random students login and location in the selected campus and cluster.

## Usage
Running the script with no Command Line Arguments will retrive you a user from 42 Lisboa's campus at cluster 1 that is currently active. Alternativelly, if you'd like to select a specific campus or cluster you can run
```
randominette -s
```
## Requirements
Besides those defined in the requirements.txt file, you must have set the following two environment variables:
| Variable | Expansion |
| ----------- | ----------- |
| 42-UID | The UID provided by 42's platform |
| 42-SECRET | The Secret token provided by 42's platform |

## Resources
Since we're all (*the three of us*) new to python,  here are some helpful resources:
| Subject | Link |
| ----------- | ----------- |
| Python for C Programmers | [CS50 40-minute semminar](https://www.youtube.com/watch?v=Q98L3yaNEao&ab_channel=CS50) to learn the basics of Python for those proficient in C. |
| Virtual Environments | [Documentation](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a,part%20of%20your%20operating%20system.) and [Youtube tutorial](https://youtu.be/N5vscPTWKOk).|
| Requests Library | We access the API via HTTP requests. There is a [library](https://docs.python-requests.org/en/latest/) that makes it very "user-friendly". |
| Decouple Library | We store our tokens in a .env file so that we don't share them in our code. That is done with the [Decouple library](https://pypi.org/project/python-decouple/). |
| 42's API | We can access all loads of 42 stuff via its [API](https://api.intra.42.fr/apidoc).|
| OAUTH2 | 42's API uses OAUTH2 for authentication. You can learn about OAUTH2 [here](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2) and about its specific implementation in 42's API [here](https://api.intra.42.fr/apidoc/guides).|


