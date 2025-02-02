#!/usr/bin/env python
# coding: utf-8

# In[9]:


#1. Read the Sequence FASTA file.
FASTA_file = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Untitled Folder 2/FASTA_LAB05.txt", "r")
print(FASTA_file.read())
#FASTA_file.close()


# In[15]:


#2. Transcribe the DNA sequence to RNA.
FASTA_content = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall 2023 Semester/Introduction to Bioinformatics I/Lab/Untitled Folder 2/FASTA_LAB05.txt", "r")
eliminate = FASTA_content.readline()
#print(eliminate)
sequence_FASTA = FASTA_content.read()
sequence = ""
for line in sequence_FASTA:
    for nucleotide in line:
        if nucleotide in ["T", "G", "C", "A"]:
            sequence = sequence + nucleotide
#print(sequence)
Transcribed_sequence = sequence.replace("T", "U")
print("\n" + str(Transcribed_sequence))
FASTA_content.close()


# In[14]:


#3. Obtain all (6) reading frames, and show the first and last 4 codons of each frame.
def getPositiveORF(seq):
    list_ORF = {}
    ListOfCodons = []
    first_nucleo = 0
    LenOfACodon = 3
    seq = seq.upper()
    while first_nucleo < 3:
        for position in range(first_nucleo, len(seq), LenOfACodon):
            ListOfCodons.append(seq[position:position+LenOfACodon])
            list_ORF["ORF+"+str(first_nucleo+1)] = ListOfCodons
        first_nucleo = first_nucleo + 1
        ListOfCodons = []
    return print("Open Reading Frame +1: \n" + str(list_ORF["ORF+1"])), print("\n First 4 codons of ORF+1: \n" + str(list_ORF["ORF+1"][0:4])), print("\n Last 4 codons of ORF+1: \n" + str(list_ORF["ORF+1"][-5:-1])), print("\nOpen Reading Frame +2: \n" + str(list_ORF["ORF+2"])), print("\n First 4 codons of ORF+2: \n" + str(list_ORF["ORF+2"][0:4])), print("\n Last 4 codons of ORF+2: \n" + str(list_ORF["ORF+2"][-5:-1])), print("\nOpen Reading Frame +3: \n" + str(list_ORF["ORF+3"]), print("\n First 4 codons of ORF+3: \n" + str(list_ORF["ORF+3"][0:4])), print("\n Last 4 codons of ORF+3: \n" + str(list_ORF["ORF+3"][-5:-1])))

def reverse_complement(seq):
    reverse = seq[::-1]
    reverse_complement = ""
    complements = {"U":"A",
                   "A":"U",
                   "G":"C",
                   "C":"G"}
    for nucleo in reverse:
        if nucleo in complements.keys():
            reverse_complement = reverse_complement + complements.get(nucleo)
    return reverse_complement

def getNegativeORF(seq):
    list_ORF = {}
    ListOfCodons = []
    first_nucleo = 0
    LenOfACodon = 3
    i = 1
    seq = seq.upper()
    seq = str(reverse_complement(seq))
    while first_nucleo < 3:
        for position in range(first_nucleo, len(seq), LenOfACodon):
            ListOfCodons.append(seq[position:position+LenOfACodon])
            list_ORF["ORF"+str(first_nucleo-i)] = ListOfCodons
        first_nucleo = first_nucleo + 1
        i = i + 2
        ListOfCodons = []
    return print("\nOpen Reading Frame -1: \n" + str(list_ORF["ORF-1"])), print("\n First 4 codons of ORF-1: \n" + str(list_ORF["ORF-1"][0:4])), print("\n Last 4 codons of ORF-1: \n" + str(list_ORF["ORF-1"][-5:-1])), print("\nOpen Reading Frame -2: \n" + str(list_ORF["ORF-2"])), print("\n First 4 codons of ORF-2: \n" + str(list_ORF["ORF-2"][0:4])), print("\n Last 4 codons of ORF-2: \n" + str(list_ORF["ORF-2"][-5:-1])), print("\nOpen Reading Frame -3: \n" + str(list_ORF["ORF-3"]), print("\n First 4 codons of ORF-3: \n" + str(list_ORF["ORF-3"][0:4])), print("\n Last 4 codons of ORF-3: \n" + str(list_ORF["ORF-3"][-5:-1])))

