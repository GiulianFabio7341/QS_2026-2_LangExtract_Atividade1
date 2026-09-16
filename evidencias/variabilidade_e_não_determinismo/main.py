import langextract as lx
import datetime
import time
import json

# 1. Carregar o trecho reduzido do Capítulo 8
caminho_arquivo = "docs/exemplo_dados.txt"
with open(caminho_arquivo, "r", encoding="utf-8") as f:
    texto_capitulo8 = f.read()

# 2. Estruturando cada prompt com seu próprio exemplo específico para guiar o modelo
tarefas = [
    {
        "id": 1,
        "prompt": "Extraia os nomes de todas as pessoas (personagens) mencionadas no texto e adicione o atributo 'papel' indicando se é jogador, técnico, executivo ou cônjuge.",
        "exemplo": lx.data.ExampleData(
            text="Billy Beane era o gerente geral, enquanto Wash treinava o time.",
            extractions=[
                lx.data.Extraction(extraction_class="personagem", extraction_text="Billy Beane", attributes={"papel": "executivo"}),
                lx.data.Extraction(extraction_class="personagem", extraction_text="Wash", attributes={"papel": "técnico"})
            ]
        )
    },
    {
        "id": 2,
        "prompt": "Extraia as menções a Scott Hatteberg e adicione um atributo 'autoavaliacao_ou_status' resumindo como ele se via ou como era avaliado em relação à sua nova posição (primeira base).",
        "exemplo": lx.data.ExampleData(
            text="Hatty sentia que não era um jogador de verdade, mas Wash o via como um superpegador.",
            extractions=[
                lx.data.Extraction(extraction_class="avaliacao", extraction_text="Hatty", attributes={"autoavaliacao_ou_status": "sentia que não era um jogador de verdade"})
            ]
        )
    },
    {
        "id": 3,
        "prompt": "Extraia os nomes dos times da Liga Nacional de Futebol Americano (NFL) mencionados no texto e os valores exatos de seus patrocínios.",
        "exemplo": lx.data.ExampleData(
            text="O Dallas Cowboys assinou um patrocínio de 10 milhões.",
            extractions=[
                lx.data.Extraction(extraction_class="time_nfl", extraction_text="Dallas Cowboys", attributes={"patrocinio": "10 milhões"})
            ]
        )
    },
    {
        "id": 4,
        "prompt": "Extraia os nomes dos jogadores de beisebol citados e atribua a chave 'perfil_rebatedor' preenchida estritamente com 'Estrela' ou 'Analítico/Secundário'.",
        "exemplo": lx.data.ExampleData(
            text="Jason Giambi era o astro, mas Jeremy Giambi tinha paciência no bastão.",
            extractions=[
                lx.data.Extraction(extraction_class="jogador", extraction_text="Jason Giambi", attributes={"perfil_rebatedor": "Estrela"}),
                lx.data.Extraction(extraction_class="jogador", extraction_text="Jeremy Giambi", attributes={"perfil_rebatedor": "Analítico/Secundário"})
            ]
        )
    },
    {
        "id": 5,
        "prompt": "Extraia as métricas estatísticas ou características secundárias de rebatida valorizadas pela diretoria (como aproveitamento em base ou contagem de strikes), indicando o atributo 'valor_para_o_time'.",
        "exemplo": lx.data.ExampleData(
            text="Eles valorizavam a paciência no bastão, pois evitava eliminações.",
            extractions=[
                lx.data.Extraction(extraction_class="metrica", extraction_text="paciência no bastão", attributes={"valor_para_o_time": "evitava eliminações"})
            ]
        )
    }
]

# 3. Execução iterativa
for tarefa in tarefas:
    print(f"\n========================================")
    print(f"Executando Teste para o PROMPT {tarefa['id']}")
    print(f"========================================")
    
    for rep in range(1, 4):
        agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"--- Prompt {tarefa['id']} | Repetição {rep} | Início: {agora} ---")
        
        try:
            # Chamada usando o modelo local via Ollama
            resultado = lx.extract(
                text_or_documents=texto_capitulo8,
                prompt_description=tarefa["prompt"],
                examples=[tarefa["exemplo"]], # Passando o exemplo exato da tarefa atual
                model_id="gemma2:2b",
                model_url="http://localhost:11434",
                language_model_params={"temperature": 0.7}
            )
            
            # Construindo uma lista de dicionários para conversão em JSON limpo
            extracoes_json = []
            for e in resultado.extractions:
                if e.char_interval: # Garante que a entidade foi realmente encontrada no texto
                    extracoes_json.append({
                        "entidade_encontrada": e.extraction_text,
                        "atributos": e.attributes
                    })
            
            # Converte a lista para uma string JSON indentada
            resultado_formatado = json.dumps(extracoes_json, ensure_ascii=False, indent=4)
            
            # Grava no log
            with open("evidencias_variabilidade.txt", "a", encoding="utf-8") as log:
                log.write(f"\n[Prompt {tarefa['id']}] Repetição: {rep} | Data/Hora: {agora} | Modelo: gemma2:2b (Temp: 0.7)\n")
                log.write(f"Texto do Prompt: {tarefa['prompt']}\n")
                log.write(f"Total de Entidades Encontradas: {len(extracoes_json)}\n")
                log.write(f"Resultados Extraídos:\n{resultado_formatado}\n")
                log.write("-" * 60 + "\n")
                
            print(f"Sucesso na Repetição {rep}. Log gerado em JSON.")
            
        except Exception as e:
            print(f"Erro na execução da repetição {rep}: {e}")
        
        # Pausa para estabilidade do servidor
        time.sleep(2)

print("\nConcluído! Verifique o arquivo 'evidencias_em_json.txt'.")