import json

dataset = [
    {
        "instruction": "Como funciona um loop for em Python? Me dá um exemplo simples.",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Loop For em Python
# Objetivo: Iterar sobre uma sequência de números
# ============================================

def imprimir_sequencia(inicio: int, fim: int) -> None:
    \"\"\"
    Imprime uma sequência de números.

    Args:
        inicio: Número inicial da sequência.
        fim: Número final da sequência (inclusivo).
    \"\"\"
    for numero in range(inicio, fim + 1):
        print(numero)


def main():
    # Definindo os parâmetros da sequência
    inicio = 1
    fim = 5

    print("Imprimindo sequência de {} até {}:\\n".format(inicio, fim))
    imprimir_sequencia(inicio, fim)


# Ponto de entrada do programa
if __name__ == "__main__":
    main()

# ============================================
# SAÍDA ESPERADA:
# Imprimindo sequência de 1 até 5:
#
# 1
# 2
# 3
# 4
# 5
# ============================================

# EXPLICAÇÃO:
# 1. Criamos uma função específica para a tarefa (separação de responsabilidades)
# 2. Usamos type hints (inicio: int) para deixar o código mais claro
# 3. Adicionamos docstring para documentar o que a função faz
# 4. Usamos main() como ponto de entrada organizado
# 5. O if __name__ == "__main__" garante que só roda quando executado diretamente"""
    },
    {
        "instruction": "Como criar uma lista e filtrar valores maiores que 10 em Python?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Filtrando valores em uma lista
# Objetivo: Criar uma lista e filtrar valores maiores que 10
# ============================================

from typing import List


def filtrar_valores(valores: List[int], limite: int) -> List[int]:
    \"\"\"
    Filtra valores de uma lista que são maiores que um limite.

    Args:
        valores: Lista de números inteiros.
        limite: Valor mínimo para inclusão no resultado.

    Returns:
        Nova lista contendo apenas valores maiores que o limite.
    \"\"\"
    return [valor for valor in valores if valor > limite]


def exibir_resultado(original: List[int], filtrado: List[int], limite: int) -> None:
    \"\"\"
    Exibe os resultados da filtragem de forma organizada.

    Args:
        original: Lista original antes do filtro.
        filtrado: Lista após aplicar o filtro.
        limite: Limite usado na filtragem.
    \"\"\"
    print(f"Lista original: {original}")
    print(f"Limite aplicado: > {limite}")
    print(f"Lista filtrada: {filtrado}")


def main():
    # Dados de entrada
    numeros = [3, 7, 12, 5, 18, 9, 25, 1, 14]
    limite = 10

    # Processamento
    resultado = filtrar_valores(numeros, limite)

    # Exibição
    exibir_resultado(numeros, resultado, limite)


if __name__ == "__main__":
    main()

# ============================================
# SAÍDA ESPERADA:
# Lista original: [3, 7, 12, 5, 18, 9, 25, 1, 14]
# Limite aplicado: > 10
# Lista filtrada: [12, 18, 25, 14]
# ============================================

# EXPLICAÇÃO:
# 1. Separamos em funções com responsabilidades claras:
#    - filtrar_valores() -> só filtra
#    - exibir_resultado() -> só exibe
# 2. Usamos List[int] do typing para ser explícito nos tipos
# 3. Cada função tem sua própria docstring
# 4. List comprehension usado de forma limpa e legível
# 5. Dados, processamento e exibição são separados no main()"""
    },
    {
        "instruction": "Como criar uma calculadora básica em Python?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Calculadora Básica
# Objetivo: Realizar operações matemáticas básicas
# Arquitetura: Separação de operações e interface
# ============================================

from typing import Callable, Dict


# ============================================
# MÓDULO DE OPERAÇÕES
# Cada operação é uma função pura e isolada
# ============================================

def somar(a: float, b: float) -> float:
    \"\"\"Retorna a soma de dois números.\"\"\"
    return a + b


def subtrair(a: float, b: float) -> float:
    \"\"\"Retorna a subtração de dois números.\"\"\"
    return a - b


def multiplicar(a: float, b: float) -> float:
    \"\"\"Retorna a multiplicação de dois números.\"\"\"
    return a * b


def dividir(a: float, b: float) -> float:
    \"\"\"
    Retorna a divisão de dois números.

    Raises:
        ValueError: Se o divisor for zero.
    \"\"\"
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


# ============================================
# MÓDULO DE MAPEAMENTO
# Conecta comandos do usuário às funções
# ============================================

OPERACOES: Dict[str, Callable[[float, float], float]] = {
    "+": somar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir,
}


def calcular(a: float, operador: str, b: float) -> float:
    \"\"\"
    Executa um cálculo baseado no operador fornecido.

    Args:
        a: Primeiro número.
        operador: Símbolo da operação (+, -, *, /).
        b: Segundo número.

    Returns:
        Resultado da operação.

    Raises:
        ValueError: Se o operador não for válido.
    \"\"\"
    if operador not in OPERACOES:
        raise ValueError(f"Operador '{operador}' não suportado. Use: {list(OPERACOES.keys())}")

    return OPERACOES[operador](a, b)


# ============================================
# MÓDULO DE INTERFACE
# Responsável pela interação com o usuário
# ============================================

def exibir_resultado(a: float, operador: str, b: float, resultado: float) -> None:
    \"\"\"Exibe o cálculo e o resultado de forma formatada.\"\"\"
    print(f"\\n  {a} {operador} {b} = {resultado}\\n")


def main():
    # Exemplos de cálculos
    exemplos = [
        (10, "+", 5),
        (20, "-", 8),
        (4, "*", 7),
        (15, "/", 3),
    ]

    print("=== Calculadora Básica ===")

    for a, operador, b in exemplos:
        try:
            resultado = calcular(a, operador, b)
            exibir_resultado(a, operador, b, resultado)
        except ValueError as erro:
            print(f"\\n  Erro: {erro}\\n")


if __name__ == "__main__":
    main()

# ============================================
# SAÍDA ESPERADA:
# === Calculadora Básica ===
#
#   10 + 5 = 15
#
#   20 - 8 = 12
#
#   4 * 7 = 28
#
#   15 / 3 = 5.0
# ============================================

# EXPLICAÇÃO DA ARQUITETURA:
# 1. Separamos em 3 módulos claros:
#    - Operações: funções puras, sem efeitos colaterais
#    - Mapeamento: conecta comandos às funções (extensível)
#    - Interface: cuida só da exibição
# 2. Usamos um dicionário para mapear operadores (fácil de extender)
# 3. Tratamento de erros com try/except
# 4. Cada função tem uma única responsabilidade
# 5. Para adicionar uma nova operação, só precisa criar a função
#    e adicionar ao dicionário OPERACOES"""
    }
]

# Salvando o dataset em formato JSON
with open("dataset.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"Dataset criado com {len(dataset)} exemplos!")
print("\nEstructura de cada exemplo:")
for i, exemplo in enumerate(dataset):
    print(f"\n  Exemplo {i+1}: {exemplo['instruction'][:60]}...")
