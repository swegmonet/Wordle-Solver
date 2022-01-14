from words import COMMON_LETTERS, FILTERED_WORD_LIST
from combos import print_best_combos

def get_word_combos(num_words):
  word_combos = []
  for word in FILTERED_WORD_LIST:
    word_combo = [word]
    i = 0

    while i < len(FILTERED_WORD_LIST):
      cur_word = FILTERED_WORD_LIST[i]
      i += 1;

      if word_combo_shares_letters(word_combo, cur_word):
        continue
      
      word_combo.append(cur_word)
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

combo_length = 4 # warning: increasing this to 4 will make the script take much longer, thanks O(N!) efficiency
# fortunately for you i've already run it on combos of 4, check 4_words_unf.csv
combos = get_word_combos(combo_length)
filtered_combos = [combo for combo in combos if len(combo) == combo_length and word_combo_contains_all_required_letters(combo)]


combo_string_list = set([
  ', '.join(combo) for combo in filtered_combos
])
csv_file = open("combos.csv", "w")
for combo in combo_string_list:
  csv_file.write(combo)
  csv_file.write('\n')
csv_file.close()
print('------------')
print_best_combos()