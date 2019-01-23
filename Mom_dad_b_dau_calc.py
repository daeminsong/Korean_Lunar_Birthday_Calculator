### Mom & Dad lunar birthday calculator ###

from datetime import date
import datetime
from korean_lunar_calendar  import KoreanLunarCalendar
import tkinter as tk
from tkinter import filedialog, messagebox

Kor_calendar = KoreanLunarCalendar()
dt = datetime.datetime.now()
Cur_YY = dt.year

for i in range(Cur_YY, Cur_YY + 3):
    Kor_calendar.setLunarDate(i,9,3,False)
    Mom_B_Day = datetime.datetime.strptime(Kor_calendar.SolarIsoFormat(), '%Y-%m-%d')
    delta = dt - Mom_B_Day

    if delta.days <= 0 and delta.days > -365:
        # print ('Countdown Mom: %s' % delta.days)
        Mom_B_Day = Kor_calendar.SolarIsoFormat()
        Kor_calendar.setLunarDate(i,9,3 + 5,False)
        dad_birthday_countdown = (int(delta.days) - 5)
        # print ('Countdown Dad: %s'  % dad_birthday_countdown)
        Dad_B_Day = Kor_calendar.SolarIsoFormat()
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Alarm", "Mom's birthday %s days left - (%s)\
        \nDad's birthday %s days left - (%s)" % (delta.days, Mom_B_Day, dad_birthday_countdown, Dad_B_Day))
