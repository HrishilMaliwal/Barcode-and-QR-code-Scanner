from tkinter import*
import sqlite3
import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np
from tkinter import messagebox

t = Tk()
t.title("Barcode Scanner")

Svar = StringVar(t)
Svar.set("one")

maincanvas = Canvas(width=1530, height=825, bg='black')
maincanvas.pack(expand=YES, fill=BOTH)
t.resizable(0, 0)

buttonfont = ('Times New Roman', 11)


def login():

    window1 = Toplevel(t)
    window1.resizable(0, 0)

    window1_canvas = Canvas(window1, width=1530, height=825, bg='black')
    window1_canvas.pack(expand=YES, fill=BOTH)

    def back1():
        window1.destroy()

    back = Button(window1_canvas, text="Log out", anchor=W, command=back1)
    back.configure(padx=5, width=7, height=1, bg="black", fg="white")
    back.pack()
    back_window = window1_canvas.create_window(82, 40, window=back)

    def display(dis):

        window2 = Toplevel(window1)
        window2.resizable(0, 0)

        window2_canvas = Canvas(window2, width=830, height=825, bg="black")
        window2_canvas.pack(expand=YES, fill=BOTH)

        dis = int(dis)

        conn = sqlite3.connect('Inventory.db')
        conn.execute(
            "UPDATE Inventory set Stock = Stock + 1 where Serial = %d" % (dis))
        conn.commit()
        cursor = conn.execute(
            "SELECT* from Inventory where Serial = %d" % (dis))
        for row in cursor:
            dict_s = {'Serial': row[0], 'Name': row[1],
                      'Price': row[2], 'Stock': row[3], 'Type': row[4]}

            def back2():
                window2.destroy()

            back2inv = Button(
                window2_canvas, text="Back to Inventory", anchor=CENTER, command=back2)

            back2inv.configure(padx=5, height=1, bg="black", fg="white")

            back2inv.pack()

            window2_canvas.create_window(110, 60, window=back2inv)

            details_header = Label(window2_canvas, text="Item Details",
                                   bg="black", fg="white", font=("Times New Roman", 30))

            details_header.pack()

            window2_canvas.create_window(400, 60, window=details_header)

            serial = Label(window2_canvas, text="Serial Number :",
                           bg="black", fg="white", font=("Times New Roman", 20))

            serial.pack()

            window2_canvas.create_window(140, 130, window=serial)

            serial_data = Label(window2_canvas, text=dict_s['Serial'], bg="black", fg="red", font=(
                "Times New Roman", 20))

            serial_data.pack()

            window2_canvas.create_window(280, 130, window=serial_data)

            name_ = Label(window2_canvas, text="Name:", bg="black",
                          fg="white", font=("Times New Roman", 20))

            name_.pack()

            window2_canvas.create_window(90, 180, window=name_)

            name_data = Label(window2_canvas, text=dict_s['Name'], width=20, bg="black", fg="red", font=(
                "Times New Roman", 20), anchor=W)

            name_data.pack()

            window2_canvas.create_window(290, 180, window=name_data)

            price = Label(window2_canvas, text="Price (in INR) :",
                          bg="black", fg="white", font=("Times New Roman", 20))

            price.pack()

            window2_canvas.create_window(140, 230, window=price)

            price_data = Label(window2_canvas, text=dict_s['Price'], bg="black", fg="red", font=(
                "Times New Roman", 20))

            price_data.pack()

            window2_canvas.create_window(250, 230, window=price_data)

            stock = Label(window2_canvas, text="Stock :", bg="black",
                          fg="white", font=("Times New Roman", 20))

            stock.pack()

            window2_canvas.create_window(92, 280, window=stock)

            stock_data = Label(window2_canvas, text=dict_s['Stock'], bg="black", fg="red", font=(
                "Times New Roman", 20))

            stock_data.pack()

            window2_canvas.create_window(160, 280, window=stock_data)

            item_type = Label(window2_canvas, text="Type :",
                              bg="black", fg="white", font=("Times New Roman", 20))

            item_type.pack()

            window2_canvas.create_window(90, 330, window=item_type)

            item_type_data = Label(window2_canvas, text=dict_s['Type'], width=20, bg="black", fg="red", font=(
                "Times New Roman", 20), anchor=W)

            item_type_data.pack()

            window2_canvas.create_window(290, 330, window=item_type_data)

        conn.close()

    def barcode(br_filename):

        def decode(img):

            decoded_data = pyzbar.decode(img)

            for obj in decoded_data:
                data = str(obj.data)

            data = data[2:-1]
            return data

        def pre_processing(img):

            a = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            a = cv2.resize(a, (256, 256))

            return a

        def noise_removal(img):

            median = cv2.medianBlur(img, 3)
            return median

        def HPF(img):

            filt = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            sharp_image = cv2.filter2D(img, -1, filt)

            return sharp_image

        def thresholding(img):

            ret, image = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
            return image

        image = cv2.imread(br_filename)

        image = pre_processing(image)

        blur_image = noise_removal(image)

        sharpend_image = HPF(blur_image)

        final_image = thresholding(sharpend_image)

        decoded_data = decode(final_image)

        display(decoded_data)

    def br_decode1():

        br_filename = ("H:\Projects\Barcode\Codes\201783_Red Bull.png")
        barcode(br_filename)

    def br_decode2():

        br_filename = ("H:\Projects\Barcode\Codes\287401_Coca Cola.png")
        barcode(br_filename)

    def br_decode3():

        br_filename = ("H:\Projects\Barcode\Codes\298732_Energy.png")
        barcode(br_filename)

    def br_decode4():

        br_filename = ("H:\Projects\Barcode\Codes\308482_Haldiram.png")
        barcode(br_filename)

    def br_decode5():

        br_filename = ("H:\Projects\Barcode\Codes\350221_Hide-n-Seek.png")
        barcode(br_filename)

    def br_decode6():

        br_filename = ("H:\Projects\Barcode\Codes\390784_Lays.png")
        barcode(br_filename)

    def br_decode7():

        br_filename = ("H:\Projects\Barcode\Codes\401490_Butter.png")
        barcode(br_filename)

    def br_decode8():

        br_filename = ("H:\Projects\Barcode\Codes\408762_Paneer.png")
        barcode(br_filename)

    def br_decode9():

        br_filename = ("H:\Projects\Barcode\Codes\495321_Cheese.png")
        barcode(br_filename)

    def br_decode10():

        br_filename = ("H:\Projects\Barcode\Codes\510326_Chicken.png")
        barcode(br_filename)

    def br_decode11():

        br_filename = ("H:\Projects\Barcode\Codes\542107_Beef.png")
        barcode(br_filename)

    def br_decode12():

        br_filename = ("H:\Projects\Barcode\Codes\592839_Egg.png")
        barcode(br_filename)

    def br_decode13():

        br_filename = ("H:\Projects\Barcode\Codes\809943_Carrot.png")
        barcode(br_filename)

    def br_decode14():

        br_filename = ("H:\Projects\Barcode\Codes\863702_Potato.png")
        barcode(br_filename)

    def br_decode15():

        br_filename = ("H:\Projects\Barcode\Codes\897463_Tomato.png")
        barcode(br_filename)

    name = Label(window1_canvas, text="Inventory Items",
                 bg="black", fg="white", font=("Times New Roman", 30))
    name.pack()
    window1_canvas.create_window(720, 40, window=name)

    barcode1 = PhotoImage(file="H:\Projects\Barcode\Codes\201783_Red Bull.png")
    window1_canvas.create_image(150, 100, anchor=NW, image=barcode1)

    barcode2 = PhotoImage(
        file="H:\Projects\Barcode\Codes\287401_Coca Cola.png")
    window1_canvas.create_image(400, 100, anchor=NW, image=barcode2)

    barcode3 = PhotoImage(file="H:\Projects\Barcode\Codes\298732_Energy.png")
    window1_canvas.create_image(650, 100, anchor=NW, image=barcode3)

    barcode4 = PhotoImage(file="H:\Projects\Barcode\Codes\308482_Haldiram.png")
    window1_canvas.create_image(900, 100, anchor=NW, image=barcode4)

    barcode5 = PhotoImage(
        file="H:\Projects\Barcode\Codes\350221_Hide-n-Seek.png")
    window1_canvas.create_image(1150, 100, anchor=NW, image=barcode5)

    barcode1_button = Button(
        window1_canvas, text="Red Bull", anchor=CENTER, command=br_decode1)
    barcode1_button.configure(padx=7, pady=7, width=7,
                              height=2, bg="black", fg="white")
    barcode1_button.pack()
    barcode1_button_window = window1_canvas.create_window(
        220, 225, window=barcode1_button)

    barcode2_button = Button(
        window1_canvas, text="Coca Cola", anchor=CENTER, command=br_decode2)
    barcode2_button.configure(padx=20, pady=7, width=7,
                              height=2, bg="black", fg="white")
    barcode2_button.pack()
    barcode2_button_window = window1_canvas.create_window(
        470, 225, window=barcode2_button)

    barcode3_button = Button(
        window1_canvas, text="Energy", anchor=CENTER, command=br_decode3)
    barcode3_button.configure(padx=7, pady=7, width=7,
                              height=2, bg="black", fg="white")
    barcode3_button.pack()
    barcode3_button_window = window1_canvas.create_window(
        720, 225, window=barcode3_button)

    barcode4_button = Button(
        window1_canvas, text="Haldiram", anchor=CENTER, command=br_decode4)
    barcode4_button.configure(padx=7, pady=7, width=7,
                              height=2, bg="black", fg="white")
    barcode4_button.pack()
    barcode4_button_window = window1_canvas.create_window(
        970, 225, window=barcode4_button)

    barcode5_button = Button(
        window1_canvas, text="Hide-n-Seek", anchor=CENTER, command=br_decode5)
    barcode5_button.configure(padx=7, pady=7, width=7,
                              height=2, bg="black", fg="white")
    barcode5_button.pack()
    barcode5_button_window = window1_canvas.create_window(
        1220, 225, window=barcode5_button)

    barcode6 = PhotoImage(file="H:\Projects\Barcode\Codes\390784_Lays.png")
    window1_canvas.create_image(150, 350, anchor=NW, image=barcode6)

    barcode7 = PhotoImage(file="H:\Projects\Barcode\Codes\401490_Butter.png")
    window1_canvas.create_image(400, 350, anchor=NW, image=barcode7)

    barcode8 = PhotoImage(file="H:\Projects\Barcode\Codes\408762_Paneer.png")
    window1_canvas.create_image(650, 350, anchor=NW, image=barcode8)

    barcode9 = PhotoImage(file="H:\Projects\Barcode\Codes\495321_Cheese.png")
    window1_canvas.create_image(900, 350, anchor=NW, image=barcode9)

    barcode10 = PhotoImage(file="H:\Projects\Barcode\Codes\510326_Chicken.png")
    window1_canvas.create_image(1150, 350, anchor=NW, image=barcode10)

    barcode6_button = Button(window1_canvas, text="Lays",
                             anchor=CENTER, command=br_decode6)
    barcode6_button.configure(padx=7, pady=7, width=7,
                              height=2, bg="black", fg="white")
    barcode6_button.pack()
    barcode6_button_window = window1_canvas.create_window(
        220, 475, window=barcode6_button)

    barcode7_button = Button(
        window1_canvas, text="Butter", anchor=CENTER, command=br_decode7)
    barcode7_button.configure(padx=20, pady=7, width=7,
                              height=2, bg="black", fg="white")
    barcode7_button.pack()
    barcode7_button_window = window1_canvas.create_window(
        470, 475, window=barcode7_button)

    barcode8_button = Button(
        window1_canvas, text="Paneer", anchor=CENTER, command=br_decode8)
    barcode8_button.configure(padx=7, pady=7, width=7,
                              height=2, bg="black", fg="white")
    barcode8_button.pack()
    barcode8_button_window = window1_canvas.create_window(
        720, 475, window=barcode8_button)

    barcode9_button = Button(
        window1_canvas, text="Cheese", anchor=CENTER, command=br_decode9)
    barcode9_button.configure(padx=7, pady=7, width=7,
                              height=2, bg="black", fg="white")
    barcode9_button.pack()
    barcode9_button_window = window1_canvas.create_window(
        970, 475, window=barcode9_button)

    barcode10_button = Button(
        window1_canvas, text="Chicken", anchor=CENTER, command=br_decode10)
    barcode10_button.configure(
        padx=20, pady=7, width=7, height=2, bg="black", fg="white")
    barcode10_button.pack()
    barcode10_button_window = window1_canvas.create_window(
        1220, 475, window=barcode10_button)

    barcode11 = PhotoImage(file="H:\Projects\Barcode\Codes\542107_Beef.png")
    window1_canvas.create_image(150, 600, anchor=NW, image=barcode11)

    barcode12 = PhotoImage(file="H:\Projects\Barcode\Codes\592839_Egg.png")
    window1_canvas.create_image(400, 600, anchor=NW, image=barcode12)

    barcode13 = PhotoImage(file="H:\Projects\Barcode\Codes\809943_Carrot.png")
    window1_canvas.create_image(650, 600, anchor=NW, image=barcode13)

    barcode14 = PhotoImage(file="H:\Projects\Barcode\Codes\863702_Potato.png")
    window1_canvas.create_image(900, 600, anchor=NW, image=barcode14)

    barcode15 = PhotoImage(file="H:\Projects\Barcode\Codes\897463_Tomato.png")
    window1_canvas.create_image(1150, 600, anchor=NW, image=barcode15)

    barcode11_button = Button(
        window1_canvas, text="Beef", anchor=CENTER, command=br_decode11)
    barcode11_button.configure(
        padx=7, pady=7, width=7, height=2, bg="black", fg="white")
    barcode11_button.pack()
    barcode11_button_window = window1_canvas.create_window(
        220, 725, window=barcode11_button)

    barcode12_button = Button(
        window1_canvas, text="Egg", anchor=CENTER, command=br_decode12)
    barcode12_button.configure(
        padx=7, pady=7, width=7, height=2, bg="black", fg="white")
    barcode12_button.pack()
    barcode12_button_window = window1_canvas.create_window(
        450, 725, window=barcode12_button)

    barcode13_button = Button(
        window1_canvas, text="Carrot", anchor=CENTER, command=br_decode13)
    barcode13_button.configure(
        padx=7, pady=7, width=7, height=2, bg="black", fg="white")
    barcode13_button.pack()
    barcode13_button_window = window1_canvas.create_window(
        720, 725, window=barcode13_button)

    barcode14_button = Button(
        window1_canvas, text="Potato", anchor=CENTER, command=br_decode14)
    barcode14_button.configure(
        padx=7, pady=7, width=7, height=2, bg="black", fg="white")
    barcode14_button.pack()
    barcode14_button_window = window1_canvas.create_window(
        970, 725, window=barcode14_button)

    barcode15_button = Button(
        window1_canvas, text="Tomato", anchor=CENTER, command=br_decode15)
    barcode15_button.configure(
        padx=20, pady=7, width=7, height=2, bg="black", fg="white")
    barcode15_button.pack()
    barcode15_button_window = window1_canvas.create_window(
        1220, 725, window=barcode15_button)

    window1.mainloop()


