import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path='artifacts/model.pkl'
            preprocessor_path='artifacts/preprocessor.pkl'
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        squareMeters: int,
        numberOfRooms: int,
        hasYard: int,
        hasPool: int,
        floors: int,
        cityCode: int,
        cityPartRange: int,
        numPrevOwners: int,
        made: int,
        isNewBuilt: int,
        hasStormProtector: int,
        basement: int,
        attic: int,
        garage: int,
        hasStorageRoom: int,
        hasGuestRoom: int,
        # price: float = None  # Optional, since this is the target variable
    ):
        self.squareMeters = squareMeters
        self.numberOfRooms = numberOfRooms
        self.hasYard = hasYard
        self.hasPool = hasPool
        self.floors = floors
        self.cityCode = cityCode
        self.cityPartRange = cityPartRange
        self.numPrevOwners = numPrevOwners
        self.made = made
        self.isNewBuilt = isNewBuilt
        self.hasStormProtector = hasStormProtector
        self.basement = basement
        self.attic = attic
        self.garage = garage
        self.hasStorageRoom = hasStorageRoom
        self.hasGuestRoom = hasGuestRoom
        # self.price = price  # Optional, as it's the target value

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
            "squareMeters": [self.squareMeters],
            "numberOfRooms": [self.numberOfRooms],
            "hasYard": [self.hasYard],
            "hasPool": [self.hasPool],
            "floors": [self.floors],
            "cityCode": [self.cityCode],
            "cityPartRange": [self.cityPartRange],
            "numPrevOwners": [self.numPrevOwners],
            "made": [self.made],
            "isNewBuilt": [self.isNewBuilt],
            "hasStormProtector": [self.hasStormProtector],
            "basement": [self.basement],
            "attic": [self.attic],
            "garage": [self.garage],
            "hasStorageRoom": [self.hasStorageRoom],
            "hasGuestRoom": [self.hasGuestRoom],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)