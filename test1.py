
import requests


url = "https://maker.ifttt.com/trigger/push_toline/with/key/jpI_ooi5j640Qddyzwc8H87Hq4Cmorv78rfNDFVyIzr?value1='這是用python傳的'&value2='測試2'"


r = requests.post(url)

print(r.status_code)
print(r.content)