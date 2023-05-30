import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataingestionConfig:
    train_data_path:str=os.path.join("artifacts","train.csv") #it will save the train data into artifacts folder with naim train.csv
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","raw.csv")

class Dataingestion:
    def __init__(self):
        self.ingestion_config=DataingestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the Data ingestion method or component") # it will show in to the logging, it is used only for logging


        try:
            df=pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as data frame")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #jar ka path exist kels tar to ok aahe navin create karaichi garaj nai

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test split Initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=Dataingestion()
    obj.initiate_data_ingestion()
