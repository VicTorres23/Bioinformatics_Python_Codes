#!/usr/bin/env python
# coding: utf-8

# In[22]:


# 1. Read in a nucleotide FASTA file that is at least 250 nucleotides.
FASTA_content = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Untitled Folder/sequence(1).fasta", "r")
print(FASTA_content.read())
FASTA_content.close()


# In[24]:


# 2. Print out only the header.
FASTA_content = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Untitled Folder/sequence(1).fasta", "r")
print(FASTA_content.readline())
FASTA_content.close()


# In[80]:


# 3. Print the length of the sequence.
FASTA_content = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Untitled Folder/sequence(1).fasta", "r")
sequence = ""
for line in FASTA_content:
    for nucleotide in line:
        if nucleotide in ["T", "G", "C", "A"]:
            sequence = sequence + nucleotide
print("The lenght of the DNA sequence is " + str(len(sequence)))
FASTA_content.close()


# In[73]:


# 4. Determine the GC content of the sequence (include two decimal places)
G_content = sequence.count("G")
C_content = sequence.count("C")
GC_content = G_content + C_content
percentage_of_GC = ((GC_content/len(sequence))*100)
print("There are " + str(G_content) + " Guanines and " + str(C_content) + " Cytosines. \n The sum of both are " + str(GC_content) + " aminoacids. \n The percentage of GC content in the sequence is approximately "+ format(percentage_of_GC, ".2f") + "%")


# In[81]:


# 5. Header
#  o Sequence
#  o My sequence has XXXX nucleotides
#  o The GC content is: XXX
FASTA_content = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Untitled Folder/sequence(1).fasta", "r")
print(FASTA_content.readline() + "\n" + sequence + "\n My sequence has " + str(len(sequence)) + " nucleotides \n The GC content is: " + format(percentage_of_GC, ".2f") + "%")
FASTA_content.close()


# In[123]:


# 6. Make a program that reads all the numbers from the second column of an excel file (save it as .csv) and prints the average of these values. (Excel file of your choice)
csv_file = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Untitled Folder/L3(2).csv", "r")
sum_values = 0
length = 0
for value in csv_file:
    split_csv_file = value.split(",")
    split_csv_file1 = split_csv_file.pop(1)
    sum_values = sum_values + int(split_csv_file1)
    length = length + 1
AverageOfValues = sum_values/length
print("The average of the values in the file is: " + str(AverageOfValues))


# In[ ]:





# In[ ]:




