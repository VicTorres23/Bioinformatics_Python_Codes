
#sequence1 = "ATCGATCGTA"
#sequence2 = "ATCGAGCGCC"
def CompareSequence(seq1, seq2):
    differences = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]: 
            differences = differences + 1
    return differences

print(CompareSequence(input("Input your First DNA sequence "), input("Input your second DNA sequence: ")))