RNA_seq_positive = getPositiveORF(Transcribed_sequence)
RNA_seq_negative = getNegativeORF(Transcribed_sequence)


# In[5]:


#4. Translate and show all (6) reading frames.
codons_aminoacids = {"UUU":"Phe",
                    "UUC": "Phe",
                    "UUA": "Leu",
                    "UUG": "Leu",
                    "UCU": "Ser",
                    "UCC": "Ser",
                    "UCA": "Ser",
                    "UCG": "Ser",
                    "UAU": "Tyr",
                    "UAC": "Tyr",
                    "UGU": "Cys",
                    "UGC": "Cys",
                    "UGG": "Trp",
                    "CUU": "Leu",
                    "CUC": "Leu",
                    "CUA": "Leu",
                    "CUG": "Leu",
                    "CCU": "Pro",
                    "CCC": "Pro",
                    "CCA": "Pro",
                    "CCG": "Pro",
                    "CAU": "His",
                    "CAC": "His",
                    "CAA": "Gln",
                    "CAG": "Gln",
                    "CGU": "Arg",
                    "CGC": "Arg",
                    "CGA": "Arg",
                    "CGG": "Arg",
                    "AUU": "Ile",
                    "AUC": "Ile",
                    "AUA": "Ile",
                    "AUG": "Met",
                    "ACU": "Thr",
                    "ACC": "Thr",
                    "ACA": "Thr",
                    "ACG": "Thr",
                    "AAU": "Asn",
                    "AAC": "Asn",
                    "AAA": "Lys",
                    "AAG": "Lys",
                    "AGU": "Ser",
                    "AGC": "Ser",
                    "AGA": "Arg",
                    "AGG": "Arg",
                    "GUU": "Val",
                    "GUC": "Val",
                    "GUA": "Val",
                    "GUG": "Val",
                    "GCU": "Ala",
                    "GCC": "Ala",
                    "GCA": "Ala",
                    "GCG": "Ala",
                    "GAU": "Asp",
                    "GAC": "Asp",
                    "GAA": "Glu",
                    "GAG": "Glu",
                    "GGU": "Gly",
                    "GGC": "Gly",
                    "GGA": "Gly",
                    "GGG": "Gly",
                    "UAA": "STOP",
                    "UAG": "STOP",
                    "UGA": "STOP"}

def getPositiveORF(seq):
    list_ORF = {}
    ListOfCodons = []
    first_nucleo = 0
    LenOfACodon = 3
    seq = seq.upper()
    while first_nucleo < 3:
        for position in range(first_nucleo, len(seq), LenOfACodon):
            ListOfCodons.append(seq[position:position+LenOfACodon])
            list_ORF["ORF+"+str(first_nucleo+1)] = ListOfCodons
        first_nucleo = first_nucleo + 1
        ListOfCodons = []
    return list_ORF

def reverse_complement(seq):
    reverse = seq[::-1]
    reverse_complement = ""
    complements = {"T":"A",
                   "A":"U",
                   "G":"C",
                   "C":"G"}
    for nucleo in reverse:
        if nucleo in complements.keys():
            reverse_complement = reverse_complement + complements.get(nucleo)
    return reverse_complement

def getNegativeORF(seq):
    list_ORF = {}
    ListOfCodons = []
    first_nucleo = 0
    LenOfACodon = 3
    i = 1
    seq = seq.upper()
    seq = str(reverse_complement(seq))
    while first_nucleo < 3:
        for position in range(first_nucleo, len(seq), LenOfACodon):
            ListOfCodons.append(seq[position:position+LenOfACodon])
            list_ORF["ORF"+str(first_nucleo-i)] = ListOfCodons
        first_nucleo = first_nucleo + 1
        i = i + 2
        ListOfCodons = []
    return list_ORF
            
