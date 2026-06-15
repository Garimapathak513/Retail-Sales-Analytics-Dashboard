import pandas as pd
from sqlalchemy import create_engine


username = "root"
password = "your_password"
host = "localhost"
database = "ccdb"


engine = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
)


customers_df = pd.read_excel("Customers.xlsx")
products_df = pd.read_excel("Products.xlsx")
stores_df = pd.read_excel("Stores.xlsx")
employees_df = pd.read_excel("Employees.xlsx")
sales_df = pd.read_excel("Sales.xlsx")


customers_df.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)


products_df.to_sql(
    "products",
    engine,
    if_exists="replace",
    index=False
)


stores_df.to_sql(
    "stores",
    engine,
    if_exists="replace",
    index=False
)


employees_df.to_sql(
    "employees",
    engine,
    if_exists="replace",
    index=False
)


sales_df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)


print("Data uploaded successfully")
