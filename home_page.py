from tkinter import *
import unstructured
import structured



def home_page():
    def goto_unstrucred():
        root1.destroy()
        unstructured.window_uns()

    def goto_strucred():
        root1.destroy()
        structured.window_str()

    # root file
    root1 = Tk()
    root1.title('HOME')
    root1.geometry('400x400')
    # root1.configure(bg='#272727')
    # title of the app
    Label(root1, text="HOME", padx=25, pady=8, font=("", 15), bg="#4F98CA", width=40).pack()

    Button(root1, text="Unstructured data",font=("", 11), command=goto_unstrucred,bg='#4F98CA',fg="white").pack(padx=20, pady=40)
    Button(root1, text="Structured data",font=("", 11), command=goto_strucred, bg='#4F98CA',fg="white").pack(padx=20, pady=20)

    root1.mainloop()


if __name__ == "__main__":
    home_page()
