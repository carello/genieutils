import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://10.18.190.94/rest/logon"

payload = "{\n\t'expirationTime': 0\n}"
headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': "Basic ZGVtb3VzZXI6ZGVtb0RDTk0xMjM=",
    'Cache-Control': "no-cache",
    'Host': "10.18.190.94",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "24",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)
