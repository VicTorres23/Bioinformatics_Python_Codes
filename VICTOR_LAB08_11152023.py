#!/usr/bin/env python
# coding: utf-8

# In[2]:


sequence = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_8/Lab8_sequence.fasta", "r")
header = sequence.readline()
read_sequence = sequence.read()
print(read_sequence)


# In[3]:


# 1. Using regular expression do the following in the sequence fasta: – Show if the following restriction
# sites exists, and print how many times they appear if they exist.
# GAG
# GAGG
# GAGGT
import re

restr_sitesGAG = re.findall(r"G\s?A\s?G", read_sequence)
restr_sitesGAGG = re.findall(r"G\s?A\s?G\s?G", read_sequence)
restr_sitesGAGGT = re.findall(r"G\s?A\s?G\s?G\s?T", read_sequence)

print(len(restr_sitesGAG))
print(len(restr_sitesGAGG))
print(len(restr_sitesGAGGT))


# In[4]:


# 1.1 Get the full sequence starting from the restriction site GAGGT until the pattern TGGA
match = re.search(r"G\s?A\s?G\s?G\s?T\s?[ATCG]+\s?[ACGT]+\s?T\s?G\s?G\s?A", read_sequence)

full_seq = match.group(0)
full_seq = re.sub("\s", "", full_seq)
print(full_seq)


# In[13]:


# 1.2 Show how many and which unique motifs are found with GGNC, where N is any base.
def find_n_count(regexPattern, file):
    file = re.sub("\n", "", file)
    listmotif = re.findall(str(regexPattern), file)
    count = len(listmotif)
    Info = ""
    setmotif = list(set(listmotif))
    #print(NAGGXset)
    countlistmotif = []
    for j in range(len(setmotif)):
        for i in range(len(listmotif)):
            if setmotif[j] == listmotif[i]:
                countlistmotif.append(listmotif[i])
        Info = Info + str(setmotif[j]) + " " + str(len(countlistmotif)) + "\n"
        countlistmotif = []
    return print(str(count) + "\n" + str(listmotif) + "\n" + str(Info))

find_n_count("G\s?G\s?[ACGT]\s?C", read_sequence)


# In[17]:


# 2. Find all motifs with CCGN, where N is any base expect adenine
find_n_count("C\s?C\s?G\s?[TCG]", read_sequence)


# In[15]:


# 3. Find all motifs with NAGGX, where N is any base expect thymine and X any base
find_n_count("[ACG]\s?A\s?G\s?G\s?[TCGA]", read_sequence)


# In[18]:


# 4. Find all sequences that follows the pattern: CGA, with a minimum of 1 C and A, and
# maximum of 3 C and 2 A.
find_n_count("C{1,3}GA{1,2}", read_sequence)


# In[19]:


# 5. Show the longest sequence starting with GCGCA and ending in TTTT, show the position
# where both starting and ending positions are located.
removing_n = re.sub(r"\n", "", read_sequence)
pattern = re.compile(r"GCGCA")
GCGCA = pattern.finditer(removing_n)
GCGCA_found = []
for match in GCGCA:
    GCGCA_found.append((match.start()))

pattern = re.compile(r"TTTT")
TTTT = pattern.finditer(removing_n)
TTTT_found = []
for match in TTTT:
    TTTT_found.append(match.end())
#print(GCGCA_found)
#print(TTTT_found)
listOfSequences = []
coordinates_start = []
coordinates_end = []
while (len(TTTT_found) != 0):
    if GCGCA_found[0] < TTTT_found[0]:
        listOfSequences.append(removing_n[GCGCA_found[0]:TTTT_found[0]])
        coordinates_start.append(GCGCA_found[0])
        coordinates_end.append(TTTT_found[0])
        GCGCA_found.remove(GCGCA_found[0])
        TTTT_found.remove(TTTT_found[0])
    elif GCGCA_found[i] > TTTT_found[0]:
        GCGCA_found.remove(GCGCA_found[0])
while (len(listOfSequences) != 1):
    if len(listOfSequences[0]) < len(listOfSequences[1]):
        listOfSequences.remove(listOfSequences[0])
        coordinates_start.remove(coordinates_start[0])
        coordinates_end.remove(coordinates_end[0])
    elif len(listOfSequences[0]) < len(listOfSequences[1]):
        listOfSequences.remove[1]
        coordinates_start.remove[1]
        coordinates_end.remove[1]
print(str(coordinates_start[0]) + "\n" + str(coordinates_end[0]) + "\n" + str(listOfSequences[0]))


# In[20]:


# 6. Show all sequences that starts with “ATG”, followed by 5 bases, followed by a G or C,
# followed by another 3 bases.
CGA = re.findall(r"ATG[ACGT]{5}[GC][ATCG]{3}", removing_n)
print(len(CGA))
print(CGA)

