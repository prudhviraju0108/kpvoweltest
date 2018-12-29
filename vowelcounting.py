#!/usr/bin/python
import sys
word=sys.argv[1]
def vowelcounter(word):
	word=word.lower()
	vowels=['a','e','i','o','u']
	for i in vowels:
		if i in word:
			count=word.count(i)
			print (i,count)
print("Now printing number of vowels")
vowelcounter(word)
