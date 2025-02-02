class DNA_sequence: # We create a class of DNA sequence.
    def __init__(self, sequence): # We use the __init__ function to establish the characteristics of the class object.
        self.sequence = sequence # This characteristic corresponds to the sequence itself.
    
    def GC_content(self): # We crate a name for our method with the parameter as self.
        # We calculate the GC content in the sequence in the next line.
        GC_Content = (self.sequence.count("G") + self.sequence.count("C"))/len(self.sequence)
        return GC_Content # We return the result.

sequence = DNA_sequence("ATCGTACGTAGC") # We define the string sequence as a DNA sequence object.
print(sequence.GC_content()) # We print the result.