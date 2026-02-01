import json

dataset = [

    # =============================================
    # TEMA 1: CLASSES E OOP
    # =============================================
    {
        "instruction": "Como criar uma classe básica em Python com métodos e atributos?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Classe básica em Python
# Objetivo: Criar uma classe com atributos e métodos
# Conceitos: __init__, self, métodos, encapsulamento
# ============================================

class Produto:
    \"\"\"Representa um produto em um catálogo.\"\"\"

    def __init__(self, nome: str, preco: float, quantidade: int = 0) -> None:
        \"\"\"
        Inicializa um produto.

        Args:
            nome: Nome do produto.
            preco: Preço unitário (deve ser positivo).
            quantidade: Quantidade no estoque.
        \"\"\"
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self) -> float:
        \"\"\"Retorna o valor total do produto no estoque.\"\"\"
        return self.preco * self.quantidade

    def adicionar_estoque(self, quantidade: int) -> None:
        \"\"\"Adiciona unidades ao estoque.\"\"\"
        if quantidade > 0:
            self.quantidade += quantidade
            print(f"Adicionadas {quantidade} unidades de '{self.nome}'.")

    def __str__(self) -> str:
        \"\"\"Representação em string do produto.\"\"\"
        return f"{self.nome} | R$ {self.preco:.2f} | Estoque: {self.quantidade}"


def main():
    produto = Produto(nome="Notebook", preco=4500.00, quantidade=10)
    print(produto)

    produto.adicionar_estoque(5)
    print(produto)

    print(f"Valor total no estoque: R$ {produto.valor_total():.2f}")


if __name__ == "__main__":
    main()

# SAÍDA ESPERADA:
# Notebook | R$ 4500.00 | Estoque: 10
# Adicionadas 5 unidades de 'Notebook'.
# Notebook | R$ 4500.00 | Estoque: 15
# Valor total no estoque: R$ 67500.00

# CONCEITOS-CHAVE:
# 1. __init__ é o construtor, roda automaticamente ao criar a instância
# 2. self se refere à própria instância da classe
# 3. __str__ controla o que aparece quando você faz print()
# 4. Cada método tem uma única responsabilidade"""
    },
    {
        "instruction": "Como usar herança em Python para reutilizar código entre classes?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Herança em Python
# Objetivo: Reutilizar código com classes pai e filha
# Conceitos: herança, super(), polimorfismo
# ============================================

class Animal:
    \"\"\"Classe base que representa um animal.\"\"\"

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def descrever(self) -> str:
        \"\"\"Retorna uma descrição básica do animal.\"\"\"
        return f"{self.nome}, {self.idade} anos"

    def falar(self) -> str:
        \"\"\"Método a ser sobrescrito pelas subclasses.\"\"\"
        raise NotImplementedError("Subclasses devem implementar falar()")


class Cachorro(Animal):
    \"\"\"Representa um cachorro, estendendo Animal.\"\"\"

    def __init__(self, nome: str, idade: int, raca: str) -> None:
        super().__init__(nome, idade)  # Chama o construtor da classe pai
        self.raca = raca

    def falar(self) -> str:
        return f"{self.nome} diz: Au au!"

    def descrever(self) -> str:
        base = super().descrever()  # Reutiliza o método da classe pai
        return f"{base} | Raça: {self.raca}"


class Gato(Animal):
    \"\"\"Representa um gato, estendendo Animal.\"\"\"

    def __init__(self, nome: str, idade: int, eh_doméstico: bool) -> None:
        super().__init__(nome, idade)
        self.eh_doméstico = eh_doméstico

    def falar(self) -> str:
        return f"{self.nome} diz: Miau!"

    def descrever(self) -> str:
        base = super().descrever()
        tipo = "doméstico" if self.eh_doméstico else "selvagem"
        return f"{base} | Tipo: {tipo}"


def apresentar_animais(animais: list) -> None:
    \"\"\"Apresenta uma lista de animais (polimorfismo em ação).\"\"\"
    for animal in animais:
        print(f"  {animal.descrever()}")
        print(f"  {animal.falar()}\\n")


def main():
    animais = [
        Cachorro(nome="Rex", idade=3, raca="Pastor Alemão"),
        Gato(nome="Luna", idade=2, eh_doméstico=True),
        Cachorro(nome="Buddy", idade=5, raca="Golden Retriever"),
        Gato(nome="Shadow", idade=4, eh_doméstico=False),
    ]

    print("=== Lista de Animais ===\\n")
    apresentar_animais(animais)


if __name__ == "__main__":
    main()

# CONCEITOS-CHAVE:
# 1. Cachorro e Gato herdam de Animal sem repetir código
# 2. super() conecta a subclasse ao construtor da classe pai
# 3. Polimorfismo: a função apresentar_animais não precisa saber
#    se é cachorro ou gato, apenas chama falar() e descrever()
# 4. NotImplementedError força subclasses a implementarem falar()"""
    },
    {
        "instruction": "Como usar métodos estáticos e de classe em Python?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Métodos estáticos e de classe
# Objetivo: Diferenciar métodos de instância, estáticos e de classe
# Conceitos: @staticmethod, @classmethod, self vs cls
# ============================================

class Conversor:
    \"\"\"Classe utilitária para conversões de temperatura.\"\"\"

    # Atributo de classe (compartilhado por todas as instâncias)
    historico: list = []

    def __init__(self, nome: str) -> None:
        self.nome = nome

    @staticmethod
    def celsius_para_fahrenheit(celsius: float) -> float:
        \"\"\"
        Converte Celsius para Fahrenheit.
        Método estático: não precisa da instância nem da classe.
        \"\"\"
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_para_celsius(fahrenheit: float) -> float:
        \"\"\"Converte Fahrenheit para Celsius.\"\"\"
        return (fahrenheit - 32) * 5 / 9

    @classmethod
    def registrar_conversao(cls, descricao: str) -> None:
        \"\"\"
        Registra uma conversão no histórico.
        Método de classe: tem acesso aos atributos da classe (cls).
        \"\"\"
        cls.historico.append(descricao)

    @classmethod
    def mostrar_historico(cls) -> None:
        \"\"\"Exibe o histórico de conversões.\"\"\"
        if not cls.historico:
            print("  Nenhuma conversão registrada.\\n")
            return
        for i, entrada in enumerate(cls.historico, 1):
            print(f"  {i}. {entrada}")
        print()


def main():
    # Método estático: chamado sem criar instância
    celsius = 100
    fahrenheit = Conversor.celsius_para_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit}°F")
    Conversor.registrar_conversao(f"{celsius}°C -> {fahrenheit}°F")

    fahrenheit = 32
    celsius = Conversor.fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius}°C")
    Conversor.registrar_conversao(f"{fahrenheit}°F -> {celsius}°C\\n")

    print("=== Histórico de Conversões ===")
    Conversor.mostrar_historico()


if __name__ == "__main__":
    main()

