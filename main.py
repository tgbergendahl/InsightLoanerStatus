import requests
import json

workspaceId = "b05cdfec-a5a3-44ee-b42b-733584cd353d"

url = f"https://api.atlassian.com/jsm/assets/workspace/{workspaceId}/v1/aql/objects"

headers = {"Authorization": "Basic dGhiMTkwMDd3b3JrQHVjb25uLmVkdTpBVEFUVDN4RmZHRjAwRW1nUlFKOUhNUTZzSklUVWdpMFd3Z2piWXhpdU1HTjZ6UFMtWmZhZVVYcjloZXljUGpVcTBqdE9hZXBYbTJnYXRsVzk5SFo1Nkh0X1h4Szl0dG1XUWM5RXhfWnFsUDhyMjUzZmlVMUljazh2OUtqb25xLWxDMzVTekF1enQ2OFlwTFA0ejlPME0tdmRuTzh5Wnl3SzBXWFhuaWNXLThSRG1PYnhqTFc1QU09REFDQkY0M0M",
           "Accept": "application/json"}

response = requests.request("GET", url, headers=headers)


print(json.dumps(json.loads(response.text),
      sort_keys=True, indent=4, separators=(",", ": ")))