RNA_seq_positive = getPositiveORF(Transcribed_sequence)
RNA_seq_negative = getNegativeORF(Transcribed_sequence)

ORFs = getPositiveORF(Transcribed_sequence)
ORFs.update(getNegativeORF(Transcribed_sequence))

Translated_codons = []
for ORF in ORFs.values():
    for codon in ORF:
        if codon in codons_aminoacids.keys():
            Translated_codons.append(codons_aminoacids.get(codon))

#print(Translated_codons)
splitting = []
for i in range(0, len(Translated_codons), len(ORF)):
    splitting.append(Translated_codons[i:i+len(ORF)])

ORFs["ORF+1"] = splitting[0]
ORFs["ORF+2"] = splitting[1]
ORFs["ORF+3"] = splitting[2]
ORFs["ORF-1"] = splitting[3]
ORFs["ORF-2"] = splitting[4]
ORFs["ORF-3"] = splitting[5]

print("Open Reading Frame +1: \n" + str(ORFs["ORF+1"]) + "\n\nOpen Reading Frame +2: \n" + str(ORFs["ORF+2"]) + "\n\n Open Reading Frame +3: \n" + str(ORFs["ORF+3"]) + "\n\n Open Reading Frame -1: \n" + str(ORFs["ORF-1"]) + "\n\n Open Reading Frame -2: \n" + str(ORFs["ORF-2"]) + "\n\n Open Reading Frame -3: \n" + str(ORFs["ORF-3"]))


# In[6]:


#6. Save in the file "frames_output.txt" all ORF within each reading frame like this.

ORFs_file = open("frames_output.txt", "w")
#RNA_seq_positive = getPositiveORF(Transcribed_sequence)
#RNA_seq_negative
content = "Open Reading Frame +1: \n" + str(RNA_seq_positive["ORF+1"]) + "\n\n" + str(ORFs["ORF+1"]) + "\n\nOpen Reading Frame +2: \n" + str(RNA_seq_positive["ORF+2"]) + "\n\n" + str(ORFs["ORF+2"]) + "\n\n Open Reading Frame +3: \n" + str(RNA_seq_positive["ORF+3"]) + "\n\n" + str(ORFs["ORF+3"]) + "\n\n Open Reading Frame -1: \n" + str(RNA_seq_negative["ORF-1"]) + "\n\n" + str(ORFs["ORF-1"]) + "\n\n Open Reading Frame -2: \n" + str(RNA_seq_negative["ORF-2"]) + "\n\n" + str(ORFs["ORF-2"]) + "\n\n Open Reading Frame -3: \n" + str(RNA_seq_negative["ORF-3"]) + "\n\n" + str(ORFs["ORF-3"])
#print(content)
ORFs_file.write(content)
ORFs_file = open("frames_output.txt", "r")
print(ORFs_file.read())


# In[7]:


#7. Can a function be called without any parameters/arguments?

#   A default value will be used if the function doesn't have any arguments, so the answer is yes.


# In[ ]:


#8. Can a function be defined without return statement? If yes, then what does it return?

# Yes it can, if the function doesn't have any return statement, it will returns None.


# In[ ]:


#9. Does every function need to know in advance how many parameters it will receive?

#   It is not necessary, the funtion will still work even if there are no parameters defined, however, it is recommended to define the parameters to allow different input values to be used when running a function.


# In[ ]:


#10. Which variable will be used if the name is defined both inside and outside the function?

#   The function will give the value given by the variable inside the function and it will ignore the one outside the function.


# In[ ]:


#11. Can you define a variable as global inside a function? If yes, how do you define?

#   Yes, it can be done if you type the word "global" before the name of the variable.

