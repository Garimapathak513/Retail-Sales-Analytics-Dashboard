import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta


fake = Faker()

# ---------------------------
# 1. Customers Table
# ---------------------------

customers = []

for i in range(1, 501):
    customers.append([
        i,
        fake.name(),
        fake.email(),
        random.choice(["Delhi","Mumbai","Pune","Bangalore","Chennai"]),
        random.choice(["Male","Female"]),
        random.randint(20,60)
    ])


customers_df = pd.DataFrame(
    customers,
    columns=[
        "Customer_ID",
        "Customer_Name",
        "Email",
        "City",
        "Gender",
        "Age"
    ]
)


# ---------------------------
# 2. Products Table
# ---------------------------

products=[]

categories = {
    "Electronics":["Laptop","Mobile","Tablet","Headphone"],
    "Furniture":["Chair","Table","Sofa"],
    "Clothing":["Shirt","Jeans","Jacket"],
    "Grocery":["Rice","Oil","Snacks"]
}


pid=1

for cat,items in categories.items():

    for item in items:

        products.append([
            pid,
            item,
            cat,
            random.randint(500,50000),
            random.randint(5,100)
        ])

        pid+=1



products_df=pd.DataFrame(
    products,
    columns=[
        "Product_ID",
        "Product_Name",
        "Category",
        "Price",
        "Stock"
    ]
)



# ---------------------------
# 3. Stores Table
# ---------------------------


stores=[]

for i in range(1,21):

    stores.append([
        i,
        "Store_"+str(i),
        random.choice(
            ["Delhi","Mumbai","Pune","Bangalore"]
        ),
        random.choice(
            ["North","South","West"]
        )
    ])


stores_df=pd.DataFrame(
    stores,
    columns=[
        "Store_ID",
        "Store_Name",
        "City",
        "Region"
    ]
)




# ---------------------------
# 4. Employees Table
# ---------------------------


employees=[]

for i in range(1,51):

    employees.append([
        i,
        fake.name(),
        random.choice(
            ["Sales","Manager","Support"]
        ),
        random.randint(20000,80000)
    ])



employees_df=pd.DataFrame(
    employees,
    columns=[
        "Employee_ID",
        "Employee_Name",
        "Department",
        "Salary"
    ]
)



# ---------------------------
# 5. Sales Fact Table
# ---------------------------


sales=[]


start_date=datetime(2024,1,1)


for i in range(1,10001):

    product=random.choice(products_df.Product_ID.tolist())

    qty=random.randint(1,10)


    price=int(
        products_df[
            products_df.Product_ID==product
        ].Price
    )


    sales.append([

        i,

        random.randint(
            1,500
        ),

        product,

        random.randint(
            1,20
        ),

        random.randint(
            1,50
        ),

        random.randint(
            1,20
        ),

        start_date + timedelta(
            days=random.randint(0,730)
        ),

        qty,

        qty*price

    ])



sales_df=pd.DataFrame(
    sales,
    columns=[
        "Sales_ID",
        "Customer_ID",
        "Product_ID",
        "Store_ID",
        "Employee_ID",
        "Order_ID",
        "Order_Date",
        "Quantity",
        "Revenue"
    ]
)



# ---------------------------
# Save Excel files
# ---------------------------


customers_df.to_excel(
    "Customers.xlsx",
    index=False
)

products_df.to_excel(
    "Products.xlsx",
    index=False
)

stores_df.to_excel(
    "Stores.xlsx",
    index=False
)

employees_df.to_excel(
    "Employees.xlsx",
    index=False
)

sales_df.to_excel(
    "Sales.xlsx",
    index=False
)



print("5 Power BI tables generated successfully!")
