#!/usr/bin/env python
# coding: utf-8

# In[450]:


# 1. Read the file sequence.gb.txt
sequence = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_7/sequence.txt", "r")

read_sequence = str(sequence.read())
print(read_sequence)


# In[451]:


# 2. Create a txt file named “cattle_IL6” with this information:
#    1. Organism
import re
Info = ""

name_and_gene = re.compile(r"DEFINITION\s{2}(.+\.)")
matches = name_and_gene.finditer(read_sequence)

for match in matches:
    Info = Info + "The organism and name of gene is: \n" + match.group(1)

organism = re.compile(r"ORGANISM\s{2}(.+\s)")
matches2 = organism.finditer(read_sequence)
for match in matches2:
    Info = Info + "\n\n1. The organism is: \n" + match.group(1)
#print(Info)

#    2. Name of gene
Gene = re.compile(r"DEFINITION.+\(([A-Z0-9]{3})\)")
matches = Gene.finditer(read_sequence)

for match in matches:
    Info = Info + "\n\n2. The name of the gene is: \n" + match.group(1)
#print(Info)
    
#    3. Number of base pairs
Base_pairs = re.compile(r"(\d+)\sbp")
matches = Base_pairs.finditer(read_sequence)

for match in matches:
    Info = Info + "\n\n3. The number of base pairs is: \n" + match.group(1)
#print(Info)

#    4. Accession Number
Accession = re.compile(r"ACCESSION.+([A-Z]{2}\_[0-9]{6})")
matches = Accession.finditer(read_sequence)

for match in matches:
    Info = Info + "\n\n4. The accession number is: \n" + match.group(1)
#print(Info)

#    5. List of Pubmed article ID's related to this gene
Pubmed = re.findall(r"PUBMED\s+(\d+)\s", read_sequence)

string = ""
for match in Pubmed:
    string = string + match + "\n"
Info = Info + "\n\n5. List of PubMed articles ID's related to this gene: \n" + string
#print(Info)

#    6. Full sequence
Full_sequence = re.compile(r"([acgt]+)\s([acgt]+)\s([acgt]+)\s([acgt]+)?\s?([acgt]+)?\s?([acgt]+)?\s?")
matches = Full_sequence.finditer(read_sequence)
string = ""
for match in matches:
    #print(match)
    string = string + match.group(1) + match.group(2) + match.group(3) + str(match.group(4)) + str(match.group(5)) + str(match.group(6))
Info = Info + "\n\n6. The full sequence is: \n" + string
Info = re.sub(r"None", "", Info)
print(Info)

new_file = open("cattle_IL6.txt", "w")
new_file.write(Info)


# In[452]:


# 3. Show the first three, followed by the last three classification level in the lineage of the
# organism
Class_level_first = re.findall(r"\s(\w+\;\s\w+\;\s\w+\;)\s\w+\;\s\w+\;\s\w+\;", read_sequence)
Class_level_last = re.findall(r"\s(\w+\;\s\w+\;\s\w+\.)", read_sequence)
Class_level = Class_level_first + Class_level_last
print(Class_level)


# In[453]:


# 4. Show all references in this format:
#    1. Title of article
References = re.findall(r"TITLE\s+(.+)\s+(.+)\s+(.+)\s+(.+)\s+(.+)", read_sequence)

string = ""
for matches in References:
    for match in matches:
        string = string + match + "\n"
string = re.sub(r"JOURNAL.+\s", "\n", string)
string = re.sub(r"REMARK.+\s", "", string)
string = re.sub(r"PUBMED.+\s", "", string)
string = re.sub(r"COMMENT.+\s", "", string)
string = re.sub(r"NCBI.+\s", "", string)
string = re.sub(r"REFERENCE.+\s", "", string)
print(string)


# In[454]:


#    2. Journal name (only name) followed by PubMed ID
Info = ""
clean_data = []
Journal = re.findall(r"JOURNAL\s+([a-zA-Z0-9\.]+\s[a-zA-Z0-9\.]+\s[a-zA-Z0-9\.]+\s?[A-Za-z\(\)]+)", read_sequence)
for match in Journal:
    match = re.sub(r"\d+\s\(", "", match)
    clean_data.append(match)
#print(clean_data)
Pubmed = re.findall(r"PUBMED\s+(\d+)\s", read_sequence)
#print(Pubmed)
for i in range(len(Journal)):
    Info = Info + clean_data[i]+ " " + Pubmed[i] + "\n"
