import numpy as np
import pandas as pd
import argparse

def clean_csv(file):
    df = pd.read_csv(args.file)
    df['neck'].fillna(df['neck'].mode()[0], inplace=True)
    df['pattern'].fillna(df['pattern'].mode()[0], inplace=True)
    df['sleeve_length'].fillna(df['sleeve_length'].mode()[0], inplace=True)
    neck_hot = pd.get_dummies(data['neck'].astype(int), prefix='neck')
    sleeve_hot = pd.get_dummies(data['sleeve_length'].astype(int), prefix='sleeve length')
    pattern_hot = pd.get_dummies(data['pattern'].astype(int), prefix='pattern')
    result = pd.concat([data, neck_hot, sleeve_hot, pattern_hot], axis=1, join="inner")
    result = result.drop(['neck', 'sleeve_length', 'pattern'], axis=1)
    return result
