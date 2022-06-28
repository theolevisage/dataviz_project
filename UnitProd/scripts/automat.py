import random


class Automat:

    def __init__(self, number, type):
        self.number = number
        self.type = type
        self.infos = None

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def set_infos(self, infos):
        self.infos = infos

    def get_infos(self):
        return self.infos

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def generate_infos(self):
        # Uncomment to simulate anomalies on unit_number 1
        # if unit_number == str(1):
        #    automat_number = 45
        # else:
        #    automat_number = i + 1
        tank_temp = round(random.random() * 1.5 + 2.5, 1)
        ext_temp = round(random.random() * 6 + 8, 1)
        milk_weight = round(random.random() * 1095) + 3512
        ph = round(random.random() * 0.4 + 6.8, 1)
        kplus = round(random.random() * 12) + 35
        nacl = round(random.random() * 0.7 + 1, 1)
        salmonella = round(random.random() * 20) + 17
        e_coli = round(random.random() * 14) + 35
        listeria = round(random.random() * 26) + 28
        self.set_infos(
            {
                "automat_type": self.type,
                "automat_number": self.number,
                "tank_temp": tank_temp,
                "ext_temp": ext_temp,
                "milk_weight": milk_weight,
                "ph": ph,
                "kplus": kplus,
                "nacl": nacl,
                "salmonella": salmonella,
                "e_coli": e_coli,
                "listeria": listeria
            }
        )
