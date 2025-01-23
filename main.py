"""
Code shows if the greeting and response

RowSR - January 2025
"""

def theword(word1: str, word2: str) -> bool:

    # Creates list so program can find if they have the same letters
    alphbet: list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    for i in range (26):
            
            for a in range (len(word1)):    
                word1 = word1.replace(alphbet[i],"")
            for a in range (len(word2)):   
                word2 = word2.replace(alphbet[i],"")
            
            if len(word1) != len(word2):
                print("False") 
                
            print("True")
    else:
        print("False")

def main() -> None:
  words: str = input()

    
def main() -> None:
  
  words: str = input()
  
  words_formated = words.lower()
  words_formated = words_formated.replace(" ","")

    # Make sure program knows their 2 diff words
  word1, word2 = words_formated.split(",")

    # Is it an anagram? And prints results
  anagrame: bool = theword(word1, word2)
  if anagrame == True:
        print(f"{words} -> anagrams")
        
  if anagrame == False:
        print(f"{words} -> not anagrams")


if __name__ == "__main__":
  main()
