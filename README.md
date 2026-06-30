# 📊 Churn Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Google Looker Studio](https://img.shields.io/badge/Google%20Looker%20Studio-4285F4?style=for-the-badge&logo=googlelookerstudio&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![NeonDB](https://img.shields.io/badge/NeonDB-00E599?style=for-the-badge&logo=neon&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

This project focuses on Exploratory Data Analysis (EDA), data insight analysis, 
conversion rate evaluation, and data pipeline development.  
The goal of this project is to uncover meaningful insights from the data, 
track and analyze conversion rates, and automate the data workflow through 
a structured pipeline.  
This repository includes Python scripts that handle the ETL process, data 
transformation, exploratory analysis, and conversion rate reporting from 
end to end — with final results visualized using Google Looker Studio.

---

# 📑 Table of Contents

1. [Dataset Link](#-Table-of-Contents)
2. [Project Overview](#-project-overview)
3. [Methods Used](#️-Methods-Used)
4. [List File](#-List-File)
5. [Additional Operations](#-Additional-Operations)
6. [Libraries](#-libraries)
7. [Author](#-author)

---

# 🔗 Dataset Link

- [Telco Kaggle Dataset](https://www.kaggle.com/datasets/abbas829/telco-customer-churn-dataset/data)

---

# 📌 Project Overview

In this project, I used Python libraries such as Pandas to perform 
Exploratory Data Analysis (EDA) and data analysis, Apache Airflow to 
automate the ETL (Extract, Transform, Load) process, NeonDB as the 
database solution, and Google Looker Studio to create data visualization dashboards. 
Additionally, I conducted a business analysis to determine promotional 
targets by evaluating and comparing improvement rates across customer 
segments, enabling more strategic and data-driven decision-making for 
future campaigns.

## 1. Exploratory Data Analysis (EDA)

- Performing data exploration and analysis using Python libraries such as Pandas
to uncover patterns, trends, and insights from the data.

## 2. Business Analysis & Promotional Targeting

- Conducting business analysis to determine promotional targets by evaluating
and comparing improvement rates across customer segments, enabling more
strategic and data-driven decision-making for future campaigns.

## 3. Data Visualization

- Creating interactive and insightful data visualization dashboards using
Google Looker Studio to present findings in a clear and actionable format.

## 4. ETL Pipeline Development

- Building and automating the ETL (Extract, Transform, Load) process using
Apache Airflow to ensure a structured and efficient data workflow.

## 5. Database Management

- Utilizing NeonDB as the database solution to store, manage, and retrieve
data throughout the pipeline.

---

# ⚒️ Methods Used

- Exploratory Data Analysis (EDA)
- Business Analysis & Promotional Targeting with Improvement Rate
- Data Visualization
- ETL (Extract, Transform, Load) use Automation Workflow
- Database Management

---

# 📁 List File

## 1. Data Analyst

- `Churn_EDA_and_Business_Analysis.ipynb` : A Python script containing the steps for Exploratory Data Analysis (EDA) 
and business analysis.
- `Algoritma_Improvement_Rate.ipynb` : A Jupyter Notebook containing the algorithm to determine target customers 
for promotional campaigns based on improvement rate analysis.

## 2. Data Engineer

- `Data Modelling Folder` : Contains the data modelling schema images along 
with DDL scripts using SQL (PostgreSQL).
- `EDA & GX Folder` : Contains exploratory data analysis used for data 
validation with Great Expectations (GX).
- `ETL Folder` : Contains Python scripts for the Extract, Transform, and Load 
process, designed to be automated using Apache Airflow.

---

# 💻 Additional Operations

## 1. Open Apache Airflow in browser with docker

```text
http://localhost:8080
```

## 2. Run the DAG in Airflow to start the ETL process.

- Enable the DAG on the Airflow dashboard
- Click the **Trigger DAG** button

---

# 📚 Libraries

- Apache Airflow
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Great Expectations

---

# ✍️ Author

## Kurnia Surya

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/kurniasuryab/)

---
