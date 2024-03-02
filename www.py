from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root=Tk()
root.title("weather app")
root.geometry("900x500+300+200")
# root.configure(bg="#57adff")
root.resizable(False,False)

def getWeather():
    try:
        
        city=textfield.get()
    
        geolocator= Nominatim(user_agent="geoapiExercise")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        # print(result)
        #ptoblem yaha pe aa raha hai 
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRNENT WEATHER")
    
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c349054f7765dd952ec19837fc9c0da1"
   
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']



        t.config(text=(temp,"°"))
        c.config(text=(condition,"|", "FEELS", "LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")






#search box
Search_image=PhotoImage(file="searc.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")

textfield.place(x=50,y=40)
textfield.focus()
#icon
Search_icon=PhotoImage(file="icon1.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#logo

logo_img=PhotoImage(file="logo.png")
logo=Label(image=logo_img)
logo.place(x=150,y=100)

#bottom box
Frame_img=PhotoImage(file="box.png")
Frame_myimage=Label(image=Frame_img)
Frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)



#label
Label1=Label(root,text="WIND",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label1.place(x=130,y=400)


Label2=Label(root,text="HUMIDITY",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label2.place(x=260,y=400)

Label3=Label(root,text="DESCRIPTION",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label3.place(x=430,y=400)

Label4=Label(root,text="PRESSURE",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label4.place(x=620,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)


w=Label(text=".....",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=140,y=430)

h=Label(text=".....",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text=".....",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=460,y=430)

p=Label(text=".....",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=650,y=430)



root.mainloop()