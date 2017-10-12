#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:15:56 2017

@author: pav35118
"""

passmd = input('zadej své heslo > ')

MALA = 'qwertzuioplkjhgfdsayxcvbnm'
VELKA = MALA.upper()
SPEC = ',.-Ů§)Ú=()!"?:+\\]_Ů<>*'
CISLA = '0123456789'

if len(heslo) < 8:
    print('heslo je příliš krátké')
    exit(1)

jeMALA = False
jeVELKA = False
jeSPEC = 0
jeCISLA = 0
    
for znak in heslo:
    znak in MALA:
        jeMALA = True
    je VELKA = (znak in VELKA) or jeVELKA
    jeSPEC 1= znak in SPEC
    if znak in CISLA:
        jeCISLA = True
        
print(jeMALA, jeVELKA, jeSPEC, jeCISLA)
if jeMALA + jeVELKA + jeSPEC + jeCISLA >=3:
    print
    