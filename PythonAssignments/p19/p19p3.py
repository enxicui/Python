#p19p3.py

import os

def check(s):
	# count numbers
	n1 = s.count("<")
	n2 = s.count(">")
	n3 = s.count("(")
	n4 = s.count(")")
	n5 = s.count("{")
	n6 = s.count("}")
	n7 = s.count("[")
	n8 = s.count("]")

	print ("The number of < is :", n1)
	print ("The number of > is :", n2)
	print ("The number of ( is :", n3)
	print ("The number of ) is :", n4)
	print ("The number of { is :", n5)
	print ("The number of } is :", n6)
	print ("The number of [ is :", n7)
	print ("The number of ] is :", n8)

	if n1 == n2 and n3 == n4 and n5 == n6 and n7 == n8 :
		print ("Tis file has balanced brackets.")
	else :
		print ("This file has not balanced brackets.")
	print ("Finished!")
	

if not os.path.isfile("/Users/judy/Desktop/p18.txt") :
	# check whether the p18.txt exist
	print ("Error, p18.txt is not exist.")
else :
	# if p18.txt exist, read it and transform its content to chenk function
	file = open("/Users/judy/Desktop/p18.txt", 'r')
	content = file.read()
	check(content)
	
