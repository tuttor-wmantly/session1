def remove_duplicate(string):
	duplicates = ''
	return_string = ''
	last = string[0]

	for letter in string[1:]:
		if letter == last:
			duplicates += letter
		else:
			return_string += letter
		last = letter

	return return_string, duplicates
