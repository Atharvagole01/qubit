"""

"""


import requests
from _links import links

# url = "https://linkedin-bulk-data-scraper.p.rapidapi.com/companies"

# payload = {
#     "links":links
# }

# headers = {
#     "x-rapidapi-key": "e6545e8a19msh298ac820737d44ep179512jsn4a3dca1da8fa",
#     "x-rapidapi-host": "linkedin-bulk-data-scraper.p.rapidapi.com",
#     "Content-Type": "application/json",
# }

# response = requests.post(url, json=payload, headers=headers)

# res = response.json()

from _sample_response import response


dataset = [
    (
        item['data']["companyId"],
        item['data']["companyName"],
        item['data']["employeeCount"],
        item['data']["followerCount"],
        item['data'].get("industry",None),
        item['data']["description"],
        item['data'].get("foundedOn",None).get('year',None),
        item['data']["universalName"]
    )
    for item in response['data']
]

print(dataset)