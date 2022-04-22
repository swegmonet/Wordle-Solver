import csv
from functools import cmp_to_key

LETTER_VALUES = {
  'd': 0,
  'e': 0,
  'i': 0,
  'n': 0,
  'r': 0,
  's': 0,
  't': 0,
  'a': 1,
  'c': 1,
  'f': 1,
  'l': 1,
  'm': 1,
  'o': 1,
  'w': 1,
  'y': 1,
  'b': 2,
  'g': 2,
  'k': 2,
  'p': 2,
  'u': 2,
  'h': 3,
  'v': 3,
  'j': 4,
  'z': 4,
  'x': 5,
  'q': 6
}

def determine_combo_value(combo_row):
  combo_value = 0
  for word in combo_row:
    combo_value += determine_word_value(word)
  return combo_value

def determine_word_value(word):
  word_value = 0
  for letter in word:
    if letter in ', ':
      continue
    word_value += LETTER_VALUES.get(letter, 6)
  return word_value

def count_values_under_amount(amount, value_list):
  count = 0
  for value in value_list:
    if value < amount:
      count += 1
  return count

def compare_word_values(item1, item2):
  if determine_word_value(item1) < determine_word_value(item2):
    return -1
  elif determine_word_value(item1) > determine_word_value(item2):
    return 1
  else:
    return 0

def print_best_combos():
  value_to_combos_dict = {}
  csv_file = open("sortedcombos.csv", "r")
  write_csv_file = open('bestvaluecombos.csv', 'w')
  reader = csv.reader(csv_file, delimiter=',', quotechar='|')
  for row in reader:
    row_value = determine_combo_value(row)
    word_values = [
      determine_word_value(word) for word in row
    ]
    value_count = count_values_under_amount(3, word_values)
    if value_count == 2 and row_value == 18:
      sorted_row = sorted(row, key=cmp_to_key(compare_word_values))
      print(word_values)
      write_csv_file.write(','.join(sorted_row))
      write_csv_file.write('\n')
    

    # if not value_to_combos_dict.get(row_value):
    #   value_to_combos_dict[row_value] = []
    # value_to_combos_dict[row_value].append(row)
  csv_file.close()
  write_csv_file.close()
  # keys_list = [key for key in value_to_combos_dict]
  # keys_list.sort()
  # best_value = 100
  # if keys_list:
  #   best_value = keys_list[0]
  # print('Best combos have a score of %s' % best_value)
  # best_combos = value_to_combos_dict[best_value]
  # best_combos.sort()
  # for best_combo in best_combos:
  #   print(best_combo)
  # return value_to_combos_dict[best_value]

# For the record, the best combos of 4 letter words with a value of 40 are:
# ['gawds', ' elfin', ' umpty', ' brock']
# ['flawn', ' mebos', ' dript', ' gucky']
# ['pecks', ' admin', ' growl', ' bufty']
# ['speck', ' admin', ' growl', ' bufty']
# ['navew', ' brods', ' umpty', ' flick']
# ['fawny', ' golem', ' dript', ' bucks']
# ['bavin', ' dowts', ' fleck', ' rumpy']
# ['bilgy', ' croft', ' dwaum', ' penks']
# ['bilgy', ' croft', ' swank', ' umped']
# ['bilgy', ' croft', ' umped', ' wanks']
# ['bilgy', ' drawn', ' focus', ' kempt']
# ['bings', ' croft', ' dwalm', ' pukey']
# ['blimp', ' croft', ' gawsy', ' nuked']
# ['bowet', ' dangs', ' flick', ' rumpy']
# ['bowet', ' dings', ' flack', ' rumpy']
# ['budge', ' croft', ' skimp', ' wanly']
# ['cadgy', ' frown', ' plumb', ' tikes']
# ['croft', ' debug', ' skimp', ' wanly']