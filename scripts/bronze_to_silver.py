#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pathlib import Path
import duckdb


# In[ ]:


base_path = Path().resolve() / "data"
bronze_path = base_path / "bronze/sales.parquet"
silver_path = base_path / "silver"


# In[8]:


duckdb.sql(f'''
        copy
            (
                select distinct
                    Product_ID                  as product_id
                    , trim(Product_Category)    as product_category
                from
                    "{bronze_path}"
            )
        to "{silver_path}/product.parquet"
''')


# In[9]:


duckdb.sql(f'''
        copy
            (
                select distinct
                    trim(Sales_Rep)    as representative
                from
                    "{bronze_path}"
            )
        to "{silver_path}/representative.parquet"
''')


# In[10]:


duckdb.sql(f'''
        copy
            (
                select distinct
                    trim(Region)    as region
                from
                    "{bronze_path}"
            )
        to "{silver_path}/region.parquet"
''')


# In[32]:


duckdb.sql(f'''
        copy
            (
                select distinct
                    trim(Customer_Type)    as customer_type
                from
                    "{bronze_path}"
            )
        to "{silver_path}/customer_type.parquet"
''')


# In[12]:


duckdb.sql(f'''
        copy
            (
                select distinct
                    trim(Payment_Method)    as payment_method
                from
                    "{bronze_path}"
            )
        to "{silver_path}/payment_method.parquet"
''')


# In[13]:


duckdb.sql(f'''
        copy
            (
                select distinct
                    trim(Sales_Channel)    as sales_channel
                from
                    "{bronze_path}"
            )
        to "{silver_path}/sales_channel.parquet"
''')


# In[18]:


duckdb.sql(f'''
        copy
            (
                select distinct
                    Product_ID                as product_id
                    , Sale_Date               as sales_date
                    , trim(Sales_Rep)         as representative
                    , trim(Region)            as region
                    , Sales_Amount            as sales_amount
                    , Quantity_Sold           as quantity_sold
                    , trim(Product_Category)  as product_category
                    , Unit_Cost               as unit_cost
                    , Unit_Price              as unit_price
                    , trim(Customer_Type)     as customer_type
                    , Discount                as discount
                    , trim(Payment_Method)    as payment_method
                    , trim(Sales_Channel)     as sales_channel
                from
                    "{bronze_path}"
            )
        to "{silver_path}/sales.parquet"
''')

