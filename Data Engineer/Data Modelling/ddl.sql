-- ddl
-- dim_customer table
create table dim_customer(
	customer_id text primary key,
	gender text,
	senior_citizen int,
	partner text,
	dependents text
);

-- create dim_billing table
create table dim_billing(
	billing_id serial primary key,
	paperless_billing text,
	payment_method text
);

-- create dim_contract table
create table dim_contract(
	contract_id serial primary key,
	contract text
);

-- create dim_service table
create table dim_service(
	service_id serial primary key,
	phone_service text,
    multiple_lines text,
    internet_service text,
    online_security text,
    online_backup text,
    device_protection text,
    tech_support text,
    streaming_tv text,
    streaming_movies text
);

-- create fact_subscription table
create table fact_subscription(
	subscription_id serial primary key,
	customer_id text references dim_customer(customer_id),
	contract_id int references dim_contract(contract_id),
	service_id int references dim_service(service_id),
    billing_id int references dim_billing(billing_id),
	tenure int,
	monthly_charges numeric(10,2),
	total_charges numeric(10,2),
    churn_status int
);

-- for dashboard uses
  create table raw_data(
    customerID text primary KEY,
    gender text,
    SeniorCitizen int,
    Partner text,
    Dependents text,
    tenure int,
    PhoneService text,
    MultipleLines text,
    InternetService text,
    OnlineSecurity text,
    OnlineBackup text,
    DeviceProtection text,
    TechSupport text,
    StreamingTV text,
    StreamingMovies text,
    Contract text,
    PaperlessBilling text,
    PaymentMethod text,
    MonthlyCharges float,
    TotalCharges float,
    Churn  text
  );