from fastapi import FastAPI
import pandas as pd

app=FastAPI()
data=pd.read_csv(r'C:\Users\vs390\OneDrive\Desktop\customer_segmentation_projects\Data\customer_segment_data.csv')

total_customer=len(data)
  
segment_stats=data.groupby('segment').agg({
    'Monthly_Revenue':'mean',
    'CLTV':'mean',
    'Age':'mean',
    'Customer_ID':'count'
}).rename(columns={'Customer_ID':'customer_count'}).round(2)


