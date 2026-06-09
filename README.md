# 🌱 Mission Control AI — Projeto É.D.E.N.
### Monitoramento Inteligente da Biocápsula Botânica

---

## 👥 Equipe

**ExoGenesis**

| Nome | RM |
|------|----|
| Arthur Vettorazzo de Souza | RM: 569445  |
| Brayan Barbosa Dos Santos  | RM: 573682  |
| Giovanne Gomes Petenuci    | RM: 574091  |

---

## 📖 Sobre o Projeto

Com o avanço do aquecimento global e o risco de extinção de plantas nativas da Mata Atlântica, o Brasil lança uma missão espacial revolucionária: o **Projeto É.D.E.N. (Ecossistema de Desenvolvimento Espacial Natural)**.

Trata-se de uma biocápsula/estufa botânica 100% automatizada enviada à órbita da Terra. O objetivo científico é expor sementes e mudas tropicais a picos controlados de estresse espacial — microgravidade e doses calculadas de radiação cósmica — induzindo micro mutações que ativam genes de defesa nas plantas.

As espécies resultantes, **hiper-resilientes**, serão trazidas de volta para reflorestar a Terra e combater a crise climática, alinhando-se aos ODS da ONU (ODS 13 — Ação Climática e ODS 15 — Vida Terrestre).

Como não há humanos a bordo, o software **Mission Control AI** é o cérebro que gerencia o ecossistema. A IA monitora continuamente os sistemas da cápsula, permite o estresse espacial controlado para que as plantas evoluam, e intervém imediatamente se os sensores indicarem risco de morte iminente das mudas.

---

## 🚀 Como executar

**Pré-requisitos:** Python 3.x instalado

**Passos:**

1. Clone o repositório:
```bash
git clone https://github.com/ExoGenesis-PROJETO-E-D-E-N/Mission-Control-ai-ExoGnesis-1CCPZ.git
```

2. Acesse a pasta:
```bash
cd Mission-Control-ai
```

3. Execute o programa:
```bash
python Mission-Control-ai
```

O sistema roda apenas com Python puro.

---

## 📊 Estrutura dos dados

A missão é simulada por meio de **10 ciclos de monitoramento**. Cada ciclo representa um momento da missão É.D.E.N. e contém 5 variáveis:

```
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

| Posição | Variável | Unidade | Significado no É.D.E.N. |
|---------|----------|---------|--------------------------|
| 0 | Temperatura | °C | Temperatura interna da estufa botânica |
| 1 | Comunicação | % | Qualidade do sinal com a estação terrestre |
| 2 | Bateria | % | Nível de energia do sistema |
| 3 | Oxigênio | % | Concentração de O₂ no interior da cápsula |
| 4 | Estabilidade | % | Estabilidade estrutural e operacional da cápsula |

---

## 🔔 Regras de alerta

O sistema classifica cada variável como **NORMAL**, **ATENÇÃO** ou **CRÍTICO**:

### Temperatura (°C)
| Condição | Classificação |
|----------|--------------|
| Menor que 18 | ATENÇÃO |
| De 18 até 30 | NORMAL |
| Maior que 30 até 35 | ATENÇÃO |
| Maior que 35 | CRÍTICO |

### Comunicação (%)
| Condição | Classificação |
|----------|--------------|
| Menor que 30 | CRÍTICO |
| De 30 até 59 | ATENÇÃO |
| 60 ou mais | NORMAL |

### Bateria (%)
| Condição | Classificação |
|----------|--------------|
| Menor que 20 | CRÍTICO |
| De 20 até 49 | ATENÇÃO |
| 50 ou mais | NORMAL |

### Oxigênio (%)
| Condição | Classificação |
|----------|--------------|
| Menor que 80 | CRÍTICO |
| De 80 até 89 | ATENÇÃO |
| 90 ou mais | NORMAL |

### Estabilidade (%)
| Condição | Classificação |
|----------|--------------|
| Menor que 40 | CRÍTICO |
| De 40 até 69 | ATENÇÃO |
| 70 ou mais | NORMAL |

---

## 🎯 Pontuação de risco e classificação dos ciclos

Cada classificação gera uma pontuação por variável:
- NORMAL = 0 pontos
- ATENÇÃO = 1 ponto
- CRÍTICO = 2 pontos

Pontuação máxima por ciclo: **10 pontos** (5 variáveis × 2)

| Pontuação total | Classificação do ciclo |
|----------------|------------------------|
| 0 a 2 pontos | MISSÃO ESTÁVEL |
| 3 a 5 pontos | MISSÃO EM ATENÇÃO |
| 6 a 10 pontos | MISSÃO CRÍTICA |

---

## ⚙️ Funções implementadas

| Função | Descrição |
|--------|-----------|
| `analisar_temperatura()` | Classifica a temperatura da estufa |
| `analisar_comunicacao()` | Classifica o sinal de comunicação |
| `analisar_bateria()` | Classifica o nível de energia |
| `analisar_oxigenio()` | Classifica a concentração de oxigênio |
| `analisar_estabilidade()` | Classifica a estabilidade da cápsula |
| `classificar_ciclo()` | Classifica o ciclo com base na pontuação total |
| `gerar_recomendacao()` | Gera recomendações automáticas por ciclo |
| `analisar_ciclo_completo()` | Orquestra a análise completa de um ciclo |
| `analisar_tendencia()` | Compara o primeiro e o último ciclo |
| `identificar_area_mais_afetada()` | Identifica a área com maior risco acumulado |
| `gerar_relatorio_final()` | Exibe o relatório completo da missão |
| `executar_missao()` | Loop principal que percorre todos os ciclos |

---

## 🧪 Narrativa dos ciclos da missão

| Ciclo | Descrição |
|-------|-----------|
| 1 | Lançamento e estabilização inicial |
| 2 | Entrada em órbita, sistemas estáveis |
| 3 | Exposição ao estresse espacial controlado |
| 4 | Queda de comunicação e energia |
| 5 | Risco crítico — intervenção necessária |
| 6 | Início da intervenção de emergência |
| 7 | Tentativa de recuperação parcial |
| 8 | Recuperação em andamento |
| 9 | Recuperação bem-sucedida |
| 10 | Estabilidade controlada temporariamente |

---



## 🎥 Vídeo Pitch

[Link do YouTube](https://youtu.be/mwRnOX7eOmc)

---

## 🏫 Informações acadêmicas

- **Instituição:** FIAP
- **Disciplina:** Pensamento Computacional e Automação com Python
- **Atividade:** Global Solution 2026.1
- **Tema:** Indústria Espacial — O Código que Move o Universo
