import sys
from stats import get_words_count, get_characters_count, get_sorted_char_list


def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()

		word_count: int = get_words_count(file_contents)

		char_dict = get_characters_count(file_contents)

		sorted_dict = get_sorted_char_list(char_dict)

		print_report(word_count, sorted_dict)

def print_report(word_count, char_dict):
	print("============ BOOKBOT ============\n")
	print("Analyzing book found at books/frankenstein.txt...\n")
	print("----------- Word Count ----------\n")
	print("Found 75767 total words\n")
	print("--------- Character Count -------\n")
	for key, value in char_dict.items():
		if key.isalpha():
			print(f"{key}: {value}")
	print("============= END ===============")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		get_book_text(sys.argv[1])
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)