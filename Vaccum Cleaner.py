import random
def display(room):
    print(room)
room=[[1 for a in range(4)]for b in range(4)]
print("ALL THE ROOMS ARE DIRTY")
display(room)
x=0
y=0
while x<4:
    while y<4:
        room[x][y]=random.choice([0,1])
        y+=1  
    x+=1
    y=0
print("BEFORE CLEANING THE ROOM 1 DETECT ALL OF THESE RANDOM DIRTS")
display(room)
x=0
y=0
z=0
while x<4:
    while y<4:
        if room[x][y]==1:
            print("VACUUM IN THIS LOCATION NOW, ",x,y)
            room[x][y]=0
            print("CLEANED ",x,y)
            z+=1
        y+=1
    x+=1
    y=0
pro=(100-((z/16)*100))
print("ROOM IS CLEAN NOW")
display(room)
print("PERFORMANCE --> ", pro,"%")
