import os
def get_first_4200_words(text):
    """Extract the first 4200 words from the given text."""
    words = text.split()
    num_words = len(words)
    print(f"Total number of words in the text: {num_words}")
    
    if num_words > 4200:
        first_4200_words = ' '.join(words[:4200])
        
    else: 
        print("You can use conversation as is")
        first_4200_words = ' '.join(words)
    
    return first_4200_words

# Prompt the user to enter a file path
file_path = input("Please enter the file path: ")

# Check if the file exists
if os.path.exists(file_path):
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    first_4200_words = get_first_4200_words(file_contents)   
    print("\nNumber of words in the extracted text:", len(first_4200_words.split()))
    print(first_4200_words)
else:
    print("The file was not found. Please check the file path and try again.")
