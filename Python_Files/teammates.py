# Script for teammate specific buffs

class teammate:
    def __init__(self, name):
        self.name = name

class astra_yao(teammate):
    def __init__(self, name, atk_buff, dmg_buff, crit_dam_buff):
        super().__init__(name)
        
        self.atk_buff = atk_buff
        
        self.dmg_buff = dmg_buff
        self.crit_dam_buff = crit_dam_buff

class rina(teammate):
    def __init__(self, name, pen_buff):
        super().__init__(name)
        
        # Percentages
        self.pen_buff = pen_buff

class nicole(teammate):
    def __init__(self, name, def_shred, crit_rate_buff):
        super().__init__(name)
        
        # Percentages
        self.def_shred = def_shred
        self.crit_rate_buff = crit_rate_buff