def main():
    with open("./books/frankenstein.txt") as f:
        print("--- Begin report of books/frankenstein.txt ---")
        file_contents = f.read()
        file_contents = file_contents.lower()
        words = set(file_contents.split())
        print(f"{len(words)} found in the document")
        letters = {}
        for word in words:
            for letter in word:
                if(not letter.isalpha()):
                    continue
                if letter in letters:
                    #print(f"+1 {letter} to {letters}")
                    letters[letter] +=1
                else:
                    #print(f"New {letter} to {letters}")
                    letters[letter] = 1
        
        for result in sorted(letters):
            print(f"The '{result} character was found {letters[result]} times")
    
    


main()