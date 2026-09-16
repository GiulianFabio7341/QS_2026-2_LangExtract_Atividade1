# Projeto

Script para executar os testes de extração de informações do texto de arquivos usando o LangExtract e o modelo local `gemma2:2b`.

## Pré-requisitos

- Python 3.10 ou superior
- [Ollama](https://ollama.com/) instalado e em execução
- Modelo baixado:

```bash
ollama pull gemma2:2b
```

## Instalação

Com o ambiente virtual ativado, instale a dependência:

```bash
pip install langextract
```

## Como rodar

Na raiz do projeto, execute:

```bash
python main.py
```

O script executa os 5 prompts três vezes cada e registra os resultados em `evidencias_variabilidade.txt`.
