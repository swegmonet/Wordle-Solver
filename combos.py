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
  csv_file = open("combos.csv", "r")
  reader = csv.reader(csv_file, delimiter=',', quotechar='|')
  lowest_value = 50
  for row in reader:
    row_value = determine_combo_value(row)
    if row_value <= lowest_value:
      print(row)
      print(row_value)
      lowest_value = row_value
  csv_file.close()

# For the record, the best combos of 4 letter words with a value of 40 are:
# ['gawds', ' elfin', ' umpty', ' brock']
# ['flawn', ' mebos', ' dript', ' gucky']
# ['pecks', ' admin', ' growl', ' bufty']
# ['speck', ' admin', ' growl', ' bufty']
# ['navew', ' brods', ' umpty', ' flick']
# ['fawny', ' golem', ' dript', ' bucks']