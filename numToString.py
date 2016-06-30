ones = ["zero",
		"one",
		"two",
		"three",
		"four",
		"five",
		"six",
		"seven",
		"eight",
		"nine",]

teens = ["ten",
		"eleven",
		"twelve",
		"thirteen",
		"fourteen",
		"fifteen",
		"sixteen",
		"seventeen",
		"eighteen",
		"nineteen",]

tens = ["blank",
		"blank",
		"twenty",
		"thirty",
		"fourty",
		"fifty",
		"sixty",
		"seventy",
		"eighty",
		"ninety",]

def formString (inNum):
	if inNum < 10:
		stringSoFar = ones[inNum]
	elif inNum < 20:
		stringSoFar = teens[inNum-10]
	elif inNum < 100:
		stringSoFar = tens[inNum//10]
		stringSoFar = stringSoFar + " " + ones[(inNum%10)]
	else:
		stringSoFar = str(ones[inNum//100])
		stringSoFar = stringSoFar + " hundred "
		leftOver = (inNum % 100)
		if leftOver < 10 and leftOver > 0:
			stringSoFar = stringSoFar + ones[leftOver]
		elif leftOver < 20:
			stringSoFar = stringSoFar +teens[leftOver-10]
		else:
			stringSoFar = stringSoFar + tens[leftOver//10]
			if (leftOver%10 !=0):
				stringSoFar = stringSoFar + " " + ones[(leftOver%10)]
	return stringSoFar
	
def thousandLevels (inNum, n):
	if ((inNum // 1000) >= 1):
		soFar = thousandLevels ((inNum//1000), n+1)
		if (inNum % 1000 != 0):
			soFar = soFar + formString(inNum % 1000)
	else:
		if (inNum % 1000 != 0 or (n == 0)):
			soFar = formString(inNum)
	
	if (inNum % 1000 != 0):	
		if n == 1:
			soFar = soFar + " thousand "
		elif n == 2:
			soFar = soFar + " million "

	return soFar
		 

def stringToWord (a):
	return thousandLevels(a,0)


myStr = stringToWord(995);
print myStr
myStr = stringToWord(1000860);
print myStr



