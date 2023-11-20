import requests
import düzenle

düzenle.main("192.168.1.39","10.0.2.4",__file__)

site = "http://192.168.1.39"
login = "http://192.168.1.39/bWAPP/login.php"
data = {"login":"bee","password":"bug","form":"submit"}

session = requests.session()
session.post(login,data=data)

içerik = requests.get(site).text

print(session.get("http://192.168.1.39/bWAPP/htmli_post.php").text)

durum_kodu = requests.get(site).status_code
