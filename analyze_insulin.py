import re
with open('preproinsulin_seq.txt','r') as file:
    data = file.read()
    
    data = re.sub(r'\s+', '', data)
    data = re.sub(r'[^a-z]', '', data)
    
with open('preproinsulin_seq_clean.txt','w') as file:
    file.write(data)
print("File cleaned")
    
protein_sequence = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
sequence_length = len(protein_sequence)    
print("The protein sequence length is:", sequence_length)

with open('preproinsulin_seq_clean.txt', 'r') as file:
    sequence =file.read()
    
Isinsulin = sequence[:24]
with open('Isinsulin_seq_clean.txt','w') as file:
    file.write(Isinsulin)
    Isinsulin_length = len(Isinsulin)
    print("The length of the Isinsulin is:", Isinsulin_length)
    
Binsulin = sequence[24:54]
with open('binsulin_seq_clean,txt', 'w') as file:
    file.write(Binsulin)
    Binsulin_length = len(Binsulin)
    print("The length of the Binsulin is:", Binsulin_length)
    
Cinsulin = sequence[54:89]
with open('Cinsulin_seq_clean.txt', 'w') as file:
    file.write(Cinsulin)
    Cinsulin_length = len(Cinsulin)
    print("The length of the Cinsulin is:", Cinsulin_length)
    
Ainsulin = sequence[89:110]
with open('ainsulin_seq_clean.txt', 'w') as file:
    file.write(Ainsulin)
    Ainsulin_length = len(Ainsulin)
    print("The length of the Ainsulin is:", Ainsulin_length)


    