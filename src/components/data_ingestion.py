import sys
import os
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


#Saare file paths ek jagah rakhne ke liye i.e artifacts folder me 
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() #This line creates a configuration object and stores all data file paths so they can be used throughout the Data Ingestion class.
    
    def initiate_data_ingestion(self):
        logging.info("We Have Entered into the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Exported or read datasets as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            # above line extracts the artifacts folder from the file path and creates it if it doesn't already exist.
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            # above line saves the original dataset as data.csv in the artifacts folder for future use. 🚀
            logging.info("Train Test Split initiated")
            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        # We are returning the locations (paths) where the train and 
        # test datasets are stored, so that the next components can 
        # directly access and use those files.
        except Exception as e:
            raise CustomException(e,sys)
if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()
'''if __name__ == "__main__" is not required to run the file, 
but it prevents the code from running automatically when the 
file is imported into another module.
'''
