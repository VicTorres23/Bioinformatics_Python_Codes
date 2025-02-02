#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. Read both psi-blast files: hsp & htt
l9hsp = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_9/L9hsp.txt", "r")

read_l9hsp = l9hsp.read()
print(read_l9hsp)


# In[3]:


l9ttc = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_9/L9ttc.txt", "r")

read_l9ttc = l9ttc.read()
print(read_l9ttc)


# In[4]:


# 2. Show description of psi-blast in following format:
#    1. Database
#    2. Matrix
#    3. Gap penalty
#    4. Window for multiple hit
import re

Database = re.search(r"Database:.+", read_l9hsp)
print(Database.group())
Matrix = re.search(r"Matrix:.+", read_l9hsp)
print(Matrix.group())
Gap_Penalties = re.search(r"Gap Penalties:.+", read_l9hsp)
print(Gap_Penalties.group())
Neighboring = re.search(r"Neigh.+", read_l9hsp)
print(Neighboring.group())
Window = re.search(r"Window.+", read_l9hsp)
print(Window.group())


# In[5]:


# 3. Print all hits found in both files in this format:
#    1. Number hit
#    2. Description of hit, organism, accession number

def count_n_print(regex_pattern, file):
    Hits = re.findall(regex_pattern, file)
    counts = len(Hits)
    matches = ""
    for match in Hits:
        matches = matches + str(match) + "\n"
    return str(counts) + "\n" + str(matches)

print("Number of hits in hsp: " + count_n_print(r"(\>.+\])\s", read_l9hsp))
print("Number of hits in ttc: " + count_n_print(r"(\>.+\])\s", read_l9ttc))


# In[6]:


# 4. Get best e-value for each file.

def getEvalue(file):
    matches = re.findall(r"gi.+\s+\d\d\.\d\s+(\d\.\d)\d?", file)
    bestEvalue = min(matches)
    return bestEvalue

print("Best E-value hsp: " + str(getEvalue(read_l9hsp)))
print("Best E-value ttc: " + str(getEvalue(read_l9ttc)))
        


# In[7]:


# 5. Show total of significant alignments found

def SigAlign(file):
    matches = re.findall(r"gi\|.+[\]\.]\s+\d", file)
    return len(matches)
print("The total of significance alignments in hsp: " + str(SigAlign(read_l9hsp)))
print("The total of significance alignments in ttc: " + str(SigAlign(read_l9ttc)))


# In[48]:


# 6. Show total of queries found

def TotalQueries(file):
    matches = re.findall(r"Query\s", file)
    return len(matches)
print("The total of queries in hsp: " + str(TotalQueries(read_l9hsp)))
print("The total of queries in ttc: " + str(TotalQueries(read_l9ttc)))


# In[49]:


# 7. Show total of subjects found

def TotalSubjects(file):
    matches = re.findall(r"Sbjct\s", file)
    return len(matches)
print("The total of subjects in hsp: " + str(TotalSubjects(read_l9hsp)))
print("The total of subjects in ttc: " + str(TotalSubjects(read_l9ttc)))


# In[113]:


# 8. Show in decreasing order the full description based on e-values in both files
matcheshsp = re.findall(r"gi.+\s+\d\d\.\d\s+(\d\.\d\d?)", read_l9hsp)
matchesttc = re.findall(r"gi.+\s+\d\d\.\d\s+(\d\.\d\d?)", read_l9ttc)
matches = matcheshsp + matchesttc
matches.sort(reverse=True)

listOfDescriptions = []
for match in matches:
    if re.search(r"\s+(.+\])\s+\d\d\.\d\s+" + str(match), read_l9hsp):
        description = re.search(r"\s+(.+[\.\]])\s+\d\d\.\d\s+" + str(match), read_l9hsp)
        listOfDescriptions.append(description.group(1))
    elif re.search(r"\s+(.+[\.\]])\s+\d\d\.\d\s+" + str(match), read_l9ttc):
        description = re.search(r"\s+(.+[\.\]])\s+\d\d\.\d\s+" + str(match), read_l9ttc)
        listOfDescriptions.append(description.group(1))
for i in range(len(matches)):
    print(str(matches[i] + " " + listOfDescriptions[i]))
    


# In[163]:


# 9. Create a file “top5_evals” with the best 5 e-values found in both files, with this format:
#    1. Full description of hits by e-value order
#    2. Show in order the corresponding query, corresponding file
matches.sort()
listOfDescriptionsAscend = listOfDescriptions[::-1]
i = 0
top5 = []
info = ""
while i < 5:
    info = info + str(matches[i] + " " + listOfDescriptionsAscend[i]) + "\n"
    top5.append(re.sub(r"\.\.\.", "", listOfDescriptionsAscend[i]))
    i += 1

for match in top5:
    match = re.sub(r"\|", "\|", match)
    match = re.sub(r"\[", "\[", match)
    match = re.sub(r"\]", "\]", match)
    match = re.sub(r" ", ".", match)
    
    if re.search(r"\>\s" + str(match), read_l9hsp):
        start_index = re.search(r"\>\s+" + str(match), read_l9hsp)
        end_index = re.search(r"\>", read_l9hsp[(start_index.start())+1:])
        info = info + "\n" + str(read_l9hsp[(start_index.start()):(end_index.end()+start_index.start())]) + "\n"
    elif re.search(r"\>\s" + str(match), read_l9ttc):
        start_index = re.search(r"\>\s+" + str(match), read_l9ttc)
        end_index = re.search(r"\>", read_l9ttc[(start_index.start())+1:])
        info = info + "\n" + str(read_l9ttc[(start_index.start()):(end_index.end()+start_index.start())]) + "\n"
        
new_file = open("top5_evals.txt", "w")
new_file.write(info)

