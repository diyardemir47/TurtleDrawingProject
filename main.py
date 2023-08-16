import turtle

# Pencereyi açma
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("DİYARİDEM ŞEKİL ÇİZİMLERİ")

# Kare çizimi
tur_kare = turtle.Turtle()
tur_kare.color("blue")
tur_kare.penup()  # Kalemi kaldır
tur_kare.goto(-100, 100)  # Başlangıç pozisyonu
tur_kare.pendown()  # Kalemi indir
for _ in range(4):
    tur_kare.forward(100)
    tur_kare.left(90)

# Üçgen çizimi
tur_ucgen = turtle.Turtle()
tur_ucgen.color("red")
tur_ucgen.penup()
tur_ucgen.goto(150, 150)
tur_ucgen.pendown()
for _ in range(3):
    tur_ucgen.forward(120)
    tur_ucgen.left(120)

# Daire çizimi
tur_daire = turtle.Turtle()
tur_daire.color("green")
tur_daire.penup()
tur_daire.goto(-150, -100)
tur_daire.pendown()
tur_daire.circle(60)

# Yıldız çizimi
tur_yildiz = turtle.Turtle()
tur_yildiz.color("purple")
tur_yildiz.penup()
tur_yildiz.goto(0, -150)
tur_yildiz.pendown()
for _ in range(5):
    tur_yildiz.forward(100)
    tur_yildiz.right(144)

# Poligon çizimi
tur_poligon = turtle.Turtle()
tur_poligon.color("orange")
tur_poligon.penup()
tur_poligon.goto(100, -50)
tur_poligon.pendown()
sides = 6
length = 80
angle = 360 / sides
for _ in range(sides):
    tur_poligon.forward(length)
    tur_poligon.left(angle)

# Pencereyi kapatmak için bekletme
turtle.done()
