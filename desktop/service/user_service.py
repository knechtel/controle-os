import requests

def user_find(login,password):
    url = 'http://ec2-52-67-56-229.sa-east-1.compute.amazonaws.com:8080/user-find'
    myobj = {'login': login, 'password':password}
    x = requests.post(url, json = myobj)

    try:
        return x.json()
    except:
        return None