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
#     bg='green', font=('Arial', 12), width=15, height=2)
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
lb = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox
#创建一个list并将值循环添加到Listbox控件中
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
# lb.delete(2)
lb.pack()


src.mainloop()





