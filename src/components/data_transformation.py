import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer        #used to create pipeline
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
import os

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts",'preprocessor.pkl')

class DataTransformer:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_trasnformer_obj(self):

        '''
        This is Responsible for data transformation
        '''

        try:
            numerical_columns = [
                "writing_score",
                "reading_score"
            ]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            logging.info('Numerical Column standard column Started')
            logging.info('Categorical Column encoding Started')

            numerical_pipeline = Pipeline(                  #order in which all the steps/components take place
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),        #handle missing values;median coz various outliers are present shown in EDA
                    ('scaler',StandardScaler(with_mean=False))             #scaling all values;instead of subtracting mean from all values which is resulting in negative values, features are scaled based on their variance
                ]
            )

            categorical_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy="most_frequent")),
                    ('one_hot_encoder',OneHotEncoder()),                     #ohe -> less no of categories in every cat. column
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor = ColumnTransformer(                       #combining both pipelines
                [
                    ('num_pipeline',numerical_pipeline,numerical_columns),
                    ('cat_pipeline',categorical_pipeline,categorical_columns)
                ]
            )

            return preprocessor


        except Exception as e:
            raise CustomException(e,sys)


    def initiate_data_transformation(self,train_path,test_path):            #both paths will be available from data ingestion

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Reading of Training and Test Data Completed')

            logging.info('Obtaining Preprocessing Object')

            preprocessing_object = self.get_data_trasnformer_obj()

            target_column_name = 'math_score'
            numerical_columns = [
                "writing_score",
                "reading_score"
            ]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr = preprocessing_object.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_object.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_object
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)