file_name = input("File name: ")

try:
    with open(file_name) as file:
        content = file.read()

        content_lines = content.splitlines()
        counter_lines = len(content_lines)

        counter_characters = len(content)

        content_words = content.split()
        counter_words = len(content_words)

        print("Number of lines: ", counter_lines)
        print("Number of characters: ", counter_characters)
        print("Number of words: ", counter_words)
except FileNotFoundError:
    print(f"Hey! The file {file_name} does not exist.")
