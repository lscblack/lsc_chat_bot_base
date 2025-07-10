from pathlib import Path
from typing import List

def load_text_documents(directory: str) -> List[str]:
    documents = []
    for file in Path(directory).rglob("*.txt"):
        with open(file, 'r', encoding='utf-8') as f:
            documents.append(f.read())
    return documents