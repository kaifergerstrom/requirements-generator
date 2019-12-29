import spotipy, pickle, os, graphviz, pydotplus, io, imageio, argparse
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from spotipy.oauth2 import SpotifyClientCredentials
from scipy import misc