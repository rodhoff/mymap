import requests


def retrieve_token():
    url = 'https://prod-api.plugfield.com.br/login'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key' : 'GGKuXMdgUb4ZlPulr7WdU5qRRlAIvOHh6fOWoUh5'      
    }
    data = {
        "username" : "claudio@ltecno.com.br",
        "password" : "Cl@udio12"
    }
    
    response = requests.post(url=url, headers=headers, json=data)
    
    print("Status code:", response.status_code, ",", response.json())
    




def retrieve_devices():
    url = "https://prod-api.plugfield.com.br/device?page=1"
    headers = {
        'Content-Type': 'application/json',
        'x-api-key' : 'GGKuXMdgUb4ZlPulr7WdU5qRRlAIvOHh6fOWoUh5',
        'Authorization' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjM1OTYsImFjY291bnRJZCI6MjYwOTgsInVzZXJuYW1lIjoiY2xhdWRpb0BsdGVjbm8uY29tLmJyIiwiaWF0IjoxNzAxODc1NDA3fQ.3mJLCtOPGTo9NwjGW0yzH-JD6Jby6OZWNLRsr3Pc7Z4'
            }


    response = requests.get(url, headers=headers)
    
    print(response.status_code, ", ", response.json())


    
    