# CONCEITOS-CHAVE:
# 1. @staticmethod: não usa self nem cls, é só um método agrupado na classe
# 2. @classmethod: usa cls para acessar atributos da classe (como historico)
# 3. Método de instância (normal): usa self para acessar dados da instância
# 4. Escolha baseada na necessidade:
#    - Precisa da instância? -> método normal (self)
#    - Precisa da classe? -> @classmethod (cls)
#    - Não precisa de nenhum? -> @staticmethod"""
    },

    # =============================================
    # TEMA 2: LISTAS E DICIONÁRIOS
    # =============================================
    {
        "instruction": "Como manipular listas de forma eficiente em Python?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Manipulação eficiente de listas
# Objetivo: Usar list comprehensions, filter e map
# Conceitos: list comprehension, lambda, sorted, filter
# ============================================

from typing import List


def filtrar_pares(numeros: List[int]) -> List[int]:
    \"\"\"Retorna apenas os números pares da lista.\"\"\"
    return [n for n in numeros if n % 2 == 0]


def elevar_ao_quadrado(numeros: List[int]) -> List[int]:
    \"\"\"Retorna cada número elevado ao quadrado.\"\"\"
    return [n ** 2 for n in numeros]


def ordenar_por_tamanho(palavras: List[str]) -> List[str]:
    \"\"\"Ordena palavras pelo número de caracteres.\"\"\"
    return sorted(palavras, key=len)


def resumo_lista(numeros: List[int]) -> dict:
    \"\"\"
    Gera um resumo estatístico da lista.

    Returns:
        Dicionário com soma, média, mínimo e máximo.
    \"\"\"
    return {
        "soma": sum(numeros),
        "media": sum(numeros) / len(numeros),
        "minimo": min(numeros),
        "maximo": max(numeros),
    }


def main():
    numeros = [3, 8, 1, 12, 5, 20, 7, 14, 2, 9]
    palavras = ["Python", "é", "uma", "linguagem", "incrível"]

    print(f"Original:  {numeros}")
    print(f"Pares:     {filtrar_pares(numeros)}")
    print(f"Quadrados: {elevar_ao_quadrado(numeros)}\\n")

    print(f"Palavras originais:  {palavras}")
    print(f"Ordenadas por tamanho: {ordenar_por_tamanho(palavras)}\\n")

    resumo = resumo_lista(numeros)
    print("=== Resumo ===")
    for chave, valor in resumo.items():
        print(f"  {chave}: {valor}")


if __name__ == "__main__":
    main()

# CONCEITOS-CHAVE:
# 1. List comprehension é mais legível que um loop + append
# 2. sorted() com key= permite ordenar por critério customizado
# 3. Cada operação é uma função separada (reutilizável e testável)
# 4. Funções puras: recebem entrada e retornam saída sem efeitos laterais"""
    },
    {
        "instruction": "Como usar dicionários para estruturar dados em Python?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Estruturando dados com dicionários
# Objetivo: Usar dicionários como estrutura de dados organizada
# Conceitos: dicionários aninhados, iteração, manipulação
# ============================================

from typing import Dict, List


# Estrutura de dados: lista de alunos com suas notas
ALUNOS: List[Dict] = [
    {"nome": "Ana", "notas": [85, 92, 78, 90]},
    {"nome": "Pedro", "notas": [70, 65, 80, 75]},
    {"nome": "Lucia", "notas": [95, 98, 92, 97]},
    {"nome": "Carlos", "notas": [60, 55, 70, 65]},
]


def calcular_media(notas: List[float]) -> float:
    \"\"\"Calcula a média de uma lista de notas.\"\"\"
    return sum(notas) / len(notas)


def classificar_aluno(media: float) -> str:
    \"\"\"Classifica o aluno baseado na média.\"\"\"
    if media >= 90:
        return "Excelente"
    elif media >= 75:
        return "Bom"
    elif media >= 60:
        return "Satisfatório"
    return "Precisa melhorar"


def gerar_relatorio(alunos: List[Dict]) -> List[Dict]:
    \"\"\"
    Gera um relatório completo de cada aluno.

    Returns:
        Lista de dicionários com nome, média e classificação.
    \"\"\"
    relatorio = []
    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        relatorio.append({
            "nome": aluno["nome"],
            "media": round(media, 2),
            "classificacao": classificar_aluno(media),
        })
    return relatorio


def exibir_relatorio(relatorio: List[Dict]) -> None:
    \"\"\"Exibe o relatório formatado.\"\"\"
    print("=" * 40)
    print(f"  {'Nome':<10} {'Média':<8} {'Classificação'}")
    print("=" * 40)
    for aluno in relatorio:
        print(f"  {aluno['nome']:<10} {aluno['media']:<8} {aluno['classificacao']}")
    print("=" * 40)


def main():
    relatorio = gerar_relatorio(ALUNOS)
    exibir_relatorio(relatorio)

    # Encontrando o melhor aluno
    melhor = max(relatorio, key=lambda a: a["media"])
    print(f"\\n  Melhor aluno: {melhor['nome']} (média: {melhor['media']})")


if __name__ == "__main__":
    main()

# CONCEITOS-CHAVE:
# 1. Dicionários são perfeitos para estruturar dados relacionados
# 2. Separamos: dados (ALUNOS), lógica (calcular/classificar) e exibição
# 3. A função gerar_relatorio transforma dados brutos em dados processados
# 4. max() com key= encontra o elemento por um critério específico"""
    },

    # =============================================
    # TEMA 3: TRATAMENTO DE ERROS
    # =============================================
    {
        "instruction": "Como usar try/except de forma organizada em Python?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Tratamento de erros organizado
# Objetivo: Usar try/except de forma estruturada e informativa
# Conceitos: try/except/else/finally, exceções customizadas
# ============================================


# ============================================
# EXCEÇÕES CUSTOMIZADAS
# Criam erros específicos pro seu domínio
# ============================================

class ErroValidacao(Exception):
    \"\"\"Erro lançado quando dados de entrada são inválidos.\"\"\"
    pass


class ErroIdadeInvalida(ErroValidacao):
    \"\"\"Erro específico para idade fora do intervalo válido.\"\"\"
    pass


# ============================================
# LÓGICA DE NEGÓCIO
# ============================================

def validar_idade(idade: int) -> None:
    \"\"\"
    Valida se a idade está dentro do intervalo permitido.

    Raises:
        ErroIdadeInvalida: Se a idade for menor que 0 ou maior que 150.
        TypeError: Se a idade não for um inteiro.
    \"\"\"
    if not isinstance(idade, int):
        raise TypeError(f"Idade deve ser um inteiro, recebeu: {type(idade).__name__}")
    if idade < 0 or idade > 150:
        raise ErroIdadeInvalida(f"Idade inválida: {idade}. Deve estar entre 0 e 150.")


def cadastrar_pessoa(nome: str, idade: int) -> dict:
    \"\"\"Cadastra uma pessoa após validar os dados.\"\"\"
    validar_idade(idade)
    return {"nome": nome, "idade": idade}


# ============================================
# FUNÇÃO PRINCIPAL COM TRATAMENTO DE ERROS
# ============================================

def processar_cadastro(nome: str, idade) -> None:
    \"\"\"
    Tenta cadastrar uma pessoa, tratando cada tipo de erro.
    \"\"\"
    try:
        pessoa = cadastrar_pessoa(nome, idade)

    except ErroIdadeInvalida as erro:
        # Erro específico do nosso domínio
        print(f"  [ERRO DE VALIDAÇÃO] {erro}")

    except TypeError as erro:
        # Erro de tipo de dado
        print(f"  [ERRO DE TIPO] {erro}")

    except Exception as erro:
        # Captura qualquer outro erro inesperado
        print(f"  [ERRO INESPERADO] {erro}")

    else:
        # Roda APENAS se não houve erro
        print(f"  [SUCESSO] Pessoa cadastrada: {pessoa}")

    finally:
        # Roda SEMPRE, independente do resultado
        print(f"  [LOG] Tentativa de cadastro para '{nome}' finalizada.\\n")


def main():
    print("=== Testando Tratamento de Erros ===\\n")

    # Caso 1: Dados válidos
    processar_cadastro("Ana", 25)

    # Caso 2: Idade negativa
    processar_cadastro("Pedro", -5)

    # Caso 3: Idade muito alta
    processar_cadastro("Lucia", 200)

    # Caso 4: Tipo de dado errado
    processar_cadastro("Carlos", "vinte e cinco")


if __name__ == "__main__":
    main()

# CONCEITOS-CHAVE:
# 1. Exceções customizadas criam erros específicos e descritivos
# 2. Captura do mais específico para o mais geral (ErroIdadeInvalida antes de Exception)
# 3. else: roda só com sucesso | finally: roda sempre (útil pra logs e cleanup)
# 4. Cada bloco except trata um tipo de problema de forma diferente"""
    },
    {
        "instruction": "Como criar um sistema de logs em Python para monitorar erros?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Sistema de logs básico
# Objetivo: Monitorar operações e registrar erros
# Conceitos: logging, níveis de log, formatação
# ============================================

import logging
from datetime import datetime


# ============================================
# CONFIGURAÇÃO DO SISTEMA DE LOGS
# ============================================

def configurar_logs() -> logging.Logger:
    \"\"\"
    Configura e retorna um logger formatado.

    Returns:
        Logger configurado com formato e nível apropriados.
    \"\"\"
    logger = logging.getLogger("MeuApp")
    logger.setLevel(logging.DEBUG)

    # Formato: [hora] [nível] mensagem
    formato = logging.Formatter(
        fmt="[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    # Handler para console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formato)

    logger.addHandler(console)
    return logger


# ============================================
# OPERAÇÕES COM LOG
# ============================================

logger = configurar_logs()


def dividir(a: float, b: float) -> float:
    \"\"\"Divide dois números com log de operação.\"\"\"
    logger.info(f"Iniciando divisão: {a} / {b}")

    if b == 0:
        logger.error("Divisão por zero tentada!")
        raise ValueError("Não é possível dividir por zero.")

    resultado = a / b
    logger.info(f"Resultado: {resultado}")
    return resultado


def processar_lista(valores: list) -> None:
    \"\"\"Processa uma lista de divisões, registrando cada etapa.\"\"\"
    logger.info(f"Processando {len(valores)} operações...\\n")

    for i, (a, b) in enumerate(valores, 1):
        logger.debug(f"Operação {i}: {a} / {b}")
        try:
            dividir(a, b)
        except ValueError as erro:
            logger.warning(f"Operação {i} falhou: {erro}")
        print()  # Espaçamento entre operações


def main():
    operacoes = [
        (10, 2),
        (20, 0),   # Vai causar erro
        (15, 3),
    ]

    processar_lista(operacoes)


if __name__ == "__main__":
    main()

# NÍVEIS DE LOG (do menos ao mais grave):
# DEBUG    -> Informações detalhadas pra desenvolvimento
# INFO     -> Confirmação de operações normais
# WARNING  -> Algo inesperado aconteceu, mas ainda funciona
# ERROR    -> Um erro grave impediu uma operação
# CRITICAL -> Erro tão grave que pode parar o sistema

# CONCEITOS-CHAVE:
# 1. logging é melhor que print() pra monitoramento
# 2. Níveis permitem filtrar mensagens por importância
# 3. Formatadores organizam a saída de forma consistente
# 4. Cada função registra suas próprias operações no log"""
    },

    # =============================================
    # TEMA 4: LEITURA E ESCRITA DE ARQUIVOS
    # =============================================
    {
        "instruction": "Como ler e escrever arquivos de forma segura em Python?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Leitura e escrita de arquivos
# Objetivo: Manipular arquivos de forma segura e organizada
# Conceitos: open(), with, tratamento de erros com arquivos
# ============================================

import os
from pathlib import Path


# ============================================
# CONFIGURAÇÃO DE CAMINHOS
# ============================================

DIRETORIO_BASE = Path("dados")
ARQUIVO_NOTAS = DIRETORIO_BASE / "notas.txt"


def garantir_diretorio() -> None:
    \"\"\"Cria o diretório de dados se não existir.\"\"\"
    DIRETORIO_BASE.mkdir(exist_ok=True)


# ============================================
# OPERAÇÕES COM ARQUIVOS
# ============================================

def escrever_arquivo(caminho: Path, conteudo: str) -> None:
    \"\"\"
    Escreve conteúdo em um arquivo.

    Args:
        caminho: Caminho do arquivo.
        conteudo: Texto a ser escrito.
    \"\"\"
    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
        print(f"  Arquivo salvo: {caminho}")

    except OSError as erro:
        print(f"  Erro ao salvar arquivo: {erro}")


def ler_arquivo(caminho: Path) -> str | None:
    \"\"\"
    Lê o conteúdo de um arquivo.

    Returns:
        Conteúdo do arquivo ou None se não existir.
    \"\"\"
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    except FileNotFoundError:
        print(f"  Arquivo não encontrado: {caminho}")
        return None

    except OSError as erro:
        print(f"  Erro ao ler arquivo: {erro}")
        return None


def adicionar_nota(nota: str) -> None:
    \"\"\"Adiciona uma nota ao arquivo (modo append).\"\"\"
    try:
        with open(ARQUIVO_NOTAS, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"- {nota}\\n")
        print(f"  Nota adicionada!")

    except OSError as erro:
        print(f"  Erro ao adicionar nota: {erro}")


# ============================================
# FUNÇÃO PRINCIPAL
# ============================================

def main():
    garantir_diretorio()

    # Escrevendo um arquivo
    print("=== Escrevendo arquivo ===")
    escrever_arquivo(ARQUIVO_NOTAS, "Minhas notas:\\n")

    # Adicionando notas
    print("\\n=== Adicionando notas ===")
    adicionar_nota("Aprender Python")
    adicionar_nota("Criar projeto de ML")
    adicionar_nota("Fazer deploy da aplicação")

    # Lendo o arquivo
    print("\\n=== Lendo arquivo ===")
    conteudo = ler_arquivo(ARQUIVO_NOTAS)
    if conteudo:
        print(conteudo)

    # Tentando ler arquivo inexistente
    print("=== Testando erro ===")
    ler_arquivo(Path("dados/inexistente.txt"))


if __name__ == "__main__":
    main()

# CONCEITOS-CHAVE:
# 1. with open() garante que o arquivo seja fechado automaticamente
# 2. Path do pathlib é mais seguro e legível que strings de caminho
# 3. encoding="utf-8" evita problemas com caracteres especiais
# 4. Modos: "w" (escrever), "r" (ler), "a" (adicionar ao final)
# 5. Cada operação trata seus próprios erros específicos"""
    },
    {
        "instruction": "Como trabalhar com arquivos JSON em Python?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Manipulação de arquivos JSON
# Objetivo: Salvar e carregar dados estruturados em JSON
# Conceitos: json.dump, json.load, estruturas aninhadas
# ============================================

import json
from pathlib import Path
from typing import Any, Dict, List


# ============================================
# CONFIGURAÇÃO
# ============================================

ARQUIVO_DADOS = Path("dados/usuarios.json")


def garantir_diretorio() -> None:
    \"\"\"Cria o diretório necessário.\"\"\"
    ARQUIVO_DADOS.parent.mkdir(exist_ok=True)


# ============================================
# OPERAÇÕES COM JSON
# ============================================

def salvar_json(dados: Any, caminho: Path) -> None:
    \"\"\"Salva dados em um arquivo JSON formatado.\"\"\"
    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)
        print(f"  Dados salvos em: {caminho}")

    except (OSError, TypeError) as erro:
        print(f"  Erro ao salvar JSON: {erro}")


def carregar_json(caminho: Path) -> Any | None:
    \"\"\"Carrega dados de um arquivo JSON.\"\"\"
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        print(f"  Arquivo não encontrado: {caminho}")
        return None

    except json.JSONDecodeError as erro:
        print(f"  Erro ao decodificar JSON: {erro}")
        return None


# ============================================
# LÓGICA DE NEGÓCIO
# ============================================

def criar_usuario(nome: str, email: str, idade: int) -> Dict:
    \"\"\"Cria um dicionário de usuário.\"\"\"
    return {
        "nome": nome,
        "email": email,
        "idade": idade,
    }


def adicionar_usuario(novo_usuario: Dict) -> None:
    \"\"\"Adiciona um usuário ao arquivo JSON.\"\"\"
    usuarios = carregar_json(ARQUIVO_DADOS) or []
    usuarios.append(novo_usuario)
    salvar_json(usuarios, ARQUIVO_DADOS)


def listar_usuarios() -> None:
    \"\"\"Exibe todos os usuários cadastrados.\"\"\"
    usuarios = carregar_json(ARQUIVO_DADOS)
    if not usuarios:
        print("  Nenhum usuário cadastrado.\\n")
        return

    print("\\n=== Usuários Cadastrados ===")
    for i, usuario in enumerate(usuarios, 1):
        print(f"  {i}. {usuario['nome']} | {usuario['email']} | {usuario['idade']} anos")
    print()


def main():
    garantir_diretorio()

    # Cadastrando usuários
    print("=== Cadastrando Usuários ===")
    adicionar_usuario(criar_usuario("Ana Silva", "ana@email.com", 28))
    adicionar_usuario(criar_usuario("Pedro Santos", "pedro@email.com", 34))
    adicionar_usuario(criar_usuario("Lucia Oliveira", "lucia@email.com", 22))

    # Listando usuários
    listar_usuarios()


if __name__ == "__main__":
    main()

# CONCEITOS-CHAVE:
# 1. json.dump salva dados Python como JSON no arquivo
# 2. json.load carrega JSON do arquivo e converte pra Python
# 3. ensure_ascii=False permite caracteres como ã, é no JSON
# 4. indent=2 formata o JSON pra ser legível por humanos
# 5. Separamos criação, persistência e exibição em funções distintas"""
    },

    # =============================================
    # TEMA 5: APIs E REQUISIÇÕES HTTP
    # =============================================
    {
        "instruction": "Como fazer requisições HTTP em Python usando requests?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Requisições HTTP com requests
# Objetivo: Consumir uma API pública de forma organizada
# Conceitos: GET, POST, tratamento de erros HTTP, headers
# ============================================

import requests
from typing import Any, Dict, Optional


# ============================================
# CONFIGURAÇÃO DA API
# ============================================

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10  # segundos


# ============================================
# CAMADA DE REQUISIÇÃO (baixo nível)
# Responsável apenas por fazer a chamada HTTP
# ============================================

def fazer_requisicao(
    metodo: str,
    endpoint: str,
    dados: Optional[Dict] = None
) -> Optional[requests.Response]:
    \"\"\"
    Faz uma requisição HTTP genérica.

    Args:
        metodo: Tipo da requisição (GET, POST, etc.)
        endpoint: Caminho da API.
        dados: Corpo da requisição (para POST/PUT).

    Returns:
        Response do servidor ou None em caso de erro.
    \"\"\"
    url = f"{BASE_URL}{endpoint}"

    try:
        resposta = requests.request(
            method=metodo,
            url=url,
            json=dados,
            timeout=TIMEOUT
        )
        resposta.raise_for_status()  # Lança exceção se status >= 400
        return resposta

    except requests.exceptions.Timeout:
        print(f"  [ERRO] Timeout na requisição para {url}")
    except requests.exceptions.ConnectionError:
        print(f"  [ERRO] Não foi possível conectar a {url}")
    except requests.exceptions.HTTPError as erro:
        print(f"  [ERRO HTTP] {erro}")

    return None


# ============================================
# CAMADA DE SERVIÇO (alto nível)
# Usa a camada de requisição pra realizar operações
# ============================================

def buscar_post(post_id: int) -> Optional[Dict]:
    \"\"\"Busca um post pelo ID.\"\"\"
    resposta = fazer_requisicao("GET", f"/posts/{post_id}")
    return resposta.json() if resposta else None


def listar_posts(limit: int = 5) -> list:
    \"\"\"Lista os primeiros posts disponíveis.\"\"\"
    resposta = fazer_requisicao("GET", "/posts")
    if resposta:
        return resposta.json()[:limit]
    return []


def criar_post(titulo: str, corpo: str) -> Optional[Dict]:
    \"\"\"Cria um novo post na API.\"\"\"
    dados = {"title": titulo, "body": corpo, "userId": 1}
    resposta = fazer_requisicao("POST", "/posts", dados=dados)
    return resposta.json() if resposta else None


# ============================================
# EXIBIÇÃO
# ============================================

def exibir_post(post: Dict) -> None:
    \"\"\"Exibe um post formatado.\"\"\"
    print(f"  ID:    {post.get('id')}")
    print(f"  Título: {post.get('title')}")
    print(f"  Corpo:  {post.get('body')[:60]}...")
    print()


def main():
    # Listando posts
    print("=== Posts Disponíveis ===\\n")
    posts = listar_posts(limit=3)
    for post in posts:
        exibir_post(post)

    # Buscando um post específico
    print("=== Buscando Post #1 ===\\n")
    post = buscar_post(1)
    if post:
        exibir_post(post)

    # Criando um novo post
    print("=== Criando Novo Post ===\\n")
    novo_post = criar_post(
        titulo="Meu primeiro post via API",
        corpo="Isso é um exemplo de POST usando requests em Python."
    )
    if novo_post:
        print("  Post criado com sucesso!")
        exibir_post(novo_post)


if __name__ == "__main__":
    main()

# CONCEITOS-CHAVE:
# 1. Separamos em duas camadas: requisição (baixo) e serviço (alto)
# 2. raise_for_status() simplifica o tratamento de erros HTTP
# 3. timeout é essencial pra evitar que o programa trave
# 4. A camada de serviço não precisa saber como a requisição funciona
# 5. Cada função tem uma única responsabilidade"""
    },
    {
        "instruction": "Como criar uma classe para gerenciar conexões com APIs?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Classe para gerenciar conexões com APIs
# Objetivo: Criar uma classe reutilizável para chamadas HTTP
# Conceitos: Session, autenticação, retry, encapsulamento
# ============================================

import requests
from typing import Any, Dict, Optional


class Cliente_API:
    \"\"\"
    Cliente reutilizável para consumir APIs REST.

    Encapsula configurações comuns como base URL,
    headers e tratamento de erros.
    \"\"\"

    def __init__(self, base_url: str, api_key: Optional[str] = None) -> None:
        \"\"\"
        Inicializa o cliente com configurações base.

        Args:
            base_url: URL base da API.
            api_key: Chave de autenticação (opcional).
        \"\"\"
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.timeout = 10

        # Configurando headers padrão
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

        # Adicionando autenticação se fornecida
        if api_key:
            self.session.headers["Authorization"] = f"Bearer {api_key}"

    def _url_completa(self, endpoint: str) -> str:
        \"\"\"Monta a URL completa a partir do endpoint.\"\"\"
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def _tratar_erro(self, erro: Exception) -> None:
        \"\"\"Centraliza o tratamento de erros HTTP.\"\"\"
        if isinstance(erro, requests.exceptions.Timeout):
            print("  [ERRO] Requisição expirou (timeout).")
        elif isinstance(erro, requests.exceptions.ConnectionError):
            print("  [ERRO] Falha na conexão.")
        elif isinstance(erro, requests.exceptions.HTTPError):
            print(f"  [ERRO HTTP] {erro.response.status_code}: {erro}")
        else:
            print(f"  [ERRO] {erro}")

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Any]:
        \"\"\"Realiza uma requisição GET.\"\"\"
        try:
            resposta = self.session.get(
                self._url_completa(endpoint),
                params=params,
                timeout=self.timeout
            )
            resposta.raise_for_status()
            return resposta.json()

        except Exception as erro:
            self._tratar_erro(erro)
            return None

    def post(self, endpoint: str, dados: Optional[Dict] = None) -> Optional[Any]:
        \"\"\"Realiza uma requisição POST.\"\"\"
        try:
            resposta = self.session.post(
                self._url_completa(endpoint),
                json=dados,
                timeout=self.timeout
            )
            resposta.raise_for_status()
            return resposta.json()

        except Exception as erro:
            self._tratar_erro(erro)
            return None


