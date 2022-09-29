import requests

headers = {}
headers['Authorization']='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNjg0NDQ0LCJpYXQiOjE2NjM2ODQxNDQsImp0aSI6ImY1ZTJmYzljMmZlODQ3MDM4MTUzYWI5NzlkOWFmNGQ1IiwidXNlcl9pZCI6MX0.gUKTw4z-Z0oktGHswZ4a7bKSGKBMWjyVBNJ2qF2kAu8'
r=requests.get('http://127.0.0.1:8000/workers/', headers=headers)
print(r.text)