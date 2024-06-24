import re

def check_sequence(seq):
    sequences = re.findall(r'0+|1+', seq)
    
    for i in range(0, len(sequences), 2):
        if i + 1 >= len(sequences) or len(sequences[i]) != len(sequences[i + 1]):
            return False
    
    return True

print(check_sequence("01010101"))      
print(check_sequence("000111000111"))    
