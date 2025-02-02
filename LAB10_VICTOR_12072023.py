#!/usr/bin/env python
# coding: utf-8

# In[42]:


# 1. Choose 10 sequences from GenBank (might be useful to make this a function)
BRCA1 = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_10/Lab 10 Python/BRCA1.txt", "r")
read_BRCA1 = BRCA1.read()
EGFR = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_10/Lab 10 Python/EGFR.txt", "r")
read_EGFR = EGFR.read()
KRAS = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_10/Lab 10 Python/KRAS.txt", "r")
read_KRAS = KRAS.read()
CDH1 = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_10/Lab 10 Python/CDH1.txt", "r")
read_CDH1 = CDH1.read()
TP53 = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_10/Lab 10 Python/TP53.txt", "r")
read_TP53 = TP53.read()
IDH1 =open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_10/Lab 10 Python/IDH1.txt", "r")
read_IDH1 = IDH1.read()
MSH2 = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_10/Lab 10 Python/MSH2.txt", "r")
read_MSH2 = MSH2.read()
CDC5L = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_10/Lab 10 Python/CDC5L.txt", "r")
read_CDC5L = CDC5L.read()
MYC = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_10/Lab 10 Python/MYC.txt", "r")
read_MYC = MYC.read()
ERG = open("C:/Users/vemma/Documents/Master in Bioinformatics/Fall_2023_Semester/Introduction_to_Bioinformatics_I/Lab/Lab_10/Lab 10 Python/ERG.txt", "r")
read_ERG = ERG.read()

# a. Extract sequence itself
# b. Parse for sequence
# c. c. Label and Print sequence only

import re

def extract_seq(file):
    Info = ""
    match1 = re.search("DEFINITION\s+(.+)", file)
    Info = Info + "\n" + match1.group(1) + "\n"
    file = re.sub("\n", "", file)
    match2 = re.search(r"ORIGIN(.+)", file)
    file = re.sub(r"\s", "", match2.group(1))
    file = re.sub(r"\d", "", file)
    file = re.sub(r"\/\/", "", file)
    Info = Info + "\n" + file
    return Info
read_BRCA1 = extract_seq(read_BRCA1)
print(read_BRCA1)
read_EGFR = extract_seq(read_EGFR)
print(read_EGFR)
read_KRAS = extract_seq(read_KRAS)
print(read_KRAS)
read_CDH1 = extract_seq(read_CDH1)
print(read_CDH1)
read_TP53 = extract_seq(read_TP53)
print(read_TP53)
read_IDH1 = extract_seq(read_IDH1)
print(read_IDH1)
read_MSH2 = extract_seq(read_MSH2)
print(read_MSH2)
read_CDC5L = extract_seq(read_CDC5L)
print(read_CDC5L)
read_MYC = extract_seq(read_MYC)
print(read_MYC)
read_ERG = extract_seq(read_ERG)
print(read_ERG)


# In[28]:


# 2. For every sequence, create a dictionary of the count of each codon.
#    a. Say sequence is ATCATG, then the codons are ATC and ATG, and the count of the codons are ATC:1 ATG: 1
#    b. Print Every dictionary for every taxa

def find_n_count(file):
    file = re.sub(r".+\.\n", "", file)
    file = re.sub(r"\n", "", file)
    codonsList = []
    for i in range(0, len(file), 3):
        codonsList.append(file[i:i+3])
    for codon in codonsList:
        if len(codon) < 3:
            codonsList.remove(codon)
    Info = ""
    codonsSet = list(set(codonsList))
    countlistcodons = []
    codon_n_frequency = {}
    for j in range(len(codonsSet)):
        for i in range(len(codonsList)):
            if codonsSet[j] == codonsList[i]:
                countlistcodons.append(codonsList[i])
        codon_n_frequency[str(codonsSet[j])] = len(countlistcodons)
        countlistmotif = []
    return codon_n_frequency

codonCountBRCA1 = find_n_count(read_BRCA1)
print("Codons and their frequency in the BRCA1 gene: \n" + str(codonCountBRCA1) + "\n")
codonCountEGFR = find_n_count(read_EGFR)
print("Codons and their frequency in the EGFR gene: \n" + str(codonCountEGFR) + "\n")
codonCountKRAS = find_n_count(read_KRAS)
print("Codons and their frequency in the KRAS gene: \n" + str(codonCountKRAS) + "\n")
codonCountCDH1 = find_n_count(read_CDH1)
print("Codons and their frequency in the CDH1 gene: \n" + str(codonCountCDH1) + "\n")
codonCountTP53 = find_n_count(read_TP53)
print("Codons and their frequency in the TP53 gene: \n" + str(codonCountTP53) + "\n")
codonCountIDH1 = find_n_count(read_IDH1)
print("Codons and their frequency in the IDH1 gene: \n" + str(codonCountIDH1) + "\n")
codonCountMSH2 = find_n_count(read_MSH2)
print("Codons and their frequency in the MSH2 gene: \n" + str(codonCountMSH2) + "\n")
codonCountCDC5L = find_n_count(read_CDC5L)
print("Codons and their frequency in the CDC5L gene: \n" + str(codonCountCDC5L) + "\n")
codonCountMYC = find_n_count(read_MYC)
print("Codons and their frequency in the MYC gene: \n" + str(codonCountMYC) + "\n")
codonCountERG = find_n_count(read_ERG)
print("Codons and their frequency in the ERG gene: \n" + str(codonCountERG) + "\n")


