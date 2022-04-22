from words import FILTERED_WORDS, UNIQUE_LETTER_WORDS
from combos import print_best_combos
from itertools import combinations
import operator
import csv

# refix,umpty,wolds,ganch
def check_for_working_combo(combo):
  combo_works = combination_has_unique_letters(combo)
  return combo_works


def write_word_combos_csv(num_words):
  print('Getting combinations')
  all_combinations = combinations(
    FILTERED_WORDS, 
    num_words
  )
  index = 0
  interval = 10000000
  csv_file = open("combos.csv", "a")

  for combination in all_combinations:
    index += 1
    if index % interval == 0:
      interval_num = index // interval
      print('Processed %s x10M combos' % interval_num)

    if not combination_has_unique_letters(combination):
      continue

    combo_str = ','.join(combination)
    print('combination found: %s' % combo_str)
    csv_file.write(combo_str)
    csv_file.write('\n')

  csv_file.close()

def combination_has_unique_letters(combination_tuple):
  letters = ''.join(combination_tuple)
  letters_list = list(letters)
  return len(letters_list) == len(set(letters_list))

def get_sorted_letters(word1, word2):
  combined_word = word1 + word2
  return ''.join(sorted(combined_word))

def get_remaining_letters(used_letters):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  remaining_letters = ''
  for letter in alphabet:
    if letter not in used_letters:
      remaining_letters += letter
  return remaining_letters

def sequence_contains_all_unused_letters(sequence, unused_letters):
  for letter in sequence:
    if letter not in unused_letters:
      return False
  return True

def shares_no_letters(word1, word2):
  for letter in word1:
    if letter in word2:
      return False
  return True

def shares_any_letters(word1, word2):
  return not shares_no_letters(word1, word2)

def four_sum_combos_to_csv():
  word_list = UNIQUE_LETTER_WORDS
  index_pairs = dict()
  len_words = len(word_list)
  csv_file = open("allcombos.csv", "a")

  for i in range(0, len_words):
    first_word = word_list[i]

    compatible_words = [
      word for word in word_list[i+1:] if shares_no_letters(first_word, word)
    ]
    print('%s/%s: %s has %s compatible words' % (i, len_words, first_word, len(compatible_words)))
    for second_word in compatible_words:
      word_combo = [first_word, second_word]
      if not combination_has_unique_letters(word_combo):
        continue

      sorted_letters_key = get_sorted_letters(first_word, second_word)

      compatible_keys = [key for key in index_pairs.keys() if shares_no_letters(key, sorted_letters_key)]
      if compatible_keys:
        print('Checking %s against %s keys' % (word_combo, len(compatible_keys)))


      for key in compatible_keys:
        pairs = index_pairs[key]
        compatible_pairs = [
          pair for pair in pairs if first_word not in pair and second_word not in pair
        ]
        print('Checking %s against %s pairs' % (word_combo, len(compatible_pairs)))

        for pair in compatible_pairs:
          combination = sorted(word_combo + pair) # Avoid duplicate
          combo_str = ','.join(combination)
          print('combination found: %s' % combo_str)
          csv_file.write(combo_str)
          csv_file.write('\n')

      if index_pairs.get(sorted_letters_key): # create or append to list in key
          index_pairs[sorted_letters_key].append(word_combo)
      else:
          index_pairs[sorted_letters_key] = [word_combo]


def main():
  four_sum_combos_to_csv()



main()
