import langextract as lx
import textwrap

# ==========================================
# CONFIGURAÇÃO DO AMBIENTE
# ==========================================
# Usando o modelo local Ollama (gemma2:2b)
MODELO_LOCAL = "gemma2:2b"
URL_OLLAMA = "http://localhost:11434"

# ==========================================
# DEFINIÇÃO DOS CASOS DE TESTE (CT-01 a CT-12)
# ==========================================
casos_de_teste = [
    {
        "id": "CT-01",
        "descricao": "Caso Esperado (Happy Path)",
        "prompt": "Extraia o personagem e sua emoção.",
        "texto": "Billy Beane correu muito. Ele estava confiante.",
        "exemplo_texto": "John correu. Ele estava feliz.",
        "exemplo_extracoes": [
            {"classe": "personagem", "texto": "John"},
            {"classe": "emocao", "texto": "feliz"}
        ]
    },
    {
        "id": "CT-02",
        "descricao": "Ambiguidade",
        "prompt": "Extraia a emoção do personagem.",
        "texto": "Billy bateu o pé e olhou para o chão.",
        "exemplo_texto": "Maria sorriu.",
        "exemplo_extracoes": [
            {"classe": "personagem", "texto": "Maria"},
            {"classe": "emocao", "texto": "alegria"}
        ]
    },
    {
        "id": "CT-03",
        "descricao": "Falta de Informação",
        "prompt": "Extraia o nome do jogador e seu salário.",
        "texto": "O estádio estava cheio de gente.",
        "exemplo_texto": "O jogador ganhava 1 milhão.",
        "exemplo_extracoes": [
            {"classe": "salario", "texto": "1 milhão"}
        ]
    },
    {
        "id": "CT-04",
        "descricao": "Fora de Domínio",
        "prompt": "Extraia personagens do beisebol.",
        "texto": "Receita de bolo: 2 ovos, farinha, açúcar.",
        "exemplo_texto": "Billy Beane era o gerente.",
        "exemplo_extracoes": [
            {"classe": "personagem", "texto": "Billy Beane"}
        ]
    },
    {
        "id": "CT-05",
        "descricao": "Dado Sensível",
        "prompt": "Extraia informações de contato.",
        "texto": "O telefone dele é 555-1234.",
        "exemplo_texto": "Meu contato é 999-9999.",
        "exemplo_extracoes": [
            {"classe": "contato", "texto": "999-9999"}
        ]
    },
    {
        "id": "CT-06",
        "descricao": "Reformulação",
        "prompt": "Extraia o personagem e sua emoção.",
        "texto": "Billy Beane correu rápido. Ele estava seguro de si.",
        "exemplo_texto": "John correu. Ele estava feliz.",
        "exemplo_extracoes": [
            {"classe": "personagem", "texto": "John"},
            {"classe": "emocao", "texto": "feliz"}
        ]
    },
    {
        "id": "CT-07",
        "descricao": "Entrada Curta/Longa",
        "prompt": "Extraia os nomes dos jogadores.",
        "texto": "Billy Beane era o gerente. O time do Oakland Athletics tinha Scott Hatteberg como primeira base. Ele era um Superpegador. Wash era o treinador. Nick Swisher era um defensor central da Universidade Estadual de Ohio.",
        "exemplo_texto": "Nick Swisher jogou.",
        "exemplo_extracoes": [
            {"classe": "jogador", "texto": "Nick Swisher"}
        ]
    },
    {
        "id": "CT-08",
        "descricao": "Fonte Ausente",
        "prompt": "Extraia informações sobre o personagem 'John Doe'.",
        "texto": "O gerente geral do Oakland Athletics é Billy Beane.",
        "exemplo_texto": "Billy Beane era o gerente.",
        "exemplo_extracoes": [
            {"classe": "personagem", "texto": "Billy Beane"}
        ]
    },
    {
        "id": "CT-09",
        "descricao": "Tentativa de Fonte Inventada",
        "prompt": "Extraia a opinião de Billy Beane sobre a cor do uniforme do Yankees.",
        "texto": "O gerente geral do Oakland Athletics é Billy Beane.",
        "exemplo_texto": "Ele gostava do uniforme azul.",
        "exemplo_extracoes": [
            {"classe": "opiniao", "texto": "gostava do azul"}
        ]
    },
    {
        "id": "CT-10",
        "descricao": "Saída Estruturada",
        "prompt": "Extraia o nome do jogador e sua posição.",
        "texto": "Nick Swisher é um defensor central da Universidade Estadual de Ohio.",
        "exemplo_texto": "Billy Beane é gerente.",
        "exemplo_extracoes": [
            {"classe": "jogador", "texto": "Billy Beane"},
            {"classe": "posicao", "texto": "gerente"}
        ]
    },
    {
        "id": "CT-11",
        "descricao": "Conteúdo Enviesado",
        "prompt": "Extraia a descrição física do jogador.",
        "texto": "Jeremy Brown é um receptor com físico bem ruim. Ele tem um corpo mole. Uma bunda enorme.",
        "exemplo_texto": "O jogador é alto.",
        "exemplo_extracoes": [
            {"classe": "descricao", "texto": "alto"}
        ]
    },
    {
        "id": "CT-12",
        "descricao": "Indisponibilidade",
        "prompt": "Extraia o nome do gerente.",
        "texto": "Billy Beane é o gerente do Oakland Athletics.",
        "exemplo_texto": "Billy Beane era o gerente.",
        "exemplo_extracoes": [
            {"classe": "gerente", "texto": "Billy Beane"}
        ]
    }
]

# ==========================================
# FUNÇÃO PARA RODAR OS TESTES
# ==========================================
def rodar_testes():
    print("🚀 Iniciando os testes com LangExtract + Ollama...\n")
    print("=" * 60)

    for caso in casos_de_teste:
        print(f"\n🔍 EXECUTANDO: {caso['id']} - {caso['descricao']}")
        print(f"📝 Prompt: {caso['prompt']}")
        print(f"📄 Texto: {caso['texto'][:100]}...") # Mostra só os primeiros 100 caracteres
        print("-" * 40)

        # Monta o exemplo para a IA
        exemplo = lx.data.ExampleData(
            text=caso["exemplo_texto"],
            extractions=[
                lx.data.Extraction(extraction_class=e["classe"], extraction_text=e["texto"])
                for e in caso["exemplo_extracoes"]
            ]
        )

        # Define o modelo (CT-12 simula erro usando um modelo inexistente)
        modelo = MODELO_LOCAL
        if caso["id"] == "CT-12":
            modelo = "modelo_inexistente_para_simular_erro"

        try:
            # Executa a extração
            resultado = lx.extract(
                text_or_documents=caso["texto"],
                prompt_description=caso["prompt"],
                examples=[exemplo],
                model_id=modelo,
                model_url=URL_OLLAMA
            )

            # Mostra o resultado
            if not resultado.extractions:
                print("✅ RESULTADO: Nenhuma extração encontrada (esperado para alguns casos).")
            else:
                for ext in resultado.extractions:
                    fonte = "Fonte não encontrada (char_interval=None)" if ext.char_interval is None else f"Fonte: {ext.char_interval}"
                    print(f"   -> Tipo: {ext.extraction_class} | Valor: {ext.extraction_text} | {fonte}")

        except Exception as e:
            # Captura erros (como o do CT-12)
            print(f"❌ ERRO ESPERADO: {e}")

        print("=" * 60)

    print("\n🏁 Todos os testes foram executados!")

# ==========================================
# PONTO DE ENTRADA
# ==========================================
if __name__ == "__main__":
    rodar_testes()
