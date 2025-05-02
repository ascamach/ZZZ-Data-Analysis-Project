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
base_dmg = dmg_bonus = crit_multi = 0
def_multi = res_multi = 0
dmg_taken_multi = 0
stunned_multi = 150
dmg_standard = 0

def base_dmg_calc(ability_multi, atk):
    base_dmg = ability_multi * atk
    return base_dmg

def total_dmg_bonus(dmg_bonus):
    return dmg_bonus + 1

def total_crit_multiplier(crit_damage, crit_rate):
    total_crit = 1 + crit_damage
    average_crit = 1 + (crit_rate * crit_damage)

    return total_crit, average_crit

def defense_multiplier(pen_ratio, total_pen):
    # Level Factor, defense of the enemy at specific levels
    # Level factor at 60+ is 794
    level_factor = 794

    # Defense Value
    # At level 1, starts between 36-60, then follows the same growth pattern as Level Factor
    # Refer to the 'def_growth_pattern.md'
    # Total Value Increase at level 60+: 710
    defense_value = 710

    def_multi = (level_factor) / ((max(defense_value * (1-pen_ratio)-total_pen),0) + level_factor)

    return def_multi

def res_multi(res_ignore, effectiveness):
    # Variables depending on weaknesses and resistances of the enemy target
    res_reduction = 0.8
    res_effective = 1.2

    # Effectiveness is based on if the target has appropriate weakness
    # If the typing is neutral, there is no res variables used

    if (effectiveness == "effective") :
        return res_effective + res_ignore
    elif (effectiveness == "non_effective"):
        return res_reduction + res_ignore
    else:
        return 1 + res_ignore

# This function takes into consideration damage taken and damage taken reduced buffs/debuffs from bosses
# We can safely ignore this when doing our calculations, but keeping this function for reference
def dmg_taken(dmg_taken_increase, dmg_taken_decrease):
    dmg_taken_multi = 1 + dmg_taken_increase - dmg_taken_decrease

    return dmg_taken_multi

def stunned_multi(damage_dealt, stunned_multiplier):
    return damage_dealt * stunned_multiplier