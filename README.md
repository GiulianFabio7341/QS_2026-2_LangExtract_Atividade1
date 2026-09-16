# Qualidade de Software — AV1: Avaliação do LangExtract

> **Disciplina:** Qualidade de Software (2026.2)  
> **Atividade:** AV1 — Especificação e avaliação inicial da qualidade de uma aplicação de IA generativa  
> **Projeto Avaliado:** [LangExtract](https://github.com/google/langextract) (Google LLC)

---

## 🎥 Vídeo da Atividade

A apresentação e demonstração da equipe está disponível no link abaixo:

> 🔗 **[Inserir URL do Vídeo Aqui]**
>
> 📄 Arquivo com informações do vídeo: [`VIDEO.md`](./VIDEO.md)

---

## 👥 Integrantes e Contribuições Individuais

| Nome | Matrícula | Seção do Relatório |
| :--- | :---: | :--- |
| Augusto César Honorato dos Santos | 202000139031 | 1 — Identificação e caracterização |
| Giulian Fabio Bastos Amorim Lima | 202100095207 | 2 — Contexto, Partes Interessadas e Riscos |
| Kauä Ribeiro de Almeida Nascimento | 202100045958 | 3 — Requisitos de Qualidade |
| Roseane Resende | 202100115373 | 4 — Avaliação ISO/IEC 25010:2023 |
| **Pedro Miguel Castro França** | **202300061741** | **5 — Casos de Teste e Avaliação Inicial** |
| Paulo Henrique dos Santos Reis | 202100115524 | 6 — Variabilidade e não determinismo |
| Paulo Henrique Carvalho de Andrade | 202200060090 | 7 — Diagnóstico e plano de melhoria |

---

## 📖 Sobre o Projeto Avaliado

O **LangExtract** é uma biblioteca Python de código aberto desenvolvida pelo Google que utiliza Grandes Modelos de Linguagem (LLMs) para extrair informações estruturadas de textos não estruturados. Seu principal diferencial é o **embasamento preciso na fonte** (*precise source grounding*), que mapeia cada informação extraída ao trecho exato do documento original, em nível de caractere, permitindo rastreabilidade e verificabilidade.

- **Licença:** Apache 2.0
- **Requisito:** Python 3.10+
- **Modelo recomendado:** `gemini-2.5-flash` (ou local via Ollama)
- **Saída:** JSONL + Visualização HTML interativa

---

## 📋 Resumo das Seções Avaliadas

### 1. Identificação e Caracterização
- Nome: LangExtract
- Desenvolvedor: Google LLC
- Repositório: `github.com/google/langextract`

### 2. Contexto, Partes Interessadas e Riscos
Avaliação do uso em documentos acadêmicos/institucionais públicos. Principais riscos identificados:
- **R-01:** Extração de informação inexistente
- **R-02:** Omissão ou interpretação ambígua
- **R-03:** Exposição de dados pessoais
- **R-04:** Confiança excessiva no resultado

### 3. Requisitos de Qualidade
Definição de 10 requisitos (REQ-01 a REQ-10) distribuídos entre:
- Adequação Funcional, Confiabilidade, Interoperabilidade, Segurança, Desempenho, Usabilidade, Privacidade, Viés, Robustez e Portabilidade.

### 4. Avaliação ISO/IEC 25010:2023
Sob a ótica da norma, o LangExtract (com `gemma2:2b` local):
- ✅ **Atende:** Compatibilidade (saída JSON validada).
- ⚠️ **Atende parcialmente:** Adequação Funcional, Eficiência, Manutenibilidade.
- ❌ **Não atende de forma consistente:** Confiabilidade e Segurança.

### 5. Casos de Teste e Avaliação Inicial (Pedro Miguel)
Foram executados **12 casos de teste (CT-01 a CT-12)** com o modelo local `gemma2:2b` via Ollama.

**Resultados Consolidados:**

| Métrica | Valor | Percentual |
| :--- | :---: | :---: |
| Total de Testes | 12 | 100% |
| Aprovados (A) | 9 | 75,0% |
| Parciais (P) | 1 | 8,3% |
| Reprovados (R) | 2 | 16,7% |

**Principais Achados:**
- ✅ **Pontos Fortes:** Rastreabilidade e Grounding (CT-01, CT-06, CT-10); Anti-alucinação quando a fonte não existe (CT-08, CT-09); Tratamento controlado de erros (CT-12).
- ❌ **Pontos Fracos:** Falta de contexto/domínio (CT-04); Falha de privacidade (CT-05); Inferência sem fonte (CT-02).

> 📄 Tabela completa e evidências em [`/evidencias/testes`](./evidencias/testes).

### 6. Variabilidade e Não Determinismo
Com 5 prompts e 3 repetições cada, o modelo `gemma2:2b` demonstrou ser **não determinístico**, com variações na quantidade e classificação de entidades entre execuções.

### 7. Diagnóstico e Plano de Melhoria
Foram identificados 5 achados principais (ACH-01 a ACH-05), com plano de ação contendo responsáveis, prioridades e indicadores de acompanhamento.

---
