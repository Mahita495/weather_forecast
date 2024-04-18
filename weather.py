from tkinter import *
from tkinter import messagebox
import requests  
from configparser import ConfigParser


url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
c_file = 'config.inii'
c=ConfigParser()
c.read(c_file)
a_key = c['api_key']['key']

def weather_get(city):
    result = requests.get(url.format(city,a_key))
    if result:
        json=result.json()
        city = json['name']
        country=json['sys']['country']
        temp_k=json['main']['temp']
        temp_c =temp_k-273.15
        temp_f = (temp_k-273.15)*9/5 + 32
        icon=json['weather'][0]['icon']
        weather=json['weather'][0]['main']
        f=(city, country, temp_c, temp_f, icon, weather)
        return f
    else:
        return None
    
def search():
    city=text_city.get()
    weather = weather_get(city)
    global image 
    if weather:
        loc_label['text']='{} {}'.format(weather[0],weather[1])
        temp_label['text']='{:.2f} C, {:.2f} F'.format(weather[2],weather[3])
        w_label['text']=weather[5]

    else:
        messagebox.showerror('Error','Cannot find the city'.format(city))

    
w_window = Tk()
w_window.title("My Weather App")
w_window.config(background="light blue")
w_window.geometry("600x500")


text_city = StringVar()
entry_city = Entry(w_window, textvariable=text_city, fg="Blue", font=("Arial",30,"bold"))
entry_city.pack()


search_button = Button(w_window, text="Find weather", width=20, bg="blue", fg="light blue", font=("Arial",25,"bold"), command=search)
search_button.pack()

loc_label = Label(w_window, text="", font=("Arial",35,"bold"),bg="light pink")
loc_label.pack()


i=Label(w_window, bitmap='')
i.pack()

temp_label = Label(w_window, text="", font=("Arrial",35, "bold"), bg="light pink")
temp_label.pack()

w_label =Label(w_window,text="", font=("Arial",35,"bold"), bg="Light green")
w_label.pack()

w_window.mainloop()