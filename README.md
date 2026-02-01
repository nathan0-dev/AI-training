# 🤖 Fine-Tuning Phi-3 Mini — Assistente de Programação

Um projeto de Fine-Tuning do modelo **Phi-3 Mini** (Microsoft) para criar um assistente especializado em **ensino de programação** e **Vibe Coding**, que sempre responde com código bem estruturado e seguindo boas práticas.

---

## 📌 O que este projeto faz?

Pega o modelo open-source Phi-3 Mini e o ajusta (fine-tuning) para que, ao responder perguntas sobre programação, ele sempre entregue código **organizado, documentado e com boa arquitetura** — ao invés de snippets soltos sem estrutura.

### Antes do Fine-Tuning (modelo base):
```python
for numero in range(1, 6):
    print(numero)
```

### Depois do Fine-Tuning (modelo treinado):
```python
from typing import List

def imprimir_sequencia(inicio: int, fim: int) -> None:
    """
    Imprime uma sequência de números.

    Args:
        inicio: Número inicial da sequência.
        fim: Número final da sequência (inclusivo).
    """
    for numero in range(inicio, fim + 1):
        print(numero)


def main():
    imprimir_sequencia(inicio=1, fim=5)


if __name__ == "__main__":
    main()
```

---

## 🏗️ Estrutura do Projeto

```
├── fine_tuning_phi3.ipynb      # Notebook completo do projeto (Google Colab)
├── dataset_exemplo.py          # 3 exemplos base do dataset
├── dataset_completo.py         # 17 exemplos por tema
├── preparar_dataset.py         # Script para combinar e formatar o dataset
└── README.md                   # Este arquivo
```

---

## 📚 Temas Cobertos no Dataset

| Tema | Exemplos |
|------|----------|
| Classes e OOP | 3 |
| Listas e Dicionários | 2 |
| Tratamento de Erros | 2 |
| Leitura e Escrita de Arquivos | 2 |
| APIs e Requisições HTTP | 2 |
| Estrutura de Diretórios e Módulos | 1 |
| Projetos Pequenos Completos | 2 |
| Vibe Coding | 3 |
| **Total** | **20** |

---

## ⚙️ Tecnologias Usadas

- **Python 3.10+**
- **PyTorch** — Framework de deep learning
- **Hugging Face Transformers** — Carregamento e gerenciamento de modelos
- **PEFT (LoRA)** — Técnica de fine-tuning eficiente
- **BitsAndBytes** — Quantização 4-bit para reduzir uso de memória
- **Google Colab** — Ambiente de execução com GPU gratuita

---

## 🚀 Como Rodar

### 1. Pré-requisitos
- Conta no [Google Colab](https://colab.research.google.com)
- Conta no [Hugging Face](https://huggingface.co)

### 2. Passos

1. Faça clone do repositório:
```bash
git clone https://github.com/SEU_USUARIO/fine-tuning-phi3.git
```

2. Abra o notebook `fine_tuning_phi3.ipynb` no Google Colab

3. Ative a GPU: **Ambiente de execução → Alterar ambiente de execução → T4 GPU**

4. Faça upload dos arquapós `.py` no Colab (painel lateral → upload)

5. Rode as células na ordem — o notebook vai guiar todo o processo

---

## 📊 Resultados do Treinamento

| Epoch | Loss Média |
|-------|------------|
| 1 | 0.8715 |
| 2 | 0.5065 |
| 3 | 0.3742 |

O Loss diminuiu consistentemente, confirmando que o modelo aprendeu o padrão do dataset.

### Parâmetros do LoRA:
- **Parâmetros treinados:** 9,437,184
- **Parâmetros totais:** 3,830,516,736
- **Porcentagem treinada:** 0.25%

---

## 🎯 Próximos Passos

- [ ] Aumentar o dataset para 50+ exemplos
- [ ] Adicionar mais temas (testes unitários, design patterns)
- [ ] Criar uma interface web para interagir com o modelo
- [ ] Fazer deploy do modelo em uma API

---

## 📄 Licença

Este projeto foi criado para fins educacionais e de portfólio.
