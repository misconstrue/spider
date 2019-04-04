import requests
import sys
import re

from viewforspider import Ui_spider_view
from collections import Counter
from requests import RequestException
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThread


# 热门 时间 评价
addr = " "
url = [
        "https://maoyan.com/films?showType=3&catId=10&sortId=1&offset=",  # 科幻
        "https://maoyan.com/films?showType=3&catId=10&sortId=2&offset=",
        "https://maoyan.com/films?showType=3&catId=10&sortId=3&offset=",
        "https://maoyan.com/films?showType=3&catId=5&sortId=1&offset=",  # 动作
        "https://maoyan.com/films?showType=3&catId=5&sortId=2&offset=",
        "https://maoyan.com/films?showType=3&catId=5&sortId=3&offset=",
        "https://maoyan.com/films?showType=3&catId=8&sortId=1&offset=",  # 悬疑
        "https://maoyan.com/films?showType=3&catId=8&sortId=2&offset=",
        "https://maoyan.com/films?showType=3&catId=8&sortId=3&offset=",
        "https://maoyan.com/films?showType=3&catId=9&sortId=1&offset=",  # 冒险
        "https://maoyan.com/films?showType=3&catId=9&sortId=2&offset=",
        "https://maoyan.com/films?showType=3&catId=9&sortId=3&offset=",
        "https://maoyan.com/films?showType=3&catId=12&sortId=1&offset=",  # 战争
        "https://maoyan.com/films?showType=3&catId=12&sortId=2&offset=",
        "https://maoyan.com/films?showType=3&catId=12&sortId=3&offset=",
        "https://maoyan.com/films?showType=3&catId=14&sortId=1&offset=",  # 奇幻
        "https://maoyan.com/films?showType=3&catId=14&sortId=2&offset=",
        "https://maoyan.com/films?showType=3&catId=14&sortId=3&offset=",
        "https://maoyan.com/films?showType=3&catId=2&sortId=1&offset=",  # 喜剧
        "https://maoyan.com/films?showType=3&catId=2&sortId=2&offset=",
        "https://maoyan.com/films?showType=3&catId=2&sortId=3&offset=",
       ]


