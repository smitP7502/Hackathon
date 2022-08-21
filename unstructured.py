from tkinter import *
from tkinter.filedialog import askopenfile
import home_page
# import sos


def window_uns():

    def on_closing():
        root.destroy()
        home_page.home_page()

    # function for upload video
    def open_file():
        file_path = askopenfile(mode='r', filetypes=[('Video Files', '*mp4')])
        lbl.configure(text=str(file_path.name))
        # print(type(file_path))
        if file_path is not None:
            pass

    # function which contain model
    def classify():

        # load model code
        # sos.func()
        lbl.configure(text="File is classified")

    # root file
    root = Tk()
    root.title('Predik Desktop App')
    root.resizable(height=None, width=None)

    # title of the app
    Label(root, text="Unstructured Model", padx=25, pady=6, font=("", 12), bg="#4F98CA", width=40).pack()
    # showing chosen video
    lbl = Label(text="No Path choose!!", wraplength=400, )
    lbl.pack(pady=20)

    canvas = Canvas(root, height=400, width=400, )
    canvas.pack()
    # frame = Frame(root, bg='white')
    # frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    # button for choose video
    choose_video = Button(root, text='Choose Video',
                          padx=35, pady=10,
                          fg="white", bg="#4F98CA", command=open_file)
    choose_video.pack(side=LEFT)

    # button for classify video
    class_video = Button(root, text='Classify Video',
                         padx=35, pady=10,
                         fg="white", bg="#4F98CA", command=classify)
    class_video.pack(side=RIGHT)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    window_uns()
