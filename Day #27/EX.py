
# EXERCISE
# Create a program capable of displaying Questions like KBC

questions=[
    ["1.What is the national sport of India?",
            "a. Hockey ",            "b. Cricket " ,
            "c. Football ",          "d. Kabaddi", "None", 1],

    ["2.Which of these colours is not the colour in traffic signal lights?  ",
            "a. red ",            "b. green " ,
            "c. yellow ",          "d. orange", "None", 4],

    ["3.Which of these planets does not have rings?",
            "a. Saturn ",            "b. Venus " ,
            "c. Jupiter ",          "d. Neptune", "None", 2],

    ["4.IF someone is spending 1.5 hours a day reading, how many hours is he reading in a week?",
            "a. 7.5 ",            "b. 9 " ,
            "c. 10.5 ",          "d. 14", "None", 3],
       
     ["5.Which thread like structure in human cells carry hereditary information?",
            "a. Carapace ",            "b. Chromosome " ,
            "c. Carotid ",          "d. carcinogen", "None", 2],
  
    ["6.Which football team won the FIFA worldcup in 2022?",
            "a. Brazil ",            "b. Argentina " ,
            "c. France ",          "d. Morocco", "None", 2],

    ["7.Who wrote the Bhagwadgita?",
            "a. Rshi Vyasa ",            "b. Rishi Valmiki " ,
            "c. Tulsidas ",          "d. Hridayram", "None", 1],
   
    ["8.Prithvi, Nag and Trishul are examples of what?",
            "a. Missiles ",            "b. Submarines " ,
            "c. Aircrafts",          "d. Rockets", "None", 4],

    ["9.Beside Sachin Tendulkar,who is only other Indian Cricketer to have scored over 13,000 runs in Test Cricket?",
            "a. V Sehwag ",            "b. V S Lakshman " ,
            "c. Rahul Dravid ",          "d. Sunil Gavaskar", "None", 3],

    ["10.According to Mahabharata, which of these was not one of the Kauravas",
            "a. Yuyutsu ",            "b. Duryodhan " ,
            "c. Dushashan ",          "d. Kichaka", "None", 1],

    ["11.Most of the texts composed by Tulsidas are based on incarnations of which of these deities?",
            "a. Lord Shiva ",            "b. Lord Vishnu " ,
            "c. Lord Ganesha ",          "d. Lord Brahma", "None", 2],

    ["12.Which Cricketer holds record of playing for maximun number of IPL teams?",
            "a. D kartik ",            "b. A finch " ,
            "c. P Patel ",          "d. Thisara", "None", 2],

    ["13.Whois credited with scoring the fastest goal in international Hockey match by an Indian?",
            "a. Srdara Singh ",            "b. Ajit Pal Singh " ,
            "c. Dhyan Chand ",          "d. Gurjant Singh", "None", 4],

    ["14.Who was the first woman president of United Nations General Assembly?",
            "a. Vijaya Laxmi Pandit ",            "b. Sarojini Naidu " ,
            "c. Sucheta Kirplani ",          "d. Amrit Kaur", "None", 1],

    ["15.What was the gas that leaked from a chemical factory on may 2020 in Vishakapatnam?",
            "a. Ricin ",            "b. Styrene " ,
            "c. Benzene ",          "d. Sevin", "None", 2],
    ]

money=[1000, 2000, 5000, 10000,20000,50000,100000,500000, 1000000,2000000,4000000,
       7500000, 10000000,20000000, 70000000]
price= 0

for i in range(0, len(questions)):
    question=questions[i]
    
    print(f"Agla prashna rupay {money[i]} ke liye apke Computer screen par ye raha.")
    print(f" {question[1]},           {question[2]}")
    print(f" {question[3]},           {question[4]}")

    reply= int (input("Sahi Vikalp Chuniye"))
    
    if(reply == question[-1]):
        print(f"Bilkul sahi jawab, aap jeet te hai {money[i]} Rupay")
        if(i==4):
            price= 20000
        elif(i==9):
            price= 2000000
            print("Yaha se aage gadhi mahashay band ho jayenge, aap apna samay le sakte hai.")
        elif(i==13):
            price=20000000
            print("aap cahe to yaha khel samapt kar sakte hai!")
            print("khel samapt karne se aap jeetoge 2cr rupay")
            print("Yadi uttar galat hua to aap keval 1cr ghar le jaoge")
            
    else:
        print("Ye Uttar galat hai")
        break