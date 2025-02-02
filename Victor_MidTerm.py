#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Write a user-defined python function to retrieve the header, sequence, total number of
# nucleotides, count of the number of times each nucleotide appears in the sequence, and the
# GC content as per convention. The function should output the results in a new text file
# "question1.txt". Sample output: "question1.txt."

# We start by opening and reading the FASTA file provided by the exam.
Sequence_FASTA = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Untitled Folder/midterm-sequence.fasta", "r")
def printBiologicalInfo(file): #We assign a name to our function and assign it one parameter.
    header = file.readline() # We assing the header of the FASTA file to a variable.
    sequence = file.read() # We assign the sequence contents of the FASTA to a variable.
    sequence = sequence.replace("\n", "") # We remove the "\n" charachters of the FASTA sequence.
    SequenceLength = len(sequence) # We calculate the length of the sequence and assign it to a variable.
    NucleotideACounts = sequence.count("A") #We count the number of Adenines in the sequence.
    NucleotideTCounts = sequence.count("T") #We count the number of Thymine in the sequence.
    NucleotideCCounts = sequence.count("C") #We count the number of Cytosine in the sequence.
    NucleotideGCounts = sequence.count("G") #We count the number of Guanine in the sequence.
    GC_content = ((NucleotideGCounts+NucleotideCCounts)/SequenceLength)*100 # We calculate the percentage of Guanines and Cytosines in the sequence.
    # In the next line, we create a good presentation for the information found.
    Info = str(header) + "\n" + str(sequence) + "\n\nTotal of Nucleotides: " + str(SequenceLength) + "\nNucleotide A is found: " + str(NucleotideACounts) + " times." + "\nNucleotide T is found: " + str(NucleotideTCounts) + " times." + "\nNucleotide C is found: " + str(NucleotideCCounts) + " times." + "\nNucleotide G is found: " + str(NucleotideGCounts) + " times." + "\nGC content: " + "{:.2f}".format(GC_content) + "%"
    # We create a file to store the information recollected.
    New_file = open("question1.txt", "w")
    #We write the information inside the file.
    New_file.write(Info)
# We call our function and apply it to the FASTA file provided for the realization of this exam.
printBiologicalInfo(Sequence_FASTA)
#We close the FASTA file.
Sequence_FASTA.close()


# In[9]:


# Write a function to show the percentage of each nucleotide and GC, AT content of the whole
# sequence as per convention.

# We start by opening and reading the FASTA file provided by the exam.
Sequence_FASTA = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Untitled Folder/midterm-sequence.fasta", "r")
# We assign a name to our function and assign it one parameter.
def PercentagesOfNucleotides(seq):
    header = seq.readline() # We assing the header of the FASTA file to a variable.
    sequence = seq.read() # We assign the sequence contents of the FASTA to a variable.
    sequence = sequence.replace("\n", "") # We remove the "\n" charachters of the FASTA sequence.
    SequenceLength = len(sequence) # We calculate the length of the sequence and assign it to a variable.
    A_Percentage = (sequence.count("A")/SequenceLength)*100 #We calculate the percentage of Adenine in the sequence.
    T_Percentage = (sequence.count("T")/SequenceLength)*100 #We calculate the percentage of Thymine in the sequence.
    C_Percentage = (sequence.count("C")/SequenceLength)*100 #We calculate the percentage of Cytosine in the sequence.
    G_Percentage = (sequence.count("G")/SequenceLength)*100 #We calculate the percentage of Guanine in the sequence.
    GC_content = G_Percentage + C_Percentage #We sum the percentages of Guanine and Cytosine.
    AT_content = A_Percentage + T_Percentage #We sum the percentages of Adenine and Thymine.
    # We organize and assign a variable to all of the information collected.
    Percent_Info = "The percentage of nucleotide 'A' is: " + "{:.2f}".format(A_Percentage) + "%" + "\nThe percentage of nucleotide 'T' is: " + "{:.2f}".format(T_Percentage) + "%" + "\nThe percentage of nucleotide 'C' is: " + "{:.2f}".format(C_Percentage) + "%" + "\nThe percentage of nucleotide 'G' is: " + "{:.2f}".format(G_Percentage) + "%" + "\nGC content: " + "{:.2f}".format(GC_content) + "%" + "\nAT content: " + "{:.2f}".format(AT_content) + "%"
    new_file = open("question2.txt", "w") # We create a new file.
    new_file.write(Percent_Info) # We write all of the information inside the new file.

