class IA:

    def __init__(self, nbs_baton):
        self.nbs_baton = nbs_baton
        self.choix = 0


    def reponse(self):
        choix = self.choix
        if self.nbs_baton == 10:
                choix = 1
        if self.nbs_baton == 9:
                choix = 1
        elif self.nbs_baton == 8:
                choix = 3
        elif self.nbs_baton == 7:
                choix = 2
        elif self.nbs_baton == 6:
                choix = 1
        elif self.nbs_baton == 5:
                choix = 1
        elif self.nbs_baton == 4:
                choix = 3
        elif self.nbs_baton == 3:
                choix = 2
        elif self.nbs_baton == 2:
                choix = 1
        elif self.nbs_baton == 1:
                choix = 1

        return choix












