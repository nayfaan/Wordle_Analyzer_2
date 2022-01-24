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

def filter_out_func(sol, filter_word):
    filtered_sol = []
    for word in sol:
        if len(set(word) & set(filter_word)) == 0:
            filtered_sol.append(word)
    return filtered_sol

def find_words_within_first_freq(frequency_sans_num, filter_out = False, filter_word = ""):
    count = 0
    words_within_first_freq = []
    
    if filter_out:
        sol_to_analyze = filter_out_func(sol_all, filter_word)
    else:
        sol_to_analyze = sol_all
    
    while count < 26:
        alpha_freq_slice = [pos[:count+1] for pos in frequency_sans_num]
        
        for word in sol_to_analyze:
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

def assign_freq_to_words(filter_out = False, filter_word = ""):
    if filter_out:
        sol_to_analyze = filter_out_func(sol_all, filter_word)
    else:
        sol_to_analyze = sol_all
    
    word_score_dict = {word: score_word(word) for word in sol_to_analyze}
    word_score_dict = dict(sorted(word_score_dict.items(), key = lambda item: item[1], reverse = True))
    print(word_score_dict)

def filter_out_coverage(filter_word):
    find_words_within_first_freq(frequency_sans_num, True, filter_word)
    assign_freq_to_words(True, filter_word)

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
    
    #find_words_within_first_freq(frequency_sans_num)
    #assign_freq_to_words()
    filter_out_coverage("saine")

if __name__ == "__main__":
    with open("./input/possible_solutions.txt", "rt") as f:
        sol = f.read().splitlines()
    with open("./input/additional_words.txt", "rt") as f:
        sol_add = f.read().splitlines()
    sol_all = sol + sol_add
    
    run()