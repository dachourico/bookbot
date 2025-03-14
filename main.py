import sys
from stats import count_words, count_character, sort_character_count


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents




def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1]
	book_text = get_book_text(book_path)
	word_count = count_words(book_text)
	character_count = count_character(book_text)
	sorted_chars = sort_character_count(character_count)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count -----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")

	for char_dict in sorted_chars:
		char = char_dict["character"]
		count = char_dict["count"]
		if char.isalpha():
			print(f"{char}: {count}")


	print("============= END ==================")

if __name__ == "__main__":
	main()
