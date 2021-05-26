import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import time


class Error(Exception):
    pass


class Razmer(Error):
    def __str__(self):
        messagebox.showinfo("Ошибка", 'Размер доски должен быть больше 2 и меньше или равен 15', )


class ProverkaMin(Error):
    def __str__(self):
        messagebox.showinfo("Ошибка",
                            'Количество мин должно быть меньше длины и ширины доски -1 и больше нуля', )


class Breakout(Error):
    def __str__(self):
        messagebox.showinfo("Ошибка", 'Предоставлены неверные данные ', )


start_window = Tk()
start_window.title("Saper")
start_window.geometry("350x400")

lgame = Label(start_window, text="Saper", font=("Arial Bold", 30))
lgame.grid(column=0, row=0)
l_input_name = Label(start_window, text="Введите имя", font=("Arial Bold", 20))
l_input_m = Label(start_window, text="Введите ширину доски", font=("Arial Bold", 20))
l_input_n = Label(start_window, text="Введите высоту доски", font=("Arial Bold", 20))
l_input_miny = Label(start_window, text="Введите количество минут", font=("Arial Bold", 20))
l_input_name.grid(column=0, row=1)
l_input_m.grid(column=0, row=3)
l_input_n.grid(column=0, row=6)
l_input_miny.grid(column=0, row=8)
input_name = Entry(start_window, width='10')
input_m = Entry(start_window, width='10')
input_n = Entry(start_window, width='10')
input_min = Entry(start_window, width='10')
input_name.grid(column=0, row=2)
input_m.grid(column=0, row=4)
input_n.grid(column=0, row=7)
input_min.grid(column=0, row=9)


