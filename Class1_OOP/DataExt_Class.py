import pandas as pd

class DataExt:

    def __init__(self, file_path:str):
        self.file_path=file_path

    def fetch_csv(self, separator:str):
        # write Custom Logic
        df=pd.read_csv(self.file_path, sep=separator)
        print(df.head())

    def fetch_json(self):
        # write Custom Logic
        df=pd.read_json(self.file_path)
        print(df.head())

    def fetch_parquet(self):
        # write Custom Logic
        df=pd.read_parquet(self.file_path)
        print(df.head())

    def fetch_text(self, separator:str):
        # write Custom Logic
        df=pd.read_csv(self.file_path,sep=separator)
        print(df.head())

obj=DataExt("D:\Project for Job\Python _Class\Baiscs\Class1_OOP\Files\orders.csv") # D:\Project for Job\Python _Class\Class1_OOP\Files\orders.csv
obj.fetch_csv(',')

#D:\Project for Job\Python _Class\Baiscs\Class1_OOP\Files\orders.csv

#print KJSON file
print("Parquet files")
#obj1=DataExt("Class1_OOP\Files\orders.parquet")
#obj1.fetch_parquet()
#obj1.fetch_text("\t")




#Class1_OOP\Files\orders.csv