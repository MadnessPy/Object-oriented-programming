from tkinter import *
import math

class menu:
    def __init__(self, master):
        self.master = master
        self.master.title("bangun datar")
        self.master.geometry("200x200")
        self.frame = Frame(self.master)
        self.frame.pack()
        Button(self, frame, text="Segitiga", comand=self.Segitiga).pack()
        button(self, frame, text="Persegi", comand=self.Persegi).pack()
        button(self, frame, text="Lingkaran", comand=self.lingkaran).pack()
        button(self, frame, text="Keluar", comand=self.master.quit).pack()

    def segitiga(self):
        segi3 = toplevel(self, master)
        self.window = Triangle(segi3)

    def Persegi(self):
        segi4 = toplevel(self, master)
        self.window = square(segi4)

    def lingkaran(self):
        segi0 = toplevel(self, master)
        self.window = circle(segi0)

class Triangle:

    def __init__(self, sub_master):
        self.sub_master = sub_master
        self.sub_frame = Frame(self.sub_master)
        self.sub_frame.pack()
        self.sub_master.title("SEGITIGA")
        self.sub_mastergeometry("200x200")

        self.a = DoubleVar()
        self.t = DoubleVar()
        self.luas3 = DoubleVar()

        self.label1 = label(self.sub_frame, text="Nilai Alas:")
        self.label1.grid(row=0, column=0)
        self.entry1 = entry(self.sub_frame, textvariable=self.a)
        self.entry1.grid(row=0, column=1)
        self.label2 = label(self.sub_frame, text="Nilai Tinggi:")
        self.label2.grid(row=1, column=0)
        self.entry2 = Entry(self.sub_frame, textvariable=self.t)
        self.entry2.grid(row=1, column=1)
        self.hitung = Button(self.sub_frame, text="Hitung",comand=self.hitung_luas3)
        self.hitung.grid(row=2, column=1)
        self.selesai = Button(self.sub_frame, text="Selesai",comand=self.sub_master.destroy)
        self.selesai.grid(row=2, column=0)

    def hitung_luas3(self):
        try:
            self.luas3.set(round(float((self.a.get()*self.t.get())/2), 2))
            self.label3 = Label(self.sub_frame, text="L.Segitiga = ")
            self.label3.grid(row=3, column=0)
            self.label4 = Label(self.sub_frame, textvariable=self.luas3)
            self.label4.grid(row=3, column=1)
        except ValueError:
            pass

class Square:

    def __init__(self,sub_master):
        self.sub_master = sub_master
        self.sub_frame = Frame(self.sub_master)
        self.sub_frame.pack()
        self.sub_master.title("PERSEGI")
        self.sub_master.geometry("200x200")

        self.s = IntVar()
        self.luas4 = IntVar()

        self.label1 = Label(self.sub_frame, text="Nilai Sisi: ")
        self.label1.grid(row=0, column=0)
        self.entry1 = Entry(self.sub_frame, textvariable=self.s)
        self.entry1.grid(row=0, column=1)
        self.hitung = Button(self.sub_frame, text="Hitung",command=self.hitung_luas4)
        self.hitung.grid(row=2, column=1)
        self.selesai = Button(self.sub_frame, text="Selesai",command=self.sub_master.destroy)
        self.selesai.grid(rows=2, column=0)

    def hitung_luas4(self):
        try:
            self.luas4.set(self.s.get()**2)
            self.label2 = Label(self.sub_frame, text="L. Persegi = ")
            self.label2.grid(row=3, column=0)
            self.label3 = Label(self.sub_frame, textvariable=self.luas4)
            self.label3.grid(row=3, column=1)
        except ValueError:
            pass

class Circle:

    def __init__(self, sub_master):
        self.sub_master = sub_master
        self.sub_frame = Frame(self.sub_master)
        self.sub_frame.pack()
        self.sub_master.title("=LINGKARAN=")
        self.sub_master.geometry("200x200")

        self.r = DoubleVar()
        self.luas0 = DoubleVar()

        self.label1 = Label(self.sub_frame, text="Jari - Jari: ")
        self.label1.grid(row=0, column=0)
        self.entry1 = Entry(self.sub_frame, textvariable=self.r)
        self.entry1.grid(row=0, column=1)
        self.hitung = Button(self.sub_frame, text="Hitung",command=self.hitung_luas0)
        self.hitung.grid(row=2, column=1)
        self.selesai = Button(self.sub_frame, text="Selesai",command=self.sub_master.destroy)
        self.selesai.grid(rows=2, column=0)

    def hitung_luas0(self):
        try:
            self.luas0.set(round(float(math.pi*(self.r.get()**2)), 2))
            self.label3 = Label(self.sub_frame, text="L. Lingkaran = ")
            self.label3.grid(row=3, column=0)
            self.label4 = Label(self.sub_frame, textvariable=self.luas0)
            self.label4.grid(row=3, column=1)
        except ValueError:
            pass

def main_program():
    bd = Tk()
    Menu(bd)
    bd.mainloop()

main_program()