def qr_decode(filename):

    def decode(img):

        decoded_data = pyzbar.decode(img)

        for obj in decoded_data:
            data = str(obj.data)

        data = data[2:-1]
        return data

    def pre_processing(img):

        a = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        a = cv2.resize(a, (256, 256))

        return a

    def noise_removal(img):

        median = cv2.medianBlur(img, 3)
        return median

    def unsharpmask(img, blur):

        mask = (img - blur) * 100
        sharp = img + mask

        return sharp

    def thresholding(img):

        ret, image = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        return image

    image = cv2.imread(filename)

    image = pre_processing(image)

    blur_image = noise_removal(image)

    sharpend_image = unsharpmask(image, blur_image)

    final_image = thresholding(sharpend_image)

    decoded_data = decode(final_image)

    if(decoded_data == 'Hrishil'):

        login()

    elif(decoded_data == 'Mihir'):

        login()

    elif(decoded_data == 'Sharvil'):

        login()

    else:
        messagebox.showerror("Login failed", "User is not registered")


def q1():
    filename = ("H:\Projects\Barcode\Codes\Mihir.png")
    qr_decode(filename)


def q2():
    filename = ("H:\Projects\Barcode\Codes\Sharvil.png")
    qr_decode(filename)


def q3():
    filename = ("H:\Projects\Barcode\Codes\Hrishil.png")
    qr_decode(filename)


