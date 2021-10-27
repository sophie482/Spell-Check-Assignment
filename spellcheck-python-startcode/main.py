# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    # alice words array to lowercase
    for i in range(len(aliceWords)):
      aliceWords[i] = aliceWords[i].lower()

    loop = True 
    while loop: 
      print("\nMAIN MENU")
      print("1: Single Word (Linear)")
      print("2: Single Word (Binary)")
      print("3: Alice in Wonderland (Linear)")
      print("4: Alice in Wonderland (Binary)")
      print("5: EXIT")

      # Get Menu Selection from User
      selection = input("Enter Selection (1-5): ")
      

      if selection == "1": 
        wordToSearchFor = input("Please enter a word: ")
        wordToSearchFor = wordToSearchFor.lower()
        print("Linear search starting...")
        start = time.time()
        position = linearSearch(dictionary, wordToSearchFor)
        if position == -1:
          print("Not in the dictionary :(")
        else:
          print(wordToSearchFor + " is in the dictionary at position " + str(position))
        end = time.time()
        print("Time: " + str((end - start)) + " seconds")
      elif selection == "2":
        wordToSearchFor = input("Please enter a word: ")
        wordToSearchFor = wordToSearchFor.lower()
        print("Binary search starting...")
        start = time.time()
        position = binarySearch(dictionary, wordToSearchFor)
        if position == -1:
          print("Not in the dictionary :(")
        else:
          print(wordToSearchFor + " is in the dictionary at position " + str(position))
        end = time.time()
        print("Time: " + str((end - start)) + " seconds")
      elif selection == "3": 
        print("Linear search starting...")
        number = 0
        start = time.time()
        for word in aliceWords:
          position = linearSearch(dictionary, word)
          if (position == -1 ):
            number += 1
        end = time.time()
        print("Number of words not found in dictionary: " + str(number))
        print("Time: " + str((end - start)) + " seconds")
      elif selection == "4": 
        print("Binary search starting...")
        number = 0
        start = time.time()
        for word in aliceWords:
          position = binarySearch(dictionary, word)
          if (position == -1 ):
            number += 1
        end = time.time()
        print("Number of words not found in dictionary: " + str(number))
        print("Time: " + str((end - start)) + " seconds")
      elif selection == "5":
        print("goodbye :(")
        loop = False
      else: 
        print("Invalid selection choice")
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

def linearSearch(anArray, item):
 for i in range(len(anArray)):
    if anArray[i] == item: 
      return i
 return -1

def binarySearch(anArray, item):
  lowerIndex = 0
  upperIndex = len(anArray) - 1

  while lowerIndex <= upperIndex: 
    middleIndex = (lowerIndex + upperIndex) // 2
    if (item == anArray[middleIndex]):
      return middleIndex
    elif (item < anArray[middleIndex]):
      upperIndex = middleIndex - 1
    else: 
      lowerIndex = middleIndex + 1

  return -1

# Call main() to begin program
main()