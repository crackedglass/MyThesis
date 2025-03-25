import kagglehub
import pandas as pd

def load_dataset():
    path = kagglehub.dataset_download("hetulmehta/website-classification")
    
    df = pd.read_csv(path + '/website_classification.csv')
    df = df[df["Category"] != "Adult"]
    return df