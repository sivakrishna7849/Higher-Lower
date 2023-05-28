import random
from art import logo
from art import vs
from game_data import data
import os
ans=True
i=1
count=0

def choose(data):
  return random.choice(data)
  
def compare(choice,a,b):
  
  if(a['follower_count']>b['follower_count']):
    return 'A'
  else:
    return 'B'
    
while(ans!=False):
  
  while(i!=0):
    
    print(logo)
    a=choose(data)
    i-=1
  b=choose(data)
  
  while(a==b):
    
    b=choose(data)
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}. ")
  print(vs)
  print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}. ")
  choice=input("Who has more followers?. Type 'A' or 'B': ").upper()
  answer=compare(choice,a,b)
  
  if(answer==choice):
    
    os.system('cls')
    print(logo)
    count+=1
    print(f"You're right! Current score is {count}")
    if(a['follower_count']<b['follower_count']):
      
      data.remove(a)
      a=b
    else:
      
      data.remove(b)
      
  else:
    print(f"sorry that's wrong your final score is {count}")
    ans=False
    
  if(count==49):
    print("\nCongratulations you have completed and won the game")
    
print("Thank you for playing the game")