# -*- coding: utf-8 -*-
import sys, os


def replaceStr(string):
	return string.replace("veřejný","global").replace("funkce","def").replace("vstup","input").replace("zkus:","try:").replace("chyť","except").replace("chybu","Exception").replace("poslední","pop").replace("délka","len").replace("list","[]").replace("nebude","!=").replace("nic",'""').replace("takypokud","elif").replace("jestli", "if").replace("pokud","if").replace(" v "," in ").replace("pro","for").replace("vypiš","print").replace("vypis","print").replace(" s "," with ").replace("otevři","open").replace("otevri","open").replace("jako","as").replace("vlož","import").replace("prečti","read").replace("precti","read").replace("rozděl","split").replace("rozdel","split").replace("nahrad","replace").replace("nahraď","replace").replace("vrať","return").replace("vrat","return").replace("bude","==").replace("rozsah","range").replace("přidej","append").replace("jinak","else").replace(" nebo "," or ").replace("zruš","break").replace("Nepravda","False").replace("Pravda","True").replace("je","=")

def replaceCode(code):
	replacedCode = ""
	toBeReplacedCode = ""

	inQuotes1 = False
	inQuotes2 = False

	for char in code:
		if char == "'" and not inQuotes1:
			inQuotes2 = not inQuotes2

			if inQuotes2:
				replacedCode += replaceStr(toBeReplacedCode)
				toBeReplacedCode = ""

			replacedCode += "'"

		elif char == '"' and not inQuotes2:
			inQuotes1 = not inQuotes1

			if inQuotes1:
				replacedCode += replaceStr(toBeReplacedCode)
				toBeReplacedCode = ""

			replacedCode += '"'

		elif inQuotes1 or inQuotes2:
			replacedCode += char

		else:
			toBeReplacedCode += char

	replacedCode += replaceStr(toBeReplacedCode)
	
	return replacedCode

file = sys.argv[1]

with open(file,"r",encoding="UTF-8") as f:
	code = f.read()
	replacedCode = replaceCode(code)

with open("run.py","w",encoding="UTF-8") as f:
	f.write(replacedCode)

import run
