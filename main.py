import requests
import json
import credentials

workspaceId = "b05cdfec-a5a3-44ee-b42b-733584cd353d"
key = credentials.KEY
headers = {"Authorization": key,
           "Accept": "application/json"}
baseurl = f"https://api.atlassian.com/jsm/assets/workspace/{workspaceId}/v1/"


def getObjectSchema():
    addurl = f"objectschema/list"
    url = baseurl+addurl
    response = requests.request("GET", url, headers=headers)

    objectSchema = json.dumps(json.loads(response.text),
                              sort_keys=True, indent=4, separators=(",", ": "))

    with open("schema.txt", "w") as ofile:
        ofile.write(objectSchema)

    return


def getObjectSchemaTypes(schemaID):
    addurl = f"objectschema/{schemaID}/objecttypes/flat"
    url = baseurl+addurl
    response = requests.request("GET", url, headers=headers)

    schemaTypes = json.dumps(json.loads(response.text),
                             sort_keys=True, indent=4, separators=(",", ": "))

    with open("pcTypes.txt", "w") as ofile:
        ofile.write(schemaTypes)

    return


def getLoanerStatus():
    addurl = f"aql/objects?qlQuery=objectTypeId=59&resultPerPage=999&includeExtendedInfo=true"
    url = baseurl+addurl
    response = requests.request("GET", url, headers=headers)

    objectData = json.dumps(json.loads(response.text),
                            sort_keys=True, indent=4, separators=(",", ": "))

    with open("loaners.txt", "w") as ofile:
        ofile.write(objectData)

    return


if __name__ == "__main__":
    pcSchemaId = "7"
    # getObjectSchemaTypes(pcSchemaId)
    getLoanerStatus()
