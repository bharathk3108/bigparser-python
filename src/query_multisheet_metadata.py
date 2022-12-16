import requests
import json

grid_url = "https://www.bigparser.com/api/v2/grid/62da9478e2e1aa116a14716b/query_multisheet_metadata"
headers =  {"authId":"a12703ef-e959-446b-938b-d2aec0511ec5"}
 
response = requests.get(grid_url,headers)
responseData = json.loads(response.content)

print(responseData)