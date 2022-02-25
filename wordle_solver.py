import re


def do_black(words_now, l, input_word, p):
    w=[]
    if l in input_word[:p]+input_word[p+1:]:
        w = words_now
    else:
        for i in words_now:
            if re.search(l, i) is None:
                w.append(i)        
    return w

def do_yellow(words_now, l, input_word, p):
    w=[]
    for i in words_now:
        if re.search(l, i) is not None and i[p]!=l:
            w.append(i)
    return w

def do_green(words_now, l, input_word, p):
    w=[]
    for i in words_now:
        if i[p] == l:
            w.append(i)
    return w

def do_guess(words_now, input_word, input_color):
    for i,j in enumerate(zip(input_word, input_color)):
        if j[1] == 'b':
            words_now = do_black(words_now, j[0], input_word, i)
        if j[1] == 'y':
            words_now = do_yellow(words_now, j[0], input_word, i)
        if j[1] == 'g':
            words_now = do_green(words_now, j[0], input_word, i)
    if input_color != 'ggggg' and input_word in words_now:
        words_now.remove(input_word)
    input_word = words_now[0]
    return words_now, input_word

def pass_word(words_now):
    words_now = words_now[1:]
    input_word = words_now[0]
    return words_now, input_word

def read_words(WORD_LENGTH):
    words = []
    with open("data/words.txt") as f:
        next(f)
        for line in f:
            words.append(line.split()[0])
    # all_words = [i.lower() for i in words if len(i)==WORD_LENGTH and len(set(i))==WORD_LENGTH]
    all_words = [i.lower() for i in words if len(i)==WORD_LENGTH]
    return all_words

def main():
    WORD_LENGTH = 5
    guess_times = 1
    all_words = read_words(WORD_LENGTH)
    input_word = all_words[0]
    print(f"#{guess_times} Guess Word is: \x1b[6;30;42m{input_word}\x1b[0m")
    while True:
        guess_times += 1
        input_color = input("Please enter a color string (5 letters) \n(b is gray; y is yellow; g is green): ")
        if input_color == 'no':
            all_words, input_word = pass_word(all_words)
            print(f"\n#{guess_times} Guess Word is: \x1b[6;30;42m{input_word}\x1b[0m")
            guess_times -= 1
            continue
        elif len(input_color) != WORD_LENGTH or any(x not in ['b', 'y', 'g'] for x in input_color):
            print("Sorry, your input should be 'no'(not valid word) or '5 byg string'(the color of output)")
            print("(b is gray; y is yellow; g is green)\n")
            continue
        all_words, input_word = do_guess(all_words, input_word, input_color)
        print(f"\n#{guess_times} Guess Word is: \x1b[6;30;42m{input_word}\x1b[0m")
        


if __name__ == "__main__":
    main()