PercentagesOfNucleotides(Sequence_FASTA) # We call our function using the FASTA file provided for this exam.
Sequence_FASTA.close() #We close the FASTA file.


# In[10]:


# 3. Write a function to calculate each nucleotide's percentage in the 50 bp fragments (1-49, 50 -
#    99, 100-149, 150-199, 200-, …). Sort the fragments for each nucleotide in decreasing order
#    with a four decimals format round off. Save the output in a text file "question3.txt"

# We start by opening and reading the FASTA file provided by the exam.
Sequence_FASTA = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Untitled Folder/midterm-sequence.fasta", "r")
# We assign a name to our function and assign it one parameter.
def FragmentsPercentages(file):
    list_of_ranges = [] #We create an empty list to store the fragments.
    # We create a dictionary for every type of nucleotide.
    FragmentsA = {}
    FragmentsG = {}
    FragmentsC = {}
    FragmentsT = {}
    header = file.readline() # We assing the header of the FASTA file to a variable.
    sequence = file.read() # We assign the sequence contents of the FASTA to a variable.
    sequence = sequence.replace("\n", "") # We remove the "\n" charachters of the FASTA sequence.
    for i in range(0, len(sequence)+50, 50): # We divide the main sequence inf fragments of 50.
        list_of_ranges.append(str(sequence[i-50:i])) #We add each fragment to the list we created previously.
    list_of_ranges.pop(0) #We eliminate the empty string at the start of the list.
    # We create 4 lists, one for each type of nucleotide to store the content percentages of each fragment.
    A_content = []
    G_content = []
    C_content = []
    T_content = []
    for i in range(len(list_of_ranges)): #We iterate based on the length of the list of fragments we previously created.
        # We start adding keys and values to each dictionary, the key is the number of the fragment and the value is the percentage of each type of nucleotide.
        FragmentsA["Fragment " + str(i+1)] = round((list_of_ranges[i].count("A")/len(list_of_ranges[i])), 4)
        FragmentsT["Fragment " + str(i+1)] = round((list_of_ranges[i].count("T")/len(list_of_ranges[i])), 4)
        FragmentsC["Fragment " + str(i+1)] = round((list_of_ranges[i].count("C")/len(list_of_ranges[i])), 4)
        FragmentsG["Fragment " + str(i+1)] = round((list_of_ranges[i].count("G")/len(list_of_ranges[i])), 4)
        # We add the percentages of each fragment to the list, this will allow to sort the values in decreasing order.
        A_content.append(FragmentsA["Fragment " + str(i+1)])
        G_content.append(FragmentsG["Fragment " + str(i+1)])
        C_content.append(FragmentsC["Fragment " + str(i+1)])
        T_content.append(FragmentsT["Fragment " + str(i+1)])
    # We sort the percentages in decreasing order.
    A_content = sorted(A_content, reverse=True)
    G_content = sorted(G_content, reverse=True)
    C_content = sorted(C_content, reverse=True)
    T_content = sorted(T_content, reverse=True)
    # We create 4 lists to store the corresponding fragment number to each content percentage.
    sortedFragmentsA = []
    sortedFragmentsG = []
    sortedFragmentsC = []
    sortedFragmentsT = []
    # We create a function that will help us sort each fragment by getting the key based on the already sorted content percentage values.
    def sortTheFragments(ListOfValues, Dict, NewList):
        for i in range(len(ListOfValues)): # We create a for loop to iterate based on the length of the list of content percentages.
            NewList.append([j for j in Dict if Dict[j]==ListOfValues[i]]) # We get the key corresponding to each value of the list of content percentages and we add them to a new list.
        NoRepetitions = [] # We create a nother list to store the fragments, but this time we will eliminate the repited elements.
        for lists in NewList: #We iterate throug each list of fragments inside the list.
            for fragment in lists: #We iterate through each fragment inside the list.
                if fragment not in NoRepetitions: # We confirm if the fragment number is not repeated inside the list.
                    NoRepetitions.append(fragment) # We add the values to the new list.
        return NoRepetitions #We return the new list with the fragments sorted in decreasing order based in the sorted content percentages.
    #We apply this function to create a list of the sorted fragments for each type of nucleotide.
    sortedFragmentsA = sortTheFragments(A_content, FragmentsA, sortedFragmentsA)
    sortedFragmentsG = sortTheFragments(G_content, FragmentsG, sortedFragmentsG)
    sortedFragmentsC = sortTheFragments(C_content, FragmentsC, sortedFragmentsC)
    sortedFragmentsT = sortTheFragments(T_content, FragmentsT, sortedFragmentsT)
    # We create a function that allows to get a string of the fragment number and its corresponding content percentage.
    def getFragmentValuesPerNucleotide(Fragments, Values):
        InfoNucleotide = "" #We create an empty string to store the information.
        for i in range(len(Values)): #We iterate throung each content percentage value in the list.
            InfoNucleotide = InfoNucleotide + "\n" + str(Fragments[i]) + ": " + str(Values[i]) # We create the string with the fragment number and its corresponding content percentage value.
        return InfoNucleotide #We return the string created.
    # We collect all of the information in one whole string.
    Info = "The percentage of nucleotide A: " + getFragmentValuesPerNucleotide(sortedFragmentsA, A_content) + "\n\nThe percentage of nucleotide T: " + getFragmentValuesPerNucleotide(sortedFragmentsT, T_content) + "\n\nThe percentage of nucleotide C: " + getFragmentValuesPerNucleotide(sortedFragmentsC, C_content) + "\n\nThe percentage of nucleotide G: " + getFragmentValuesPerNucleotide(sortedFragmentsG, G_content)
    new_file = open("question3.txt", "w") #We create a new .txt file.
    new_file.write(Info) # We store all the information collected in the .txt file.
