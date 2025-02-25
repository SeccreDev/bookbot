# Count total words in a text file
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for character in text:
        character = character.lower()
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def sort_on(dictionary):
    return dictionary["number"]


def chars_dict_to_sorted_list(dictionary):
    sorted_list = []
    for character in dictionary:
        sorted_list.append({"char": character, "number": dictionary[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list