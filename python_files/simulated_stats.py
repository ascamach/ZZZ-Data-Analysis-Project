# File to simulate stats for builds
import pandas as pd

df = pd.DataFrame({'atk': [],
                   'crit_damage': [],
                   'crit_rate': [],
                   'ice_dmg_bonus': [],
                   'pen_ratio': []
                   })

df.name = "test"

df2 = pd.DataFrame(columns=['atk', 'crit_damage','crit_rate','ice_dmg_bonus','pen_ratio'])

df2.name = "not test"

df3 = pd.DataFrame({'a': [1, 2 , 3],
                    'b': [4, 5, 6]
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

initial_atk = 1000

def data_test_populate(dataframe):
    dataframe._append({'atk': 1}, ignore_index=True)

def data_population(dataframe):

    print("Accessing dataframe:", dataframe.name)
    current_atk = initial_atk

    new_data = []

    while (current_atk != 1100):    
        # print("adding data to atk column:", current_atk)
        new_data.append(current_atk)
        current_atk += 10

    print(new_data)
    new_rows = pd.Series(new_data, name="atk")

    dataframe['atk'] = new_rows.values

    return

data_population(df)
print(df)