import os
import nbformat
from nbconvert import PythonExporter

# Caminhos das pastas
PASTA_NOTEBOOKS = 'notebooks'
PASTA_SCRIPTS = 'scripts'

def converter_notebook_para_py(caminho_entrada, caminho_saida):
    with open(caminho_entrada, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    exporter = PythonExporter()
    script, _ = exporter.from_notebook_node(notebook)

    with open(caminho_saida, 'w', encoding='utf-8') as f:
        f.write(script)

    print(f"✅ Convertido: {caminho_entrada} -> {caminho_saida}")

def converter_todos():
    if not os.path.exists(PASTA_SCRIPTS):
        os.makedirs(PASTA_SCRIPTS)

    for arquivo in os.listdir(PASTA_NOTEBOOKS):
        if arquivo.endswith('.ipynb'):
            caminho_entrada = os.path.join(PASTA_NOTEBOOKS, arquivo)
            nome_saida = os.path.splitext(arquivo)[0] + '.py'
            caminho_saida = os.path.join(PASTA_SCRIPTS, nome_saida)
            converter_notebook_para_py(caminho_entrada, caminho_saida)

if __name__ == "__main__":
    converter_todos()
