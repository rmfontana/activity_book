from word_search_generator import WordSearch 

def create_search_puzzle(word_list):
    """
    The purpose of this function is to generate a word search puzzle. 
    This uses this library here: https://pypi.org/project/word-search-puzzle/
    I don't actually want to implement this one unless i have to b/c i'd have to port it to Pillow myself no thanks
    """
    print("The puzzle is currently missing")

def create_word_puzzle(word_list):
    """
    The purpose of this function is simply to create a word search puzzle. 
    This uses this beautiful library: https://github.com/joshbduncan/word-search-generator/wiki 
    Provide list of words comma delimited -> my, list, of, example, words, typed, here = [my, list, of, example, words, typed, here]
    Outputs PDF in /output/ folder // Change path for your needs 
    """
    puzzle = WordSearch(word_list)
    puzzle.save(path="/workspaces/activity_book/activity-book-scripts/output/puzzle.pdf")

def main():
    # ask the user for the list of words
    list_of_words = input("Enter your list of words to create a word search puzzle: ")
    create_word_puzzle(list_of_words)

if __name__ == "__main__":
    main()
