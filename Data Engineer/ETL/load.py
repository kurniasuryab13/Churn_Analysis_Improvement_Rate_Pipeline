import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv

load_dotenv()

spark = SparkSession.builder \
    .appName("final_project") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.2") \
    .getOrCreate() #spark initiation

conn = os.getenv("DB_URL") # built .env file to insert the url
neon_properties = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "driver": "org.postgresql.Driver",
    "ssl": "true",
    "sslmode": "require"
}


# inisiasi folder tempat data hasil transform
dim_customer_path = '/opt/airflow/data/transform_dim_customer.csv'
dim_service_path = '/opt/airflow/data/transform_dim_service.csv'
dim_billing_path = '/opt/airflow/data/transform_dim_billing.csv'
dim_contract_path = '/opt/airflow/data/transform_dim_contract.csv'
fact_subscription_path = '/opt/airflow/data/transform_fact_subscription.csv'

# inisiasi driver
driver = "org.postgresql.Driver"

# Load data menggunakan spark
dim_customer = spark.read.csv(dim_customer_path, header = True, inferSchema = True)
dim_service = spark.read.csv(dim_service_path, header = True, inferSchema = True)
dim_billing = spark.read.csv(dim_billing_path, header = True, inferSchema = True)
dim_contract = spark.read.csv(dim_contract_path, header = True, inferSchema = True)
fact_subscription = spark.read.csv(fact_subscription_path, header = True, inferSchema = True)

# Load data ke dalam database
dim_customer.write.jdbc(url=conn, table="dim_customer", mode="append", properties=neon_properties)
dim_service.write.jdbc(url=conn, table="dim_service", mode="append", properties=neon_properties)
dim_billing.write.jdbc(url=conn, table="dim_billing", mode="append", properties=neon_properties)
dim_contract.write.jdbc(url=conn, table="dim_contract", mode="append", properties=neon_properties)
fact_subscription.write.jdbc(url=conn, table="fact_subscription", mode="append", properties=neon_properties)