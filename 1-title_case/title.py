def titlecase(string, exceptions):
  # Make sure ALL the letters start out as lower case and convert the string to a list on the spaces.
	word_list = string.lower().split()

  # Walk the list of words.
	for index, word in enumerate(word_list):
    # Make sure the word is not in the passed exceptions and not the the firt word.
		if word not in exceptions or index == 0:
			word_list[index] = word.capitalize()

  # Return the title case list as string
	return ' '.join(word_list)
