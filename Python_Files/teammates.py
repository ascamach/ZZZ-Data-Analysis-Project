# Script for teammate specific buffs

class teammate:
    def __init__(self, name):
        self.name = name

class astra_yao(teammate):
    def __init__(self, atk_buff, dmg_buff, cdam_buff):
        super().__init__()
        self.name = astra_yao
        # Flat numbers
        self.atk_buff = 1000

        # Percentages
        self.dmg_buff = 20
        self.cdam_buff = 20

class rina(teammate):
    def __init__(self, pen_buff):
        super().__init__()
        self.name = rina
        # Percentages
        self.pen_buff = 27.6

class nicole(teammate):
    def __init__(self, def_shred, crate_buff):
        super().__init__()
        self.name = nicole
        # Percentages
        self.def_shred = 40
        self.crate_buff = 15