import random # We import useful functions from the random library.

def generate_random_RNA(length): # We define the name of our function here.
    nucleos = ("U", "C", "A", "G") # We create a tuple with the nucleotides found in RNA.
    random_sequence = "" # We create an empty string.
    for i in range(length): # We create a for loop to iterate based in the length of the sequence.
        random_sequence = random_sequence + str(random.choice(nucleos)) # We use random.choice to create a random RNA sequence.
    return random_sequence # We return the random sequence created.

print(generate_random_RNA(5)) #We print the result.