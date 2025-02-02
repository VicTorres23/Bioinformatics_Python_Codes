
def dna_complement(sequence): # We define the name of our function with one parameter.
    complement = "" # We create a variable with an empty string.
    nucleos = {"T": "A", # We create a dictionary with the respective complement nucleotides.
               "A": "T",
               "G": "C",
               "C": "G"}
    for nucleo in sequence: # We create a for loop to iterate each nucleotide of the sequence.
        if nucleo in nucleos.keys(): # We create an if condition to see if the nucleotides are found in the keys of the dictionary.
            complement = complement + str(nucleos.get(nucleo)) # We concatenate the values of the dictionary if the if statement is True.
    return complement #We return the complement sequence.

print(dna_complement(input("Enter your DNA sequence: "))) #We print the result.