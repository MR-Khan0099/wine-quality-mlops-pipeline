# compare the schema with the data and write the status to a file
import pandas as pd
from src.DataScienceProject import logger
from src.DataScienceProject.entity.config_entity import (DataValidationConfig)



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self) -> bool:
        try:
            validate_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = data.columns
            all_schema = self.config.all_schema.keys()

            for col in all_columns:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}\n")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}\n") 

            return validation_status
        except Exception as e:
            raise e