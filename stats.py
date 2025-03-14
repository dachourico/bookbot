def count_words(book_text):

        words = book_text.split()
        num_words = (len(words))
        return num_words



def count_character(words):

	character_count = {}

	words = words.lower()

	for character in words:

		if character in character_count:
			character_count[character] += 1
		else:
			character_count[character] = 1


	return character_count

def sort_character_count(character_count):
	char_list = []
	for char, count in character_count.items():

		char_dict = {"character": char, "count":count}
		char_list.append(char_dict)

	def sort_on(dict):
		return dict["count"]
	char_list.sort(reverse=True, key=sort_on)
	return char_list
