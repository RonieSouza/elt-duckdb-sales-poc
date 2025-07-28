import subprocess
import os

scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')

script_order = [
    "source_to_bronze.py",
    "bronze_to_silver.py",
    "silver_to_gold.py"
]

for script in script_order:
    script_path = os.path.join(scripts_dir, script)
    print(f"Executando: {script_path}")
    subprocess.run(["python", script_path], check=True)