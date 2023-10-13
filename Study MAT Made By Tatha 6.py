# -*- File Handling -*-
"""
Created on Sat Aug  6 02:47:37 2022

@author: Tathagata Sau
"""

hello=open("hello.txt","r")
#print(hello.readable())
#print(hello.read())
#print(hello.readline())
for i in hello.readlines():
    print(i)
#print(hello.readlines()) # self made array
hello.close()

## add lines don't run it more than one. if you do then the fiile is change permanent
hello=open("hello.txt","a")
hello.write("She is the most pretty humna i'v ever seen.\nShe tells lies when she needs to.\n But I can catch them pretty easy. ")
hello.close()
'''
hello = open("hello.txt", "w")
hello.write("\n Usmi is Very Bad at insulting")# fully override the file into new
hello.close()
'''
hello_html = open("Index.html","w")
hello_html.write("<p> This is a Webpage</p>")
hello_html.close()
