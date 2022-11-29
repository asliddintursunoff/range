# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:49:01 2022

@author: asad
"""

"""RANGE FUNKSIYASINI YARATAMIZ"""
sonlar=[]

def function(min=int(input("1-sonni kiriting")),max=int(input("2-sonni kiriting")),steps=int(input("aa"))):
    while min<max:
        if steps==0:
            sonlar.append(min)
            min+=1
            
        else:
            min=min+steps
            sonlar.append(min)
function()
def funk(printer):
    printer=sonlar[:]
    print(printer)
funk(sonlar[:])