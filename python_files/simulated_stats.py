# File to simulate stats for builds

import pandas as pd

df = pd.DataFrame({'atk': [],
                   'crit_damage': [],
                   'crit_rate': [],
                   'ice_dmg_bonus': [],
                   'pen_ratio': []
                   })

'''
Baseline Stats
----------------------
Atk: 2500-3000
Crit Damage: 100%-150%
Crit Rate: Assume 100% (73% for M2 + Wengine)
Ice Damage Bonus: 0%
Pen Ratio: 0%
'''

## Functions to add data to dataframe 
def atk_scaling():
    print("hello world")