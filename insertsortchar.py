import random

class SortRandomChar:
 def __init__(self):
  self.random_numbers = []
  self.letters_a_to_j = []
  self.letters_k_to_z = []

 def generate_random_numbers(self, n):
  self.random_numbers = [random.randint(0, 99) for _ in range(n)]

 def input_alpha_letters(self):
  while True:
   user_input = input("Enter a string of letters: ").lower()
   if all(char.isalpha() for char in user_input):
    return list(user_input)
   else:
    print("Please enter only alphabetical letters!\n")

 def insertion_sort(self, arraydata):
  for index in range(1, len(arraydata)):
   currentindex = arraydata[index]
   compareleft = index - 1
   while compareleft >= 0 and currentindex < arraydata[compareleft]:
    arraydata[compareleft + 1] = arraydata[compareleft]
    compareleft = compareleft - 1
   arraydata[compareleft + 1] = currentindex

 def sort_letters(self, userinput_letters):
  self.letters_a_to_j = [char for char in userinput_letters if "a" <= char <= "j"]
  self.letters_k_to_z = [char for char in userinput_letters if "k" <= char <= "z"]
  self.insertion_sort(self.letters_a_to_j)
  self.insertion_sort(self.letters_k_to_z)

 def sort_numbers(self, separate_odd_even=False):
  if separate_odd_even:
   odd_numbers = [num for num in self.random_numbers if num % 2 == 1]
   even_numbers = [num for num in self.random_numbers if num % 2 == 0]
   self.insertion_sort(odd_numbers)
   self.insertion_sort(even_numbers)
   self.random_numbers = odd_numbers + even_numbers
  else:
   self.insertion_sort(self.random_numbers)

 def sort_all_lists(self, separate_odd_even=False):
  self.sort_numbers(separate_odd_even)
  self.insertion_sort(self.letters_a_to_j)
  self.insertion_sort(self.letters_k_to_z)

 def display_lists(self):
  print("\nRandom Numbers after sorting:\n\nOdd numbers:\n")
  even_numbers_started = False
  for num in self.random_numbers:
   if num % 2 == 0 and not even_numbers_started:
    print("\nEven numbers:\n")
    even_numbers_started = True
   print(num)
  print("\nLetters A to J after sorting:", self.letters_a_to_j)
  print("\nLetters K to Z after sorting:", self.letters_k_to_z)

def main():
 char_sort = SortRandomChar()
 char_sort.generate_random_numbers(100)
 userinput_letters = char_sort.input_alpha_letters()
 char_sort.sort_letters(userinput_letters)
 char_sort.sort_all_lists(separate_odd_even=True)
 char_sort.display_lists()

if __name__ == "__main__":
    main()
