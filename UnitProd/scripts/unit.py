class Unit:

    def __init__(self, name, mail, decalage, exposant, number, automats):
        self.name = name
        self.mail = mail
        self.decalage = decalage
        self.exposant = exposant
        self.number = number
        self.automats = automats
        self.number_before_boom = 0

    def make_work_proof(self, stamp):
        xor = int(stamp) ^ int(self.exposant)
        return xor << int(self.decalage)

    def generate_automats_data(self):
        self.number_before_boom += 1
        for i in range(10):
            if int(self.number) == 2 and i == 3 and self.number_before_boom == 4:
                self.automats[i].generate_error_infos()
            else:
                self.automats[i].generate_infos()
