def count_words_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()   # Convert to lowercase for uniform counting

            # Remove punctuation
            import string
            for char in string.punctuation:
                text = text.replace(char, "")

            words = text.split()

            word_count = {}

            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            # Display results in alphabetical order
            print("\nWord Occurrences (Alphabetical Order):\n")
            for word in sorted(word_count):
                print(f"{word} : {word_count[word]}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)


# Take file input from user
filename = input("Enter file name or path: ")
count_words_in_file(filename)

