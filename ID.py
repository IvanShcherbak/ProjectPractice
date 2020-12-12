from TikTokApi import TikTokApi
import json

apiTT = TikTokApi()

GetTik = apiTT.getTikTokById('6875314617690623233')

with open("Follows.json", "w") as write_file:
   json.dump(GetTik,write_file,indent=4)

with open("Follows.json", "r") as read_file:
   Follows = json.load(read_file)

L = Follows["itemInfo"]["itemStruct"]["stats"]["diggCount"]

S = Follows["itemInfo"]["itemStruct"]["stats"]["shareCount"]

C = Follows["itemInfo"]["itemStruct"]["stats"]["commentCount"]

V = Follows["itemInfo"]["itemStruct"]["stats"]["playCount"]

F = Follows["itemInfo"]["itemStruct"]["authorStats"]["followerCount"]

ER = ((L + S + C + V)/F)*100
print(ER)