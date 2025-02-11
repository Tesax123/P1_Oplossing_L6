import turtle  # Deze import moest toegevoegd worden

aantal_punten = int(input("Hoeveel punten moet de ster hebben? ")) # We moesten het casten naar een int

t = turtle.Turtle() # Turtle was verkeerd gespeld
t.speed(4)

for i in range(aantal_punten): # Dubbelpunt ontbrak
    if i % 2 == 0:
        t.color("red")
    else:
        t.color("blue") # Indentatie stond verkeerd

    t.forward(200)
    t.right(180 - 180 / aantal_punten)  # aantal_punten had geen underscore


t.hideturtle() 
turtle.done()