# In[37]:


# 3. Make another dictionary that holds the results for all the other dictionaries
#    a. Dict_A = {‘ATC’: 1, ‘ATG’: 1}
#    b. Dict_B = {‘ATC’: 1, ‘ATG’: 1}
#    So the merged dictionary looks like:
#    Dict_All = {‘ATC’: 2, ‘ATG’: 2}
#    c. Print Merged dictionary

def mergeDict(Dict1, Dict2):
    mergedCodons = {}
    for key1 in Dict1:
        for key2 in Dict2:
            if key1 == key2:
                mergedCodons[str(key1)] = int(Dict1[key1]) + int(Dict2[key1])
    return Dict1
#print(codonCountBRCA1)
#print(codonCountEGFR)
#print(mergeDict(codonCountBRCA1, codonCountEGFR))

def mergeAllDict(Dict1, Dict2, Dict3, Dict4, Dict5, Dict6, Dict7, Dict8, Dict9, Dict10):
    mergedDict = mergeDict(Dict1, Dict2)
    mergedDict2 = mergeDict(Dict3, mergedDict)
    mergedDict3 = mergeDict(Dict4, mergedDict2)
    mergedDict4 = mergeDict(Dict5, mergedDict3)
    mergedDict5 = mergeDict(Dict6, mergedDict4)
    mergedDict6 = mergeDict(Dict7, mergedDict5)
    mergedDict7 = mergeDict(Dict8, mergedDict6)
    mergedDict8 = mergeDict(Dict9, mergedDict7)
    mergedDict9 = mergeDict(Dict10, mergedDict8)
    return mergedDict9
print(mergeAllDict(codonCountBRCA1, codonCountEGFR, codonCountKRAS, codonCountCDH1, codonCountTP53, codonCountIDH1, codonCountMSH2, codonCountCDC5L, codonCountMYC, codonCountERG))


# In[100]:


# 4. Make a function that makes a dictionary for the open reading frames for 1 of your sequences.
#    a. Take your sequence
#    b. The function needs to take only as an input the raw sequence
#    c. The function needs to make its 6 reading frames (for negative we need the reverse complement)
#    d. Remember, modularity (you can make smaller functions that are called by the bigger function)
#    e. translate
#    f. From those reading frames use REGEX to find all possible finds of the start Codon
#    methionine in UIPAC one letter code ‘M’, and ‘*’
#    g. Save the results on a list (hint: .findall() ) and place those results in a dictionary of the
#    following format: (point h)
#    h. ORF_dict = {“ORF+1”: [“MVTH*, M*], “ORF+2”: []………}
#    i. Print ORF_Dict
def getORFs(seq):
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
                       "A":"T",
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
    AllORFs = getPositiveORF(seq)
    NegativeORF = getNegativeORF(seq)
    AllORFs.update(NegativeORF)
    def Translate(DictOfCodons):
        AADict = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                  "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                  "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
                  "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W",
                  "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                  "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                  "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                  "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                  "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                  "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                  "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                  "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                  "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                  "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                  "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                  "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
        translatedORF = []
        listOfTranslatedORFs = []
        for codons in DictOfCodons.values():
            for codon in codons:
                if codon in AADict.keys():
                    translatedORF.append(AADict.get(codon))
            listOfTranslatedORFs.append(translatedORF)
            translatedORF = []
        for i in range(len(listOfTranslatedORFs)):
            if (i+1) < 4:
                DictOfCodons["ORF+" + str(i+1)] = listOfTranslatedORFs[i]
            elif (i+1) > 3:
                DictOfCodons["ORF" + str(3-(i+1))] = listOfTranslatedORFs[i]
        return DictOfCodons
    TranslatedORFs = Translate(AllORFs)
    def Met_Stop(Dict):
        listORFs = []
        ORFAminoSeq = ""
        for listAminos in Dict.values():
            for Amino in listAminos:
                ORFAminoSeq = ORFAminoSeq + str(Amino)
            matches = re.findall(r"M[A-Z]+\*", ORFAminoSeq)
            listORFs.append(matches)
            ORFAminoSeq = ""
        for i in range(len(Dict)):
            if (i+1) < 4:
                Dict["ORF+" + str(i+1)] = listORFs[i]
            elif (i+1) > 3:
                Dict["ORF" + str(3-(i+1))] = listORFs[i]
        return Dict
    return Met_Stop(TranslatedORFs)
ORF_Dict = getORFs(read_BRCA1)
print(ORF_Dict)


# In[ ]:


# 5. Can you create a dictionary key with file objects?
# Yes, you can, as long as you use the str() function between the braquets that are to the right of the name of the dictionary.
# It should look like this:
# Dictionary[str(file_object)] = value


# In[ ]:


# 6. Can the dictionary keys store multiple values for the same key?
# Yes, it can, if you create a list of values and assign to that key. This concept was applied in the development of this lab.