class spider(QThread):

    all_result = []

    def __init__(self, addrs):
        super(spider, self).__init__()
        self.addr = addrs

    def get_source(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            return None
        except RequestException as e:
            print(e)
            return None

    def parse_source(self, content):
        string = re.compile('<div.*?class.*?title="(.*?)">.*?<a.*?</a>.*?</div>', re.S)
        result = string.findall(content)
        return result

    def run(self):
        for i in range(3):
            spider.all_result += self.parse_source(self.get_source(self.addr + str(30*i)))

    def __del__(self):
        self.exiting = True
        self.wait()


class windows(Ui_spider_view, QWidget):
    def __init__(self):
        super(windows, self).__init__()
        self.setupUi(self)
        self.openfile.setEnabled(False)
        self.guessyoulike.setEnabled(False)
        self.textBrowser.setText("*********欢迎使用猫眼电影抓取*********")
        self.textBrowser.append("*********使用抓取自动保存文件*********")
        self.textBrowser.append("********使用提取则显示排序内容********")

    def execute(self):
        global addr
        if self.moviesclass.currentIndex() == 1 and self.sortclass.currentIndex() == 1:
            addr = url[0]  # 科幻热门
        elif self.moviesclass.currentIndex() == 1 and self.sortclass.currentIndex() == 2:
            addr = url[1]  # 科幻时间
        elif self.moviesclass.currentIndex() == 1 and self.sortclass.currentIndex() == 3:
            addr = url[2]  # 科幻评价
        elif self.moviesclass.currentIndex() == 2 and self.sortclass.currentIndex() == 1:
            addr = url[3]  # 动作热门
        elif self.moviesclass.currentIndex() == 2 and self.sortclass.currentIndex() == 2:
            addr = url[4]  # 动作时间
        elif self.moviesclass.currentIndex() == 2 and self.sortclass.currentIndex() == 3:
            addr = url[5]  # 动作评价
        elif self.moviesclass.currentIndex() == 3 and self.sortclass.currentIndex() == 1:
            addr = url[6]  # 悬疑热门
        elif self.moviesclass.currentIndex() == 3 and self.sortclass.currentIndex() == 2:
            addr = url[7]  # 悬疑时间
        elif self.moviesclass.currentIndex() == 3 and self.sortclass.currentIndex() == 3:
            addr = url[8]  # 悬疑评价
        elif self.moviesclass.currentIndex() == 4 and self.sortclass.currentIndex() == 1:
            addr = url[9]  # 冒险热门
        elif self.moviesclass.currentIndex() == 4 and self.sortclass.currentIndex() == 2:
            addr = url[10]  # 冒险时间
        elif self.moviesclass.currentIndex() == 4 and self.sortclass.currentIndex() == 3:
            addr = url[11]  # 冒险评价
        elif self.moviesclass.currentIndex() == 5 and self.sortclass.currentIndex() == 1:
            addr = url[12]  # 战争热门
        elif self.moviesclass.currentIndex() == 5 and self.sortclass.currentIndex() == 2:
            addr = url[13]  # 战争时间
        elif self.moviesclass.currentIndex() == 5 and self.sortclass.currentIndex() == 3:
            addr = url[14]  # 战争评价
        elif self.moviesclass.currentIndex() == 6 and self.sortclass.currentIndex() == 1:
            addr = url[15]  # 奇幻热门
        elif self.moviesclass.currentIndex() == 6 and self.sortclass.currentIndex() == 2:
            addr = url[16]  # 奇幻时间
        elif self.moviesclass.currentIndex() == 6 and self.sortclass.currentIndex() == 3:
            addr = url[17]  # 奇幻评价
        elif self.moviesclass.currentIndex() == 7 and self.sortclass.currentIndex() == 1:
            addr = url[18]  # 喜剧热门
        elif self.moviesclass.currentIndex() == 7 and self.sortclass.currentIndex() == 2:
            addr = url[19]  # 喜剧时间
        elif self.moviesclass.currentIndex() == 7 and self.sortclass.currentIndex() == 3:
            addr = url[20]  # 喜剧评价
        else:
            self.textBrowser.setText("!!!!!请选择电影类别和排序方法!!!!!")
            return

        spider.all_result = []
        spider_son = spider(addr)
        spider_son.start()

        while True:
            if len(spider.all_result) == 90:
                length = len(spider.all_result)
                print("the content is:")
                print(spider.all_result)
                print("the length of the content is :" + str(length))
                if self.moviesclass.currentIndex() == 1:
                    with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list1.txt', 'w', encoding='utf-8') as file:
                        file.write("*************科幻电影*************" + "\n")
                        if self.sortclass.currentIndex() == 1:
                            file.write("***********按照热门排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 2:
                            file.write("***********按照时间排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 3:
                            file.write("***********按照评价排序:***********" + "\n")
                        for i in range(length):
                            file.write(str(i + 1) + ':' + spider.all_result[i] + '\n')
                        file.close()
                        self.textBrowser.setText("*********科幻类电影抓取完成********")
                elif self.moviesclass.currentIndex() == 2:
                    with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list2.txt', 'w', encoding='utf-8') as file:
                        file.write("*************动作电影*************" + "\n")
                        if self.sortclass.currentIndex() == 1:
                            file.write("***********按照热门排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 2:
                            file.write("***********按照时间排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 3:
                            file.write("***********按照评价排序:***********" + "\n")
                        for i in range(length):
                            file.write(str(i + 1) + ':' + spider.all_result[i] + '\n')
                        file.close()
                        self.textBrowser.setText("*********动作类电影抓取完成********")
                elif self.moviesclass.currentIndex() == 3:
                    with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list3.txt', 'w', encoding='utf-8') as file:
                        file.write("*************悬疑电影*************" + "\n")
                        if self.sortclass.currentIndex() == 1:
                            file.write("***********按照热门排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 2:
                            file.write("***********按照时间排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 3:
                            file.write("***********按照评价排序:***********" + "\n")
                        for i in range(length):
                            file.write(str(i + 1) + ':' + spider.all_result[i] + '\n')
                        file.close()
                        self.textBrowser.setText("*********悬疑类电影抓取完成********")
                elif self.moviesclass.currentIndex() == 4:
                    with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list4.txt', 'w', encoding='utf-8') as file:
                        file.write("*************冒险电影*************" + "\n")
                        if self.sortclass.currentIndex() == 1:
                            file.write("***********按照热门排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 2:
                            file.write("***********按照时间排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 3:
                            file.write("***********按照评价排序:***********" + "\n")
                        for i in range(length):
                            file.write(str(i + 1) + ':' + spider.all_result[i] + '\n')
                        file.close()
                        self.textBrowser.setText("*********冒险类电影抓取完成********")
                elif self.moviesclass.currentIndex() == 5:
                    with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list5.txt', 'w', encoding='utf-8') as file:
                        file.write("*************战争电影*************" + "\n")
                        if self.sortclass.currentIndex() == 1:
                            file.write("***********按照热门排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 2:
                            file.write("***********按照时间排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 3:
                            file.write("***********按照评价排序:***********" + "\n")
                        for i in range(length):
                            file.write(str(i + 1) + ':' + spider.all_result[i] + '\n')
                        file.close()
                        self.textBrowser.setText("*********战争类电影抓取完成********")
                elif self.moviesclass.currentIndex() == 6:
                    with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list6.txt', 'w', encoding='utf-8') as file:
                        file.write("*************奇幻电影*************" + "\n")
                        if self.sortclass.currentIndex() == 1:
                            file.write("***********按照热门排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 2:
                            file.write("***********按照时间排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 3:
                            file.write("***********按照评价排序:***********" + "\n")
                        for i in range(length):
                            file.write(str(i + 1) + ':' + spider.all_result[i] + '\n')
                        file.close()
                        self.textBrowser.setText("*********奇幻类电影抓取完成********")
                elif self.moviesclass.currentIndex() == 7:
                    with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list7.txt', 'w', encoding='utf-8') as file:
                        file.write("*************喜剧电影*************" + "\n")
                        if self.sortclass.currentIndex() == 1:
                            file.write("***********按照热门排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 2:
                            file.write("***********按照时间排序:***********" + "\n")
                        elif self.sortclass.currentIndex() == 3:
                            file.write("***********按照评价排序:***********" + "\n")
                        for i in range(length):
                            file.write(str(i + 1) + ':' + spider.all_result[i] + '\n')
                        file.close()
                        self.textBrowser.setText("*********喜剧类电影抓取完成********")
                self.openfile.setEnabled(True)
                self.guessyoulike.setEnabled(True)
                return

    def findyoulike(self):
        self.textBrowser.setText("********可能喜欢的电影：********")
        all_movies = []
        with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list1.txt', 'r', encoding='utf-8') as file:
            file.seek(83, 0)
            tmp = file.readlines()
            j = 0
            for i in tmp:
                j += 1
                if j >= 10:
                    all_movies.append(i[3:-1])
                else:
                    all_movies.append(i[2:-1])
        file.close()
        with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list2.txt', 'r', encoding='utf-8') as file:
            file.seek(83, 0)
            tmp = file.readlines()
            j = 0
            for i in tmp:
                j += 1
                if j >= 10:
                    all_movies.append(i[3:-1])
                else:
                    all_movies.append(i[2:-1])
        file.close()
        with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list3.txt', 'r', encoding='utf-8') as file:
            file.seek(83, 0)
            tmp = file.readlines()
            j = 0
            for i in tmp:
                j += 1
                if j >= 10:
                    all_movies.append(i[3:-1])
                else:
                    all_movies.append(i[2:-1])
        file.close()
        with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list4.txt', 'r', encoding='utf-8') as file:
            file.seek(83, 0)
            tmp = file.readlines()
            j = 0
            for i in tmp:
                j += 1
                if j >= 10:
                    all_movies.append(i[3:-1])
                else:
                    all_movies.append(i[2:-1])
        file.close()
        with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list5.txt', 'r', encoding='utf-8') as file:
            file.seek(83, 0)
            tmp = file.readlines()
            j = 0
            for i in tmp:
                j += 1
                if j >= 10:
                    all_movies.append(i[3:-1])
                else:
                    all_movies.append(i[2:-1])
        file.close()
        with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list6.txt', 'r', encoding='utf-8') as file:
            file.seek(83, 0)
            tmp = file.readlines()
            j = 0
            for i in tmp:
                j += 1
                if j >= 10:
                    all_movies.append(i[3:-1])
                else:
                    all_movies.append(i[2:-1])
        file.close()
        with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list7.txt', 'r', encoding='utf-8') as file:
            file.seek(83, 0)
            tmp = file.readlines()
            j = 0
            for i in tmp:
                j += 1
                if j >= 10:
                    all_movies.append(i[3:-1])
                else:
                    all_movies.append(i[2:-1])
        file.close()
        self.guessyoulike.setEnabled(False)
        movies_dict = dict(Counter(all_movies))
        most_like = sorted(movies_dict.items(), key=lambda x: x[1], reverse=True)
        num = 1
        for i, j in most_like:
            if j >= 3:
                self.textBrowser.append(str(num) + str(':') + i)
                num += 1
        return

    def open_file(self):
        self.textBrowser.setText(" ")
        if self.moviesclass.currentIndex() == 1:
            with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list1.txt', 'r', encoding='utf-8') as fl:
                data = fl.readlines()
                for list in data:
                    self.textBrowser.append(list)
            fl.close()
        elif self.moviesclass.currentIndex() == 2:
            with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list2.txt', 'r', encoding='utf-8') as fl:
                data = fl.readlines()
                for list in data:
                    self.textBrowser.append(list)
            fl.close()
        elif self.moviesclass.currentIndex() == 3:
            with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list3.txt', 'r', encoding='utf-8') as fl:
                data = fl.readlines()
                for list in data:
                    self.textBrowser.append(list)
            fl.close()
        elif self.moviesclass.currentIndex() == 4:
            with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list4.txt', 'r', encoding='utf-8') as fl:
                data = fl.readlines()
                for list in data:
                    self.textBrowser.append(list)
            fl.close()
        elif self.moviesclass.currentIndex() == 5:
            with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list5.txt', 'r', encoding='utf-8') as fl:
                data = fl.readlines()
                for list in data:
                    self.textBrowser.append(list)
            fl.close()
        elif self.moviesclass.currentIndex() == 6:
            with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list6.txt', 'r', encoding='utf-8') as fl:
                data = fl.readlines()
                for list in data:
                    self.textBrowser.append(list)
            fl.close()
        elif self.moviesclass.currentIndex() == 7:
            with open('C:\\Users\\lijing\\Desktop\\嵌入式作业\\list7.txt', 'r', encoding='utf-8') as fl:
                data = fl.readlines()
                for list in data:
                    self.textBrowser.append(list)
            fl.close()
        self.openfile.setEnabled(False)
        return

def main():
    app = QApplication(sys.argv)
    a = windows()
    a.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
