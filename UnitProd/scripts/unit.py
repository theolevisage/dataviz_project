class Unit:

    def __init__(self, name, mail, decalage, exposant, number, automats):
        self.name = name
        self.mail = mail
        self.decalage = decalage
        self.exposant = exposant
        self.number = number
        self.automats = automats

    def make_work_proof(self, stamp):
        xor = int(stamp) ^ int(self.exposant)
        return xor << int(self.decalage)

    def generate_automats_data(self):
        for i in range(10):
            self.automats[i].generate_infos()
