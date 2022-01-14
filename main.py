from words import FILTERED_WORD_LIST
from combos import print_best_combos
from itertools import combinations

def get_word_combos(num_words):
  print('Getting combinations')
  all_combinations = combinations(FILTERED_WORD_LIST, num_words)
  print('Combinations fetched')
  filtered_combinations = []
  index = 0
  for combination in all_combinations:
    index += 1
    if index % 100 == 0:
      print('Processed %s combos' % index)
    if combination_has_unique_letters(combination) and word_combo_contains_all_required_letters(combination):
      print('combination found: %s' % combination)
      filtered_combinations.append(combination)

  return(filtered_combinations)

def combination_has_unique_letters(combination_tuple):
  letters = ''.join(combination_tuple)
  letters_list = list(letters)
  return len(letters_list) == len(set(letters_list))

  
def word_combo_contains_all_required_letters(word_combo):
  REQUIRED_LETTERS = 'strnaeiou'
  flattened_combo = ''.join(word_combo)
  for letter in REQUIRED_LETTERS:
    if letter not in flattened_combo:
      return False
  return True

def write_combos_to_csv(combos):
  combo_string_list = set([
    ', '.join(combo) for combo in combos
  ])
  csv_file = open("combos.csv", "w")
  for combo in combo_string_list:
    csv_file.write(combo)
    csv_file.write('\n')
  csv_file.close()

def main():
  combo_length = 4 
  # warning: increasing this to 4 will make the script take much longer
  # fortunately for you i've already run it on combos of 4, check 4_words_unf.csv
  combos = get_word_combos(combo_length)
  write_combos_to_csv(combos)
  print('------------')
  print_best_combos()

main()

