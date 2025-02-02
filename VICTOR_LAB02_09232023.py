#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. Make a variable called "protein" with value: vslpeplvvef
protein = "vslpeplvvef"
# 2. Show aminoacids from "e" - "e" in protein.
first_e = protein.find("e")
second_e = protein.find("e", first_e + 1)
e_to_e = protein[first_e:second_e + 1]
print(e_to_e)


# In[4]:


# 3. Using if-elif-else, print each aminoacids name.
for aminoacid in protein:
    if aminoacid == "v":
        print("Valine")
    elif aminoacid == "s":
        print("Serine")
    elif aminoacid == "l":
        print("Leucine")
    elif aminoacid == "p":
        print("Proline")
    elif aminoacid == "e":
        print("Glutamic Acid")
    elif aminoacid == "f":
        print("Phenylalanine")
    else:
        print("Error! Check if letter corresponds to other aminoacids!")


# In[18]:


# 4. Make a list of unique aminoacids in "protein", and print the result.
Unique_Aminoacids = []
for aminoacid in protein:
    if Unique_Aminoacids.count(aminoacid) == 0:
        Unique_Aminoacids.append(aminoacid)
print(Unique_Aminoacids)


# In[19]:


# 5. Print how many times each amino acid is repeated in the variable like this:
# "Amino acid v is repeated # times
#  Amino acid s is repeated # times"
for aminoacid in Unique_Aminoacids:
    print("Amino acid " + aminoacid + " is repeated " + str(protein.count(aminoacid)) + " times")


# In[28]:


# 6. Create a variable called dna_seq, and using a while loop, ask a user to input one nucleotide at a time, store each one in a variable, and when reached 5 nucleotides, print the sequence.
dna_seq = ""
i = 0
while i < 5:
    Nucleotide = input("Enter one (1) DNA nucleotide: ")
    Nucleotide = Nucleotide.upper()
    if len(Nucleotide) > 1:
        print("Only one nucleotide at a time is allowed!")
        break
    elif len(Nucleotide) == 0:
        print("Please enter a Nucleotide!")
        break
    elif Nucleotide == "U":
        print("Uracil is not found in DNA!")
        break
    elif Nucleotide not in ["T", "A", "C", "G"]:
        print("Invalid character, that is not a nucleotide!")
        break
    elif len(Nucleotide) == 1:
        dna_seq = dna_seq + Nucleotide
    i = i + 1
print("The DNA sequence is: " + dna_seq)


# In[29]:


# 7. Reverse the sequence and show output.
reverse = dna_seq[::-1]
print(reverse)


# In[30]:


# 8. Create a variable x="aggctcggatcg", y="tcg"
x = "aggctcggatcg"
y = "tcg"
# 9. Show how many times y is found in x.
times_y_in_x = x.count("tcg")
print(times_y_in_x)


# In[ ]:




