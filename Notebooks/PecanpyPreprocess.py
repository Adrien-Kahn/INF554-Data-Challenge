# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 00:18:55 2021

@author: adrie
"""
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from pecanpy import node2vec
from time import time

g = node2vec.PreComp(p=1, q=1, workers=2, verbose=True)
print("Object built")

g.read_edg('../Data/coauthorship_tab.edgelist', weighted=False, directed=False)
print("Graph read")

g.preprocess_transition_probs()
print("Preprocessed Transitions")