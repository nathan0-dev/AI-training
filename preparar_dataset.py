"""
Script para preparar o dataset no formato correto para o fine-tuning do Phi-3 Mini.
Combina o dataset_exemplo (3 exemplos) com o dataset_completo (17 exemplos) = 20 exemplos no total.
"""

import json
from pathlib import Path


def carregar_dataset(caminho: str) -> list:
    """Carrega um dataset JSON."""
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def formatar_para_phi3(exemplo: dict) -> dict:
    """
    Formata um exemplo no padrão de chat do Phi-3 Mini.
    O modelo espera mensagens no formato: system -> user -> assistant
    """
    return {
        "messages": [
            {
                "role": "system",
                "content": (
                    "Você é um assistente especializado em ensino de programação e Vibe Coding. "
                    "Sempre responda com código bem estruturado, organizado e seguindo boas práticas: "
                    "type hints, docstrings, separação de responsabilidades e comentários explicativos."
                )
            },
            {
                "role": "user",
                "content": exemplo["instruction"]
            },
            {
                "role": "assistant",
                "content": exemplo["output"]
            }
        ]
    }


def preparar_dataset() -> list:
    """Combina e formata todos os datasets."""
    # Carregando os dois datasets
    dataset_base = carregar_dataset("dataset.json")
    dataset_completo = carregar_dataset("dataset_completo.json")

    # Combinando
    todos = dataset_base + dataset_completo
    print(f"Total de exemplos combinados: {len(todos)}")

    # Formatando para o Phi-3
    formatados = [formatar_para_phi3(ex) for ex in todos]

    return formatados


def main():
    dataset_final = preparar_dataset()

    # Salvando o dataset formatado
    caminho_saida = "dataset_final.json"
    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(dataset_final, f, ensure_ascii=False, indent=2)

    print(f"Dataset final salvo em: {caminho_saida}")
    print(f"Total de exemplos: {len(dataset_final)}")
    print(f"\nEstructura de cada exemplo:")
    print(json.dumps(dataset_final[0], ensure_ascii=False, indent=2)[:300] + "...")


if __name__ == "__main__":
    main()
