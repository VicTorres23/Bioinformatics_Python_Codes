#!/usr/bin/env python
# coding: utf-8

# In[60]:


# 1. Open and read file "sequence.txt".
sequence = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Lab 6/sequence.txt", "r")
print(sequence.read())
sequence.close()


# In[61]:


# 2. Show the type of object after opening the file.
sequence = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Lab 6/sequence.txt", "r")
print(type(sequence))
sequence.close()


# In[139]:


# 3. Show the organism and gene corresponding to the file.
sequence = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Lab 6/sequence.txt", "r")
for line in sequence:
    if line.find("ORGANISM") != -1:
        organism = str(line)
        starting_point = organism.find("ORGANISM") + len("ORGANISM")
        organism = organism[starting_point:]
    elif line.find("DEFINITION") != -1:
        gene = str(line)
        starting_point = gene.find("DEFINITION") + len("DEFINITION")
        gene = gene[starting_point:]
def eliminateSpaces(string):
    for i in range(len(string)):
        if not string[0].isalpha():
            string = string[1:]
    return string
organism = eliminateSpaces(organism)
gene = eliminateSpaces(gene)
Info = str(organism) + str(gene)
print(Info)


# In[140]:


# 4. Show ONLY the accession number
sequence = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Lab 6/sequence.txt", "r")
for line in sequence:
    if line.startswith("ACCESSION"):
        number = line
        only_accession = number[len("ACCESSION"):]
        only_accession = eliminateSpaces(only_accession)
print(only_accession)
sequence.close()


# In[67]:


# 5. Show the coding region information
sequence = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Lab 6/sequence.txt", "r")
read_da_sequence = sequence.read()
position1 = read_da_sequence.find("CDS")
position2 = read_da_sequence.find("ORIGIN")
coding_region = read_da_sequence[position1:position2]
print(coding_region)


# In[110]:


# 6. Show the ORIGIN
sequence = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Lab 6/sequence.txt", "r")
string_sequence = sequence.read()
position = string_sequence.find("ORIGIN")
ORIGIN = string_sequence[position:]
print(ORIGIN)
sequence.close()


# In[109]:


# 7. Show all the references and its detailed information in a listed form.
sequence = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Lab 6/sequence.txt", "r")
readSequence = sequence.read()
Reference1_Starts = readSequence.find("AUTHORS")
Reference1_Ends = readSequence.find("REFERENCE", readSequence.find("REFERENCE")+1)
Reference1 = "REFERENCE 1: \n" + str(readSequence[(Reference1_Starts):(Reference1_Ends)])
#print(Reference1)
Reference2_Starts = readSequence.find("AUTHORS", Reference1_Starts+1)
Reference2_Ends = readSequence.find("REFERENCE", Reference1_Ends+1)
Reference2 = "REFERENCE 2: \n" + str(readSequence[(Reference2_Starts):(Reference2_Ends)])
#print(Reference2)
Reference3_Starts = readSequence.find("AUTHORS", Reference2_Starts+1)
Reference3_Ends = readSequence.find("FEATURES")
Reference3 = "REFERENCE 3: \n" + str(readSequence[(Reference3_Starts):(Reference3_Ends)])
All_References = Reference1 + "\n" + Reference2 + "\n" + Reference3
print(All_References)


# In[130]:


# Save into a file <name>_parsing.txt,the organism, gene, and origin of the file.
new_file = open("VICTOR_parsing.txt", "w")
All_Info = str(Info) + str(ORIGIN)
new_file.write(All_Info)


# In[ ]:




