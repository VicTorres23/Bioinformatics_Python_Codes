sequence = "AGGTT" # We define a variable with the sequence string.
sequence_list = [] # We create an empty list to store the nucleotides.
for nucleo in sequence: # We iterate each nucleotide in the string.
    sequence_list.append(nucleo) # We add each nucleotide to the list.
print(sequence_list) # We print our list.
reverse = "" # We create a variable with an empty string.
for nucleo in sequence_list: #We create another for loop to iterate each nucleotide in the list.
    reverse = reverse + str(nucleo) # We concatenate each nucleotide found in the list to the string variable.
reverse = reverse[::-1] # We use indexing to reverse the DNA sequence.
print(reverse) # We print the result.