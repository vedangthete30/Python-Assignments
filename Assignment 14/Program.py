import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def PlayPredictor(file):

    # Step 1 - Load the data

    data = pd.read_csv(file,index_col=0)
    print("Size of the dataset is :",len(data))

    # Step 2 - Clean,Prepare & manipulate the data

    feature_names = ["Weather","Temperature"]
    print("Features are : ",feature_names)

    weather = data.Weather
    temperature = data.Temperature
    play = data.Play

    # Create LabelEncoder
    le = preprocessing.LabelEncoder()

    # Convert string labels into numbers
    weather_encoded = le.fit_transform(weather)
    print(weather_encoded)

    temperature_encoded = le.fit_transform(temperature)
    print(temperature_encoded)

    label = le.fit_transform(play)

    # Combine weather and temperature into single list of tuples
    features = list(zip(weather_encoded,temperature_encoded))

    # Step 3 - Train the data

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(features,label)

    # Step 4 - Test the data
    predicted = model.predict([[0,2]])
    print(predicted)

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()