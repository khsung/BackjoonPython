#class Tree:
#    def __init__(self,data,lchild,rchild):
#        self.data=data
#        self.lchild=lchild
#        self.rchild=rchild
#tree=Tree(1,2,Tree(3,4,5))
#
#print(tree.data)
#print(tree.lchild)
#print(tree.rchild.data)



#from urllib import request
#from bs4 import BeautifulSoup

#target=request.urlopen("http://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp")
#soup=BeautifulSoup(target,"html.parser")
#print(soup)
#for location in soup.select("location"):
#    print("도시:", location.select_one("city").string)
#    print("날씨:", location.select_one("wf").string)
#    print("최저기온:", location.select_one("tmn").string)
#    print("최고기온:", location.select_one("tmx").string)
#    print()

#from tkinter import *
#from tkinter.colorchooser import *
#window=Tk()
#window.title("test")
#window.geometry("400x400")
#window.resizable(width=False, height=False)
##color=askcolor()
#label1=Label(window,text="Python",font=("궁서체",18),bg="red",width=10,height=10)
#label2=Label(window,text="java",font=("HY나무B",20))
##label2=Label(window,text="java",font=("HY나무B",20),bg=color[1])
#label3=Label(window,text="java",font=("HY나무B",20),bg="yellow",width=10,height=10,anchor=SW)

#button1=Button(window,text="주문")
#button1.pack(side=RIGHT)

##label1.pack()
#label2.pack()
#label3.pack()


#btnList=[None]*3
#for i in range(len(btnList)):
#    btnList[i]=Button(window,text="버튼"+str(i+1))

#for btn in btnList:
#    btn.pack(side=LEFT,padx=10,pady=10)
    
#window.mainloop()

#def func_open():
#    print("open")
#def func_exit():
#    print("exit")

#window=Tk()
#mainmenu=Menu(window)
#window.config(menu=mainmenu)

##상위메뉴
#filemenu=Menu(mainmenu)
#filemenu1=Menu(mainmenu)

#mainmenu.add_cascade(label="파일",menu=filemenu)
#mainmenu.add_cascade(label="편집",menu=filemenu1)

##하위메뉴
#filemenu.add_command(label="열기",command=func_open)
#filemenu.add_separator()
#filemenu.add_command(label="종료",command=func_exit)
#window.mainloop()



#2042 구간 합 구하기 연습
import sys

def init(left,right,index):
    global origin,segment
    if left==right:
        segment[index]=origin[left-1]
        return segment[index]
    else:
        mid=(left+right)//2
        segment[index]=init(left,mid,2*index)+init(mid+1,right,2*index+1)
        return segment[index]

def update(left,right,target,index,diff):
    global segment
    segment[index]+=diff
    if left==target and right==target:
        pass
    else:
        mid=(left+right)//2
        if mid>=target:
            return update(left,mid,target,2*index,diff)
        else:
            return update(mid+1,right,target,2*index+1,diff)

def findsum(left,right,start,end,index):
    global segment
    if left==start and right==end:
        return segment[index]
    else:
        mid=(left+right)//2
        if mid>=end:
            return findsum(left,mid,start,end,2*index)
        elif mid<start:
            return findsum(mid+1,right,start,end,2*index+1)
        else:
            temp_sum=findsum(left,mid,start,mid,2*index)+findsum(mid+1,right,mid+1,end,2*index+1)
            return temp_sum

n,m,k=map(int,sys.stdin.readline().split())
origin=[]
segment=[0 for i in range(4*n)]
left=1
right=n
init_index=1
for i in range(n):
    origin.append(int(sys.stdin.readline()))
init(left,right,init_index)
for i in range(m+k):
    command=list(map(int,sys.stdin.readline().split()))
    if command[0]==1:
        diff=command[2]-origin[command[1]-1]
        origin[command[1]-1]=command[2]
        update(left,right,command[1],init_index,diff)
    else:
        print(findsum(left,right,command[1],command[2],init_index))