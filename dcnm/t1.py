import http.client
import ssl

conn = http.client.HTTPConnection("10.18.190.94")

payload = "{\n\t'expirationTime': 0\n}"

headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': "Basic ZGVtb3VzZXI6ZGVtb0RDTk0xMjM=",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Cache-Control': "no-cache",
    'Postman-Token': "fec090b0-7e72-4cc8-b76e-369b362bc7b9,c83057a5-1a16-4917-a871-1d7ea7d999d2",
    'Host': "10.18.190.94",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "24",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

conn.request("POST", "rest,logon", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

