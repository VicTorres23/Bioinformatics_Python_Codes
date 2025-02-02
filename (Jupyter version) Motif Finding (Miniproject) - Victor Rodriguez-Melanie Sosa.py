#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing motif-related functions from BioPython
from Bio import motifs
# Importing sequence-related functions from BioPython
from Bio.Seq import Seq
# Importing numpy functions
import numpy as np


# In[11]:


# To open a file containing the DNA sequence of a BRCA1 oncogene.
BRCA1 = open("C:/Users/vemma/Documents\Master in Bioinformatics/Fall 2023 Semester/Computational & Mathematical Methods for Bioinformatics/Miniproject/BRCA1.txt", "r")

# This part of the code helps turn the contents of the FASTA file into a string.
BRCA1_sequence = ""
for line in BRCA1:
    for nucleotide in line:
        if nucleotide in ["T", "G", "C", "A"]:
            BRCA1_sequence = BRCA1_sequence + nucleotide
print("The length of the BRCA1 sequence is: " + str(len(BRCA1_sequence)))


# In[12]:


# This part of the code helps us identify were the sequences that starts with CTGC are located in the BRCA1 sequence.
BRCA1_motifs_pos = []
random = "CGTC"
for position in range(len(BRCA1_sequence)):
    if BRCA1_sequence[position:].startswith(random):
        BRCA1_motifs_pos.append(position)
print(BRCA1_motifs_pos)


# In[13]:


# Here we create a list of sequences that start with CGTC plus the 20 nucleotides after.
list_of_sequences_normal = []
for coordinates in BRCA1_motifs_pos:
    list_of_sequences_normal.append(BRCA1_sequence[coordinates:(coordinates+20)])
print(list_of_sequences_normal)


# In[15]:


# Here we use the Seq function to make the sequences compatible with the BioPython functions.
list_of_sequences = []
for string in list_of_sequences_normal:
    list_of_sequences.append(Seq(string))
print(list_of_sequences)


# In[16]:


# This function helps convert the sequences into Motifs objects.
m = motifs.create(list_of_sequences)
print(m)


# In[17]:


# This function counts the content of each nucleotide for every sequence.
print(m.counts)


# In[18]:


# We turn each count values for every nucleotide into a numpy array to
# be able to plot them later.
A_values = np.array(m.counts["A"])
C_values = np.array(m.counts["C"])
G_values = np.array(m.counts["G"])
T_values = np.array(m.counts["T"])
print(A_values)
print(C_values)
print(G_values)
print(T_values)


# In[19]:


# Labeling each nucleotide in the given sequences
no_bases = []
for i in range(0, len(A_values)):
    no_bases.append(str(i+1))


# In[20]:


# Import functions for plotting the results.
import matplotlib.pyplot as plt
from matplotlib import style


# In[21]:


# Add a grid to the chart
style.use("ggplot")
# Plot the bar representing the content of Adenine in the sequences.
plt.bar(no_bases, A_values, color="red", width=0.5, label="A")
# Plot the bar representing the content of Cytosine in the sequences.
plt.bar(no_bases, C_values, color="blue", width=0.5, bottom=A_values, label="C")
# Plot the bar representing the content of Guanine in the sequences.
plt.bar(no_bases, G_values, color="green", width=0.5, bottom=A_values+C_values, label="G")
# Plot the bar representing the content of Tyrosine in the sequences.
plt.bar(no_bases, T_values, color="yellow", width=0.5, bottom=A_values+C_values+G_values, label="T")
# Show the label in the y axis as "Quantity".
plt.ylabel("Quantity")
# Show the most and least present nucleotides of the sequences in the x axys.
plt.xlabel("The most present nucleotides in the sequences are: \n" + str(m.consensus) + "\n The least present nucleotides in the sequence are: \n" + str(m.anticonsensus))
# Show the legend to represent which color corresponds to which nucleotide.
plt.legend()
# Show the title of the graph.
plt.title("Motif Finding for BRCA1")
# Print the graph.
plt.show()


# In[ ]:




