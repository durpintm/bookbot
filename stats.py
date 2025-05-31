def get_words_count(text):
	return len(text.split(" "))

def get_characters_count(text):
	char_dict = {}
	for char in text:
		key = char.lower()
		if key in char_dict:
			char_dict[key] += 1
		else:
			char_dict[key] = 1

	return char_dict

def get_sorted_char_list(char_dict):
	sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

	return sorted_dict

