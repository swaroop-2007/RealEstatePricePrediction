import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def getArtficats():
    global __data_columns
    global __locations
    global __model

    # Check if the artifacts have already been loaded to avoid redundant loading
    if __data_columns is None or __locations is None or __model is None:
        print("Loading artifacts...")

        with open('./artifacts/columns.json', 'r') as f:
            __data_columns = json.load(f)['data_cols']
            __locations = __data_columns[3:]

        with open('./artifacts/realestatepricesmodel.pickle', 'rb') as f:
            __model = pickle.load(f)
    else:
        print("Artifacts already loaded.")


def get_location_names():
    # Ensure that the artifacts are loaded before returning locations
    getArtficats()
    return __locations

def getPrice(location, sqft, bedrooms, bath):
    # Ensure that the artifacts are loaded before calculating price
    getArtficats()

    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bedrooms
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


if __name__ == '__main__':
    getArtficats()
    print(get_location_names())
    print(getPrice('1st Phase JP Nagar', 1000, 3, 3))
