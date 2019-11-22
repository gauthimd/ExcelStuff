#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import openpyxl

for x in range(11536):
    for y in range(16):
        print("A"+str(x)+"."+str(y).zfill(2))

for x in range(32768):
    for y in range(16):
        print("D"+str(x)+"."+str(y).zfill(2))

for x in range(32768):
    for y in range(16):
        print("E"+str(x)+"."+str(y).zfill(2))

for x in range(32768):
    for y in range(16):
        print("E0_"+str(x)+"."+str(y).zfill(2))

for x in range(32768):
    for y in range(16):
        print("E1_"+str(x)+"."+str(y).zfill(2))

for x in range(32768):
    for y in range(16):
        print("E2_"+str(x)+"."+str(y).zfill(2))

for x in range(32768):
    for y in range(16):
        print("E3_"+str(x)+"."+str(y).zfill(2))

for x in range(1536):
    for y in range(16):
        print("H"+str(x)+"."+str(y).zfill(2))

for x in range(6144):
    for y in range(16):
        print(str(x)+"."+str(y).zfill(2))

for x in range(512):
    for y in range(16):
        print("W"+str(x)+"."+str(y).zfill(2))
