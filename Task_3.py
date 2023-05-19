import requests
import json
    
final_list = [print(item['title']) for item in requests.get('https://api.stackexchange.com/2.3/questions?fromdate=1684195200&todate=1684454400&order=desc&sort=activity&tagged=python&site=stackoverflow').json()['items']]