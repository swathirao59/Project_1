# -*- coding: utf-8 -*-
"""
Created on Wed May 15 00:35:45 2024

@author: swath
"""

from pydantic import BaseModel

class BirdFlu(BaseModel):
    Scientific_Name: int
    Common_Name: int
    Date: int
    Year: int
    Month: int
    Day: int
    Time: int
    Country: int
    Country_State_County: int
    State: int
    County: int
    Locality: int
    Latitude: float
    Longitude: float
    Parent_Species: int