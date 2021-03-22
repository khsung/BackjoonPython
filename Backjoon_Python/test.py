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
from urllib import request
from bs4 import BeautifulSoup

target=request.urlopen("http://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp")
soup=BeautifulSoup(target,"html.parser")
print(soup)
for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()