import json
import pickle

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations

def getArtficats():
    global __data_columns
    global __locations

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_cols']
        __locations = __data_columns[3:]

    with open('./artifacts/realestatepricesmodel.pickle', 'rb') as f:
        __model = pickle.load(f)
    



if __name__ == '__main__':
    getArtficats()
    print(get_location_names())