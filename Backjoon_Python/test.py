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

from tkinter import *
window=Tk()
window.title("test")
window.geometry("400x400")
window.resizable(width=False, height=False)
label1=Label(window,text="Python",font=("궁서체",18),bg="red",width=10,height=10)
label2=Label(window,text="java",font=("HY나무B",20),bg="yellow")
label3=Label(window,text="java",font=("HY나무B",20),bg="yellow",anchor=LEFT)
label1.pack()
label2.pack()
label3.pack()
window.mainloop()