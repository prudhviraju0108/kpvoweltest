#!/usr/bin/python
def vowelcounter(word):
	word=word.lower()
	vowels=['a','e','i','o','u']
	for i in vowels:
		if i in word:
			count=word.count(i)
			print (i,count)
print("Now printing number of vowels")
vowelcounter('prudhvI Raju')
