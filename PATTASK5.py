## Write a python program to calculate the total number of vowels and count of each indivdual vowels A,E, I, O, U n the string "Guvi Geeks Network Private Limited"
data = "Guvi Geeks network private limited"
Vowel_Count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for i in data:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
      Vowel_Count = Vowel_Count + 1
      print("Total Vowels : ", Vowel_Count)

## Create a pyramid of numbers from 1 to 20 using for loop

table = int(input("Enter number of rows: "))

for i in range(table):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")

##  Write a function that takes a string and returns new string with allthe vowels removed

    def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for character in string:
        if character not in vowels:
            result += character
    return result
# Example usage
input_string = "Guvi Geeks Network Private Limited"
output_string = remove_vowels(input_string)
print(output_string)

## Write a function that takes string and returns the number of unique cahracters in It.

x = input()
unique_character = set("Guvi Geeks Network Private Limited")
print(unique_character)

## Write a function that takes a string and return true if It is a palindrome, otherwise false.

def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))

## write a function that takes a string and returns true if it is an anagram of another string. false otherwise

from typing_extensions import TypeVarTuple
def check(str1,str2):
  print(Counter(str1))
  print(Counter(str2))
  if (Counter(str1) == Counter(str2)) :
    return True
  else:
    return false
  str1 = str(input ("Enter string 1: "))
  str2 = str(input ("Enter string 2: "))

  ## Write a function that takes a string and returns the number of words in It.

  def count_words(string):
  words = string.split()
  return len(words)
  count_words("Guvi geeks network private limited")
  count_words("zen classes")