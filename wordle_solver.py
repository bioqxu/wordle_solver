import re

def do_black(words_now, l, p):
    w=[]
    for i in words_now:
        if re.search(l, i) is None:
            w.append(i)
    return w

def do_yellow(words_now, l, p):
    w=[]
    for i in words_now:
        if re.search(l, i) is not None and i[p]!=l:
            w.append(i)
    return w

def do_green(words_now, l, p):
    w=[]
    for i in words_now:
        if i[p] == l:
            w.append(i)
    return w

def do_guess(words_now, input_word, input_color):
    for i,j in enumerate(zip(input_word, input_color)):
        if j[1] == 'b':
            words_now = do_black(words_now, j[0], i)
        if j[1] == 'y':
            words_now = do_yellow(words_now, j[0], i)
        if j[1] == 'g':
            words_now = do_green(words_now, j[0], i)
    input_word = words_now[0]
    print(input_word)
    return words_now, input_word

def read_words(WORD_LENGTH):
    words = []
    with open("english.txt") as f:
        for line in f:
            words.append(line.split()[1])
    all_words = [i.lower() for i in words if len(i)==WORD_LENGTH and len(set(i))==WORD_LENGTH]
    return all_words

def main():
    WORD_LENGTH = 5
    all_words = read_words(WORD_LENGTH)
    input_word = all_words[0]
    print(input_word)
    while True:
        input_color = input("Please enter a color string (must be 5): ")
        if len(input_color) != WORD_LENGTH or any(x not in ['b', 'y', 'g'] for x in input_color) :
            print("Sorry, your response was not good.")
            continue
        all_words, input_word = do_guess(all_words, input_word, input_color)

if __name__ == "__main__":
    main()

