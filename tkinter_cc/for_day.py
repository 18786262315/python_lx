from tkinter import *
from tkinter.messagebox import *  #这是弹出窗口


def author():#将函数与about进行了绑定
    showinfo('作者信息', '本软件由付志强完成！')
def about(): 
    showinfo('版权信息。copyright', '本软件归属于付志强')
    

root=Tk()
root.title('Fuzhiqiang Node')
root.geometry('800x500+100+100') #构建一个矩形窗体    初始化的显示位置    100  100  大小  800x500

#创建一个menu
menubar=Menu(root)
root.config(menu=menubar)
#创建一系列的子menu
filemenu=Menu(menubar)
filemenu.add_command(label='新建',accelerator='Ctrl + N')#accelerator 快捷键，  new  点击事件函数
filemenu.add_command(label='打开',accelerator='Ctrl + O')
filemenu.add_command(label='保存',accelerator='Ctrl + S')
filemenu.add_command(label='另存为',accelerator='Ctrl + Shift + S')
menubar.add_cascade(label='文件',menu=filemenu)





#编辑菜单
editmenu=Menu(menubar)
editmenu.add_command(label='撤销',accelerator='Ctrl + Z')
editmenu.add_command(label='重做',accelerator='Ctrl + Y')
editmenu.add_separator()#分隔符
editmenu.add_command(label='剪切',accelerator='Ctrl + X')
editmenu.add_command(label='复制',accelerator='Ctrl + C')
editmenu.add_command(label='粘贴',accelerator='Ctrl + V')
editmenu.add_separator()#分隔符
editmenu.add_command(label='查找',accelerator='Ctrl + F')
editmenu.add_command(label='全选',accelerator='Ctrl + A')
menubar.add_cascade(label='编辑',menu=editmenu)

#about菜单
aboutmenu=Menu(menubar)
aboutmenu.add_command(label='作者',command=author)#command  对应的函数定义在前面
aboutmenu.add_command(label='版权',command=about)
menubar.add_cascade(label='关于',menu=aboutmenu)

#实现toolbar
toolbar=Frame(root,height=25,bg='light sea green')
shortButton=Button(toolbar,text='打开')
shortButton.pack(side=LEFT,padx=5,pady=5)

shortButton=Button(toolbar,text='保存')
shortButton.pack(side=LEFT)
toolbar.pack(expand=NO,fill=X)#全部填充海蓝色，显示toolbar栏

#status bar
status=Label(root,text='Ln20',relief=SUNKEN,anchor=W)#对齐方式  W  左对齐
status.pack(side=BOTTOM,fill=X) #显示status状态栏

#linenumber&text
lnlabel=Label(root,width=2,bg='antique white')
lnlabel.pack(side=LEFT,fill=Y)#将Y轴填充满

textPad=Text(root,undo=True)
textPad.pack(expand=YES, fill=BOTH)#允许进行扩展 ,填充X，Y轴

scroll=Scrollbar(textPad)#右侧的移动下滑栏
textPad.config(yscrollcommand=scroll.set)#在Y轴显示   yscrollcommand
scroll.config(command=textPad.yview)#这是为了让编辑内容和下拉栏同时移动
scroll.pack(side=RIGHT,fill=Y)#显示

#about信息实现

root.mainloop()