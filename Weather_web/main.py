from tkinter import *

import requests as requests


def Menu_widgets():
    '''
    The function creates widgets for menu
    '''

    menu_label = Label(Menu_frame, text='Weather', fg='black', font=('Arial', 30, 'bold')).grid(column=0, row=0, padx=130, pady=50)

    Button(Menu_frame, text="Look weather", command=Go_to_weather, font=('Arial', 15)).grid(column=0, row=1, padx=20, pady=5)
    Button(Menu_frame, text="Translate degrees", command=Go_to_translator, font=('Arial', 15)).grid(column=0, row=2, padx=20, pady=5)
    Button(Menu_frame, text="Exit", command=exit_out, font=('Arial', 15)).grid(column=0, row=4, padx=20, pady=5)
    Button(Menu_frame, text='Rules', command=GoToRules, font=('Arial', 15)).grid(column=0, row=3, padx=20, pady=5)

def Weather_widgets():
    '''
    The function creates widgets for weather
    '''

    weather_label = Label(Weather_frame, text="You can look weather in different towns", fg='black', font=('Arial', 12, 'bold')).grid(column=0, row=0, padx=50, pady=5)

    Button(Weather_frame, text='Look Weather', font=('Arial', 10), command=get_weather).grid(column=0, row=2, padx=20, pady=5)
    Button(Weather_frame, text='Back to menu', font=('Arial', 10), command=BackToMenu).grid(column=0, row=4, padx=20, pady=5)


def Translator_widgets():
    '''
    The function creates widgets for translator
    '''

    Translator_label = Label(Translator_frame, text='You can translate degrees', fg='black', font=('Arial', 12, 'bold')).grid(column=0, row=0, padx=100, pady=5)
    Button(Translator_frame, text='Translate Farenheit', font=('Arial', 10), command=translateF).grid(column=0, row=2, padx=20, pady=5)
    Button(Translator_frame, text='Translate Celsius', font=('Arial', 10), command=translateC).grid(column=0, row=6, padx=20, pady=5)
    Button(Translator_frame, text='Back to menu', font=('Arial', 10), command=BackToMenu).grid(column=0, row=8, padx=20, pady=5)

def exit_out():
    '''
    The function closes the program
    '''

    tk.destroy()

def Go_to_weather():
    '''
    The function sends the user to weather
    '''

    Translator_frame.grid_forget()
    Menu_frame.grid_forget()
    Rules_frame.grid_forget()

    Weather_frame.grid(column=0, row=0, padx=20, pady=5)

def Go_to_translator():
    '''
    The function sends the user to translator
    '''

    Weather_frame.grid_forget()
    Menu_frame.grid_forget()
    Rules_frame.grid_forget()

    Translator_frame.grid(column=0, row=0, padx=20, pady=5)

def get_weather():
    '''
    Function for getting weather data in the city
    '''

    city = EnterCity.get()

    key = '3f375f09550c70c78ee98a0892836f05'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    param = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=param)
    weather = result.json()

    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'

def translateF():
    '''
    The function tranlate Farenheit to Celsius
    '''
    Far = EnterFar.get()

    Celsius = float((float(Far) - 32)*(5/9))

    Celsius = float(('{:.2f}'.format(Celsius)))
    Cel['text'] = Celsius

def BackToMenu():
    '''
    The function returns user to menu
    '''

    Weather_frame.grid_forget()
    Translator_frame.grid_forget()
    Rules_frame.grid_forget()

    Menu_frame.grid(column=0, row=0, padx=20, pady=5)

def Rules_widjets():
    '''
    The function creates widgets for rules
    '''

    rule_label1 = Label(Rules_frame, text='Welcome to the weather app!', fg='black', font=('Arial', 10, 'bold')).grid(column=0, row=1, padx=0, pady=5)
    rule_label2 = Label(Rules_frame, text='Enter cities only in English.', fg='black', font=('Arial', 10, 'bold')).grid(column=0, row=2, padx=0, pady=5)
    rule_label3 = Label(Rules_frame, text='Please do not enter too many cities, as we use the free version of the API, otherwise we will have to pay.', fg='black', font=('Arial', 10, 'bold')).grid(column=0, row=3, padx=0, pady=5)
    rule_label4 = Label(Rules_frame, text='You can only translate from Fahrenheit to Celsius, since our application displays the weather in Fahrenheit, for convenience, we have made a translation in Celsius.', fg='black', font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=0, pady=5)
    rule_label5 = Label(Rules_frame, text='Enter a number with a dot if it has decimal places!', fg='black', font=('Arial', 10, 'bold')).grid(column=0, row=4, padx=0, pady=5)
    rule_label6 = Label(Rules_frame, text='Example: 7.25', fg='black', font=('Arial', 10, 'bold')).grid(column=0, row=5, padx=0, pady=5)
    rule_label7 = Label(Rules_frame, text='Have a good day!', fg='black', font=('Arial', 15, 'bold')).grid(column=0, row=6,padx=0, pady=5)

    Button(Rules_frame, text='Back to menu', font=('Arial', 10), command=BackToMenu).grid(column=0, row=7, padx=20, pady=5)


def GoToRules():
    '''
    The function sends user to rules
    '''
    Weather_frame.grid_forget()
    Translator_frame.grid_forget()
    Menu_frame.grid_forget()

    Rules_frame.grid(column=0, row=0, padx=20, pady=5)

def translateC():
    '''
    The function tranlate Celsius TO Farenheit
    '''
    Ce = EnterC.get()

    Ce = float(Ce)

    Far = float((9/5)*Ce + 32)

    Far = float(('{:.2f}'.format(Far)))
    F['text'] = Far


tk = Tk()
tk.geometry('500x500')

Menu_frame = Frame(tk, width=500, height=500)
Menu_frame.grid(column=0, row=0, padx=20, pady=5)

Weather_frame = Frame(tk, width=300, height=300)
Weather_frame.grid(column=0, row=0, padx=20, pady=5)

Translator_frame = Frame(tk, width=300, height=300)
Translator_frame.grid(column=0, row=0, padx=20, pady=5)

Rules_frame = Frame(tk, width=500, height=500)
Rules_frame.grid(column=0, row=0, padx=20, pady=5)

Menu_widgets()
Weather_widgets()
Translator_widgets()
Rules_widjets()

Weather_frame.grid_forget()
Translator_frame.grid_forget()
Rules_frame.grid_forget()

EnterCity = Entry(Weather_frame, bg='white', font=10)
EnterCity.grid(column=0, row=1, padx=20, pady=5)

info = Label(Weather_frame, text='Weather', bg='orange', font=('Arial', 20))
info.grid(column=0, row=3, padx=20, pady=5)

EnterFar = Entry(Translator_frame, bg='white', font=10)
EnterFar.grid(column=0, row=1, padx=20, pady=5)
Cel = Label(Translator_frame, text='Celsius', bg='orange', font=('Arial', 20))
Cel.grid(column=0, row=3, padx=20, pady=5)

EnterC = Entry(Translator_frame, bg='white', font=10)
EnterC.grid(column=0, row=5, padx=20, pady=5)
F = Label(Translator_frame, text='Farenheits', bg='orange', font=('Arial', 20))
F.grid(column=0, row=7, padx=20, pady=5)

tk.mainloop()

