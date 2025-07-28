#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
import duckdb


# In[ ]:


base_path = Path().resolve() / "data"
silver_path = base_path / "silver"
gold_path = base_path / "gold"


# In[ ]:


duckdb.sql(f'''
        copy
           (
                select 
                    0                   as sk_product
                    , NULL              as product_id
                    , 'Não Encontrado'  as product_category

                union all

                select
                    row_number() over(order by product_id) as sk_product
                    , product_id
                    , product_category
                from
                    "{silver_path}/product.parquet"
            )
        to "{gold_path}/dim_product.parquet"
''')


# In[128]:


duckdb.sql(f'''
        copy
           (
                select 
                    0                   as sk_customer_type
                    , 'Não Encontrado'  as customer_type

                union all

                select
                    row_number() over(order by customer_type) as sk_customer_type
                    , customer_type
                from
                    "{silver_path}/customer_type.parquet"
            )
        to "{gold_path}/dim_customer_type.parquet"
''')


# In[ ]:


duckdb.sql(f'''
        copy
           (
                select 
                    0                   as sk_payment_method
                    , 'Não Encontrado'  as payment_method

                union all

                select
                    row_number() over(order by payment_method) as sk_payment_method
                    , payment_method
                from
                    "{silver_path}/payment_method.parquet"
            )
        to "{gold_path}/dim_payment_method.parquet"
''')


# In[52]:


duckdb.sql(f'''
        copy
           (
                select 
                    0                   as sk_region
                    , 'Não Encontrado'  as region

                union all

                select
                    row_number() over(order by region) as sk_region
                    , region
                from
                    "{silver_path}/region.parquet"
            )
        to "{gold_path}/dim_region.parquet"
''')


# In[67]:


duckdb.sql(f'''
        copy
           (
                select 
                    0                   as sk_representative
                    , 'Não Encontrado'  as representative

                union all

                select
                    row_number() over(order by representative) as sk_representative
                    , representative
                from
                    "{silver_path}/representative.parquet"
            )
        to "{gold_path}/dim_representative.parquet"
''')


# In[ ]:


duckdb.sql(f'''
        copy
           (
                select 
                    0                   as sk_sales_channel
                    , 'Não Encontrado'  as sales_channel

                union all

                select
                    row_number() over(order by sales_channel) as sk_sales_channel
                    , sales_channel
                from
                    "{silver_path}/sales_channel.parquet"
            )
        to "{gold_path}/dim_sales_channel.parquet"
''')


# In[103]:


duckdb.sql(f'''
        copy 
           (
                WITH unique_dates AS (
                    SELECT DISTINCT
                        sales_date
                    FROM
                        '{silver_path}/sales.parquet'
                )
                SELECT
                    CAST(STRFTIME(sales_date, '%Y%m%d') AS INTEGER)                               AS sk_date
                    , sales_date                                                                  AS date
                    , EXTRACT(YEAR FROM sales_date)                                               AS year
                    , EXTRACT(MONTH FROM sales_date)                                              AS month
                    , STRFTIME(sales_date, '%m')                                                  AS month_number
                    , STRFTIME(sales_date, '%B')                                                  AS month_name
                    , EXTRACT(DAY FROM sales_date)                                                AS day
                    , STRFTIME(sales_date, '%w')                                                  AS weekday_number
                    , STRFTIME(sales_date, '%A')                                                  AS weekday_name
                    , STRFTIME(sales_date, '%Y%m')                                                AS year_month
                    , STRFTIME(sales_date, '%b/%y')                                               AS month_year
                    , CASE WHEN STRFTIME(sales_date, '%w') IN ('0', '6') THEN TRUE ELSE FALSE END AS is_weekend
                FROM
                    unique_dates
                ORDER BY
                    sk_date
            )
        to "{gold_path}/dim_date.parquet"     
''')


# In[141]:


duckdb.sql(f'''
            copy
                (
                    select
                        sk_product
                        , sk_date
                        , sk_representative
                        , sk_region
                        , sk_customer_type
                        , sk_payment_method
                        , sk_sales_channel
                    from
                        "{silver_path}/sales.parquet" as sal
                        left join
                            "{gold_path}/dim_product.parquet" as prod
                            on prod.product_id = sal.product_id
                            and prod.product_category = sal.product_category
                        left join
                            "{gold_path}/dim_date.parquet" as dat
                            on dat.date = sal.sales_date
                        left join
                            "{gold_path}/dim_representative.parquet" as rep
                            on rep.representative = sal.representative
                        left join
                            "{gold_path}/dim_region.parquet" as reg
                            on reg.region = sal.region
                        left join
                            "{gold_path}/dim_customer_type.parquet" as cust
                            on cust.customer_type = sal.customer_type
                        left join
                            "{gold_path}/dim_payment_method.parquet" as pay
                            on pay.payment_method = sal.payment_method
                        left join
                            "{gold_path}/dim_sales_channel.parquet" as sc
                            on sc.sales_channel = sal.sales_channel
                )
            to "{gold_path}/fact_sales.parquet"     
           '''
)