FragmentsPercentages(Sequence_FASTA) #We call our function and apply it to the FASTA file.
Sequence_FASTA.close() # We close the FASTA file.


# In[11]:


# 4. Write a function to get the reverse complement of the whole sequence and save the output in a
#    text file "question4.txt"

# We start by opening and reading the FASTA file provided by the exam.
Sequence_FASTA = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Untitled Folder/midterm-sequence.fasta", "r")
# We assign a name to our function and assign it one parameter.
def reverse_complement(file):
    header = file.readline() # We assing the header of the FASTA file to a variable.
    sequence = file.read() # We assign the sequence contents of the FASTA to a variable.
    sequence = sequence.replace("\n", "") # We remove the "\n" charachters of the FASTA sequence.
    complement_nucleos = {"T":"A", # We create a dictionary with complement nucleotides of each type of nucleotide.
                         "A":"T",
                         "G":"C",
                         "C":"G"}
    complement_seq = "" # We create an empty string to store the complement sequence of the original sequence.
    for line in sequence: # We iterate through each line in the fasta file.
        for nucleo in line: # We iterate through each nucleotide of each line.
            if nucleo in complement_nucleos.keys(): # We check if the nucleotide is in the dictionary keys.
                complement_seq = complement_seq + complement_nucleos.get(nucleo) # If the condition is True, the we add the complement of that nucleotide to the string.
    reverse_complement = complement_seq[::-1] #We reverse the complement sequence and assign it to a variable.
    # We collect all of the information in one string.
    Info = "Input: \n" + str(sequence) + "\n\nComplement: \n" + str(complement_seq) + "\n\nReverse Complement: \n" + str(reverse_complement)
    # We create a new .txt file.
    new_file = open("question4.txt", "w")
    # We write the collected information into the new .txt file.
    new_file.write(Info)

reverse_complement(Sequence_FASTA) #We call our function and apply it to the FASTA file.
Sequence_FASTA.close() # We close the FASTA file.


# In[12]:


# 5. Write a python function to translate DNA to RNA to Protein, save the translated sequence
#    output in a text file "question5.txt."

# We start by opening and reading the FASTA file provided by the exam.
Sequence_FASTA = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Untitled Folder/midterm-sequence.fasta", "r")

