import pandas as pd
import os

# --- PATH ---
absolute_path = os.getcwd()
train_data_file = '/../data/train.csv'
test_data_file = '/../data/test.csv'
# ------------

# --- EXTRACT TRAIN DATA ---
def extract_train_data():
    df = pd.read_csv(absolute_path + train_data_file)
    return df
# --------------------

# --- EXTRACT TEST DATA ---
def extract_test_data():
    df = pd.read_csv(absolute_path + test_data_file)
    return df
# -------------------------