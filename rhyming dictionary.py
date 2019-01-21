TARGET = 'ASSOCIATE'

# fine the part which rhymes strongly, strip stress values
def find_phones( phones ):
	phones.reverse()
	
	# find the position of the last strong stress
	min_stress_to_continue = -1
	strong_stress_index = -1
	for i, phone in enumerate(phones):
		stress = phone[-1]
		if stress.isdigit():
			stress = int(stress)-(-1)**int(stress)+1	# this silly transormation is here because 1 means primary and 2 means secondary, but I want 0<1<2
			if int(stress) > min_stress_to_continue:	# by editing the cmudict, ones and twos could be switched, so I'm leaving the extra int() functions in until then
				min_stress_to_continue = int(stress)	# it would probably be best to just edit the cmudict to only have the endings of words
				strong_stress_index = i
				phones[i] = phone[:-1]	# un-pythonic solution for stripping stress values https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python
			else:
				break
	
	return phones[0:strong_stress_index+1]




# open the file from http://www.speech.cs.cmu.edu/cgi-bin/cmudict
cmu_dict_file = open('C:\\workspace\\rhyming dictionary\\my-cmudict-0.7b.txt','r')

dictionary = {}

# read in each line
for line in cmu_dict_file:
	# skip the line if we're in the header
	if line[0] == ';':
		continue
	else:
		word = line.split()[0]
		dictionary[word] = find_phones(line.split()[1::])

# check for multiple pronunciations
if TARGET + "(1)" in dictionary:
	print("Other pronunciations found! You might want to check \"" + TARGET + "(1)" + "\"", end="", flush=True)	# is flush=True really needed?
	paren = 2
	while True:
		if TARGET + "(" + str(paren) + ")" in dictionary:
			print(", \"" + TARGET + "(" + str(paren) + ")" + "\"", end="", flush=True)
			paren += 1;
		else:
			break
	print()

#output result
target_rhyme = dictionary[TARGET]
perfect_rhymes_found = 0;
for key in dictionary:
	if dictionary[key] == target_rhyme:
		print(key)
		perfect_rhymes_found += 1;
print(perfect_rhymes_found, 'perfect rhymes found for', TARGET + '.')

# close the file
cmu_dict_file.close()







# wrap file safely, main function https://stackabuse.com/read-a-file-line-by-line-in-python/
# pass by ref https://www.tutorialspoint.com/python/python_functions.htm

# format dictionary as json for faster python performance
# integrate roget's thesaurus?

# what's it called when every vowel sound starting with the last strong one rhymes, but the consonants don't?
# family rhyme?
# additive/subtractive rhymes are cool, too?

# types of rhymes
# https://www.spire.live/en/blog/songwriting/5-types-of-rhymes-you-can-use-in-your-song.html
# https://www.youtube.com/watch?v=BLlPQBLTZdU
# https://genius.com/posts/24-Rap-genius-university-rhyme-types
# https://genius.com/Lit-genius-types-of-rhyme-annotated
# https://www.dailywritingtips.com/types-of-rhyme/

# just listen to rap and try to get the dictionary to return the rhymes
# seriously, "violence" should return "silence"
# "lieutenant" and "up in it"

# With ELK the E and L are important but the K could change, allowing BELT. Maybe K has more substitutes than L.

# Check out clever rhymes in Sondheim's work

# https://www.reddit.com/r/learnpython/wiki/index
# seems good https://www.slideshare.net/MattHarrison4/learn-90
# seems very good https://learnxinyminutes.com/docs/python3/