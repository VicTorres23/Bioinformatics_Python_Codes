#!/usr/bin/env python
# coding: utf-8

# In[41]:


# 1. Make a variable called "my_dna", with value: atgcgta.
my_dna = "atgcgta"
# 2. Change my_dna to upper case.
my_dna = my_dna.upper()
# 3. Show the DNA sequence.
print(my_dna)


# In[33]:


# 4. Show "My DNA sequence has X nucleotides", where X is the total of nucleotides in sequence.
print("My DNA sequence has " + str(len(my_dna)) + " nucleotides")


# In[34]:


# 5. Print each nucleotide of the sequence.
for nucleotide in my_dna:
    print(nucleotide)


# In[35]:


# 6. Change my_dna value to: TGGTCCA
my_dna = "TGGTCCA"
# 7. Make a variable called "upstream" with value: AAA
upstream = "AAA"
# 8. Show the value of the upstream and my_dna, as a concatenated sequence, then my_dna and upstream.
print(my_dna + upstream + "\n" + my_dna + "\n" + upstream)


# In[36]:


# 9. Print the numbers from 1-10 using a loop.
for i in range(1, 11):
    print(i)


# In[37]:


# 10. Create two lists, odd & even. Using a loop, add odds numbers from 1-10 to "odd" list, and "even" numbers to "even" list. Show both lists.
odd = []
even = []
for i in range(1, 11):
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)
print(odd)
print(even)


# In[38]:


# 11. Using my_dna, show the output:
# My DNA sequence is: TGGTCCA
# T is a nucleotide
# G is a nucleotide
# ...
# A is a nucleotide
print("My DNA sequence is: " + my_dna)
for nucleotide in my_dna:
    print(nucleotide + " is a nucleotide")


# In[39]:


# 12. Using my_dna, show the output:
# nucleotide 3-6 are: GTCC
print("nucleotide 3-6 are " + my_dna[2:6])


# In[ ]:




