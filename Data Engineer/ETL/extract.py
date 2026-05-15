# Import Library yang dipakai
from pyspark.sql import SparkSession
import kagglehub
import os
import shutil

spark = SparkSession.builder.getOrCreate()

# download dataset dari kaggle
path = kagglehub.dataset_download("abbas829/telco-customer-churn-dataset")

# join path asli dari kaggle yaitu root dengan dataset yang dipakai
source = os.path.join(path, 'Telco-Customer-Churn.csv')

# Denifisikan path file yang diinginkan
file_path = '/opt/airflow/data/raw'

# Copy dataset dari root ke folder data
shutil.copy(source, file_path)

# Load Data
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Export dataset hasil extract sebagai folder
df.coalesce(1).write.csv('/opt/airflow/data/extract_dataset_telco_churn.csv', header=True, mode='overwrite')