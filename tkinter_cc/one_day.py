import tkinter as tk

# src = tk.Tk()
# src.title('one_day')
# src.geometry('400x400')
# l = tk.Label(src,
#     text='呵呵哒！！',    # 标签的文字
#     bg='brown',     # 背景颜色
#     font=('Arial', 12),     # 字体和字体大小
#     width=15, height=2  # 标签长宽
#     )
# l.pack()    # 固定窗口位置

# var = tk.StringVar()    # 这时文字变量储存器
# l = tk.Label(src,
#     textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
#     bg='green', font=('Arial', 12), width=1024, height=1440)
# l.pack()
# on_hit = False  # 默认初始状态为 False
# def hit_me():
#     global on_hit
#     if on_hit == False:     # 从 False 状态变成 True 状态
#         on_hit = True
#         var.set('you hit me')   # 设置标签的文字为 'you hit me'
#     else:       # 从 True 状态变成 False 状态
#         on_hit = False
#         var.set('') # 设置 文字为空
# b = tk.Button(src,
#     text='点我变换',      # 显示在按钮上的文字
#     width=15, height=2,
#     command=hit_me)     # 点击按钮式执行的命令
# b.pack()    # 按钮位置
# src.mainloop()

#————————————————————————————————————————————

# src = tk.Tk()
# src.title('one_day')
# src.geometry('400x400')

# e = tk.Entry(src,show=3)
# e.pack()

# def insert_point():
#     var = e.get()
#     t.insert('insert',var)
# def insert_end():
#     var = e.get()
#     t.insert(2.3,var)

# b1 = tk.Button(src,
#     text='按钮1',      # 显示在按钮上的文字
#     width=15, height=2,
#     command=insert_point)     # 点击按钮式执行的命令
# b1.pack()    # 按钮位置
# b2 = tk.Button(src,text='按钮2',command=insert_end)
# b2.pack()

# t = tk.Text(src,height=2)
# t.pack()

# src.mainloop()

#————————————————————————————————————————————

# src = tk.Tk()
# src.title('one_day')
# src.geometry('400x400')

# var1 = tk.StringVar()

# l = tk.Label(src,bg='yellow',width = 4, textvariable=var1)
# l.pack()
# def prnit_selection():
#     value = lb.get(lb.curselection())
#     var1.set(value)

# b1 = tk.Button(src,
#     text='按钮1',      # 显示在按钮上的文字
#     width=15, height=2,
#     command=prnit_selection)     # 点击按钮式执行的命令
# b1.pack()    # 按钮位置

# var2 = tk.StringVar()
# var2.set((4,11,23,145,22))
# #创建Listbox
# lb = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox
# #创建一个list并将值循环添加到Listbox控件中
# list_items = [1,2,3,4]
# for item in list_items:
#     lb.insert('end',item)
# lb.insert(1,'first')
# lb.insert(2,'second')
# # lb.delete(2)
# lb.pack()

# src.mainloop()

#————————————————————————————————

src = tk.Tk()
src.title('one_day')
src.geometry('400x400')

var1 = tk.StringVar()

l = tk.Label(src,bg='yellow',width = 4, textvariable=var1)
l.pack()
def prnit_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(src,
    text='按钮1',      # 显示在按钮上的文字
    width=15, height=2,
    command=prnit_selection)     # 点击按钮式执行的命令
b1.pack()    # 按钮位置

var2 = tk.StringVar()
var2.set((4,11,23,145,22))
#创建Listbox
lb = tk.Listbox(src, listvariable=var2)  #将var2的值赋给Listbox
#创建一个list并将值循环添加到Listbox控件中
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
# lb.delete(2)
lb.pack()

src.mainloop()

#————————————————————————————————————————————————————

# src = tk.Tk()
# src.title('one_day')
# src.geometry('800x600')

# var = tk.StringVar()

# l = tk.Label(src, bg='yellow', width=22, text = 'empty')
# l.pack()


# def print_selection():
#     l.config(text='you have selected' + var.get())


# r1 = tk.Radiobutton(
#     src, text="list A", variable=var, value="A", command=print_selection)
# r1.pack()


# r2 = tk.Radiobutton(
#     src, text="list B", variable=var, value="B", command=print_selection)
# r2.pack()


# r3 = tk.Radiobutton(
#     src, text="list C", variable=var, value="C", command=print_selection)
# r3.pack()



# src.mainloop()



#———————————————————————————————————————————————————————————————————————




# src = tk.Tk()
# src.title('one_day')
# src.geometry('800x600')


# l1 = tk.Label(src, bg='yellow', width=22, text = 'empty')
# l1.pack()


# def print_selection1(v):
#     l1.config(text='you have selected' + v)
# def print_selection2(v):
#     l2.config(text='you have selected' + v)
#     print(v)
# s1 = tk.Scale(
#     src,
#     label= 'try ma',
#     from_=5,
#     to=11,
#     orient=tk.HORIZONTAL,
#     length=200,
#     showvalue=0,
#     tickinterval=3,
#     resolution=0.01,
#     command=print_selection1
#     )
# s1.pack()
# s2 = tk.Scale(
#     src, 
#     label='try me', 
#     from_=5, to=11, 
#     orient=tk.HORIZONTAL,
#     length=200, 
#     showvalue=0, 
#     tickinterval=1, 
#     resolution=1, 
#     command=print_selection2)

# s2.pack()

# l2 = tk.Label(src, bg='yellow', width=22, text = 'empty')
# l2.pack()

# src.mainloop()




#——————————————————————————————————————————————————





# src = tk.Tk()
# src.title('one_day')
# src.geometry('1440x1024')


# l = tk.Label(src, bg='yellow', width=22, text = 'empty')
# l.pack()


# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):   #如果选中第一个选项，未选中第二个选项
#         l.config(text='I love only Python ')
#     elif (var1.get() == 0) & (var2.get() == 1): #如果选中第二个选项，未选中第一个选项
#         l.config(text='I love only C++')
#     elif (var1.get() == 0) & (var2.get() == 0):  #如果两个选项都未选中
#         l.config(text='I do not love either')
#     else:
#         l.config(text='I love both')             #如果两个选项都选中

# var1=tk.IntVar()
# var2=tk.IntVar()

# c1 = tk.Checkbutton(src,text='Python',variable=var1,onvalue=1,offvalue=0,command=print_selection)

# c2 = tk.Checkbutton(src,text='C++',variable=var2,onvalue=1,offvalue=0,command=print_selection)

# c1.pack()
# c2.pack()

# src.mainloop()

