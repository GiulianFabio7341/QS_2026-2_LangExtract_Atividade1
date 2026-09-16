# Declaração de Uso de IA Generativa

**Disciplina:** Qualidade de Software (2026.2)
**Projeto Avaliado:** LangExtract
**Responsável:** Pedro Miguel Castro França — Matrícula 202300061741

---

## 1. Ferramenta Utilizada

| Aspecto | Informação |
| :--- | :--- |
| **Ferramenta** | DeepSeek (modelo de linguagem) |
| **Versão/Família** | DeepSeek V3 |
| **Plataforma de Acesso** | Interface web oficial |
| **Período de Uso** | Setembro de 2026 |

---

## 2. Finalidade do Uso

A IA foi utilizada como **ferramenta de apoio** para:
- Estruturar a seção de Casos de Teste do relatório técnico.
- Gerar o script Python base para execução dos 12 casos de teste com o LangExtract.
- Revisar a redação técnica da análise de resultados.
- Auxiliar na organização do repositório (formatação Markdown).

**A IA não foi utilizada** para gerar conclusões técnicas, análises de qualidade ou julgamentos sobre os resultados — esses foram realizados pelo autor com base nos dados reais obtidos da execução.

---

## 3. Prompts Utilizados (5 mais relevantes)

1. *"Como estruturar uma seção de casos de teste para uma atividade de Qualidade de Software baseada na ISO/IEC 25010?"*
2. *"Gere um script Python que execute 12 casos de teste no LangExtract com o modelo gemma2:2b via Ollama."*
3. *"Como interpretar o resultado 'char_interval=None' retornado pelo LangExtract?"*
4. *"Crie um template de Dashboard Markdown para consolidação de resultados de testes."*
5. *"Formate uma tabela de casos de teste em Markdown seguindo o padrão A/P/R."*

---

## 4. Sugestões Aproveitadas, Corrigidas e Rejeitadas

### ✅ Aproveitadas
- Estrutura da tabela de casos de teste (7 colunas).
- Script Python base para execução dos testes.
- Template de dashboard de resultados.
- Conexão entre casos de teste e requisitos de qualidade (REQ-XX).

### ✏️ Corrigidas
- A IA sugeriu inicialmente extrair "todo o Capítulo 1" para o caso CT-07. **Corrigi** para trechos do Capítulo 8, pois o Capítulo 1 era muito extenso e causava timeout.
- A IA sugeriu usar API Key do Gemini. **Corrigi** para usar modelo local Ollama (`gemma2:2b`), por ser gratuito e rodar offline.

### ❌ Rejeitadas
- A IA sugeriu incluir casos de teste específicos para análise de sentimento, o que fugia do escopo da atividade.
- A IA propôs uma conclusão que afirmava que "o LangExtract é confiável para produção". **Rejeitei** porque os dados reais mostraram o contrário (falhas em CT-04, CT-05 e CT-02).

---

## 5. Erros da IA Identificados

| Erro | Descrição | Verificação Aplicada |
| :--- | :--- | :--- |
| **Alucinação técnica** | Sugeriu que o LangExtract processa PDFs diretamente | Verificado no README oficial: aceita apenas texto bruto |
| **Premissa incorreta** | Assumiu que o modelo `gemma2:2b` seria determinístico | Testes de variabilidade (Seção 6) provaram o contrário |
| **Conclusão apressada** | Afirmou que a ferramenta "não tem falhas críticas" | Rejeitado após execução dos testes CT-04 e CT-05 |

---

## 6. Verificações Realizadas

Todos os outputs da IA foram verificados por meio de:
- **Execução real** dos 12 casos de teste no ambiente local.
- **Comparação** das sugestões com a documentação oficial do LangExtract.
- **Validação cruzada** com os requisitos especificados na Seção 3 do relatório (REQ-01 a REQ-10).
- **Revisão manual** da redação e adequação técnica de cada parágrafo.

---

## 7. Contribuição Individual

A IA atuou exclusivamente como **ferramenta de apoio à escrita e estruturação**. Todas as decisões técnicas, análises de resultado, classificações de status (A/P/R) e conclusões foram realizadas pelo autor, com base em evidências obtidas pela execução real da ferramenta LangExtract.

**Nenhuma seção deste trabalho teve a IA como autoridade única de avaliação.**

---

*Assinatura: Pedro Miguel Castro França*
*Data: 16/09/2026*