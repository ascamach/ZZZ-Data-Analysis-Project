import pandas as pd

from teammates import *

# Source of damage formula:
# https://zenless-zone-zero.fandom.com/wiki/Damage

# Access dataframe for build stats
builds = pd.read_csv('builds.csv')

# Initialize classes
astra = astra_yao()
rina = rina()
nicole = nicole()

'''
Initialize variables for calculations
'''
base_dmg = dmg_bonus_multi = crit_multi = 0

def_multi = res_multi = 0

dmg_taken_multi = stunned_multi = 150

dmg_standard = 0

