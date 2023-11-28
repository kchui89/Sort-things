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

 def sort_letters(self, user_letters):
  self.letters_a_to_j = [char for char in user_letters if "a" <= char <= "j"]
  self.letters_k_to_z = [char for char in user_letters if "k" <= char <= "z"]

 def sort_numbers(self, separate_odd_even=False):
  if separate_odd_even:
   odd_numbers = [num for num in self.random_numbers if num % 2 == 1]
   even_numbers = [num for num in self.random_numbers if num % 2 == 0]

   odd_numbers.sort()
   even_numbers.sort()

   self.random_numbers = odd_numbers + even_numbers
  else:
   self.random_numbers.sort()

 def sort_all_lists(self, separate_odd_even=False):
  self.sort_numbers(separate_odd_even)
  self.letters_a_to_j.sort()
  self.letters_k_to_z.sort()

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

   
    user_letters = char_sort.input_alpha_letters()

    
    char_sort.sort_letters(user_letters)

    
    char_sort.sort_all_lists(separate_odd_even=True)

    
    char_sort.display_lists()

if __name__ == "__main__":
    main()
