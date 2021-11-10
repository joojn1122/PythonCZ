# -*- coding: utf-8 -*-
import sys, os


file = sys.argv[1]

with open(file,"r",encoding="UTF-8") as f:
	code = f.read()
	compiledCode = code.replace("veřejný","global").replace("funkce","def").replace("vstup","input").replace("zkus:","try:").replace("chyť","except").replace("chybu","Exception").replace("poslední","pop").replace("délka","len").replace("list","[]").replace("nebude","!=").replace("nic",'""').replace("takypokud","elif").replace("jestli", "if").replace("pokud","if").replace(" v "," in ").replace("pro","for").replace("vypiš","print").replace("vypis","print").replace(" s "," with ").replace("otevři","open").replace("otevri","open").replace("jako","as").replace("vlož","import").replace("prečti","read").replace("precti","read").replace("rozděl","split").replace("rozdel","split").replace("nahrad","replace").replace("nahraď","replace").replace("vrať","return").replace("vrat","return").replace("bude","==").replace("rozsah","range").replace("přidej","append").replace("jinak","else").replace(" nebo "," or ").replace("zruš","break").replace("Nepravda","False").replace("Pravda","True").replace("je","=")

with open("run.py","w",encoding="UTF-8") as f:
	f.write(compiledCode)

import run