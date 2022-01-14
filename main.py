from words import COMMON_LETTERS, WORD_LIST, FILTERED_WORD_LIST
import csv

def get_word_combos(num_words):
  word_combos = []
  for word in FILTERED_WORD_LIST:
    print('Finding combos for %s' % word)
    word_combo = [word]
    i = 0

    while i < len(FILTERED_WORD_LIST):
      cur_word = FILTERED_WORD_LIST[i]
      i += 1;

      if word_combo_shares_letters(word_combo, cur_word):
        continue
      
      word_combo.append(cur_word)

      # if word_combo_contains_only_common_letters(word_combo):
      word_combos.append(word_combo)

      if len(word_combo) >= num_words:
        break

      i = 0

  return word_combos

def word_combo_shares_letters(word_combo, word):
  flattened_combo = ''.join(word_combo)
  for letter in word:
    if letter in flattened_combo:
      return True
  return False


def word_combo_contains_only_common_letters(word_combo):
  flattened_combo = ''.join(word_combo)
  for letter in flattened_combo:
    if letter not in COMMON_LETTERS:
      return False
  return True
  
def word_combo_contains_all_required_letters(word_combo):
  REQUIRED_LETTERS = 'strnaeiou'
  flattened_combo = ''.join(word_combo)
  for letter in REQUIRED_LETTERS:
    if letter not in flattened_combo:
      return False
  return True

# combo_length = 4
# combos = get_word_combos(combo_length)
# filtered_combos = [combo for combo in combos if len(combo) == combo_length and word_combo_contains_all_required_letters(combo)]


# combo_string_list = set([
#   ', '.join(combo) for combo in filtered_combos
# ])
# csv_file = open("4_words_unf.csv", "w")
# for combo in combo_string_list:
#   csv_file.write(combo)
#   csv_file.write('\n')
# csv_file.close()

# print('ALL DONE')


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

print('-----------------------')
csv_file = open("4_words_unf.csv", "r")
reader = csv.reader(csv_file, delimiter=',', quotechar='|')
lowest_value = 50
for row in reader:
  row_value = determine_combo_value(row)
  if row_value == 40:
    print(row)
    lowest_value = row_value
csv_file.close()

