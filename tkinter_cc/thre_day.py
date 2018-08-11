import tkinter as tk

# windows = tk.Tk()
# windows.title('one_day')
# windows.geometry('1440x1024')

# canvas = tk.Canvas(windows,bg='blue',height=800,width=800)
# # image_file=tk.PhotoImage(file='E:\\ycc\\pythonlianxi\\tkinter_cc\\1.gif')
# # image = canvas.create_image(10,10,anchor='nw',image=image_file)

# x0, y0, x1, y1= 50, 50, 500, 500
# line = canvas.create_line(x0, y0, x1, y1)
# oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  #创建一个圆，填充色为`red`红色
# arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=90)  #创建一个扇形
# rect = canvas.create_rectangle(100, 30, 100+20, 30+20)   #创建一个矩形

# def moveit():
#     canvas.move(arc, 1,0)

# c1 = tk.Button(windows,text='+++',command=moveit)
# c1.pack()

# canvas.pack()

# windows.mainloop()



#————————————————————————————————————————————————————————————————————

windows = tk.Tk()
windows.title('one_day')
windows.geometry('1440x1024')

l = tk.Label(windows,text='',bg="yellow")
l.pack()





windows.mainloop()

