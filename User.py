from TikTokApi import TikTokApi
import json

apiTT = TikTokApi()

User = apiTT.byUsername('chillote')

print(json.dumps(User,indent=4))

with open("Foll.json", "w") as write_file:
   json.dump(User,write_file,indent=4)