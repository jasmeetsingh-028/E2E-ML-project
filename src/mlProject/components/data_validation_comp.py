import pandas as pd
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig



class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self):
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            check = False


            all_schema = self.config.all_schema.keys()
            print('CHECK')

            for col, check_col in zip(all_cols, all_schema):
                #print(col, check_col, str(data.dtypes[col]), self.config.all_schema[check_col])
                if col == check_col and str(data.dtypes[col] == self.config.all_schema[check_col]):
                    check = True
                else:
                    check = False
                    
            print(check)

            if check:
                 validation_status = 'Successful'
                 with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            else:
                 validation_status = 'Unsuccessful'
                 with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
        
        
        except Exception as e:
            raise e