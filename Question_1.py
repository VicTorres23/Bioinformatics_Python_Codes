
# We start creating our function, giving it a name.
def classify_AT_content(seq):
    AT_content = (seq.count("A") + seq.count("T"))/len(seq) #This parts calculates de percentage of AT content by counting the T's ans A's in the sequence and diving them by the length of the sequence.
    if AT_content >= .5: # We create an if condition to see if the percentage is greater than 50%.
        return True # If the condition is met, returns True
    else:
        return False # If the condition is not met, return False.

print(classify_AT_content(input("Enter your DNA sequence: "))) #Printing the result.