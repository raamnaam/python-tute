# here we try to count the no. of vowel and consonants in a string...


def function(n):
	
	i = len(n)-1
	vowel = 0
	consonants = 0

	for x in range(0,i):
		
		j = n[x]

		if (j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U'):
			vowel += 1

		elif j == ' ':
			pass

		else:
			consonants += 1
			#to check that it only count consonants we use to print them

			# print(j,consonants) remove this we just need answer
			# it's working do like share and subscribe to our channel for more solution like this and also to gain some additinal knowledge
			# so we need to go try some semilar kind of question thanks for watching.....

	print(vowel,consonants)



function("hello everyone in this  class we try to count number of vowel and consonants but this string nust not contain any kind of special charecter and numbers")