def q4():
    filename = ("H:\Projects\Barcode\Codes\Stranger.png")
    qr_decode(filename)


p1 = PhotoImage(file=r"H:\Projects\Barcode\Codes\Mihir.png")
p2 = PhotoImage(file=r"H:\Projects\Barcode\Codes\Sharvil.png")
p3 = PhotoImage(file=r"H:\Projects\Barcode\Codes\Hrishil.png")
p4 = PhotoImage(file=r"H:\Projects\Barcode\Codes\Stranger.png")

qr1 = Button(maincanvas, image=p1, command=q1)
qr1.configure(width=90, font=buttonfont, relief=RIDGE,
              activebackground='grey',  bg='black', fg='white')
qr1.pack()
qr1_window = maincanvas.create_window(279, 350, window=qr1)

qr2 = Button(maincanvas, image=p2, command=q2)
qr2.configure(width=90, font=buttonfont, relief=RIDGE,
              activebackground='grey',  bg='black', fg='white')
qr2.pack()
qr2_window = maincanvas.create_window(573, 350, window=qr2)

qr3 = Button(maincanvas, image=p3, command=q3)
qr3.configure(width=90, font=buttonfont, relief=RIDGE,
              activebackground='grey',  bg='black', fg='white')
qr3.pack()
qr3_window = maincanvas.create_window(867, 350, window=qr3)

qr4 = Button(maincanvas, image=p4, command=q4)
qr4.configure(width=90, height=90, font=buttonfont, relief=RIDGE,
              activebackground='grey',  bg='black', fg='white')
qr4.pack()
qr4_window = maincanvas.create_window(1161, 350, window=qr4)

t.mainloop()
