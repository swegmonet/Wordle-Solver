from words import FILTERED_WORD_LIST
from combos import print_best_combos
from itertools import combinations

def check_for_working_combo(combo):
  combo_works = combination_has_unique_letters(combo)
  return combo_works


def write_word_combos_csv(num_words):
  print('Getting combinations')
  all_combinations = combinations(FILTERED_WORD_LIST, num_words)
  index = 0

  interval = 1000000

  for combination in all_combinations:
    index += 1
    if index % interval == 0:
      interval_num = index // interval
      print('Processed %sM combos' % interval_num)

    if not check_for_working_combo(combination):
      continue

    combo_str = ','.join(combination)
    print('combination found: %s' % combo_str)
    csv_file = open("combos.csv", "w")
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
  write_word_combos_csv(combo_length)
  print('------------')
  # print_best_combos()

main()

