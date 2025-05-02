# File to simulate stats for builds
import pandas as pd

base_df = pd.DataFrame(columns=['atk', 'crit_damage', 'total_dmg_bonus','total_pen_ratio'])
stats_data = base_df.copy()
stats_data.name = "big dataframe"

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

initial_atk = 1500
initial_crit_damage = 75

def atk_data(atk):
    current_atk = atk

    atk_data = []

    while (current_atk <= 4000):    
        # print("adding data to atk column:", current_atk)
        atk_data.append(current_atk)
        current_atk += 10

    new_rows = pd.Series(atk_data, name="atk")

    '''
    test_row = pd.Series({'atk': 1000,
                          'crit_damage': 100,
                          'total_dmg_bonus': 50,
                          'total_pen_ratio': 0})
    '''
    
    return new_rows

def crit_damage_data(crit_damage, atk_data):
    current_crit_dmg = crit_damage