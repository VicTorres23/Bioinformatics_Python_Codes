# Importing motif-related functions from BioPython
from Bio import motifs
# Importing sequence-related functions from BioPython
from Bio.Seq import Seq
# Importing numpy functions
import numpy as np

# To open a file containing the DNA sequence of a BRCA1 oncogene.
BRCA1 = open("C:/Users/vemma/Documents\Master in Bioinformatics/Fall 2023 Semester/Computational & Mathematical Methods for Bioinformatics/Miniproject/BRCA1.txt", "r")

# This part of the code helps turn the contents of the FASTA file into a string.
BRCA1_sequence = "" # First we create a variable with an empty string to store our sequence.
for line in BRCA1: #We iterate each sequence line in the FASTA file.
    for nucleotide in line: #We use another for loop to iterate each nucleotide in the lines of the FASTA file.
        if nucleotide in ["T", "G", "C", "A"]: #We check if the nucleotide is indeed a nucleotide and we eliminate any character that doens't correspond to DNA.
            BRCA1_sequence = BRCA1_sequence + nucleotide #We concatenate each nucleotide and save it in a variable.
#print(len(BRCA1_sequence)) # We print the length of the BRCA1 sequence.

# This part of the code helps us identify were the sequences that starts with GT are in the BRCA1 sequence.
BRCA1_motifs_pos = [] #We create an empty list to store all the positions where the sequence GT starts in BRCA1
random = "GCG" # We create a string variable containing the second and third sequence of the RING motif.
for position in range(len(BRCA1_sequence)): # We iterate each nucleotide in the sequence.
    if BRCA1_sequence[position:].startswith(random): #If one sequence starts with "GT" then the condition will be TRUE.
        BRCA1_motifs_pos.append(position)# If the condition is TRUE it will store the index where the "GC" sequence is found.
#print(BRCA1_motifs_pos) #Uncomment this print function to see all of the sequences positions inside the sequence.

# Here we create a list of sequences that start with GC plus the 20 nucleotides after.
list_of_sequences_normal = []
background_frequency_nucleos_left = []
background_frequency_nucleos_right = []
for coordinates in BRCA1_motifs_pos:
    list_of_sequences_normal.append(BRCA1_sequence[(coordinates-1):(coordinates+10)])
    background_frequency_nucleos_left.append(BRCA1_sequence[(coordinates-8):(coordinates-4)])
    background_frequency_nucleos_right.append(BRCA1_sequence[(coordinates+11):(coordinates+15)])
number_of_motif_sequences = len(list_of_sequences_normal)
#print(background_frequency_nucleos_left)
#print(background_frequency_nucleos_right)
#print(list_of_sequences_normal)

def count_nucleos(sequences):
    number_of_As = 0
    number_of_Cs = 0
    number_of_Gs = 0
    number_of_Ts = 0
    for sequence in sequences:
        for nucleos in sequence:
            if nucleos in ["A"]:
                number_of_As = number_of_As + 1
            elif nucleos in ["C"]:
                number_of_Cs = number_of_Cs + 1
            elif nucleos in ["G"]:
                number_of_Gs = number_of_Gs + 1
            elif nucleos in ["T"]: 
                number_of_Ts = number_of_Ts + 1
    return number_of_As, number_of_Cs, number_of_Gs, number_of_Ts

As_in_left_background, Cs_in_left_background, Gs_in_left_background, Ts_in_left_background = count_nucleos(background_frequency_nucleos_left)
As_in_right_background, Cs_in_right_background, Gs_in_right_background, Ts_in_right_background = count_nucleos(background_frequency_nucleos_right)
Background_Frequency_of_A = As_in_left_background + As_in_right_background
Background_Frequency_of_C = Cs_in_left_background + Cs_in_right_background
Background_Frequency_of_G = Gs_in_left_background + Gs_in_right_background
Background_Frequency_of_T = Ts_in_left_background + Ts_in_right_background

#print(Background_Frequency_of_A)
#print(Background_Frequency_of_C)
#print(Background_Frequency_of_G)
#print(Background_Frequency_of_T)
#print(As_in_left_background, Cs_in_left_background, Gs_in_left_background, Ts_in_left_background)
#print(As_in_right_background, Cs_in_right_background, Gs_in_right_background, Ts_in_right_background)

# Here we use the Seq function to make the sequences compatible with the BioPython functions.
list_of_sequences = []
for string in list_of_sequences_normal:
    list_of_sequences.append(Seq(string))
#print(len(list_of_sequences))

# This function helps convert the sequences into Motifs objects.
m = motifs.create(list_of_sequences)
#print(m)

# This function counts the content of each nucleotide for every sequence.
#print(m.counts)

