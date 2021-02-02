import tkinter as tk
import os
import tkinter.messagebox
window = tk.Tk()
window.title('檔案管理(當前目錄改變時請按當前目錄)')
window.geometry('400x300')

ok = "0"
sao = "?"
text = tk.Entry(window, font=('Arial', 12), width=38)
ggo = sao+text.get()
label = tk.Label(window, text="目前路徑:"+ggo, fg="red", font=('Arial', 12))
空白 = tk.Label(window, text=' ', font=('Arial', 16))
frame = tk.Frame(window)
frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')


def choicedir():
    global sao, ggo
    name = text.get()
    ggo = sao+name
    os.chdir(ggo)
    label['text'] = "當前目錄:"+ggo


def c():
    os.system("cls")
    global sao
    sao = "C://"
    label['text'] = "當前目錄:"+sao


def d():
    os.system("cls")
    global sao
    sao = "D://"
    label['text'] = "當前目錄:"+sao


def e():
    os.system("cls")
    global sao
    sao = "E://"
    label['text'] = "當前目錄:"+sao


drive = tk.Menu(window)
window.config(menu=drive)
menu1 = tk.Menu(drive, tearoff=0)
menu1.add_command(label="C://", command=c)
menu1.add_command(label="D://", command=d)
menu1.add_command(label="E://", command=e)
drive.add_cascade(label='硬碟', menu=menu1)


def g():
    os.system("cls")
    name = text.get()
    label['text'] = "當前目錄:"+sao+name
    os.chdir(sao+name)
    a = os.listdir(sao+name)
    n = 0
    num = 1

    def 類型():

        for 類型 in a:

            if os.path.isdir(a[n]):
                return "資料夾:"
            else:
                return "檔案:"
    while n < len(a):
        b = os.path.getsize(a[n])
        print(num, 類型(), a[n])
        num += 1
        n += 1


enter = tk.Button(frame_l, text="列出檔案", fg="#00bfff", font=(
    'Arial', 12), width=10, height=2, command=g)


def open1():
    name = text.get()
    os.startfile(sao+name)


open1 = tk.Button(frame_r, text="開啟檔案", fg="#00ff80", font=(
    'Arial', 12), width=10, height=2, command=open1)


def add():

    add1 = tk.Toplevel(window)
    add1.title('新增檔案')
    add1.geometry('270x160')
    a1 = tk.Label(add1, text='新增資料夾')
    a2 = tk.Label(add1, text='新增檔案')
    e1 = tk.Entry(add1)
    e2 = tk.Entry(add1)

    def addfile():
        if e1.get():
            happy = sao+e1.get()
            os.mkdir(happy)
            print("新增成功")
        else:
            fp = open(e2.get(), "w")
            print("新增成功")
        add1.destroy()

    Asuna = tk.Button(add1, text='確定', command=addfile)

    a1.pack()
    e1.pack()
    a2.pack()
    e2.pack()
    Asuna.pack()


add = tk.Button(frame_l, text="新增檔案", fg="#00ff80", font=(
    'Arial', 12), width=10, height=2, command=add)


def remove():
    global ggo
    name = text.get()
    if os.path.isfile(ggo+"/"+name):
        print("刪除成功")
        os.remove(ggo+"/"+name)
    else:
        os.rmdir(ggo+"/"+name)
        print("刪除成功")


delete = tk.Button(frame_r,  text="刪除檔案", fg="#00bfff",  font=(
    'Arial', 12), width=10, height=2, command=remove)


def openapp():
    root = tk.Toplevel(window)
    root.title('更改檔名')
    root.geometry('270x160')
    a1 = tk.Label(root, text='舊檔名')
    a2 = tk.Label(root, text='新檔名')
    e1 = tk.Entry(root)
    e2 = tk.Entry(root)

    def change():
        os.rename(e1.get(), e2.get())
        root.destroy()

    Asuna = tk.Button(root, text='確定', command=change)

    a1.pack()
    e1.pack()
    a2.pack()
    e2.pack()
    Asuna.pack()


to = tk.Button(frame_l, text="更改檔名", fg="#00bfff", font=(
    'Arial', 12), width=10, height=2, command=openapp)


choice = tk.Button(frame_r, text="當前目錄", fg="#00ff80", font=(
    'Arial', 12), width=10, height=2, command=choicedir)

label.pack()
text.pack()
空白.pack()
frame.pack()
enter.pack()
open1.pack()
add.pack()
delete.pack()
to.pack()
choice.pack()
window.mainloop()
