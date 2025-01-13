import requests
from datetime import datetime


def send_msgs(**kwargs):
    token = "7989373647:AAHHdft372siCgYFRW8fB7OgZ_r2XHrVsxY"  

    user_id = "5493676904" 
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + user_id + "&text=" + f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S {kwargs}</b>')}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())

def send_msg(*args):
    token = "7989373647:AAHHdft372siCgYFRW8fB7OgZ_r2XHrVsxY"  

    user_id = "5493676904" 
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + user_id + "&text=" + f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S {args}</b>')}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())
