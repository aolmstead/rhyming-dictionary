TARGET = 'ASSOCIATE'

# fine the part which rhymes strongly, strip stress values
def find_phones(phones, symbol_conversions):
	phones.reverse()
	
	# find the position of the last strong stress
	min_stress_to_continue = -1
	strong_stress_index = -1
	for i, phone in enumerate(phones):
		stress = phone[-1]	# determine stress
		phones[i] = symbol_conversions[phone] # apply symbol map
		if stress.isdigit():
			stress = int(stress)-(-1)**int(stress)+1	# this silly transormation is here because 1 means primary and 2 means secondary, but I want 0<1<2
			if int(stress) >= min_stress_to_continue:	# by editing the cmudict, ones and twos could be switched, so I'm leaving the extra int() functions in until then
				min_stress_to_continue = int(stress)	# it would probably be best to just edit the cmudict to only have the endings of words
				strong_stress_index = i
			else:
				break
	
	return phones[0:strong_stress_index+1]



# create dictionary
symbol_conversions = {}
with open('C:\\workspace\\rhyming dictionary\\my-cmudict-0.7b.symbols','r') as cmu_symbol_file:
	for line in cmu_symbol_file:
		symbol_conversions[line.split()[0]] = line.split()[1]

# create and populate the dictionary using the files from http://www.speech.cs.cmu.edu/cgi-bin/cmudict
dictionary = {}
with open('C:\\workspace\\rhyming dictionary\\my-cmudict-0.7b.txt','r') as cmu_dict_file:
	# read in each line
	for line in cmu_dict_file:
		# skip the line if we're in the header
		if line[0] == ';':
			continue
		else:
			word = line.split()[0]
			dictionary[word] = find_phones(line.split()[1::], symbol_conversions)

# check for multiple pronunciations
if TARGET + "(1)" in dictionary:
	print("Other pronunciations found! You might want to check", TARGET + "(1)", end="", flush=True)	# is flush=True really needed?
	paren = 2
	while True:
		if TARGET + "(" + str(paren) + ")" in dictionary:
			print(",", TARGET + "(" + str(paren) + ")", end="", flush=True)
			paren += 1;
		else:
			break
	print()

#output result
target_rhyme = dictionary[TARGET]
rhymes_found = 0;
for key in dictionary:
	if dictionary[key] == target_rhyme and key != TARGET:
		print(key)
		rhymes_found += 1;
print(rhymes_found, 'perfect rhymes found for', TARGET + '.')