# ============================================
# USO DO CLIENTE
# ============================================

def main():
    # Criando o cliente uma vez
    api = Cliente_API(base_url="https://jsonplaceholder.typicode.com")

    # Usando GET
    print("=== Buscando Posts ===\\n")
    posts = api.get("/posts", params={"_limit": 3})
    if posts:
        for post in posts:
            print(f"  [{post['id']}] {post['title']}")

    # Usando POST
    print("\\n=== Criando Post ===\\n")
    novo = api.post("/posts", dados={
        "title": "Novo post",
        "body": "Criado via Cliente_API",
        "userId": 1
    })
    if novo:
        print(f"  Criado com ID: {novo['id']}")


if __name__ == "__main__":
    main()

# CONCEITOS-CHAVE:
# 1. Session reutiliza conexões HTTP (mais eficiente)
# 2. Headers e autenticação são configurados uma vez no __init__
# 3. _tratar_erro centraliza todos os erros em um lugar
# 4. Métodos get() e post() são a interface pública da classe
# 5. Para usar uma nova API, só muda a base_url"""
    },

    # =============================================
    # TEMA 6: ESTRUTURA DE DIRETÓRIOS E MÓDULOS
    # =============================================
    {
        "instruction": "Como estruturar um projeto Python com módulos e pacotes?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Estrutura de projeto Python organizada
# Objetivo: Mostrar como organizar código em módulos e pacotes
# ============================================

# Estrutura de diretórios do projeto:
#
# meu_projeto/
# ├── config/
# │   ├── __init__.py
# │   └── configuracoes.py    <- Constantes e configurações
# ├── modelos/
# │   ├── __init__.py
# │   └── usuario.py          <- Classe Usuario
# ├── servicos/
# │   ├── __init__.py
# │   └── autenticacao.py     <- Lógica de autenticação
# ├── utils/
# │   ├── __init__.py
# │   └── validadores.py      <- Funções utilitárias
# ├── main.py                 <- Ponto de entrada
# └── requirements.txt        <- Dependências do projeto

# ============================================
# config/configuracoes.py
# ============================================

# Todas as constantes do projeto ficam aqui
APP_NOME = "MeuApp"
APP_VERSAO = "1.0.0"
MAX_TENTATIVAS_LOGIN = 3
COMPRIMENTO_MINIMO_SENHA = 8

# ============================================
# utils/validadores.py
# ============================================

def validar_email(email: str) -> bool:
    \"\"\"Verifica se o email tem formato básico válido.\"\"\"
    return "@" in email and "." in email.split("@")[-1]


def validar_senha(senha: str, tamanho_minimo: int) -> tuple[bool, str]:
    \"\"\"
    Valida uma senha.

    Returns:
        Tupla com (é_válida, mensagem).
    \"\"\"
    if len(senha) < tamanho_minimo:
        return False, f"Senha deve ter pelo menos {tamanho_minimo} caracteres."
    if not any(c.isupper() for c in senha):
        return False, "Senha deve ter pelo menos uma letra maiúscula."
    return True, "Senha válida."

# ============================================
# modelos/usuario.py
# ============================================

class Usuario:
    \"\"\"Representa um usuário do sistema.\"\"\"

    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self._senha = senha  # Prefixo _ indica atributo privado

    def verificar_senha(self, senha: str) -> bool:
        \"\"\"Verifica se a senha fornecida está correta.\"\"\"
        return self._senha == senha

    def __str__(self) -> str:
        return f"Usuario(nome='{self.nome}', email='{self.email}')"

# ============================================
# servicos/autenticacao.py
# ============================================

from config.configuracoes import MAX_TENTATIVAS_LOGIN, COMPRIMENTO_MINIMO_SENHA
from utils.validadores import validar_email, validar_senha
from modelos.usuario import Usuario


class ServicoAutenticacao:
    \"\"\"Gerencia o processo de autenticação.\"\"\"

    def __init__(self) -> None:
        self.usuarios: dict[str, Usuario] = {}  # email -> Usuario

    def cadastrar(self, nome: str, email: str, senha: str) -> tuple[bool, str]:
        \"\"\"Cadastra um novo usuário após validações.\"\"\"
        if not validar_email(email):
            return False, "Email inválido."

        senha_valida, mensagem = validar_senha(senha, COMPRIMENTO_MINIMO_SENHA)
        if not senha_valida:
            return False, mensagem

        if email in self.usuarios:
            return False, "Email já cadastrado."

        self.usuarios[email] = Usuario(nome, email, senha)
        return True, f"Usuário '{nome}' cadastrado com sucesso!"

    def login(self, email: str, senha: str) -> tuple[bool, str]:
        \"\"\"Autentica um usuário.\"\"\"
        if email not in self.usuarios:
            return False, "Email não encontrado."

        usuario = self.usuarios[email]
        if not usuario.verificar_senha(senha):
            return False, "Senha incorreta."

        return True, f"Bem-vindo, {usuario.nome}!"

# ============================================
# main.py - Ponto de entrada
# ============================================

from config.configuracoes import APP_NOME, APP_VERSAO
from servicos.autenticacao import ServicoAutenticacao


def main():
    print(f"=== {APP_NOME} v{APP_VERSAO} ===\\n")
    auth = ServicoAutenticacao()

    # Cadastrando usuário
    sucesso, msg = auth.cadastrar("Ana Silva", "ana@email.com", "Senha123")
    print(f"  Cadastro: {msg}")

    # Tentativa com senha fraca
    sucesso, msg = auth.cadastrar("Pedro", "pedro@email.com", "123")
    print(f"  Cadastro: {msg}")

    # Login
    sucesso, msg = auth.login("ana@email.com", "Senha123")
    print(f"  Login:    {msg}")


if __name__ == "__main__":
    main()

# CONCEITOS-CHAVE:
# 1. config/ -> constantes e configurações centralizadas
# 2. modelos/ -> estruturas de dados (classes)
# 3. servicos/ -> lógica de negócio
# 4. utils/ -> funções auxiliares reutilizáveis
# 5. __init__.py marca um diretório como pacote Python
# 6. main.py é sempre o ponto de entrada do programa"""
    },

    # =============================================
    # TEMA 7: PROJETOS PEQUENOS COMPLETOS
    # =============================================
    {
        "instruction": "Como criar uma API REST básica com Flask em Python?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: API REST básica com Flask
# Objetivo: Criar endpoints GET e POST organizados
# Conceitos: Flask, rotas, JSON, status codes
# ============================================
# Instalar: pip install flask

from flask import Flask, jsonify, request
from typing import Dict, List


# ============================================
# CONFIGURAÇÃO
# ============================================

app = Flask(__name__)


# ============================================
# ARMAZENAMENTO (em memória para o exemplo)
# ============================================

tarefas: List[Dict] = []
proximo_id: int = 1


# ============================================
# ROTAS DA API
# ============================================

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    \"\"\"Retorna todas as tarefas.\"\"\"
    return jsonify(tarefas), 200


@app.route("/tarefas/<int:tarefa_id>", methods=["GET"])
def buscar_tarefa(tarefa_id: int):
    \"\"\"Retorna uma tarefa específica pelo ID.\"\"\"
    tarefa = next((t for t in tarefas if t["id"] == tarefa_id), None)

    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    return jsonify(tarefa), 200


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    \"\"\"Cria uma nova tarefa.\"\"\"
    global proximo_id
    dados = request.get_json()

    # Validação
    if not dados or "titulo" not in dados:
        return jsonify({"erro": "Campo 'titulo' é obrigatório"}), 400

    nova_tarefa = {
        "id": proximo_id,
        "titulo": dados["titulo"],
        "concluida": False,
    }

    tarefas.append(nova_tarefa)
    proximo_id += 1

    return jsonify(nova_tarefa), 201


@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
def atualizar_tarefa(tarefa_id: int):
    \"\"\"Marca uma tarefa como concluída.\"\"\"
    tarefa = next((t for t in tarefas if t["id"] == tarefa_id), None)

    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    tarefa["concluida"] = True
    return jsonify(tarefa), 200


# ============================================
# PONTO DE ENTRADA
# ============================================

if __name__ == "__main__":
    app.run(debug=True)

# ============================================
# TESTANDO A API (com curl no terminal):
# ============================================
# Criar tarefa:
#   curl -X POST http://localhost:5000/tarefas
#   -H "Content-Type: application/json"
#   -d '{"titulo": "Aprender Flask"}'
#
# Listar tarefas:
#   curl http://localhost:5000/tarefas
#
# Buscar tarefa:
#   curl http://localhost:5000/tarefas/1
#
# Concluir tarefa:
#   curl -X PUT http://localhost:5000/tarefas/1

# STATUS CODES USADOS:
# 200 -> Sucesso
# 201 -> Criado com sucesso
# 400 -> Dados inválidos
# 404 -> Não encontrado

# CONCEITOS-CHAVE:
# 1. Cada rota tem uma única responsabilidade
# 2. Métodos HTTP: GET (buscar), POST (criar), PUT (atualizar)
# 3. Status codes comunicam o resultado da operação
# 4. Validação de entrada antes de processar dados
# 5. debug=True recarrega automaticamente ao salvar"""
    },
    {
        "instruction": "Como criar um programa de gerenciamento de tasks no terminal?",
        "input": "",
        "output": """# ============================================
# PROJETO COMPLETO: Gerenciador de Tasks no Terminal
# Objetivo: CRUD completo com persistência em JSON
# Conceitos: menus, JSON, classes, validação
# ============================================

import json
from pathlib import Path
from datetime import datetime
from typing import List, Optional


# ============================================
# CONFIGURAÇÃO
# ============================================

ARQUIVO_DADOS = Path("tasks.json")


# ============================================
# MODELO
# ============================================

class Task:
    \"\"\"Representa uma tarefa.\"\"\"

    def __init__(self, titulo: str, descricao: str = "") -> None:
        self.id: Optional[int] = None
        self.titulo = titulo
        self.descricao = descricao
        self.criada_em = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.concluida = False

    def to_dict(self) -> dict:
        \"\"\"Converte a task pra dicionário (para salvar em JSON).\"\"\"
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "criada_em": self.criada_em,
            "concluida": self.concluida,
        }

    @staticmethod
    def from_dict(dados: dict) -> "Task":
        \"\"\"Cria uma Task a partir de um dicionário.\"\"\"
        task = Task(titulo=dados["titulo"], descricao=dados["descricao"])
        task.id = dados["id"]
        task.criada_em = dados["criada_em"]
        task.concluida = dados["concluida"]
        return task


# ============================================
# SERVIÇO (lógica de negócio)
# ============================================

class ServicoTasks:
    \"\"\"Gerencia todas as operações com tasks.\"\"\"

    def __init__(self) -> None:
        self.tasks: List[Task] = self._carregar()

    def _carregar(self) -> List[Task]:
        \"\"\"Carrega tasks do arquivo JSON.\"\"\"
        if not ARQUIVO_DADOS.exists():
            return []
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            dados = json.load(f)
        return [Task.from_dict(t) for t in dados]

    def _salvar(self) -> None:
        \"\"\"Salva tasks no arquivo JSON.\"\"\"
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tasks], f, ensure_ascii=False, indent=2)

    def _proximo_id(self) -> int:
        \"\"\"Gera o próximo ID disponível.\"\"\"
        if not self.tasks:
            return 1
        return max(t.id for t in self.tasks) + 1

    def adicionar(self, titulo: str, descricao: str = "") -> Task:
        \"\"\"Adiciona uma nova task.\"\"\"
        task = Task(titulo=titulo, descricao=descricao)
        task.id = self._proximo_id()
        self.tasks.append(task)
        self._salvar()
        return task

    def concluir(self, task_id: int) -> Optional[Task]:
        \"\"\"Marca uma task como concluída.\"\"\"
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.concluida = True
            self._salvar()
        return task

    def remover(self, task_id: int) -> bool:
        \"\"\"Remove uma task pelo ID.\"\"\"
        tamanho_original = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        if len(self.tasks) < tamanho_original:
            self._salvar()
            return True
        return False

    def listar(self, apenas_pendentes: bool = False) -> List[Task]:
        \"\"\"Retorna lista de tasks, opcionalmente apenas pendentes.\"\"\"
        if apenas_pendentes:
            return [t for t in self.tasks if not t.concluida]
        return self.tasks


# ============================================
# INTERFACE (exibição e interação)
# ============================================

def exibir_tasks(tasks: List[Task]) -> None:
    \"\"\"Exibe uma lista de tasks formatada.\"\"\"
    if not tasks:
        print("  Nenhuma task encontrada.\\n")
        return

    print(f"\\n  {'ID':<5} {'Status':<10} {'Título':<30} {'Criada em'}")
    print(f"  {'-'*60}")
    for t in tasks:
        status = "✓ Feita" if t.concluida else "○ Pendente"
        print(f"  {t.id:<5} {status:<10} {t.titulo:<30} {t.criada_em}")
    print()


def menu_principal(servico: ServicoTasks) -> None:
    \"\"\"Loop principal do menu.\"\"\"
    while True:
        print("=== Gerenciador de Tasks ===")
        print("  1. Listar todas as tasks")
        print("  2. Listar tasks pendentes")
        print("  3. Adicionar task")
        print("  4. Concluir task")
        print("  5. Remover task")
        print("  0. Sair\\n")

        opcao = input("  Sua escolha: ").strip()

        if opcao == "1":
            exibir_tasks(servico.listar())
        elif opcao == "2":
            exibir_tasks(servico.listar(apenas_pendentes=True))
        elif opcao == "3":
            titulo = input("  Título: ").strip()
            if titulo:
                task = servico.adicionar(titulo)
                print(f"  Task #{task.id} criada!\\n")
        elif opcao == "4":
            task_id = input("  ID da task: ").strip()
            if task_id.isdigit() and servico.concluir(int(task_id)):
                print(f"  Task #{task_id} concluída!\\n")
            else:
                print("  Task não encontrada.\\n")
        elif opcao == "5":
            task_id = input("  ID da task: ").strip()
            if task_id.isdigit() and servico.remover(int(task_id)):
                print(f"  Task #{task_id} removida!\\n")
            else:
                print("  Task não encontrada.\\n")
        elif opcao == "0":
            print("  Até mais!")
            break
        else:
            print("  Opção inválida.\\n")


def main():
    servico = ServicoTasks()
    menu_principal(servico)


if __name__ == "__main__":
    main()

# ARQUITETURA DO PROJETO:
# 1. Modelo (Task)     -> estrutura de dados, conversão JSON
# 2. Serviço           -> lógica de negócio, persistência
# 3. Interface         -> menus, exibição, input do usuário
# 4. main()            -> apenas conecta as partes"""
    },

    # =============================================
    # TEMA 8: VIBE CODING
    # =============================================
    {
        "instruction": "O que é Vibe Coding e como usar IA para programar de forma organizada?",
        "input": "",
        "output": """# ============================================
# GUIA: Vibe Coding com IA
# Objetivo: Usar IA como ferramenta de desenvolvimento
# sem perder controle da arquitetura do código
# ============================================

# ============================================
# O QUÉ É VIBE CODING?
# ============================================
# Vibe Coding é a prática de usar IAs (como ChatGPT,
# Claude, Copilot) para gerar código rapidamente.
# O conceito foi popularizado por Andrej Karpathy (2025).
#
# A ideia NÃO é delegar tudo à IA blindamente.
# É usar a IA como um assistente que acelera o
# desenvolvimento, mas você mantém o controle.
# ============================================

# ============================================
# BOAS PRÁTICAS DE VIBE CODING
# ============================================

# 1. DEFINA A ARQUITETURA PRIMEIRO, depois peça código
# ============================================
# ERRADO: "Me faz um app de gerenciador de tasks"
# CERTO:  "Preciso de uma classe Task com os seguintes
#          métodos: adicionar, concluir, remover.
#          Siga o padrão Repository pra persistência."
# ============================================

# 2. PEÇA UMA COISA DE VEZ
# ============================================
# ERRADO: "Me faz um app completo com login, API, banco"
# CERTO:  "Me faz apenas o modelo Usuario com validação"
# Depois: "Agora me faz o serviço de autenticação"
# ============================================

# 3. REVISE SEMPRE O CÓDIGO GERADO
# ============================================
# A IA pode gerar código que funciona mas não segue
# boas práticas. Sempre revise antes de usar.
# ============================================

# ============================================
# EXEMPLO PRÁTICO: Prompt bem estruturado
# ============================================

# Exemplo de prompt que gera código organizado:
EXEMPLO_PROMPT = \"\"\"
Cria uma classe Python chamada 'Calculadora' com:

Requisitos:
- Operações: soma, subtração, multiplicação, divisão
- Tratamento de divisão por zero
- Histórico das últimas 10 operações
- Método para limpar o histórico

Padrões a seguir:
- Type hints em todos os métodos
- Docstrings em todas as funções
- Métodos com uma única responsabilidade
- Separar lógica de exibição

Não inclua código de exemplo no main(), apenas a classe.
\"\"\"

# ============================================
# O CÓDIGO GERADO (exemplo do que a IA retorna):
# ============================================

from typing import List, Tuple
from collections import deque


class Calculadora:
    \"\"\"
    Calculadora básica com histórico de operações.
    \"\"\"

    MAX_HISTORICO = 10

    def __init__(self) -> None:
        self._historico: deque = deque(maxlen=self.MAX_HISTORICO)

    def _registrar(self, operacao: str, resultado: float) -> None:
        \"\"\"Registra uma operação no histórico.\"\"\"
        self._historico.append({"operacao": operacao, "resultado": resultado})

    def somar(self, a: float, b: float) -> float:
        \"\"\"Retorna a soma de dois números.\"\"\"
        resultado = a + b
        self._registrar(f"{a} + {b}", resultado)
        return resultado

    def subtrair(self, a: float, b: float) -> float:
        \"\"\"Retorna a subtração de dois números.\"\"\"
        resultado = a - b
        self._registrar(f"{a} - {b}", resultado)
        return resultado

    def multiplicar(self, a: float, b: float) -> float:
        \"\"\"Retorna a multiplicação de dois números.\"\"\"
        resultado = a * b
        self._registrar(f"{a} * {b}", resultado)
        return resultado

    def dividir(self, a: float, b: float) -> float:
        \"\"\"
        Retorna a divisão de dois números.

        Raises:
            ZeroDivisionError: Se o divisor for zero.
        \"\"\"
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        resultado = a / b
        self._registrar(f"{a} / {b}", resultado)
        return resultado

    def historico(self) -> List[dict]:
        \"\"\"Retorna o histórico de operações.\"\"\"
        return list(self._historico)

    def limpar_historico(self) -> None:
        \"\"\"Limpa o histórico de operações.\"\"\"
        self._historico.clear()


# ============================================
# USANDO A CALCULADORA
# ============================================

def main():
    calc = Calculadora()

    print(f"  10 + 5  = {calc.somar(10, 5)}")
    print(f"  20 - 8  = {calc.subtrair(20, 8)}")
    print(f"  4 * 7   = {calc.multiplicar(4, 7)}")
    print(f"  15 / 3  = {calc.dividir(15, 3)}\\n")

    print("=== Histórico ===")
    for op in calc.historico():
        print(f"  {op['operacao']} = {op['resultado']}")


if __name__ == "__main__":
    main()

# ============================================
# RESUMO: WORKFLOW DO VIBE CODING ORGANIZADO
# ============================================
# 1. Planejar a arquitetura (no papel ou comments)
# 2. Escrever prompts específicos e claros
# 3. Revisar o código gerado pela IA
# 4. Testar cada parte antes de continuar
# 5. Refatorar se necessário
#
# A IA acelera, mas você dirige!
# ============================================"""
    },
    {
        "instruction": "Como usar IA para refatorar código existente mantendo a arquitetura?",
        "input": "",
        "output": """# ============================================
# EXEMPLO: Refatoração com IA (Vibe Coding)
# Objetivo: Mostrar como pedir à IA pra melhorar código
# sem quebrar a estrutura existente
# ============================================

# ============================================
# CÓDIGO ORIGINAL (antes da refatoração)
# ============================================

# Esse código funciona, mas tem problemas:
# - Sem type hints
# - Sem docstrings
# - Funções grandes e com múltiplas responsabilidades
# - Sem tratamento de erros

def processar_dados_original(dados):
    resultado = []
    for item in dados:
        if item["valor"] > 0:
            item["valor"] = item["valor"] * 1.1
            item["status"] = "processado"
            resultado.append(item)
        else:
            print(f"Item inválido: {item}")
    return resultado


# ============================================
# PROMPT PARA A IA REFATORAR
# ============================================

PROMPT_REFATORACAO = \"\"\"
Refatore o código abaixo seguindo essas regras:
- Adicione type hints em todos os métodos
- Adicione docstrings descritivas
- Divida funções grandes em funções menores
- Adicione tratamento de erros
- Mantenha a mesma lógica de negócio
- NÃO mude a estrutura de dados (entrada e saída)

Código a refatorar:
[cole o código aqui]
\"\"\"


# ============================================
# CÓDIGO REFATORADO (resultado da IA + revisão)
# ============================================

from typing import Dict, List, Tuple


class ErroItemInvalido(Exception):
    \"\"\"Erro lançado quando um item possui valor inválido.\"\"\"
    pass


def validar_item(item: Dict) -> bool:
    \"\"\"
    Valida se um item possui valor positivo.

    Args:
        item: Dicionário com chave 'valor'.

    Returns:
        True se o valor for positivo, False caso contrário.
    \"\"\"
    return item.get("valor", 0) > 0


def aplicar_aumento(item: Dict, porcentagem: float = 0.10) -> Dict:
    \"\"\"
    Aplica um aumento percentual ao valor do item.

    Args:
        item: Dicionário com chave 'valor'.
        porcentagem: Percentual de aumento (default 10%).

    Returns:
        Item com valor atualizado e status 'processado'.
    \"\"\"
    item["valor"] = round(item["valor"] * (1 + porcentagem), 2)
    item["status"] = "processado"
    return item


def separar_validos_invalidos(dados: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    \"\"\"
    Separa items válidos dos inválidos.

    Returns:
        Tupla com (items_válidos, items_inválidos).
    \"\"\"
    validos = []
    invalidos = []

    for item in dados:
        if validar_item(item):
            validos.append(item)
        else:
            invalidos.append(item)

    return validos, invalidos


def processar_dados(dados: List[Dict], porcentagem: float = 0.10) -> List[Dict]:
    \"\"\"
    Processa uma lista de dados aplicando aumento nos válidos.

    Args:
        dados: Lista de dicionários com chave 'valor'.
        porcentagem: Percentual de aumento a aplicar.

    Returns:
        Lista com apenas os items processados.
    \"\"\"
    validos, invalidos = separar_validos_invalidos(dados)

    # Reportando items inválidos
    for item in invalidos:
        print(f"  [AVISO] Item ignorado - valor inválido: {item}")

    # Processando items válidos
    return [aplicar_aumento(item, porcentagem) for item in validos]


def main():
    dados = [
        {"nome": "Produto A", "valor": 100.00},
        {"nome": "Produto B", "valor": -50.00},   # Inválido
        {"nome": "Produto C", "valor": 200.00},
        {"nome": "Produto D", "valor": 0},         # Inválido
    ]

    print("=== Processando Dados ===\\n")
    resultado = processar_dados(dados, porcentagem=0.10)

    print("\\n=== Resultado ===")
    for item in resultado:
        print(f"  {item['nome']}: R$ {item['valor']}")


if __name__ == "__main__":
    main()

# ============================================
# O QUE MUDOU NA REFATORAÇÃO:
# ============================================
# 1. Função grande dividida em 3 pequenas e focadas
# 2. Type hints adicionados em toda a interface
# 3. Docstrings explicam entrada, saída e comportamento
# 4. Separação entre validação, processamento e exibição
# 5. A lógica de negócio permaneceu exatamente a mesma
#
# IMPORTANTE: A IA fez 90% do trabalho, mas foi
# necessário revisar e ajustar alguns detalhes.
# ============================================"""
    },
    {
        "instruction": "Como estruturar prompts para gerar código Python organizado com IA?",
        "input": "",
        "output": """# ============================================
# GUIA: Estruturando Prompts para Código Organizado
# Objetivo: Templates de prompt que geram código de alta qualidade
# ============================================

# ============================================
# TEMPLATE 1: Criando uma classe
# ============================================

TEMPLATE_CLASSE = \"\"\"
Cria uma classe Python para [FUNCIONALIDADE].

Nome da classe: [NOME]

Atributos:
- [atributo1]: [tipo] - [descrição]
- [atributo2]: [tipo] - [descrição]

Métodos necessários:
- [método1]: [o que ele faz]
- [método2]: [o que ele faz]

Requisitos de qualidade:
- Type hints em todos os métodos
- Docstrings completas (Args, Returns, Raises)
- Métodos com uma única responsabilidade
- Tratamento de erros específico

Não inclua código de exemplo, apenas a classe.
\"\"\"

# ============================================
# TEMPLATE 2: Criando uma API
# ============================================

TEMPLATE_API = \"\"\"
Cria uma API REST em Python usando Flask.

Recurso principal: [NOME DO RECURSO]

Endpoints necessários:
- GET  /[recurso]      - Listar todos
- GET  /[recurso]/{id} - Buscar por ID
- POST /[recurso]      - Criar novo
- PUT  /[recurso]/{id} - Atualizar

Estrutura de dados:
{
    "campo1": "tipo",
    "campo2": "tipo"
}

Requisitos:
- Separar rotas, serviço e modelo em funções distintas
- Status codes corretos (200, 201, 400, 404)
- Validação de entrada nos endpoints POST e PUT
- Tratamento de erros centralizado
\"\"\"

# ============================================
# TEMPLATE 3: Refatorando código existente
# ============================================

TEMPLATE_REFATORACAO = \"\"\"
Refatore o código abaixo sem mudar a lógica de negócio:

[COLE O CÓDIGO AQUI]

Regras de refatoração:
1. Adicione type hints em toda a interface pública
2. Adicione docstrings (descrição, Args, Returns)
3. Divida funções com mais de 15 linhas
4. Separe validação da lógica principal
5. Adicione tratamento de erros específico
6. Mantenha a mesma entrada e saída

Entregue apenas o código refatorado, sem explicações.
\"\"\"

# ============================================
# EXEMPLO PRÁTICO: Usando os templates
# ============================================

# Exemplo de prompt usando o Template 1:
EXEMPLO_PROMPT_CLASSE = \"\"\"
Cria uma classe Python para gerenciar produtos de um e-commerce.

Nome da classe: Produto

Atributos:
- nome: str - Nome do produto
- preco: float - Preço unitário (deve ser positivo)
- estoque: int - Quantidade disponível

Métodos necessários:
- adicionar_estoque(quantidade): Adiciona unidades ao estoque
- remover_estoque(quantidade): Remove unidades (com validação)
- aplicar_desconto(porcentagem): Aplica desconto no preço
- valor_total(): Retorna preço * estoque

Requisitos de qualidade:
- Type hints em todos os métodos
- Docstrings completas (Args, Returns, Raises)
- Métodos com uma única responsabilidade
- Tratamento de erros específico

Não inclua código de exemplo, apenas a classe.
\"\"\"


# ============================================
# RESULTADO DO PROMPT ACIMA:
# ============================================

class Produto:
    \"\"\"Representa um produto de um e-commerce.\"\"\"

    def __init__(self, nome: str, preco: float, estoque: int = 0) -> None:
        \"\"\"
        Inicializa um produto.

        Args:
            nome: Nome do produto.
            preco: Preço unitário (deve ser positivo).
            estoque: Quantidade inicial no estoque.

        Raises:
            ValueError: Se o preço for menor ou igual a zero.
        \"\"\"
        if preco <= 0:
            raise ValueError("O preço deve ser positivo.")
        self.nome = nome
        self._preco = preco
        self._estoque = estoque

    @property
    def preco(self) -> float:
        \"\"\"Retorna o preço atual do produto.\"\"\"
        return self._preco

    @property
    def estoque(self) -> int:
        \"\"\"Retorna a quantidade atual no estoque.\"\"\"
        return self._estoque

    def adicionar_estoque(self, quantidade: int) -> None:
        \"\"\"
        Adiciona unidades ao estoque.

        Args:
            quantidade: Número de unidades a adicionar (deve ser positivo).

        Raises:
            ValueError: Se a quantidade for menor ou igual a zero.
        \"\"\"
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser positiva.")
        self._estoque += quantidade

    def remover_estoque(self, quantidade: int) -> None:
        \"\"\"
        Remove unidades do estoque.

        Args:
            quantidade: Número de unidades a remover.

        Raises:
            ValueError: Se a quantidade for inválida ou insuficiente.
        \"\"\"
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser positiva.")
        if quantidade > self._estoque:
            raise ValueError(f"Estoque insuficiente. Disponível: {self._estoque}")
        self._estoque -= quantidade

    def aplicar_desconto(self, porcentagem: float) -> None:
        \"\"\"
        Aplica um desconto percentual no preço.

        Args:
            porcentagem: Desconto em porcentagem (0-100).

        Raises:
            ValueError: Se a porcentagem for fora do intervalo válido.
        \"\"\"
        if not 0 < porcentagem < 100:
            raise ValueError("A porcentagem deve estar entre 0 e 100.")
        self._preco -= self._preco * (porcentagem / 100)
        self._preco = round(self._preco, 2)

    def valor_total(self) -> float:
        \"\"\"Retorna o valor total do produto no estoque.\"\"\"
        return round(self._preco * self._estoque, 2)

    def __str__(self) -> str:
        return f"{self.nome} | R$ {self._preco:.2f} | Estoque: {self._estoque}"


def main():
    produto = Produto(nome="Notebook", preco=5000.00, estoque=10)
    print(produto)

    produto.aplicar_desconto(10)
    print(f"Após desconto de 10%: {produto}")

    produto.adicionar_estoque(5)
    print(f"Após adicionar 5 unidades: {produto}")

    print(f"Valor total no estoque: R$ {produto.valor_total()}")


if __name__ == "__main__":
    main()

# ============================================
# DICAS FINAIS PARA PROMPTS EFICAZES:
# ============================================
# 1. Seja específico sobre o que você quer
# 2. Defina os tipos de dados esperados
# 3. Peça padrões de qualidade explicitamente
# 4. Peça uma coisa de vez (não tudo junto)
# 5. Sempre revise o código gerado antes de usar
# ============================================"""
    },
]

# Salvando o dataset
with open("dataset_completo.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"Dataset completo gerado com {len(dataset)} exemplos!")
print("\nResumo por tema:")
temas = {
    "Classes e OOP": 3,
    "Listas e Dicionários": 2,
    "Tratamento de Erros": 2,
    "Leitura e Escrita de Arquivos": 2,
    "APIs e Requisições HTTP": 2,
    "Estrutura de Diretórios": 1,
    "Projetos Completos": 2,
    "Vibe Coding": 3,
}
for tema, quantidade in temas.items():
    print(f"  {tema}: {quantidade} exemplos")
