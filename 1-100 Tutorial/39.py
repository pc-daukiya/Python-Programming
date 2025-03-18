'''Exercise 3'''
# Make a Kon banega karorpati logic in code
questions = [
    ["which language was used to create fb?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb1?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb2?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    ["which language was used to create fb?","Python", "French", "JavaScript",
     "Php", "None", 4
    ],
    
]
    
levels = [1000, 2000, 3000, 4000, 5000, 6000, 10000, 20000, 40000, 80000, 160000, 200000, 3200000]

money = 0
for i in range(0 , len(questions)):
    question = questions[i]
    print(f"Question for Rupess Rs. {levels[i]}")
    print(f"Question: {question[0]}")
    print(f"a. {question[1]}  b. {question[2]}")
    print(f"c. {question[3]}  d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to  quit:"))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 4000
        
        elif(i == 9):
            money = 40000
        elif(i == 11):
            money = 160000
        elif(i == 13):
            money = 160000
    else:
        print("Wrong Answer!")
        break
print(f"You're take money to home is {money}")