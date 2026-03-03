xp = 0
level = 1
energy = 15
level_up = 200
def upar(xp,level):
    if xp >= level_up:
        xp-= level_up
        level += 1
        print(f"Level Up! Agora você é nível {level}")
    return xp,level

while True:
    print("1- Work +50xp")
    print("2- Sleep +75xp")
    print("3- Status")
    print("4- Treinne +15xp")
    print("5- Exit")
    option = int(input("Insert a number:"))
    if option == 1:
        xp += 50
        energy -= 10
        xp,level = upar(xp,level)
        print(f"Work with sucess :),Your xp and level is: {xp}, {level}")
    elif option == 2:
        energy += 75
        print(f"Sleep Ok! Your energy {energy}")
    elif option == 3:
        print("----::STATUS::----")
        print(f"Your xp: {xp}!")
        print(f"Your energy: {energy}")
    elif option == 4:
        upar(xp)
        xp += 15
        print(f"Treinne with sucess!! Your xp: {xp}")
    elif option == 5:
        print("Exit for sistem! :)")
        break
    else:
        print("Option invalid!")