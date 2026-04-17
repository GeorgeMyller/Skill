import os
import argparse
from pathlib import Path

# Pastas e extensões frequentemente ignoradas
SKIP_DIRS = {
    ".git", ".venv", "venv", "node_modules", "__pycache__", 
    ".next", "build", "dist", "out", ".idea", ".vscode", "coverage"
}
SKIP_EXTS = {
    ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".ico", ".svg", ".zip", 
    ".tar", ".gz", ".mp4", ".mp3", ".wav", ".exe", ".dll", ".so", 
    ".dylib", ".class", ".pyc", ".ttf", ".woff", ".woff2", ".eot"
}

def generate_tree(dir_path: Path, prefix: str = "") -> str:
    """
    Constrói a árvore de diretórios do projeto baseando-se nas regras de ignição.
    """
    tree_str = ""
    try:
        # Filtramos arquivos que começam com ponto (por precaução geral, 
        # a menos que seja um arquivo critico, mas omitiremos pra manter limpo)
        # e as pastas explícitas.
        contents = sorted([
            f for f in dir_path.iterdir() 
            if f.name not in SKIP_DIRS and not f.name.startswith('.')
        ])
    except PermissionError:
        return ""
    
    for i, path in enumerate(contents):
        is_last = (i == len(contents) - 1)
        connector = "└── " if is_last else "├── "
        tree_str += f"{prefix}{connector}{path.name}\n"
        if path.is_dir():
            extension = "    " if is_last else "│   "
            tree_str += generate_tree(path, prefix + extension)
    return tree_str

def compile_codebase(root_path: Path) -> str:
    """
    Percorre todo o código válido e agrupa num único bloco Markdown.
    """
    content = "# Base de Conhecimento do Projeto (Codebase Context)\n\n"
    content += "## 📂 Estrutura de Pastas\n```text\n"
    content += f"{root_path.name}/\n"
    content += generate_tree(root_path)
    content += "```\n\n"
    content += "---\n\n## 📝 Código dos Arquivos\n\n"
    
    for root, dirs, files in os.walk(root_path):
        # Filtra os diretórios in-place para que o os.walk() ignore a subida
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        
        for file in sorted(files):
            # Omitir dotfiles padrões, se for essencial (.env) também é melhor pular 
            # para não expor tokens para o RAG, embora se trate local.
            if file.startswith('.'):
                continue
            
            file_path = Path(root) / file
            if file_path.suffix.lower() in SKIP_EXTS:
                continue
            
            try:
                # Lê o arquivo. Se for binário que não identificamos acima,
                # o UnicodeDecodeError geralmente protegerá e irá bypassar.
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                
                rel_path = file_path.relative_to(root_path)
                ext = file_path.suffix.lstrip('.')
                
                # Para evitar conflitos de sintaxe com arquivos sem extensão clara
                if not ext:
                    ext = "text"
                    
                content += f"### Caminho: `{rel_path}`\n\n"
                content += f"```{ext}\n"
                content += file_content
                if not file_content.endswith('\n'):
                    content += "\n"
                content += "```\n\n"
                
            except UnicodeDecodeError:
                continue # Pular se bater de frente com leitura binária
            except Exception as e:
                print(f"Skipping {file_path}: {e}")
                
    return content

def main():
    parser = argparse.ArgumentParser(description="Compila a codebase do projeto atual para um Markdown unificado apto a ingestão (NotebookLM/RAG).")
    parser.add_argument("--dir", default=".", help="Diretório alvo (padrão: pastas atuais)")
    parser.add_argument("--out", default="codebase_context.md", help="Nome do arquivo de saída em markdown (padrão: codebase_context.md)")
    args = parser.parse_args()
    
    root_path = Path(args.dir).resolve()
    print(f"🔍 Escaneando o diretório e indexando: {root_path} ...")
    
    markdown_content = compile_codebase(root_path)
    
    out_path = Path(args.out).resolve()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print("✅ Sucesso!")
    print(f"👉 Arquivo {out_path.name} gerado.\nSuba-o no NotebookLM ou utilize a tool na sua conversa para fazer sua query!")

if __name__ == "__main__":
    main()
