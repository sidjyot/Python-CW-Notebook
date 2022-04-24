#tracker.py - A Python program to tracker a mobile number location

from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root=Tk()
root.title("Phone Number Tracker")
root.geometry("365x584")
root.resizable(False,False)

#logo
logo=PhotoImage(file="./phone_tracker/images/logo_image.png")
Label(root,image=logo).place(x=240,y=70)

Heading=Label(root,text="TRACK NUMBER", font=("arial",14,"bold"))
Heading.place(x=70,y=110)

#entry
Entry_back=PhotoImage(file="./phone_tracker/images/search_button.png")
Label(root,image=Entry_back).place(x=20,y=190)


root.mainloop()

