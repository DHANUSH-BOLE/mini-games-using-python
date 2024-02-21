import random
import os
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
stages = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    '''
]
stages.reverse()
word=["AlanTuring",
    "GraceHopper",
    "AdaLovelace",
    "DonaldKnuth",
    "JohnvonNeumann",
    "TimBerners-Lee",
    "DennisRitchie",
    "KenThompson",
    "VintCerf",
    "LinusTorvalds",
    "MargaretHamilton",
    "LarryPage",
    "SergeyBrin",
    "BarbaraLiskov",
    "BjarneStroustrup",
    "GuidovanRossum",
    "RichardStallman",
    "EdsgerDijkstra",
    "NiklausWirth",
    "BillGates"]
choi=random.choice(word)
k=6
li=[]
for i in range(len(choi)):
    li.append('_')
while '_' in li and k>0:
    guess=input("Enter the letter:")
    clear_screen()
    for i in range(len(choi)):
        if guess==choi[i]:
            li[i]=guess
    if guess not in choi:
        k-=1
        print(stages[k])
    print(li)
if '_' not in li:
    print("Hurray!, You won")
else:
    print("you have Lost and the word is",choi)