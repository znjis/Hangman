

# CREATION D'UN HANGMAN A L'AIDE DU CONCEPT DE CLASSES


class GameError(Exception):
    def __str__(self) -> str:
        return super().__str__()

class hangman():
    def __init__(self, mot):
        self.mot = mot
        print(self)  # dessine le hangman
        
        
    def __str__(self):
        # a quoi est-ce que je veux que l'affichage ressemble?
        # des tirets qui definissent ou se situront les lettres

            # changer les tirets pour des lettres lorsque le mot est correct

        # devrais-je dessiner le bonhomme?
            # comment dessiner le bonhomme dans un tel cas?
        
        L1 = [" ----\n"]
        L2 = ["|    |\n"]
        L3 = ["|"]
        L4 = ["\n|"]
        L5 = ["\n|"]
        L6 = ["\n|"]
        L7 = ["\n|"]
        L8 = ["\n|"]
        L9 = ["\n--- "]
        lettres = []
        for i in self.mot:
            lettres += [" _"]
        

        # check if letter is right:
        for rights in self.guess()[0]:
            for index, letter in enumerate(self.mot):
                if rights == letter and lettres[index] == ' _':  # CALCULER L'INDEX
                    lettres[index] = f" {rights}"
                
        

        # check if letter is wrong:
        if len(self.guess()[1]) == 1:
            L3 += '    O'

        if len(self.guess()[1]) == 2:
            L4 += '   -'

        if len(self.guess()[1]) == 3:
            L4 += '|'

        if len(self.guess()[1]) == 4:
            L4 += '-'

        if len(self.guess()[1]) == 5:
            L5 += '   / '

        if len(self.guess()[1]) == 6:
            L5 += "\\"

        hang = L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9 + lettres
        return ''.join(hang)


    #def draw(self):
        

    #    L1 = " ----\n"
    #    L2 = "|    |\n"
    #    L3 = "|"
    #    L4 = "\n|"
    #    L5 = "\n|"
    #    L6 = "\n|"
    #    L7 = "\n|"
    #    L8 = "\n|"
    #    L9 = "\n---"
    #    print(L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9)


    def guess(self):
        # demande un input du joueur
            # bon ou pas bon?
            # que faire si reponse pas bonne?
        # doit changer la forme de dessinerHANG() // ajouter lettre
        essai = input("Pick a letter or make a guess: \n")            
        guesses = [[''],['']]  # right 0 and wrong 1 guesses


        # if the guess is not 1 letter or right amount of letters:
        #if not isinstance(essai, str) or len(essai) != 1 or len(essai) != len(self.mot):
         #   print("Must be 1 letter or guess a word with the same amount of letters")
          #  self.guess()
       
       
        #if he guesses a word:
        if len(essai) == len(self.mot) and essai == self.mot:
            raise GameError("Vous avez gagné la partie!!!")
        
        # if he guesses a letter and letter is right:
        elif len(essai) == 1 and essai in self.mot:
            # remplacer le tiret de la lettre par la lettre devinée
            guesses[0] += essai
            pass
        
        # if he guesses a letter and letter is wrong:
        elif len(essai) == 1 and essai not in self.mot:
            # ajouter un membre du bonhomme pendu
            guesses[1] += essai
            pass
        
        return guesses


    def gagner(self):
        #lorsque toute les lettres sont les bonnes
        pass


# ----
#|    |
#|    O
#|   -|-
#|   / \
#|
#|
#|
#---  _ _ _ _ _

# 5 tries // for each body part
    # 1) head 
    # 2) body 
    # 3) left arm
    # 4) right arm 
    # 5) left leg 
    # 6) right leg


#    O
#   -|-
#   / \

test = hangman("allogyujhv")
