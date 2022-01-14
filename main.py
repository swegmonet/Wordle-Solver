from words import FILTERED_WORD_LIST
from combos import print_best_combos
from itertools import combinations

# FILTERED_WORD_LIST = ['gawds', 'elfin', 'umpty', 'brock', 'flawn', 'mebos', 'dript', 'gucky']
def check_for_working_combo(combo):
  combo_works = combination_has_unique_letters(combo) and word_combo_contains_all_required_letters(combo)
  return combo_works


def write_word_combos_csv(num_words):
  print('Getting combinations')
  all_combinations = combinations(FILTERED_WORD_LIST, num_words)
  compressed_combinations = filter(
    check_for_working_combo, 
    all_combinations
  )
  index = 0
  csv_file = open("combos.csv", "w")

  for combination in compressed_combinations:
    print(combination)
    index += 1
    if index % 10000000 == 0:
      print('Processed %s combos' % index)
    if combination_has_unique_letters(combination) and word_combo_contains_all_required_letters(combination):
      combo_str = ','.join(combination)
      print('combination found: %s' % combo_str)
      csv_file.write(combo_str)
      csv_file.write('\n')
  csv_file.close()

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

def main():
  combo_length = 4
  # warning: increasing this to 4 will make the script take much longer
  # fortunately for you i've already run it on combos of 4, check 4_words_unf.csv
  write_word_combos_csv(combo_length)
  print('------------')
  # print_best_combos()

main()