# We assign a name to our function and assign it one parameter.
def TranscribeAndTranslate(file):
    header = file.readline() # We assing the header of the FASTA file to a variable.
    sequence = file.read() # We assign the sequence contents of the FASTA to a variable.
    sequence = sequence.replace("\n", "") # We remove the "\n" charachters of the FASTA sequence.
    transcribed = sequence.replace("T", "U") # We replace the T character of the sequence for a U, that way we turn the DNA into an RNA.
    RNAtoAA = { # We create a dictionary with all of the corresponding aminoacids of each codon.
        "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
        "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
        "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    codons = [] # We create a list to store all of the codons in the transcribed sequence.
    for i in range(0, len(transcribed)+3, 3): # We iterate through each codon of the sequence.
        codons.append(transcribed[i-3:i]) # We store the codons inside the list.
    codons.pop(0) #We eliminate the empty string found at the start of the list.
    aminoacids = "" # We create an empty string to store the translated sequence.
    for codon in codons: # We iterate through each codon inside the list.
        if codon in RNAtoAA: #If the codon is found in the keys of the dictionary then the statement will be True.
            aminoacids = aminoacids + str(RNAtoAA.get(codon)) # If the condition is True, we add the corresponding aminoacid of each codon to the new list.
    # We collect all of the information in one string.
    Info = "Input DNA: \n" + str(sequence) + "\n\nTranscribed RNA: \n" + str(transcribed) + "\n\nTranslate: \n" + str(aminoacids)
    new_file = open("question5.txt", "w") #We create a new .txt file.
    new_file.write(Info) # We write all of the information collected inside the .txt file.

TranscribeAndTranslate(Sequence_FASTA) #We call our function and apply it to the FASTA file.
Sequence_FASTA.close() # We close the FASTA file.


# In[144]:


# 6. Let x=123 be the variable declared inside the function. Is it possible to access the variable
# outside the function? If "no," then how to modify the variable "x" to make it accessible
# outside the function? Explain in brief with Sample code.

# No, the variable will not be accesible outside the function. To make it accesible outside the function we have to 
# define this variable outside the function or write the word "global" before defining the variable inside the function.

# We can see this in the next example, this code will give us an error because the local variable is unaccesible:
def exampleFunction(number):
    x=123
    return x*number

print(x)


# In[145]:


# To be able to access the variable outside the function the code should look like this:

x=123
def exampleFunction(number):
    return x*number
print(x)


# In[152]:


#Or like this:

def exampleFunction(number):
    global x
    x=123
    return x*number

print(x)


# In[148]:


# 7. If a variable name is defined both outside and inside the function, then which variable will be
# used by python? Explain the reason for your choice.

# The function will give the value given by the variable inside the function
# and it will ignore the one outside the function.

# We can see this in the next code:
x=123
def exampleFunction():
    x=321
    return x
print(exampleFunction())


# In[ ]:


# 8. What is the difference between a list and a tuple? When would you use each one?

# You can modify the contents of a list but you can't modify the contents of a tuple. The tuple runs faster than a list, so
# if I had some values which are not necessary to alter for the program to work and I needed it to run faster then the
# tuple will be the election.


# In[186]:


# 9. a. What is the main usage (advantage) of functions?
#    b. Does function always have to return a value?

# a. The main advantage of functions is that they help us avoid repetition in the program that we are writing, making them
#    less redundant.
# b. No, they don't need to always have a return statement, if the task that the program is doing doesn't require to print
# something or give a result that will be used for other functions then is not necessary. Just like the functions build
# for this exam, their output is the creaton of .txt file and therefore the return statement is not necessary.


# In[185]:


# 10. Can functions have default arguments? If yes, write a function definition of your choice that
# takes default arguments? If no, then explain why.

# Yes, if no arguments are specified when calling the function, the default arguments defined at the name of the 
# function will be used.

#We can see this in the next code example:

def getWeight(planet="Earth", gravity=9.8, mass=8.15):
    return "Your weigth in " + str(planet) + " is " + "{:.2f}".format((gravity*mass))
print(getWeight())
print(getWeight(planet="Mars", gravity=3.71, mass=7.15))
print(getWeight(planet="Jupiter", gravity=24.79))


# In[ ]:




