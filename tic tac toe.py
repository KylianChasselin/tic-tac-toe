grille =['*','*','*','*','*','*','*','*','*']

print("0 1 2")
print("3 4 5")
print("6 7 8")

joueur = "X"
tour = 1
victoire_user = 0


def AjouteSymbole(joueur):
	caseBonne = 0
	while(caseBonne != 1):
		NumeroCase = int(input("choisissez une case : "))
		if(grille[NumeroCase]=='*'):
			CaseBonne = 1
	grille[NumeroCase] = joueur


def Afficher_Grille():
	for i in range(3):
		print(grille[i*3],grille[i*3+1],grille[i*3+2])


def Joueur_O_X(joueur_f):
	if(joueur_f == "X"):
		joueur = "O"
	else:
		joueur = "X"
	return joueur


def Win(victoire):
	for i in range(3):

		if (grille[i*3] == grille[i*3+1] == grille[i*3+2] != "*"):
			victoire = 1
		if (grille[i] == grille[i+3] == grille[i+6] != "*"):
			victoire = 1

	for i in range(2):
		if (grille[i+i] == grille[i+4-i] == grille[i+8-(i*3)] != "*"):
			victoire = 1
	
	return victoire


while (tour<=9 and victoire_user ==0):
	AjouteSymbole(joueur)
	Afficher_Grille()
	victoire_user = win(victoire_user)
	joueur = joueur_O_X(joueur)
	tour = tour+1


if(victoire_user == 1):
	joueur = joueur_O_X(joueur)
	print("le joueur",joueur,"a gagné !!")
else:
	print("Match nul ! Relancez une partie pour vous départagez")

input()