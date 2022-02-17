"""
Names & Student Numbers:

Shawn Lu            130545205
Victoria Villani    124307208

This program uses the nltk package to process and clean text to prepare for anagram creation. The clean text
is processed word by word, creating its anagram. The words' letters are rearranged and this sorted string
will be stored as the unique key to the dictionary.  The values of the dictionary are also stored in a dictionary that
will take the format {anagram 1: freq1, anagram2: feq1... anagramN: freqN}. If the anagram is already present, the
frequency will increase by 1. User input is used to search through the dictionary for a given word and its anagrams.
Informative messaged will be displayed if input is invalid

Note:
NLTK package needs to be installed before running the program.
"""
import nltk
from nltk.stem import WordNetLemmatizer
from tabulate import tabulate

nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()


class Text(object):
    """ Represents the text object"""
    def __init__(self, file_ref):
        self.raw_text = file_ref.read().replace('\n', ' ')
        self.clean_list = []
        self.words_grouped = {}

    def clean_text(self):
        """
        This function takes a text file as input and removes all stop words.
        Output: list of words in the text, with no stop words or punctuation
        """
        no_punc = []

        art = self.raw_text
        # locates the target article from the given list

        for char in art:
            if char.isalpha():
                no_punc.append(char)
            elif char == '-':
                no_punc.append('')
            else:
                no_punc.append(' ')
        # finishes removing punctuation from text
        no_punc = ''.join(no_punc).split()

        stopwords = set()

        sw = open('stopWords.txt', 'r')
        raw_stopwords = sw.read().split(', ')
        # reads the file stopwords.txt

        for word in raw_stopwords:
            result = word.strip('\"').strip('\'').strip('\n')
            stopwords.add(result)
        # cleans the given stopwords.txt document and create a list of stopwords

        for word in no_punc:
            if word.lower() not in stopwords and len(list(word)) > 1:
                self.clean_list.append(lemmatizer.lemmatize(word.lower()))
        # finishes removing stopwords from text

    def group_by_char(self):
        """ This method creates the dictionary in the form {sorted string: {anagram1: freq1... anagramN freqN}}"""
        for word in self.clean_list:
            unified_str = ''.join(sorted(list(word)))
            if unified_str not in self.words_grouped:
                self.words_grouped[unified_str] = {}
                self.words_grouped[unified_str][word] = 1
            elif word not in self.words_grouped[unified_str]:
                self.words_grouped[unified_str][word] = 1
            else:
                self.words_grouped[unified_str][word] += 1

    def search_anagram(self):
        """ This method takes user input and searches through the dictionary to find the given word's anagrams
        and its associated frequency.  Informative messages are given if input is not valid"""
        while True:
            try:
                keyword = input('Which word are you interested in?  ')
                if len(keyword.split()) > 1:
                    raise KeyError
                    # if multiple words are entered, raise KeyError
            except KeyError:
                print('please provide one word only!\n')

            else:
                try:
                    sorted_keyword = ''.join(sorted(list(keyword)))
                    # generate a string with sorted characters from the given keyword
                    target_dict = self.words_grouped[sorted_keyword]
                    # locate the anagram dictionary based on the re-arranged string of
                    # the keyword, if nothing was found, a KeyError will be raised by
                    # the dictionary

                    if keyword in target_dict and len(target_dict) == 1:
                        print(f'word: {keyword}\n'
                              f'frequency:{target_dict[keyword]}\n------------\n'
                              f'no anagrams')
                        break
                        # output when keyword is the only word in target sub dictionary

                    elif keyword not in target_dict:

                        print(f'word not found in text\n------------\n'
                              f'anagrams:')
                        # output when keyword is not in target sub dictionary

                    else:
                        print(f'word: {keyword}\n'
                              f'frequency:{target_dict[keyword]}\n------------\n'
                              f'anagrams:')
                        # output when keyword is in target sub dictionary

                    for word in target_dict:
                        if word != keyword:
                            print(f'word: {word:<15}frequency: {target_dict[word]:<4d}')
                        # print the frequency of words in the target sub dictionary
                        # that are not the keyword

                    print('\n')
                    break
                except KeyError:
                    print('the word and its anagrams are not found, please try again\n')

    def print_anagrams(self):
        """This function formats the dictionary into a table containing a words' anagrams and their
        associated frequency """
        rows = []
        for item in self.words_grouped:
            if len(self.words_grouped[item]) > 1:  # only include anagrams with more than one word
                temp = []
                left = ', '.join(self.words_grouped[item].keys())
                # left side of list will contain the anagrams
                right = sum(self.words_grouped[item].values())
                # right side of list will contain the anagrams associated frequency
                temp.append(left)
                temp.append(right)
                rows.append(temp)
                # creating final list in format [left,left, right] for tabular formatting

        headers = ["Anagrams", "Frequency"]
        print(tabulate(rows, headers, tablefmt="fancy_grid"))


def main():

    f = open('adventures_of_huckleberry_finn.txt', 'r')
    text = Text(f)
    text.clean_text()
    text.group_by_char()

    while True:
        try:
            user_instruction = input('Please use the number to choose '
                                     'one of the following option:\n'
                                     '1. generate anagram\n'
                                     '2. search for specific word\n'
                                     '3. exit\n')

            if user_instruction == '1':
                text.print_anagrams()
                continue

            elif user_instruction == '2':
                text.search_anagram()
                continue

            elif user_instruction == '3':
                print("bye, have a nice day!")
                break

            else:
                raise KeyError

        except KeyError:
            print('invalid input! please try again.')


if __name__ == "__main__":
    main()
