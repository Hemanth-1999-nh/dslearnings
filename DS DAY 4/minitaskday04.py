# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:46:50 2022

@author: HEMANTH NAGUNOORI
"""

#step-1 : To create an empty dictionary
csv = {}

print(" Create a program that reads from one CSV file (/etc/passwd),and writes to another one ")
csv = open("data doc day_04.txt", "r")

print(csv.read())
csv.close()

csv = open("data doc day_04.txt", "r")
print(csv.readline())
csv.close()

csv = open("data doc day_04.txt", "r")
print(csv.readlines())
csv.close()

csv = open("data doc day_04.txt", "w")
print(csv.write("upri;.1802"))
csv.close()

print(csv.read())
csv.close()

csv = open("data doc day_04.txt", "r")
csv.close()

csv = open("data doc day_04.txt", "w")
print(csv.write("username;,00874"
"heman;,1864"
"vampire;,1852"
"headache;,1867"
"pacer;,1848"
"unnie;,1862"
"mukku;,1866"
"fatthi;,1847"
"striker;,1829"
"kukka;,1849"
"telugu;,1888"
"puli;,1886"))
csv.close()

