import random

while True:
    print('Benvenuto a sasso, carta, forbici by jordyno!')
    pc_choice = ['sasso', 'carta', 'forbici']
    pl_choice1 = ['sasso', 'carta', 'forbici']
    pl_choice = input("Prego immettere la giocata desiderata, o premere q per uscire: ")

    def inv_input():
        try:
            if pl_choice != pl_choice1:
                print('invalid input')
        except ValueError:
            print('invalid input.')


    def compare():
        if pl_choice == 'sasso':
            pc_choice1 = random.choice(pc_choice)
            print('Hai scelto: ' + pl_choice)
            print('il pc ha scelto: ' + pc_choice1)
            if pc_choice1 == pc_choice[2]:
                print('Hai vinto')
            elif pc_choice1 == pc_choice[0]:
                print('Parità.')
            else:
                print('Hai perso')
        elif pl_choice == 'carta':
            pc_choice1 = random.choice(pc_choice)
            print('Hai scelto: ' + pl_choice)
            print('il pc ha scelto: ' + pc_choice1)
            if pc_choice1 == pc_choice[0]:
                print('Hai vinto')
            elif pc_choice1 == pc_choice[2]:
                print('Hai perso')
            else:
                print('Parità')
        elif pl_choice == 'forbici':
            pc_choice1 = random.choice(pc_choice)
            print('Hai scelto: ' + pl_choice)
            print('il pc ha scelto: ' + pc_choice1)
            if pc_choice1 == pc_choice[1]:
                print('Hai vinto.')
            elif pc_choice1 == pc_choice[0]:
                print('Hai perso.')
            else:
                print('Parità.')
        else:
            inv_input()

    compare()
    if pl_choice == 'q':
        break