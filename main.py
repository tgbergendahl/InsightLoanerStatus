import requests
import json

workspaceId = "b05cdfec-a5a3-44ee-b42b-733584cd353d"

url = f"https://api.atlassian.com/jsm/assets/workspace/{workspaceId}/v1/aql/objects?objectSchema='Personal Computing'"

headers = {"Authorization": "Basic {key}",
           "Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

objectData = json.dumps(json.loads(response.text),
                        sort_keys=True, indent=4, separators=(",", ": "))

f = open("out.txt", "w")
f.write(objectData)
f.close()
