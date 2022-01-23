class match:
    def __init__(self, comb):
        self.comb = comb
        self.cover = self.__cover__()
    
    '''def __eq__(self, other):
        return self.comb == self.comb
    
    def __gt__(self, other):
        return self.comb > self.comb
    
    def __hash__(self):
        return hash((self.w1, self.w2))'''
    
    def __cover__(self):
        intersect = set("".join(self.comb))
        return len(intersect)
    
    def __str__(self):
        return str(self.cover) + ': ' + ', '.join(self.comb)

if __name__ == "__main__":
    pass