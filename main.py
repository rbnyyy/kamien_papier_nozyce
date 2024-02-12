import random

znaki = [
    """
   _____
---'   __)
      (___)
      (___)
      (__)
---.__(_)
""",
"""
    _____
---'    __)____
            ____)
            _____)
            _____)
---.__________)         
         
""",
"""
    _____
---'   __)____
          ____)
       ________)
      (__)
---.__(_)        
"""
         ]

punkty_gracza = 0
punkty_kompa = 0

while not punkty_kompa == 3 or punkty_gracza == 3:

    print("Kamień - 1")
    print("Papier - 2")
    print("Nożyce - 3")
    wybor_gracz = int(input("Jaki wybierasz znak?"))

    if wybor_gracz == 1:
        print(znaki[0])
    elif wybor_gracz == 2:
        print(znaki[1])
    elif wybor_gracz == 3:
        print(znaki[2])

    wybor_kompa = random.choice(znaki)

    print(wybor_kompa)

    if wybor_kompa == znaki[0] and wybor_gracz == 2:
        punkty_gracza += 1
        print(f"CPU : Player {punkty_kompa}:{punkty_gracza}")

    elif wybor_kompa == znaki[1] and wybor_gracz == 1:
        punkty_kompa += 1
        print(f"CPU : Player {punkty_kompa}:{punkty_gracza}")

    elif wybor_kompa == znaki[0] and wybor_gracz == 3:
        punkty_kompa += 1
        print(f"CPU : Player {punkty_kompa}:{punkty_gracza}")

    elif wybor_kompa == znaki[2] and wybor_gracz == 1:
        punkty_gracza += 1
        print(f"CPU : Player {punkty_kompa}:{punkty_gracza}")

    elif wybor_kompa == znaki[1] and wybor_gracz == 3:
        punkty_gracza += 1
        print(f"CPU : Player {punkty_kompa}:{punkty_gracza}")

    elif wybor_kompa == znaki[2] and wybor_gracz == 2:
        punkty_kompa += 1
        print(f"CPU : Player {punkty_kompa}:{punkty_gracza}")

    elif wybor_kompa == znaki[0] and wybor_gracz == 1:
        print("Draw")
        print(f"CPU : Player {punkty_kompa}:{punkty_gracza}")

    elif wybor_kompa == znaki[1] and wybor_gracz == 2:
        print("Draw")
        print(f"CPU : Player {punkty_kompa}:{punkty_gracza}")

    elif wybor_kompa == znaki[2] and wybor_gracz == 3:
        print("Draw")
        print(f"CPU : Player {punkty_kompa}:{punkty_gracza}")