def game_window(m, n, l_min, name):
    start = time.time()
    file = open('history.txt', 'w')
    x_width = n * 52
    y_height = m * 42
    game_window = Tk()
    game_window.geometry(str(x_width) + "x" + str(y_height))
    game_window.title("SAPER")
    photo = PhotoImage(file=r"img/pole.png")
    bomb = PhotoImage(file=r"img/bomb1.png")
    jeden = PhotoImage(file=r"img/jeden.png")
    dwa = PhotoImage(file=r"img/dwa.png")
    trzy = PhotoImage(file=r"img/trzy.png")
    cztery = PhotoImage(file=r"img/cztery.png")
    piec = PhotoImage(file=r"img/piec.png")
    szesc = PhotoImage(file=r"img/szesc.png")
    siedem = PhotoImage(file=r"img/siedem.png")
    osiem = PhotoImage(file=r"img/osiem.png")
    block = PhotoImage(file=r"img/block.png")
    flag = PhotoImage(file=r"img/pole_f.png")
    dark_pole = PhotoImage(file=r"img/dark_pole.png")

    tab_l_click = []
    tab_r_click = []

    text = []

    def key(event):

        text.append(event.char)
        #print(text)
        model = ["x", "y", "z", "z", "y"]
        if model == text:
            dark_mine()

    def dark_mine():
        for i in range(len(list_min)):
            tmp = []
            for j in range(len(list_min[i])):
                tmp.append(list_min[i][j])
            #print("x", tmp[0])
            #print("y", tmp[1])
            pole[tmp[0]][tmp[1]].configure(image=dark_pole)

    def l_click(x, y):
        #print("x", x)
        #print("y", y)
        tmp_tabg = []
        tmp_tabg.append(x)
        tmp_tabg.append(y)
        tab_l_click.append(tmp_tabg)
        #print(tmp_tabg)
        if tmp_tabg in list_min:
            #print("boom")
            pole[x][y].configure(image=bomb)
            file.write('Игрок: ' + str(name) + '\n')
            file.write('Сложность: ' + str(n) + 'x' + str(m) + '\n')
            file.write('Количество мин: ' + str(l_min) + '\n')
            end = round(time.time() - start, 1)
            file.write('Время: ' + str(end) + '\n')
            file.write('Итог: Поражение')
            file.close()
            msend = messagebox.showerror(title="Поражение", message="Конец игры")
            exit()

        count_mine = count_near_mine(x, y)
        if (count_mine == 1 and tmp_tabg not in list_min):
            pole[x][y].configure(image=jeden)

        if (count_mine == 2 and tmp_tabg not in list_min):
            pole[x][y].configure(image=dwa)

        if (count_mine == 3 and tmp_tabg not in list_min):
            pole[x][y].configure(image=trzy)
        if (count_mine == 4 and tmp_tabg not in list_min):
            pole[x][y].configure(image=cztery)
        if (count_mine == 5 and tmp_tabg not in list_min):
            pole[x][y].configure(image=piec)
        if (count_mine == 6 and tmp_tabg not in list_min):
            pole[x][y].configure(image=szesc)
        if (count_mine == 7 and tmp_tabg not in list_min):
            pole[x][y].configure(image=siedem)

        if (count_mine == 8 and tmp_tabg not in list_min):
            pole[x][y].configure(image=osiem)

        if (count_mine == 0 and tmp_tabg not in list_min):
            pole[x][y].configure(image=block)
            sasiednie_pole(x, y)

        #print(tab_l_click)

    def sasiednie_pole(x, y):
        if (x < m and y < n and y > 0 and x > 0):
            tmp_tab = []
            tmp_tab.append(x - 1)
            tmp_tab.append(y)
            if tmp_tab not in list_min and tmp_tab not in tab_l_click:
                l_click(x - 1, y)
                #print("aaaa", tab_l_click)
        if (x < m and y < n and y > 0 and x > 0):
            tmp_tab = []
            tmp_tab.append(x + 1)
            tmp_tab.append(y + 1)
            if tmp_tab not in list_min and tmp_tab not in tab_l_click:
                l_click(x + 1, y + 1)
        if (x < m and y < n and y > 0 and x > 0):
            tmp_tab = []
            tmp_tab.append(x - 1)
            tmp_tab.append(y + 1)
            if tmp_tab not in list_min and tmp_tab not in tab_l_click:
                l_click(x - 1, y + 1)
        if (x < m and y < n and y > 0 and x > 0):
            tmp_tab = []
            tmp_tab.append(x)
            tmp_tab.append(y + 1)
            if tmp_tab not in list_min and tmp_tab not in tab_l_click:
                l_click(x, y + 1)
        if (x < m and y < n and y > 0 and x > 0):
            tmp_tab = []
            tmp_tab.append(x - 1)
            tmp_tab.append(y - 1)
            if tmp_tab not in list_min and tmp_tab not in tab_l_click:
                l_click(x - 1, y - 1)
        if (x < m and y < n and y > 0 and x > 0):
            tmp_tab = []
            tmp_tab.append(x)
            tmp_tab.append(y - 1)
            if tmp_tab not in list_min and tmp_tab not in tab_l_click:
                l_click(x, y - 1)
        if (x < m and y < n and y > 0 and x > 0):
            tmp_tab = []
            tmp_tab.append(x + 1)
            tmp_tab.append(y - 1)
            if tmp_tab not in list_min and tmp_tab not in tab_l_click:
                l_click(x + 1, y - 1)
        if (x < m and y < n and y > 0 and x > 0):
            tmp_tab = []
            tmp_tab.append(x + 1)
            tmp_tab.append(y)
            if tmp_tab not in list_min and tmp_tab not in tab_l_click:
                l_click(x + 1, y)
        if (x < m and y < n and y > 0 and x > 0):
            tmp_tab = []
            tmp_tab.append(x - 1)
            tmp_tab.append(y)
            if tmp_tab not in list_min and tmp_tab not in tab_l_click:
                l_click(x - 1, y)

    def count_near_mine(x, y):
        suma_min_s = 0
        tmp_tab = []
        tmp_tab.append(x - 1)
        tmp_tab.append(y - 1)
        if tmp_tab in list_min:
            suma_min_s += 1

        tmp_tab = []
        tmp_tab.append(x)
        tmp_tab.append(y - 1)
        if tmp_tab in list_min:
            suma_min_s += 1
        tmp_tab = []
        tmp_tab.append(x + 1)
        tmp_tab.append(y - 1)
        if tmp_tab in list_min:
            suma_min_s += 1
        tmp_tab = []
        tmp_tab.append(x - 1)
        tmp_tab.append(y)
        if tmp_tab in list_min:
            suma_min_s += 1
        tmp_tab = []
        tmp_tab.append(x + 1)
        tmp_tab.append(y)
        if tmp_tab in list_min:
            suma_min_s += 1

        tmp_tab = []
        tmp_tab.append(x - 1)
        tmp_tab.append(y + 1)
        if tmp_tab in list_min:
            suma_min_s += 1

        tmp_tab = []
        tmp_tab.append(x)
        tmp_tab.append(y + 1)
        if tmp_tab in list_min:
            suma_min_s += 1

        tmp_tab = []
        tmp_tab.append(x + 1)
        tmp_tab.append(y + 1)
        if tmp_tab in list_min:
            suma_min_s += 1

        #print("сумма соседних мин =", suma_min_s)
        return suma_min_s

    def gen(number):
        n = 1
        while n < number:
            yield n
            n += 1

    def r_click(x, y):

        #print("x", x, "y=", y)
        #print(tab_r_click)
        tmp = []
        tmp.append(x)
        tmp.append(y)
        #print(tmp)
        if tmp in tab_r_click:
            tab_r_click.remove(tmp)
            pole[x][y].configure(image=photo)
        else:
            tab_r_click.append(tmp)
            pole[x][y].configure(image=flag)
        if tmp in list_min:
            try:
                next(l_val)
            except(StopIteration):
                if (len(tab_r_click) == l_min):
                    file.write('Игрок: ' + str(name) + '\n')
                    file.write('Сложность: ' + str(n) + 'x' + str(m) + '\n')
                    file.write('Количество мин: ' + str(l_min) + '\n')
                    end = round(time.time() - start, 1)
                    file.write('Время: ' + str(end) + '\n')
                    file.write('Итог: Победа')
                    file.close()
                    wygrana = messagebox.showinfo(title="Победа", message="Вы выиграли ")
                    exit()

    pole = []
    list_min = []
    tmp_l_min = l_min
    while (tmp_l_min != 0):
        min = []
        x_random_min = random.randint(0, m - 1)
        y_random_min = random.randint(0, n - 1)
        min.append(x_random_min)
        min.append(y_random_min)
        if min not in list_min:
            list_min.append(min)
            tmp_l_min -= 1
    l_val = gen(l_min)
    for x in range(m):
        pole.append([])

        for y in range(n):
            pole[x].append(
                Button(game_window, width='45', height='35', image=photo, command=lambda x=x, y=y: l_click(x, y)))

            pole[x][y].grid(row=x, column=y)
            pole[x][y].bind('<Button-3>', lambda evt, x=x, y=y: r_click(x, y))

    game_window.bind("<Key>", key)

    game_window.mainloop()


def getvalue_start():
    try:
        name = input_name.get()
        m = input_m.get()
        n = input_n.get()
        l_min = input_min.get()

        m_m = int(m)
        n_n = int(n)
        l_mine = int(l_min)
    except ValueError:
        raise Breakout()
    if (m_m <= 2 or n_n <= 2 or m_m > 15 or n_n > 15):
        raise Razmer()
    if (l_mine > m_m * n_n - 1 or l_mine < 1):
        raise ProverkaMin()
    else:
        start_window.destroy()
        game_window(m_m, n_n, l_mine, name)


b_start = Button(start_window, text="Играть", width='20', height='5', command=getvalue_start)
b_start.grid(column=0, row=10)

m = input_m.get()
n = input_n.get()
l_min = input_min.get()
start_window.mainloop()
