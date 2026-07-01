import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object
from src.utils import evaluate_models

from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestionConfig

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationconfig

@dataclass
class ModelTrainerConfig:
    trained_model_filepath=os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    def initiate_modeltrainer(self,training_array,testing_array,preprocessor_path):
        try:
            logging.info("Splitting of train and test data")
            x_train,y_train,x_test,y_test=(
                training_array[ :,:-1],
                training_array[:,-1],
                testing_array[:,:-1],
                testing_array[:,-1]
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            model_report=evaluate_models(X_train=x_train,y_train=y_train,X_test=x_test,y_test=y_test,models=models)
            best_model_score=max(list(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            if best_model_score<0.6:
                raise CustomException("NO BEST MODEL FOUND")
            logging.info("Best model has been selected based on r2 score")

            save_object(

                file_path=self.model_trainer_config.trained_model_filepath,
                obj=best_model
            )
            predicted=best_model.predict(x_test)

            r2score=r2_score(y_test,predicted)

            return r2score

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=='__main__':
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    obj2=DataTransformation()
    train_arr,test_arr,_=obj2.initiate_data_transformation(train_data,test_data)

    obj3=ModelTrainer()
    obj3.initiate_modeltrainer(train_arr,test_arr,_)
