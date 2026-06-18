def pandas_decorator(fx):
    def mainfunc(*args):
        response=fx(*args)
        # Pandas specific processing here
        response.to_parquet("temp.parquet")
        return response
    
    return mainfunc

@pandas_decorator
def csv_to_parquet(file_path:str):
    import pandas as pd
    df=pd.read_csv(file_path)
    return df

rep=csv_to_parquet("Class3_Polymorphism&Decorators\\orders.csv")
print(rep.head())

#  Class3_Polymorphism&Decorators\orders.csv