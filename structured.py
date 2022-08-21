import model_setup
from tkinter import *
import home_page


def window_str():
    global year
    global month
    global dayofweek
    global hour
    global lan
    global lng

    def on_closing():
        root.destroy()
        home_page.home_page()

    def display():
        label.configure(text='Predicting.....')
        Dict = {'MONDAY': 1, 'TUESDAY': 5, 'WEDNESDAY': 6, 'THURSDAY': 4, 'FRIDAY': 0, 'SATURDAY': 2, 'SUNDAY': 3}
        y = int(year.get())
        m = int(month.get())
        h = int(hour.get())
        l1 = float(lan.get())
        l2 = float(lng.get())
        day = str(dayofweek.get()).upper()

        result = model_setup.model(y, m, Dict[day], h, l1, l2)
        label.configure(text=result)

    root = Tk()
    root.title('Predik Desktop App')
    root.resizable(height=None, width=None)

    # title of the app
    Label(root, text="Structured Model", padx=25, pady=6, font=("", 12), bg="#4F98CA", width=40).pack()

    Label(root, text="Year").pack()
    year = Entry(root)
    year.pack()
    year.focus_set()
    Label(root, text="Month").pack()
    month = Entry(root)
    month.pack()
    # month.focus_set()
    Label(root, text="Hour").pack()
    hour = Entry(root)
    hour.pack()
    # hour.focus_set()
    Label(root, text="DayOfWeek").pack()
    dayofweek = Entry(root)
    dayofweek.pack()
    # dayofweek.focus_set()
    Label(root, text="Latitude").pack()
    lan = Entry(root)
    lan.pack()
    # lan.focus_set()
    Label(root, text="Longitude").pack()
    lng = Entry(root)
    lng.pack()
    # lng.focus_set()
    label = Label(root, text='')
    label.pack(pady=10)

    b = Button(root, text="PREDICT",bg="#4F98CA" , fg="white",command=display)
    b.pack(side=BOTTOM, pady=10)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    window_str()
