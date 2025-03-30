from tkinter import *
import tkinter.messagebox as messagebox
from math import *
import os
from sys import prefix
from pathlib import Path

folder=Path(__file__).parent.resolve()

def main():
    def One():
        Expressions.insert(END,'1')
    def Two():
        Expressions.insert(END,'2')
    def Three():
        Expressions.insert(END,'3')
    def Four():
        Expressions.insert(END,'4')
    def Five():
        Expressions.insert(END,'5')
    def Six():
        Expressions.insert(END,'6')
    def Seven():
        Expressions.insert(END,'7')
    def Eight():
        Expressions.insert(END,'8')
    def Nine():
        Expressions.insert(END,'9')
    def Zero():
        Expressions.insert(END,'0')
    def LeftBrackrt():
        Expressions.insert(END,'(')
    def RightBracket():
        Expressions.insert(END,')')
    def ce():
        Expressions.delete(0,END)
    def Point():
        Expressions.insert(END,'.')
    def Delete():
        string=Expressions.get()
        Expressions.delete(0,END)
        Expressions.insert(0,string[0:len(string)-1])
    def Add():
        Expressions.insert(END,'+')
    def Sub():
        Expressions.insert(END,'-')
    def Mul():
        Expressions.insert(END,'*')
    def Div():
        Expressions.insert(END,'/')
    def Equal():
        if Expressions.get()=='':
            messagebox.showwarning(title='未输入数字',message='你还没有输入数字')
        else:
            try:
                Expressions.insert(END,'='+str(eval(Expressions.get())))
            except:
                messagebox.showerror(title='错误！',message="无法将表达式'"+Expressions.get()+"'解析")
    
    def calculator():
        global Expressions

        root=Tk()
        root.iconbitmap(os.path.join(folder,'icon.ico'))
        size=21
        root.title('计算器')
        root.geometry('545x370')

        Expressions=Entry(root,width=35,font=('黑体',24))
        one=Button(root,text='1',width=size//3,font=('微软雅黑',24),command=One)
        two=Button(root,text='2',width=size//3,font=('微软雅黑',24),command=Two)
        three=Button(root,text='3',width=size//3,font=('微软雅黑',24),command=Three)
        four=Button(root,text='4',width=size//3,font=('微软雅黑',24),command=Four)
        five=Button(root,text='5',width=size//3,font=('微软雅黑',24),command=Five)
        six=Button(root,text='6',width=size//3,font=('微软雅黑',24),command=Six)
        seven=Button(root,text='7',width=size//3,font=('微软雅黑',24),command=Seven)
        eight=Button(root,text='8',width=size//3,font=('微软雅黑',24),command=Eight)
        nine=Button(root,text='9',width=size//3,font=('微软雅黑',24),command=Nine)
        zero=Button(root,text='0',width=size//3,font=('微软雅黑',24),command=Zero)
        leftBracket=Button(root,text='(',width=size//3,font=('微软雅黑',24),command=LeftBrackrt)
        rightBracket=Button(root,text=')',width=size//3,font=('微软雅黑',24),command=RightBracket)
        CE=Button(root,text='CE',width=size//3,font=('微软雅黑',24),command=ce)
        point=Button(root,text='.',width=size//3,font=('微软雅黑',24),command=Point)
        equal=Button(root,text='=',width=size//3,font=('微软雅黑',24),command=Equal)
        delete_=Button(root,text='删除',width=size//3,font=('微软雅黑',24),command=Delete)
        add=Button(root,text='+',width=size//3,font=('微软雅黑',24),command=Add)
        sub=Button(root,text='-',width=size//3,font=('微软雅黑',24),command=Sub)
        mul=Button(root,text='*',width=size//3,font=('微软雅黑',24),command=Mul)
        div=Button(root,text='/',width=size//3,font=('微软雅黑',24),command=Div)

        Expressions.place(x=0,y=0)
        one.place(x=0,y=100)
        two.place(x=135,y=100)
        three.place(x=270,y=100)
        four.place(x=0,y=165)
        five.place(x=135,y=165)
        six.place(x=270,y=165)
        seven.place(x=0,y=230)
        eight.place(x=135,y=230)
        nine.place(x=270,y=230)
        zero.place(x=135,y=300)
        leftBracket.place(x=0,y=35)
        rightBracket.place(x=135,y=35)
        CE.place(x=270,y=35)
        point.place(x=0,y=300)
        equal.place(x=270,y=300)
        delete_.place(x=405,y=35)
        add.place(x=405,y=100)
        sub.place(x=405,y=165)
        mul.place(x=405,y=230)
        div.place(x=405,y=300)

        root.mainloop()
    
    calculator()

main()