# We turn each count values for every nucleotide into a numpy array to
# be able to plot them later.
A_values = np.array(m.counts["A"])
C_values = np.array(m.counts["C"])
G_values = np.array(m.counts["G"])
T_values = np.array(m.counts["T"])
print(A_values)
#print(C_values)
#print(G_values)
#print(T_values)

# Labeling each nucleotide in the given sequences
no_bases = []
for i in range(0, len(A_values)):
    no_bases.append(str(i+1))
    backg = -len(A_values)

# Import functions for plotting the results.
import matplotlib.pyplot as plt
from matplotlib import style

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
plt.xlabel("Positions \n\n" + "The most present nucleotides in the sequences are: \n" + str(m.consensus) + "\n The least present nucleotides in the sequence are: \n" + str(m.anticonsensus))
# Show the legend to represent which color corresponds to which nucleotide.
plt.legend()
# Show the title of the graph.
plt.title("Motif Finding for BRCA1")
# Print the graph.
plt.show()

# Get the probability of ocurrences of a residue in a given motif position.
def prob_of_ocurrences(motif_frequency):
    pseudo_count = 0.5
    Frequency_counts = []
    for i in range(len(motif_frequency)):
        Frequency_counts.append("{:.2f}".format((int((motif_frequency[i]))+pseudo_count)/(number_of_motif_sequences+(4*pseudo_count))))
    return Frequency_counts

A_prob_of_ocurrences = prob_of_ocurrences(A_values)
C_prob_of_ocurrences = prob_of_ocurrences(C_values)
G_prob_of_ocurrences = prob_of_ocurrences(G_values)
T_prob_of_ocurrences = prob_of_ocurrences(T_values)

print(A_prob_of_ocurrences)
print(C_prob_of_ocurrences)
print(G_prob_of_ocurrences)
print(T_prob_of_ocurrences)

def getBackground_Frequencies(A_counts, C_counts, G_counts, T_counts):
    pseudo_count = 0.5
    Background_FrequencyA = (A_counts+pseudo_count)/((A_counts+C_counts+G_counts+T_counts)+pseudo_count*4)
    Background_FrequencyC = (C_counts+pseudo_count)/((A_counts+C_counts+G_counts+T_counts)+pseudo_count*4)
    Background_FrequencyG = (G_counts+pseudo_count)/((A_counts+C_counts+G_counts+T_counts)+pseudo_count*4)
    Background_FrequencyT = (T_counts+pseudo_count)/((A_counts+C_counts+G_counts+T_counts)+pseudo_count*4)
    return "{:.2f}".format(Background_FrequencyA), "{:.2f}".format(Background_FrequencyC), "{:.2f}".format(Background_FrequencyG), "{:.2f}".format(Background_FrequencyT)

BackgroundA, BackgroundC, BackgroundG, BackgroundT = getBackground_Frequencies(Background_Frequency_of_A, Background_Frequency_of_C, Background_Frequency_of_G, Background_Frequency_of_T)
print("Background Frequency of A: " + str(BackgroundA), "\nBackground Frequency of C: " + str(BackgroundC), "\nBackground Frequency of G: " + str(BackgroundG), "\nBackground Frequency of T: " + str(BackgroundT))
print(A_prob_of_ocurrences, C_prob_of_ocurrences, G_prob_of_ocurrences, T_prob_of_ocurrences)
#print(number_of_motif_sequences)

motif = "TGTCACTGTGC"
def getMotif_Probability_of_Ocurrence(motif):
    pseudocount = .85
    prob_of_ocurrences_motif = []
    background_frequency_motif = []
    for i in range(len(motif)):
        if motif[i] in ["T"]:
            prob_of_ocurrences_motif.append(T_prob_of_ocurrences[i])
            background_frequency_motif.append(BackgroundT)
        elif motif[i] in ["G"]:
            prob_of_ocurrences_motif.append(G_prob_of_ocurrences[i])
            background_frequency_motif.append(BackgroundG)
        elif motif[i] in ["C"]:
            prob_of_ocurrences_motif.append(C_prob_of_ocurrences[i])
            background_frequency_motif.append(BackgroundC)
        elif motif[i] in ["A"]:
            prob_of_ocurrences_motif.append(A_prob_of_ocurrences[i])
            background_frequency_motif.append(BackgroundA)
    sum_of_prob_ocurrences = 0
    for value in prob_of_ocurrences_motif:
        sum_of_prob_ocurrences = sum_of_prob_ocurrences + float(value)
    backgroundsum = 0
    for value in background_frequency_motif:
        backgroundsum = backgroundsum + float(value)
    return "{:.2f}".format((sum_of_prob_ocurrences/sum_of_prob_ocurrences-pseudocount))

print("The probability to find the motif in BRCA1 is: " + str(getMotif_Probability_of_Ocurrence(motif)))
    