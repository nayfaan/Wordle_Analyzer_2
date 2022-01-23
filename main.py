import services.match
import itertools
#import math

def index_display(match, sol):
    disp = []
    digit = len(str(len(sol)))
    for word in match.comb:
        disp.append(str(sol.index(word)).rjust(digit))
    return disp

def run(length, compare):
    if not isinstance(length, int):
        raise TypeError("Word length must be an integer.")
    if length < 2 or length > 15:
        raise ValueError("Word length must be between 2-15.")
    if not isinstance(compare, int):
        raise TypeError("No. of words to compare must be an integer.")
    if compare < 2:
        raise ValueError("No. of words to compare must be at least 2.")
    
    with open("./input/split/dictionary_"+str(length)+".txt", "rt") as f:
        sol = f.read().splitlines()
                
    max_coverage = 1
    
    length_of_dict = len(sol)
    print("# of words with "+str(length)+" letters: "+str(length_of_dict))
    print_interval = 1000000
    count = 0
    
    match_comb = itertools.combinations(sol, compare)
    good_set = []
    #threshold = 0#int(math.ceil((2-pow(2,1-compare))*length))
    for comb in match_comb:
        comb_match = services.match.match(comb)
        if comb_match.cover == max_coverage:
            good_set.append(comb_match)
        elif comb_match.cover > max_coverage:
            good_set = [comb_match]
            max_coverage = comb_match.cover
        
        count += 1
        if count % print_interval == 0:
            print("Analyzed: [",", ".join(index_display(comb_match, sol)),"] ...",sep='')
            
    #good_set.sort(key=len)
    for x in good_set:
        if x.cover == max_coverage:
            print(x)

if __name__ == "__main__":
    length = 4
    compare = 3
    run(length, compare)