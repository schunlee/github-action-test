import requests
requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a7a7f25b-45dc-4201-aa72-33e43c41b792',json={"msgtype": "text","text": {"content": "Hello from Github Action 😁"}})
