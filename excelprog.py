#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

i = 1
for x in range(11536):
    for y in range(16):
        z = "A"+str(x)+"."+str(y).zfill(2)
        w = "A"+str(i)
        sheet[w] = z
        i += 1
        
i = 1
for x in range(32768):
    for y in range(16):
        z = "D"+str(x)+"."+str(y).zfill(2)
        w = "B"+str(i)
        sheet[w] = z
        i += 1   

i = 1
for x in range(32768):
    for y in range(16):
        z = "E"+str(x)+"."+str(y).zfill(2)
        w = "C"+str(i)
        sheet[w] = z
        i += 1 

i = 1
for x in range(32768):
    for y in range(16):
        z = "E0_"+str(x)+"."+str(y).zfill(2)
        w = "D"+str(i)
        sheet[w] = z
        i += 1 

i = 1
for x in range(32768):
    for y in range(16):
        z = "E1_"+str(x)+"."+str(y).zfill(2)
        w = "E"+str(i)
        sheet[w] = z
        i += 1 

i = 1
for x in range(32768):
    for y in range(16):
        z = "E2_"+str(x)+"."+str(y).zfill(2)
        w = "F"+str(i)
        sheet[w] = z
        i += 1 

i = 1
for x in range(32768):
    for y in range(16):
        z = "E3_"+str(x)+"."+str(y).zfill(2)
        w = "G"+str(i)
        sheet[w] = z
        i += 1 

i = 1
for x in range(1536):
    for y in range(16):
        z = "H"+str(x)+"."+str(y).zfill(2)
        w = "H"+str(i)
        sheet[w] = z
        i += 1 

i = 1
for x in range(6144):
    for y in range(16):
        z = str(x)+"."+str(y).zfill(2)
        w = "I"+str(i)
        sheet[w] = z
        i += 1 

i = 1
for x in range(512):
    for y in range(16):
        z = "W"+str(x)+"."+str(y).zfill(2)
        w = "J"+str(i)
        sheet[w] = z
        i += 1 

wb.save(filename='output.xlsx')
