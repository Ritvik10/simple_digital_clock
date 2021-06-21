#CLOCK APP
from time import strftime
from tkinter import Label, Tk

# ======= Configuring window =========
window = Tk()
window.title("DIGITAL CLOCK:CURRENT TIME")
window.geometry("1000x800")
window.configure(bg="blue")  # =======Background of the clock=====
window.resizable(True, True)  # =====setting a fixed window size =======

clock_label = Label(window, bg="red", fg="white", font=("Times", 30, "bold"), relief="flat")
clock_label.place(x=400, y=300)


def update_label():
    """
    This function will update the clock
    every 80 milliseconds
    """
    current_time = strftime("%H: %M: %S")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)


update_label()
window.mainloop()