print(Info)


# In[457]:


#    3. All authors last name, separated by “,”
clean_Authors = []
Authors = re.findall(r"AUTHORS\s+(.+\s+.+)", read_sequence)
#print(Authors)
for match in Authors:
    match = re.sub(r"\n\s+TITLE.+", "", match)
    match = re.sub(r"\sand", ",", match)
    match = re.sub(r"\s+[A-Z][A-Z]?[\,\.]", "", match)
    match = re.sub(r"\n\s+", " ", match)
    match = re.sub(r"\s[A-Z]\s\,", "", match)
    match = re.sub(" ", ",", match)
    clean_Authors.append(match)
#print(clean_Authors)

for Authors1 in clean_Authors:
    print(Authors1 + "\n")


# In[491]:


#     4. All authors initials , separated by “tab”
clean_Initials = []
Initials = re.findall(r"AUTHORS\s+(.+\s+.+)", read_sequence)
for match in Initials:
    match = re.sub(r"\n\s+TITLE.+", "", match)
    match = re.sub(r"\n\s+", " ", match)
    match = re.sub(r"\sand", ",", match)
    match = re.sub(r"\s?[A-Z][a-z]+\s?", "", match)
    match = re.sub(r"\,", "\t", match)
    match = re.sub(r"  ", " ", match)
    #match = re.sub(r" ", "\t", match)
    clean_Initials.append(match)
#print(clean_Initials)
for initials in clean_Initials:
    print(initials)


# In[523]:


# 5. Show the exons positions in this format:
#    1. Exons: #:#, #:#, #:#, #:#, …
Exons = re.compile(r"exon\s+(\d+\.{2}[0-9]+)\s")
matches = Exons.finditer(read_sequence)

Info = ""
for match in matches:
    #print(match)
    #print(match.group(1))
    Info = Info + match.group(1) +" "
Info = re.sub(r"\s", ",", Info)
Info = re.sub(r"\,$", "", Info)
print("Exons: " + Info)


# In[582]:


# 6. Show the coding region in this format:
#    1. Abbreviated name of gene
Info = ""
Gene = re.compile(r"DEFINITION.+\(([A-Z0-9]{3})\)")
matches = Gene.finditer(read_sequence)

for match in matches:
    Info = Info + "1. The abbreviated name of gene is: " + match.group(1)
print(Info)
#    2. Full name of gene
Info = ""
Gene = re.compile(r"([A-Z]{2}\-\d\;.+\s)")
matches = Gene.finditer(read_sequence)

for match in matches:
    #print(match)
    Info = Info + "2. The full name of the gene is: " + match.group(1)
Info = re.sub(r"\"", "", Info)
#print(Info)
#    3. Nucleotide position of coding region
coding_region = re.compile(r"codon_start\=(\d)")
matches = coding_region.finditer(read_sequence)

for match in matches:
    Info = Info + "3. The nucleotide position of coding region is: " + match.group(1)
#print(Info)
#    4. Translated sequence
Translated = re.compile(r"translation\=\"([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)")
matches1 = Translated.finditer(read_sequence)

for match1 in matches1:
    #print(match1)
    Info = Info + "\n4. The translate sequence is: " + match1.group(1) + match1.group(2) + match1.group(3) + match1.group(4)
#Info = re.sub(r"\"", "", Info)

print(Info)
#    5. Protein ID
Info = ""
Protein_ID = re.compile(r"protein_id\=\"([A-Z][A-Z].+)\"")
matches = Protein_ID.finditer(read_sequence)

for match in matches:
    Info = Info + "5. The Protein ID is: " + match.group(1)
print(Info)


# In[579]:


# 7. Show the nucleotides from position [971 – end] from the sequence:
Info = ""
string = ""
Full_sequence = re.compile(r"961\s[acgt]{10}(.+\s+.+\s+.+)")
matches = Full_sequence.finditer(read_sequence)
for match in matches:
    string = Info + match.group(1)
string = re.sub(" ", "", string)
string = re.sub(r"\d+", "", string)
string = re.sub(r"\s+", "", string)
Info = Info + "The nucleotides fro position [971-end] from the sequence is: \n" + string
Info = re.sub(r"None", "", Info)
print(Info)


# In[ ]:




