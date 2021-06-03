# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:27:37 2021

@author: shimizu203
"""



clist=[]
Plain=(input("Insert plain text(*large only) ="))
aseed=int(input("main seed="))
bseed=int(input("sub seed="))
x=1


plist=list(Plain)
print(plist[:])
j=len(plist)



for i in range(j):
    qlist=[]
    for num in range(25):
        x=(x+aseed)%25
        qlist.append(x) 
    
    
    print(qlist [:])


    na=ord(plist[i])
    print(na)

    o=na-65

    xa=qlist[o]
    xa=xa+65
    crypt=chr(xa)
    print(crypt)
    
    aseed=aseed+bseed
    
