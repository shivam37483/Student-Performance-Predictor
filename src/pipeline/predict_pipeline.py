import sys
import pandas as pd

from src.exception import CustomException
from src.utils import load_object

class CustomData:                               #responsible for mapping all the inputs we are giving in html to backend with its values
    def __init__( self,
                gender: str,
                race_ethnicity: str,                                       #THese values are coming from name -> home.html
                parental_level_of_education,
                lunch: str,
                test_preparation_course: str,
                reading_score: int,
                writing_score: int):

        self.gender = gender
        self.race_ethinicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_input_as_data_frame(self):                      #we train our model with dataframe
        try: 
            custom_input_data_dict = {                              #mapping all the inputs to newly dict -> dataframe
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethinicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }

            return pd.DataFrame(custom_input_data_dict)
        
        except Exception as e:
            raise CustomException(e,sys)


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path = "artifacts\model.pkl"
            preprocessor_path = "artifacts\preprocessor.pkl"                      #REsponsible hadling all categorical features,feature scaling
    
            model = load_object(file_path=model_path)                #loading pkl file
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)

            preds = model.predict(data_scaled)

            return preds

        except Exception as e:
            raise CustomException(e,sys)



