from tkinter import *

window = Tk()

window.title('Üyelik Formu')
window.geometry('500x350+600+300')
window.resizable(height=False, width=False)
window.iconbitmap('forms.ico')
window.configure(bg='#D7C6EE')

frame1 = Frame(window, bg='#D7C6EE')
frame1.grid(row=0, column=0)
frame2 = Frame(window, bg='#D7C6EE')
frame2.grid(row=0, column=1)
frame3 = Frame(window, bg='#D7C6EE')
frame3.grid(row=0, column=2)
frame4 = Frame(window, bg='#D7C6EE')
frame4.grid(row=1, column=2)

frame5 = Frame(window, bg='#D7C6EE')
frame5.place(x=0, y=230)
cv = Canvas(frame5, bg='#D7C6EE', highlightthickness=10, highlightbackground='#D7C6EE')
cv.create_line(100, 10, 500, 10)
cv.pack()


Label(frame1, text='Ad', font='Arial 12 bold', bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame1, text='Soyad', font='Arial 12 bold', bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame1, text='Yaş', font='Arial 12 bold', bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame1, text='Doğum', font='Arial 12 bold', bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame1, text='Cinsiyet', font='Arial 12 bold', bg='#D7C6EE', padx=5, pady=5).pack()

Label(frame2, text=':', font='Arial 12 bold', bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame2, text=':', font='Arial 12 bold', bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame2, text=':', font='Arial 12 bold', bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame2, text=':', font='Arial 12 bold', bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame2, text=':', font='Arial 12 bold', bg='#D7C6EE', padx=5, pady=5).pack()

Entry(frame3, font='Arial 12 bold', bg='#ECE8F0', justify='center').pack(padx=5, pady=5)
Entry(frame3, font='Arial 12 bold', bg='#ECE8F0', justify='center').pack(padx=5, pady=5)

Button(window, text='Kaydet', font='Arial 12 bold', bg='green', width=12).place(x=100, y=270)
Button(window, text='Temizle', font='Arial 12 bold', bg='yellow', width=12).place(x=260, y=270)

photo = PhotoImage(file='profile.png')
photoResized = photo.subsample(4,4)
Button(window, text='Yükle', image=photoResized, compound=TOP).place(x=330, y=11)

Spinbox(frame3, from_=18, to=60, font='Arial 12 bold', bg='#ECE8F0',
        justify='center', width=19).pack(padx=5, pady=5)

optionList = [
    'Ocak',
    'Şubat',
    'Mart',
    'Nisan',
    'Mayıs'
]

sval = StringVar(frame3)
sval.set(optionList[0])
opm1 = OptionMenu(frame3, sval, *optionList)
opm1.config(width=24)
opm1.pack(padx=5, pady=5)

ivar = IntVar()

def sel():
    selection = 'Selected radiobutton val = ' + str(ivar.get())
    print(selection)

rd1 = Radiobutton(frame3, text='Erkek', variable=ivar, value=1, command=sel, font='Times, 12', bg='#D7C6EE')
rd2 = Radiobutton(frame3, text='Kadın', variable=ivar, value=2, command=sel, font='Times, 12', bg='#D7C6EE')
rd1.pack(side='left')
rd2.pack(side='left')

cb1 = Checkbutton(frame4, text='Formu okudum, onaylıyorum.')
cb1.pack()

window.mainloop()