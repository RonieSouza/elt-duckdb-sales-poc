from pathlib import Path
import duckdb

base_path = Path().resolve() / "data"
source_path = base_path / "source/sales.csv"
bronze_path = base_path / "bronze/sales.parquet"

duckdb.sql(f'''
            copy (select * from "{source_path}")
            to "{bronze_path}";
''')