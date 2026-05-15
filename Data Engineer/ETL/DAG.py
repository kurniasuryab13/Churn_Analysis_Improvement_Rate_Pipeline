# import library
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': '<owner>', # inisiasi pemilik DAG
    'start_date': dt.datetime(2026, 5, 1), # inisasi kapan DAG aktif
    'retries': 1, # inisiasi berapa kali jumlah pengulangan jika terjadi fail
    'retry_delay': dt.timedelta(minutes=10), # inisiasi berapa menit jeda sebelum retry terjadi
}


with DAG('project', # Nama DAG
         default_args=default_args, # konfigurasi task DAG
         schedule_interval='0 0 1 1-12 *', # Jadwal DAG yaitu menit ke setiap jam 00.00 tanggal 1 setiap bulan
         catchup=False, # jalankan task dari awal mulai hingga seterusnya
         ) as dag:

    # Jalankan proses extract dengan menjalankan script extract.py
    python_extract = BashOperator(task_id='python_extract', bash_command='sudo -u airflow python /opt/airflow/scripts/extract.py')

    # Jalankan proses transform dengan menjalankan script transform.py
    python_transform = BashOperator(task_id='python_transform', bash_command='sudo -u airflow python /opt/airflow/scripts/transform.py')
    
    # Jalankan proses load dengan menjalankan script load.py
    python_load = BashOperator(task_id='python_load', bash_command='sudo -u airflow python /opt/airflow/scripts/load.py')
    
# Tentukan urutan task
python_extract >> python_transform >> python_load