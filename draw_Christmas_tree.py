from turtle import *
bgcolor("cornflower blue")
speed(0)
pu()
goto(-30,-130)
pd()
ht()

# tree trunk
color('saddle brown','saddle brown')
begin_fill()
for i in range (2):
    fd(60)
    rt(90)
    fd(50)
    rt(90)
end_fill()

# tree branches 
color('forest green','dark green')

# lower branch
pu()
goto(-150,-130)
pd()
begin_fill()
goto(150,-130)
goto(90,-40)
goto(-90,-40)
goto(-150,-130)
end_fill()

# middle branch
pu()
goto(-110,-40)
pd()
begin_fill()
goto(110,-40)
goto(50,50)
goto(-50,50)
goto(-110,-40)
end_fill()

# upper branch
pu()
goto(-70,50)
pd()
begin_fill()
goto(70,50)
goto(0,150)
goto(-70,50)
end_fill()

# color balls
centers=[(-110,-130), (110,-130), (-60,-90), 
        (40,-80), (-30,-40), (90,-20),(-80,0),(40,60)]
colors=['yellow', 'purple', 'white', 'pink', 'yellow', 'white', 'red', 'blue']

i=0
for center in centers:
    pu()
    goto(center)
    pd()
    color(colors[i], colors[i])
    begin_fill()
    circle(12)
    end_fill()
    i+=1

# top star
pu()
goto(-30,160)
color('yellow','yellow')
begin_fill()
for i in range (5):
    fd(50)
    rt(144)
end_fill()

# write message
pu()
goto(-200,180)
pd()
pencolor('red')
write("Merry Christmas!", font=['vladimir script', 50, 'bold'])
mainloop()