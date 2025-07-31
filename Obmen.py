import requests
import json
from tkinter import *
from tkinter.ttk import meessagebox as mb


def

window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты").pack(padx=10, pady=10)

entry = Entry(window)
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()

#import pprint
#result = requests.get("https://open.er-api.com/v6/latest/USD")
#data = json.loads(result.text)
#p = pprint.PrettyPrinter(indent=4)
#p.pprint(data)