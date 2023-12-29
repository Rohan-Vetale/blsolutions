def reverStr(str1):
	outputStr = ""
	for char in str1:
		outputStr = char + outputStr
		print(char)
	return outputStr

#assuming a static input
ogStr = "HelloWorld" 

#string reversed will be returned here
response = reverStr(ogStr)

#printing of the reversed string and original string
print("The given original string was " + ogStr + " and reversed string is " + response) 
