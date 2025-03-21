import os
import subprocess
from agents import function_tool

base_path = "/Users/nelson.frugeri/SoftwareDevelopment/workoutspace/artificial_intelligence/test-pilot"


@function_tool
def execute_command(command: str) -> str:
    """
    Executa um comando no terminal e retorna a saída.

    Args:
        command (str): O comando a ser executado.

    Returns:
        str: A saída do comando ou uma mensagem de erro, caso falhe.
    """
    try:
        command = f"cd {base_path} && {command}"
        print("execute_command | Comando recebido:", command)
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=120
        )
        if result.returncode == 0:
            print("execute_command | Comando executado com sucesso:", result.stdout)
            return f"Comando executado com sucesso:\n{result.stdout}"

        print("execute_command | Erro ao executar o comando:", result.stderr)
        return f"Erro ao executar o comando:\n{result.stderr}"
    except Exception as e:
        print("execute_command | Erro inesperado ao executar o comando:", str(e))
        return f"Erro inesperado ao executar o comando: {str(e)}"


# Função para escrever informações em um arquivo
@function_tool
def write_to_file(path: str, content: str) -> str:
    """
    Escreve o conteúdo textual no arquivo especificado.

    Args:
        path (str): O caminho do arquivo onde o texto será salvo.
        content (str): O conteúdo a ser escrito no arquivo.

    Returns:
        str: Confirmação de que o conteúdo foi salvo com sucesso.
    """
    try:
        full_path = f"{base_path}/{path}"
        print("write_to_file | Escrevendo no arquivo:", full_path)
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(content)
        print("write_to_file | Texto escrito com sucesso no arquivo:", full_path)
        return f"Texto escrito com sucesso no arquivo: {full_path}"
    except Exception as e:
        print("write_to_file | Erro ao escrever no arquivo:", str(e))
        return f"Erro ao escrever no arquivo: {str(e)}"


@function_tool
def list_directory_tree() -> str:
    """
    Lista a estrutura de diretórios e arquivos de forma recursiva a partir de um caminho especificado.

    Args:
        path (str): O caminho do diretório raiz.

    Returns:
        str: A estrutura da árvore de diretórios e arquivos.
    """
    try:
        tree_structure = []
        for root, dirs, files in os.walk(base_path):         
            # Ignorar o diretório venv
            dirs[:] = [d for d in dirs if d != 'venv']   
            level = root.replace(base_path, "").count(os.sep)
            indent = " " * 4 * level
            tree_structure.append(f"{indent}{os.path.basename(root)}/")
            sub_indent = " " * 4 * (level + 1)
            for d in dirs:
                print(f"list_directory_tree | dir {d}")
                tree_structure.append(f"{sub_indent}{d}/")
            for f in files:
                print(f"list_directory_tree | file {f}")
                tree_structure.append(f"{sub_indent}{f}")
        print(f"Arvere de diretórios {"\n".join(tree_structure)}")
        return "\n".join(tree_structure)
    except Exception as e:
        print("list_directory_tree | Erro ao listar a estrutura de diretórios:", str(e))
        return f"Erro ao listar a estrutura de diretórios: {str(e)}"
