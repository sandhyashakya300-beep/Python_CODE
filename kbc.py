questions = [["How many series of a HARRY POTTER ?", "4", "7", "8", "9", "none" , 2],
             [" Who was the actor which play the role of HARRY POTTER ?", " Robert Pattison", " Daniel Radcliffe", "Tom Holland", "Tom Cruice", 1],
             [" Which character played by Emma Watson ?", "Lilly POTER ", " Ginny Weasley ",  "Luna Lovegood"," Harmione Granger", 3],
             [" Who was the Half blood prince in HARRY POTTER series ?" , "Severus Snape ", "Darco Malfoy", " Sirius Black", "Tom Riddle", 0],
             [" Which character played by Rupert Grint ?", "Remus Lupin", " Albus Potter", " Cedric Diggory", " Ron Weasley", "Lord Voldemort",3],
             [" Which character played by Emma Watson ?", "Lilly POTER ", " Ginny Weasley ",  "Luna Lovegood"," Harmione Granger", 3],
             [" Who was the actor which play the role of HARRY POTTER ?", " Robert Pattison", " Daniel Radcliffe", "Tom Holland", "Tom Cruice", 1],
             [" Which character played by Rupert Grint ?", "Remus Lupin", " Albus Potter", " Cedric Diggory", " Ron Weasley", "Lord Voldemort",3],
             [" Who was the Half blood prince in HARRY POTTER series ?" , "Severus Snape ", "Darco Malfoy", " Sirius Black", "Tom Riddle", 0],
             [" Which character played by Emma Watson ?", "Lilly POTER ", " Ginny Weasley ",  "Luna Lovegood"," Harmione Granger", 3],
             [" Who was the actor which play the role of HARRY POTTER ?", " Robert Pattison", " Daniel Radcliffe", "Tom Holland", "Tom Cruice", 1],]

Levels = [ 1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(question)
    print(f"question for Rs.{Levels[i]}")
    print(f"a.{question[1]}      b.{question[2]} c.{question[3]}     d.{question[4]}")
    
    reply = int(input("Enter your answer (1-4)or 0 toquit :\n" ))
    if(reply == 0):
        money = Levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs.{Levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        
    else:
        print("Wrong answer |")
        break 
print(f"Your total money is {money}")




