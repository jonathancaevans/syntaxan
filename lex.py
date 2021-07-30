#!/usr/bin/python

import sys

inputString = sys.argv[1]
lexemes = []
def di(name, token):
	print("Next token is: ", token, " Next lexeme is ", name)
	lexemes.insert(0, token)
	

def lex(string, lexeme):
	if string == "":
		return
	if lexeme != 0:
		if lexeme == 1 and string[0] == 'r':
			lex(string[1:], 0)
			di("for", 1)
		elif lexeme == 2 and string[0:3] == 'oat':
			lex(string[3:], 0)
			di("float", 2)
		elif lexeme == 3 and string[0] == 't':
			lex(string[1:], 0)
			di("int", 3)
		elif lexeme == 4 and string[0] == 'f':
			lex(string[1:], 0)
			di("int", 4)
	else:
		if string[0].isspace():
			return lex(string[1:], 0)
		elif string[0] == 'f':
			if string[1] == 'o':
				return lex(string[2:], 1)
			elif string[1] == 'l':
				return lex(string[2:], 2)
		elif string[0] == 'i':
			if string[1] == 'n':
				return lex(string[2:], 3)
			elif string[1] == 'f':
				return lex(string[2:], 4)
		elif string[0:4] == 'else':
			lex(string[4:], 0)
			di("else", 5)
		elif string[0:5] == 'while':
			lex(string[5:], 0)
			di("while", 6)
		elif string[0:2] == 'do':
			lex(string[2:], 0)
			di("do", 7)
		elif string[0:6] == 'switch':
			lex(string[6:], 0)
			di("switch", 8)
		elif string[0:5] == 'class':
			lex(string[5:], 0)
			di("class", 9)
		elif string[0:4] == 'void':
			lex(string[4:], 0)
			di("void", 10)
		elif string[0:4] == 'bool':
			lex(string[4:], 0)
			di("bool", 11)
		elif string[0] == '{':
			lex(string[1:], 0)
			di("{", 12)
		elif string[0] == '}':
			lex(string[1:], 0)
			di("}", 13)
		elif string[0] == '(':
			lex(string[1:], 0)
			di("(", 14)
		elif string[0] == ')':
			lex(string[1:], 0)
			di(")", 15)
def syn(lexe, lex):
	if(len(lexe) == 0):
		return
	print(lexe, lex)
	if lex == 14 and lexe[0] == 14 and lexe[1] == 15:
		syn(lexe[2:], 12)
	elif lex == 12 and lexe[0] == 12:
		i = 0
		for x in lexe[1:]:
			if x == 13:
				syn(lexe[1:i], 0)
			i+=1

	if lexe[0] == 6:
		syn(lexe[1:], 14)
	elif lexe[0] == 4:
		syn(lexe[1:], 14)
	elif lexe[0] == 7:
		syn(lexe[1:], 14)

lex(inputString, 0)

syn(lexemes, 0)
