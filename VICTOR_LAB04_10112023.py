#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Can a function be called without any parameters/arguments?

#   A default value will be used if the function doesn't have any arguments, so the answer is yes.


# In[ ]:


#2. Can a function be defined without return statement? If yes, then what does it return?

#   Yes it can, if the function doesn't have any return statement, it will returns None.


# In[ ]:


#3. Does every function need to know in advance how many parameters it will receive?

#   It is not necessary, the funtion will still work even if there are no parameters defined, however, it is recommended to define the parameters to allow different input values to be used when running a function.


# In[ ]:


#4. Which variable will be used if the name is defined both inside and outside the function?

#   The function will give the value given by the variable inside the function and it will ignore the one outside the function.


# In[ ]:


#5. Can you define a variable as global inside a function? If yes, how do you define?

#   Yes, it can be done if you type the word "global" before the name of the variable.


# In[15]:


#6. Run the below code:
def duplicate(x):
    y=1
    print("y={0}".format(y))
    return (2*x)
#a. What will be the output of the below code when x=10?
duplicate(10)

#   The function printed the local variable y=1.

#b. When you type print(y) after the above code you get an error. Explain why you get this error
#   and how to overcome this error.

# The next print function has been commented to let the rest of the code run,
# uncomment it to see the error.

# print(y)

#  The error is because the function print() cannot access a local variable inside the function.


# In[16]:


#7. Write a function ‘count_values’ to count the number of times a base is repeated in DNA
#   sequence. The function must take 2 parameters, the first one is the sequence, and the second is
#   the base we are looking for. Use the test cases below to test your function.

def count_values(seq, nucleotide):
    count_base = seq.count(nucleotide)
    return print(count_base)

#   1. dna_sequence1 = "GGTTGCCCTCATCTCTTACCTCGGC" and base1 = "C". Then calculate the
#      number of times C is repeated in the string dna by using the function you created.

dna_sequence1 = "GGTTGCCCTCATCTCTTACCTCGGC"
base1 = "C"

count_values(dna_sequence1, base1)

#   2. dna_sequence2 = "ACTGATGCCTCAAGGGCATCAGAAC" and base2 = "A". . Then calculate
#   the number of times A is repeated in the string dna by using the function you created.

dna_sequence2 = "ACTGATGCCTCAAGGGCATCAGAAC"
base2 = "A"

count_values(dna_sequence2, base2)

#   You should print the output using the print function. The print statement needs to be inside the
#   scope of the function.


# In[17]:


#8. Write a python function called getGC_content that calculates the GC content of a DNA strand.

def getGC_content(seq):
    GC_percentage = (seq.count("G") + seq.count("C"))/len(seq)
    return print(GC_percentage)

getGC_content(dna_sequence1)


# In[18]:


#9. Now, write a function called getAT_content that calculates the AT content for a DNA strand.
def getAT_content(seq):
    AT_percentage = (seq.count("A") + seq.count("T"))/len(seq)
    return print(AT_percentage)

getAT_content(dna_sequence1)


# In[24]:


#10. Write a python function to compute the reverse complement of a DNA strand.

def reverse_complement(seq):
    reverse = seq[::-1]
    reverse_complement = ""
    complements = {"T":"A",
                   "A":"T",
                   "G":"C",
                   "C":"G"}
    for nucleo in reverse:
        if nucleo in complements.keys():
            reverse_complement = reverse_complement + complements.get(nucleo)
    return print(reverse_complement)

print("The original sequence is: " + str(dna_sequence1) + "\n\nThe reverse complement is: ")
reverse_complement(dna_sequence1)


# In[ ]:





# In[ ]:




