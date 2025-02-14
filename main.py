def main():
    path_to_file = 'books/frankenstein.txt'
    
    # Open the file and read its contents
    with open(path_to_file) as f:
        file_contents = f.read()

    # Function to count the number of words in the text
    def count_words(text):
        return len(text.split())

    # Function to count the occurrences of each character in the text
    def count_characters(text):
        character_counts = {}

        # Iterate through each character in the text (converted to lowercase)
        for char in text.lower():
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
        
        return character_counts

    # Function to sort the character counts in descending order
    def sort_characters(dictionary):
        # Convert the dictionary into a list of dictionaries
        sorted_list = [{"char": key, "num": value} for key, value in dictionary.items()]
        # Sort the list by the "num" key in descending order
        sorted_list.sort(reverse=True, key=lambda x: x["num"])
        return sorted_list

    # Print the report header
    print('--- Begin report of books/frankenstein.txt ---')

    # Count and print the number of words
    words = count_words(file_contents)
    print(f'{words} words found in the document\n')

    # Count the characters and sort them
    character_counts = count_characters(file_contents)
    sorted_characters = sort_characters(character_counts)

    # Print the counts for alphabetical characters only
    for item in sorted_characters:
        if item["char"].isalpha():
            print(f'The \'{item["char"]}\' character was found {item["num"]} times')

    # Print the report footer
    print('--- End report ---')

# Call the main function to execute the program
if __name__ == "__main__":
    main()