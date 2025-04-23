import pandas as pd

from teammates import *

# Source of damage formula:
# https://zenless-zone-zero.fandom.com/wiki/Damage

# Access dataframe for build stats
builds = pd.read_csv('builds.csv')

# Initialize classes
# Variables: Name, Atk Buff, Dmg % Buff, Crit Damage Buff
astra_yao = astra_yao(astra_yao, 1200, 20, 20)
# Name, Pen Ratio Buff
rina = rina(rina, 27.6)
# Name, Def Shred, Crit Rate Buff
nicole = nicole(nicole, 40, 15)

'''
Initialize variables for calculations
'''
base_dmg = dmg_bonus_multi = crit_multi = 0

def_multi = res_multi = 0

dmg_taken_multi = stunned_multi = 150

dmg_standard = 0

