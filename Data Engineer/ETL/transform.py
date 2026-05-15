# Import library
from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.window import Window

# definisikan spark untuk menjalankan pyspark
spark = SparkSession.builder.getOrCreate()

# definisikan lokasi file yang ingin dipakai
file_path = '/opt/airflow/data/extract_dataset_telco_churn.csv'

# load datasetnya
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Proses Transform

# Rename kolom
df = df.select(
    func.col('customerID').alias('customer_id'),
    func.col('gender'),
    func.col('SeniorCitizen').alias('senior_citizen'),
    func.col('Partner').alias('partner'),
    func.col('Dependents').alias('dependents'),
    func.col('tenure'),
    func.col('PaperlessBilling').alias('paperless_billing'),
    func.col('PaymentMethod').alias('payment_method'),
    func.col('MonthlyCharges').alias('monthly_charges'),
    func.col('TotalCharges').alias('total_charges'),
    func.col('Churn').alias('churn_status'),
    func.col('PhoneService').alias('phone_service'),
    func.col('MultipleLines').alias('multiple_lines'),
    func.col('InternetService').alias('internet_service'),
    func.col('OnlineSecurity').alias('online_security'),
    func.col('OnlineBackup').alias('online_backup'),
    func.col('DeviceProtection').alias('device_protection'),
    func.col('TechSupport').alias('tech_support'),
    func.col('StreamingTV').alias('streaming_tv'),
    func.col('StreamingMovies').alias('streaming_movies'),
    func.col('Contract').alias('contract')
)

# ubah string kosong menjadi 0 pada total_charges
df = df.withColumn('total_charges', 
                   func.when(func.col('total_charges') == ' ', 0)
                   .otherwise(func.col('total_charges'))
                   )

# isi missing value apda kolom total_charges
df = df.na.fill({'total_charges' : 0})

# ubah tipe data kolom total_charges
df = df.withColumn('total_charges', func.col('total_charges').cast('float'))

# ubah value yes no dari kolom churn_status menjadi 1 dan 0
df = df.withColumn('churn_status', func.when(func.col('churn_status') == 'Yes', 1).otherwise(0))


# Pembuatan Dim Table
# Dim Customer
dim_customer = df.select('customer_id', 'gender', 'senior_citizen', 'partner', 'dependents')

# DIm Service
dim_service = df.select('phone_service', 'multiple_lines', 'internet_service', 'online_security', 
                  'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 
                  'streaming_movies').distinct()

# membuat primary key untuk dim service
dim_service = dim_service.withColumn('service_id', func.row_number().over(
    Window.orderBy(func.monotonically_increasing_id())
))

# Dim Billing
dim_billing = df.select('paperless_billing', 'payment_method').distinct()

# membuat primary key untuk dim service
dim_billing = dim_billing.withColumn('billing_id', func.row_number().over(
    Window.orderBy(func.monotonically_increasing_id())
))

# Dim contract
dim_contract = df.select('contract').distinct()

# membuat primary key untuk dim contract
dim_contract = dim_contract.withColumn('contract_id', func.row_number().over(
    Window.orderBy(func.monotonically_increasing_id())
))


# Fact Table
# Join tabel dimensi ke tabel fact
fact_subscription = df.join(dim_billing, ["paperless_billing", "payment_method"]) \
                      .join(dim_contract, ['contract']) \
                      .join(dim_service, ['phone_service', 'multiple_lines', 'internet_service', 'online_security', 
                        'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies'])

# select kolom untuk fact table
fact_subscription = fact_subscription.select(
    'customer_id', 'contract_id', 'service_id', 'billing_id',
    'tenure', 'monthly_charges', 'total_charges', 'churn_status'
)

# membuat primary key untuk fact subscription
fact_subscription = fact_subscription.withColumn('subscription_id', func.row_number().over(
    Window.orderBy(func.monotonically_increasing_id())
))
    

# Export dim_customer sebagai csv
dim_customer.coalesce(1).write.csv('/opt/airflow/data/transform_dim_customer.csv', header=True, mode='overwrite')

# Export dim_service sebagai csv
dim_service.coalesce(1).write.csv('/opt/airflow/data/transform_dim_service.csv', header=True, mode='overwrite')

# Export dim_billing sebagai csv
dim_billing.coalesce(1).write.csv('/opt/airflow/data/transform_dim_billing.csv', header=True, mode='overwrite')

# Export dim_contract sebagai csv
dim_contract.coalesce(1).write.csv('/opt/airflow/data/transform_dim_contract.csv', header=True, mode='overwrite')

# Export fact_subscription sebagai csv
fact_subscription.coalesce(1).write.csv('/opt/airflow/data/transform_fact_subscription.csv', header=True, mode='overwrite')
