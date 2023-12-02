import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkinter import *
from math import *
from PIL import Image, ImageTk
from matplotlib.ft2font import BOLD
import tkinter.font

window = Tk()
window.title("Kalkulator gerak jatuh bebas dan gerak peluru")
window.geometry("500x500")
window.configure(bg='salmon')

def gp():
    window_gp = Tk()
    window_gp.title("Gerak Peluru")
    window_gp.configure(bg="palegreen")

    b = Label(window_gp, text="kecepatan Awal", bg="salmon", fg="black")
    b.grid(row=1, column=0)
    v0 = Entry(window_gp, width=40, bd=5)
    v0.grid(row=1, column=1)
    v0.get()

    s = Label(window_gp, text="Sudut Lintasan", bg="salmon", fg="black")
    s.grid(row=2, column=0)
    theta = Entry(window_gp, width=40, bd=5)
    theta.grid(row=2, column=1)
    theta.get()

    g = Label(window_gp, text="g = 9.81 m/s2")
    g.grid(row=0, column=0)

    satuan2 = Label(window_gp, text="m/s", bg="salmon", fg="black")
    satuan2.grid(row=1, column=2)
    satuan3 = Label(window_gp, text="Derajat", bg="salmon", fg="black")
    satuan3.grid(row=2, column=2)

    a = Label(window_gp, text="Ketinggian Awal (h0) = 0 m", fg="black")
    a.grid(row=3, column=0)

    def rumusgp():
        y = np.array(0)
        x = np.array(0)
        T = np.array(0)

        g = 9.81 #m/s2
        ketinggian = 0
        jarak = 0
        v = int(v0.get())
        t = 0.0
        dt = 0.01
        teta = np.deg2rad(float(theta.get()))

        while ketinggian >= 0:
            ketinggian = (v * np.sin(teta) * t) - (0.5 * g * t ** 2)
            jarak = v * np.cos(teta) * t
            x = np.append(x, jarak)
            y = np.append(y, ketinggian)
            T = np.append(T, t)
            t = t + dt

        print("Ketinggian Maks : ", np.max(y), "Meter")
        print("Jarak Maks : ", x[-1], "Meter")
        print("Waktu Tempuh : ", T[-1], "S")

        if len(x) == len(y):
            plt.plot(x, y)
            plt.xlabel("Jarak (m)")
            plt.ylabel("Ketinggian (m)")
            plt.title("Gerak Peluru")
            plt.grid()

            plt.show()
        else:
            print("Error: Length of x and y are not equal")
    button_1 = Button(window_gp, text="Buat Grafik", command=rumusgp, bg="green")
    button_1.grid(row=5, column=2)

    def reset():
        theta.delete(0, END)
        v0.delete(0, END)
    reset = Button(window_gp, text="RESET", command=reset, bg="red")
    reset.grid(row=5, column=0)

def gjb():
    window_gjb = Tk()
    window_gjb.title("Gerak Jatuh Bebas")
    window_gjb.configure(bg="skyblue")

    o = Label(window_gjb, text="Ketinggian Awal", bg="red", fg="yellow")
    o.grid(row=1, column=0)
    o1 = Entry(window_gjb, width=40, bd=5)
    o1.grid(row=1, column=1)
    o1.get()

    p = Label(window_gjb, text="Koefisien Drag: ", bg="red", fg="yellow")
    p.grid(row=2, column=0)
    p1 = Entry(window_gjb, width=40, bd=5)
    p1.grid(row=2, column=1)
    p1.get()

    satuan4 = Label(window_gjb, text="m", bg="palegreen", fg="black")
    satuan4.grid(row=1, column=2)
    satuan5 = Label(window_gjb, text=" ", bg="palegreen", fg="black")
    satuan5.grid(row=2, column=2)

    def rumusgjb():
        g = 9.81
        p = float(p1.get())
        y0 = int(o1.get())
        v0 = 0.0
        t0 = 0.0
        dt = 0.01

        y = np.array([y0])
        t = np.array([t0])
        v = np.array([v0])
        a = np.array([g])
        n = int(np.ceil(t/dt))
        y = np.zeros(n, float)
        v = np.zeros(n, float)
        t = np.zeros(n, float)
        a = np.zeros(n, float)

        tinggi = y0
        kecepatan = v0
        gravitasi = g
        waktu = t0

        while tinggi >= 0:
            kecepatan = kecepatan - (g + p*kecepatan**2) * dt
            v = np.append(v, kecepatan)
            tinggi = tinggi + kecepatan*dt
            y = np.append(y, tinggi)
            waktu = waktu + dt
            t = np.append(t, waktu)
            percepatan = -g + p*kecepatan**2

        print(y)
        print(v[-1])
        print(t[-1])

        fig, ax = plt.subplots(2,1,sharex= True)
        fig.subplots_adjust(hspace = 0.5)

        ax[0].plot(t, y, color="b")
        ax[0].set_xlabel("Waktu, t(s)")
        ax[0].set_ylabel("Ketinggian, y(m)")
        ax[0].set_title("Ketingian")
        plt.grid()

        ax[1].plot(t, v, color="r")
        ax[1].set_xlabel("Waktu, t(s)")
        ax[1].set_ylabel("Kecepatan, v(m/s)")
        ax[1].set_title("Kecepatan Jatuh Bebas")
        plt.grid()

        plt.show()
    tmbl_2 = Button(window_gjb, text="Buat Grafik", command=rumusgjb, bg="purple", fg="white")
    tmbl_2.grid(row=3, column=2)

    def reset():
        o1.delete(0, END)
        p1.delete(0, END)
    reset = Button(window_gjb, text="Reset", bg="red", command=reset)
    reset.grid(row=3, column=0)

label_1 = Label(window, text="Pilih jenis kalkulator", fg="black")
label_1.place(x=190, y=185)
button_1 = Button(window, text="Gerak Peluru", width=25, bd=5, command=gp, bg="palegreen")
button_1.place(x=150, y=220)
button_2 = Button(window, text="Gerak Jatuh Bebas", width=25, bd=5,command=gjb ,bg="skyblue")
button_2.place(x=150, y=270)

window.mainloop()