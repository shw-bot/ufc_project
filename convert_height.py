# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 17:33:56 2023

@author: cinshalewolfe
"""

def convert_height(height):
    if height == "--":
        return None
    else:
        feet_inches = height.split("' ")
        if len(feet_inches) == 2:
            feet, inches = feet_inches
            total_inches = int(feet) * 12 + int(inches.strip('"'))
            return total_inches
        else:
            return None