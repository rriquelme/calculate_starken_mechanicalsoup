#! /usr/bin/python3

# import re
import mechanicalsoup

# Connect to starken
browser = mechanicalsoup.StatefulBrowser()
browser.open("http://www.starken.cl/cotiza-tu-envio/")
browser.select_form('form[action="/cotiza-tu-envio"]')
browser["ciudadOrigen"] = 104
browser["ciudadDestino"] = 1
browser["alto"] = 10
browser["ancho"] = 10
browser["largo"] = 10
browser["kilos"] = 1
string = str(browser.get_current_page().find_all(attrs={"for": "edit-verificacion"})[0])
leng = len("/sites/all/themes/starken/img/")
string = string[string.index("/sites/all/themes/starken/img/") + leng :]
n1 = string[0]
string = string[string.index("/sites/all/themes/starken/img/") + leng :]
signo = string[:2]
string = string[string.index("/sites/all/themes/starken/img/") + leng :]
n2 = string[0]

print(n1,signo,n2)

if signo=="11":
    browser["verificacion"] = str(int(n1)+int(n2))
if signo == "12":
    browser["verificacion"] = str(int(n1)-int(n2))
if signo == "13":
    browser["verificacion"] = str(int(n1)*int(n2))

browser.submit_selected()
result = browser.get_current_page()
print(result.find_all(attrs={"class","tabla-resultado-tabla"}))
string = str(result.find_all(attrs={"class","tabla-resultado-tabla"})[0])
print(string.split("</tr><tr>"))
print(string.index('$'))
aux = string.index('$')
print(string[aux:(aux+7)])



# print(result.find_all(attrs={"class","ts ts-n ts-n-dom"}))
# print(result.find_all(attrs={"class","ts ts-n ts-n-ag"}))



