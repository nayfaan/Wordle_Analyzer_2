from copy import deepcopy as dcopy

def strip_0 (__frequency):
    frequency_temp = []
    for pos in __frequency:
        temp = dcopy(pos)
        
        for alpha, freq in pos.items():
            if freq == 0:
                temp.pop(alpha)        
        frequency_temp.append(temp)
    return frequency_temp

def find_words_within_first_freq(frequency_sans_num):
    count = 0
    words_within_first_freq = []
    
    while count < 26:
        alpha_freq_slice = [pos[:count+1] for pos in frequency_sans_num]
        
        for word in sol_all:
            word_list = list(word)
            if word_list[0] in alpha_freq_slice[0] and word_list[1] in alpha_freq_slice[1] and word_list[2] in alpha_freq_slice[2] and word_list[3] in alpha_freq_slice[3] and word_list[4] in alpha_freq_slice[4]:
                words_within_first_freq.append(word)
        
        if len(words_within_first_freq) > 0:
            break
        
        count += 1
        
    print(words_within_first_freq)
    
def score_word(word):
    score = 0
    
    for index, alpha in enumerate(list(word)):
        score += frequency[index][alpha]
    return score

def assign_freq_to_words():
    word_score_dict = {word: score_word(word) for word in sol_all}
    word_score_dict = dict(sorted(word_score_dict.items(), key = lambda item: item[1], reverse = True))
    print(word_score_dict)

def run():
        
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    temp = {}
    for a in alpha:
        temp[a] = 0
    
    global frequency
    frequency = [dcopy(temp) for _ in range(5)]
    
    for word in sol:
        for index, a in enumerate(list(word)):
            frequency[index][a] += 1
    
    frequency = [dict(sorted(pos.items(), key = lambda item: item[1], reverse = True)) for pos in frequency]
    
    #frequency = strip_0(frequency)
    
    global frequency_sans_num
    frequency_sans_num = [list(pos) for pos in frequency]
    
    find_words_within_first_freq(frequency_sans_num)
    print()
    assign_freq_to_words()

if __name__ == "__main__":
    with open("./input/possible_solutions.txt", "rt") as f:
        sol = f.read().splitlines()
    with open("./input/additional_words.txt", "rt") as f:
        sol_add = f.read().splitlines()
    sol_all = sol + sol_add
    
    run()