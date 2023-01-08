from constants import RESOLUTION
from func_utils import get_ISO_times
import pandas as pd
import numpy as np
from pprint import pprint
import time


#Get relevant time periods for iso from an to
ISO_TIMES = get_ISO_times()

pprint(ISO_TIMES)

#Construct market prices
def construct_market_prices(client):
    pass