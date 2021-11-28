import string 

story = "Breathe in. Let your eyes close. Let your mind wander. Think back to a time when you were happy as a child. There must have been times when you were happy. Notice any tension in your forehead. Relax the muscles between your eyebrows. The time when you were three and your parents took you to a water park"

inp1 = input("Enter a Adj: ")
inp2 = input("Enter a verb: ")
inp3 = input("Enter a Noun: ")
inp4 = input("Enter a preposition: ")

print("Original Story:\n", story)
story2 = inp2 + " in. Let your eyes close. Let your mind "+ inp2 + ". Think back to a time when you were " + inp1 + " as a " + inp3 + ".\n There must have been times when you were " + inp1 + ". Notice any tension in your forehead. Relax the muscles " + inp4 + " your eyebrows. The time when you were three and your parents took you to a " + inp3

print("Modified Story:\n",story2)