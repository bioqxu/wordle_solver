import re
import random
import statistics

from wordle_solver import *

def read_words2(WORD_LENGTH):
    words = []
    p=[]
    with open("data/words2.txt") as f:
        next(f)
        for line in f:
            a = line.split()
            if len(a[0]) == WORD_LENGTH:
                words.append(a[0].lower())
                p.append(float(a[1]))    
    return words, p

def report_color(final_word, test_word):
    color=[0,0,0,0,0]
    for i,l in enumerate(test_word):
        if final_word[i]==l:
            color[i]='g'
        else:
            if l in final_word[:i]+final_word[i+1:]:
                if final_word.count(l)<=test_word[:i].count(l):
                    color[i]='b'
                else:
                    color[i]='y'
            else:
                color[i]='b'
    return ''.join(color)

def main():
    WORD_LENGTH=5
    words,p = read_words2(WORD_LENGTH)
    num_steps=[]
    for i in range(100):
        all_words = words.copy()
        all_p = p.copy()
        steps=1
        final_word = random.choices(all_words,all_p)[0]
        
        input_word = all_words[0]
        while input_word != final_word:
            input_color = report_color(final_word, input_word)
            all_words, input_word = do_guess(all_words, input_word, input_color)
            steps+=1
        print(f"{final_word}: {steps}")
        num_steps.append(steps)
    print(f"Average steps: {statistics.mean(num_steps)}")

if __name__ == "__main__":
    main()

