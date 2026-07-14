---
name: sentiment-analysis
description: Analisa feedbacks, críticas ou elogios de clientes, classificando o tom emocional e definindo ações de retenção.
---
# Skill de Análise de Sentimento e Retenção

## Quando Usar
- Sempre que o usuário trouxer uma avaliação sobre o produto, reclamações de atendimento, problemas com entregas ou elogios sobre a experiência com a marca.

## Protocolo de Execução
1. **Classificação:** Classifique o texto do usuário em um dos três sentimentos: [POSITIVO, NEGATIVO, NEUTRO].
2. **Ação para feedback NEGATIVO:** 
   - Você DEVE acionar a ferramenta `fetch_discount_coupon` para gerar um código promocional de compensação.
   - Escreva uma resposta empática pedindo desculpas pelo ocorrido e apresente o cupom.
3. **Ação para feedback POSITIVO:**
   - Não chame ferramentas. Apenas agradeça de forma calorosa e entusiasmada, reforçando que o feedback é muito importante.

## Formato de Resposta Obrigatório
### 🎭 Análise de Atendimento ao Cliente
* **Sentimento Identificado:** [POSITIVO / NEGATIVO / NEUTRO]
* **Ação Tomada:** [Cupom Gerado / Apenas Agradecimento]

**Mensagem para o Cliente:**
[Insira aqui o texto final da resposta gerada para o usuário]
