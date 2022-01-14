import csv

LETTER_VALUES = {
  'a': 0,
  'e': 0,
  'i': 0,
  'o': 0,
  'u': 0,
  't': 1,
  'n': 1,
  's': 1,
  'r': 2,
  'd': 2,
  'l': 2,
  'c': 3,
  'm': 3,
  'f': 3,
  'w': 3,
  'y': 3,
  'g': 4,
  'p': 4,
  'b': 4,
  'v': 4,
  'k': 4,
}

def determine_combo_value(combo_row):
  combo_value = 0
  for word in combo_row:
    for letter in word:
      if letter in ', ':
        continue
      combo_value += LETTER_VALUES.get(letter, 5)

  return combo_value


def print_best_combos():
  value_to_combos_dict = {}
  csv_file = open("combos.csv", "r")
  reader = csv.reader(csv_file, delimiter=',', quotechar='|')
  for row in reader:
    row_value = determine_combo_value(row)
    if not value_to_combos_dict.get(row_value):
      value_to_combos_dict[row_value] = []
    value_to_combos_dict[row_value].append(row)
  csv_file.close()
  keys_list = [key for key in value_to_combos_dict]
  keys_list.sort()
  best_value = 100
  if keys_list:
    best_value = keys_list[0]
  print('Best combos have a score of %s' % best_value)
  best_combos = value_to_combos_dict[best_value]
  best_combos.sort()
  for best_combo in best_combos:
    print(best_combo)
  return value_to_combos_dict[best_value]

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