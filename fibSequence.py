# Fibonacci Sequence Generator
# input n: size of the sequence
# output: first n numbers of Fibonacci sequence 
def fibSequence(n):
    assert n>0
    
    serie = [1]
    
    while len(serie) < n:
        if len(serie)==1:
            serie.append(1)
        else:
            serie.append(serie[-1]+serie[-2])
    
    
    return serie

def main():
    print(fibSequence((int)(input('insert number: '))))

if __name__ == "__main__":
    main()
            
