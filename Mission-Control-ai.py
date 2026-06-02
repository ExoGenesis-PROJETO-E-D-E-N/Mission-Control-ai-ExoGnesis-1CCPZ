# ============================================================
# MISSION CONTROL AI — PROJETO É.D.E.N.
# Monitoramento Inteligente da Biocápsula Botânica
# ============================================================

NOME_MISSAO = "Projeto É.D.E.N. — Missão Orbital"
NOME_EQUIPE = "ExoGenesis"


# Contexto É.D.E.N.:
"""
Com o avanço do aquecimento global e o risco de extinção de plantas
nativas da Mata Atlântica, o Brasil lança uma missão espacial revolucionária: o PROJETO É.D.E.N. 
Trata-se de uma biocápsula/estufa botânica 100% automatizada enviada à órbita da Terra.

🔭🔬🧬 O objetivo científico é:
expor sementes e mudas tropicais a picos controlados de estresse espacial (microgravidade e doses calculadas de radiação cósmica)

🌱🌎 Esse processo induz micro mutações e ativa genes de defesa nas plantas, 
desenvolvendo espécies "hiper resilientes" que serão trazidas de volta para reflorestar a Terra e combater a crise climática 
"""

#   temperatura  → temperatura interna da estufa botânica (°C)
#   comunicacao  → qualidade do sinal com a estação terrestre (%)
#   bateria      → nível de energia (%)
#   oxigenio     → concentração de O₂ no interior da cápsula (%)
#   estabilidade → estabilidade estrutural e operacional da cápsula (%)

dados_missao = [
    [22, 95, 91, 97, 93],   # Ciclo 1 — lançamento e estabilização inicial
    [24, 88, 83, 95, 87],   # Ciclo 2 — entrada em órbita, sistemas estáveis
    [28, 71, 65, 92, 74],   # Ciclo 3 — exposição ao estresse espacial controlado
    [33, 48, 41, 88, 58],   # Ciclo 4 — queda de comunicação e energia
    [38, 26, 18, 79, 34],   # Ciclo 5 — risco crítico: intervenção necessária
    [43, 24, 17, 67, 29],   # Ciclo 6 - inicio da intervenção
    [25, 62, 35, 85, 52],   # Ciclo 7 — tentativa de recuperação parcial
    [19, 73, 40, 81, 67],   # Ciclo 8 - tentativa de recuperação em andamento
    [22, 76, 38, 85, 72],   # Ciclo 9 - tentativade recuperação bem sucedida
    [25, 82, 53, 90, 79],   # Ciclo 10 - estabilidade da missão controlada temporariamente
]

areas_monitoradas = [
    "Temperatura da estufa",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade da cápsula"
]


# ============================================================
# FUNÇÕES DE ANÁLISE — classificam cada variável do ciclo
# Retornam: (classificacao, pontuacao, mensagem)
# ============================================================

def analisar_temperatura(temp):
    if temp > 35:
        return ("CRÍTICO", 2, "Risco de superaquecimento na estufa — mudas em perigo")
    elif temp > 30:
        return ("ATENÇÃO", 1, "Temperatura elevada — monitorar estufa botânica")
    elif temp < 18:
        return ("ATENÇÃO", 1, "Temperatura baixa — risco de dano às mudas tropicais")
    else:
        return ("NORMAL", 0, "Temperatura estável — condições ideais para as plantas")


def analisar_comunicacao(sinal):
    if sinal < 30:
        return ("CRÍTICO", 2, "Comunicação com a base em nível crítico")
    elif sinal < 60:
        return ("ATENÇÃO", 1, "Sinal instável — risco de perda de contato")
    else:
        return ("NORMAL", 0, "Comunicação estável com a estação terrestre")


def analisar_bateria(bateria):
    if bateria < 20:
        return ("CRÍTICO", 2, "Energia crítica — risco de falha total dos sistemas")
    elif bateria < 50:
        return ("ATENÇÃO", 1, "Energia abaixo do recomendado — reduzir consumo")
    else:
        return ("NORMAL", 0, "Sistema de energia operando normalmente")


def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        return ("CRÍTICO", 2, "Oxigênio crítico — acionar protocolo de suporte à vida vegetal")
    elif oxigenio < 90:
        return ("ATENÇÃO", 1, "Oxigênio abaixo do ideal para as plantas")
    else:
        return ("NORMAL", 0, "Concentração de oxigênio adequada na cápsula")


def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        return ("CRÍTICO", 2, "Estabilidade crítica — integridade da cápsula em risco")
    elif estabilidade < 70:
        return ("ATENÇÃO", 1, "Estabilidade reduzida — verificar estrutura da cápsula")
    else:
        return ("NORMAL", 0, "Cápsula operando com estabilidade adequada")




# ============================================================
# FUNÇÕES DE CLASSIFICAÇÃO E RECOMENDAÇÃO
# ============================================================

def classificar_ciclo(pontuacao_total):
    if pontuacao_total <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao_total <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(resultados_ciclo):

    recomendacoes = []

    classificacoes = [r[0] for r in resultados_ciclo]
    areas = [
        "temperatura da estufa",
        "comunicação com a base",
        "sistema de energia",
        "suporte de oxigênio",
        "estabilidade da cápsula"
    ]

    acoes = [
        "Acionar resfriamento emergencial da estufa botânica.",
        "Tentar restabelecer contato com a estação terrestre.",
        "Ativar modo de economia de energia — reduzir sistemas não essenciais.",
        "Acionar protocolo de suporte à vida vegetal imediatamente.",
        "Reduzir operações e verificar integridade estrutural da cápsula."
    ]

    for i in range(5):
        if classificacoes[i] == "CRÍTICO":
            recomendacoes.append(f"[URGENTE] {areas[i].upper()}: {acoes[i]}")
        elif classificacoes[i] == "ATENÇÃO":
            recomendacoes.append(f"[ATENÇÃO] {areas[i].capitalize()}: monitorar de perto.")

    if not recomendacoes:
        return ["Manter operação normal e continuar monitoramento da biocápsula."]

    return recomendacoes


def analisar_ciclo_completo(ciclo):

    temp, com, bat, oxi, est = ciclo

    resultados = [
        analisar_temperatura(temp),
        analisar_comunicacao(com),
        analisar_bateria(bat),
        analisar_oxigenio(oxi),
        analisar_estabilidade(est)
    ]

    pontuacao_total = sum(r[1] for r in resultados)
    classificacao   = classificar_ciclo(pontuacao_total)
    recomendacoes   = gerar_recomendacao(resultados)

    return resultados, pontuacao_total, classificacao, recomendacoes



# ============================================================
# FUNÇÕES AUXILIARES DE EXIBIÇÃO
# ============================================================

def linha_dupla():
    print("=" * 60)

def linha_simples():
    print("-" * 60)


def exibir_cabecalho():
    linha_dupla()
    print("       MISSION CONTROL AI — PROJETO É.D.E.N.")
    print("   Monitoramento Inteligente da Biocápsula Botânica")
    linha_dupla()
    print(f"Missão : {NOME_MISSAO}")
    print(f"Equipe : {NOME_EQUIPE}")
    print(f"Ciclos : {len(dados_missao)} ciclos de monitoramento")
    linha_dupla()


def exibir_ciclo(numero_ciclo, ciclo, resultados, pontuacao, classificacao, recomendacoes):
    nomes_variaveis = [
        "Temperatura",
        "Comunicação",
        "Bateria    ",
        "Oxigênio   ",
        "Estabilidade"
    ]

    unidades = ["°C", "%", "%", "%", "%"]

    print(f"\nCICLO {numero_ciclo}")
    linha_simples()

    for i in range(5):
        valor       = ciclo[i]
        classe      = resultados[i][0]
        mensagem    = resultados[i][2]
        unidade     = unidades[i]
        nome        = nomes_variaveis[i]
        print(f"{nome}: {valor}{unidade} | {classe} | {mensagem}")

    print()
    print(f"Pontuação de risco : {pontuacao} / 10")
    print(f"Classificação      : {classificacao}")
    print()
    print("Recomendações:")
    for rec in recomendacoes:
        print(f"  --> {rec}")


# ============================================================
# LOOP PRINCIPAL — percorre todos os ciclos da missão
# ============================================================

def executar_missao():
    exibir_cabecalho()

    # Listas para guardar os dados de todos os ciclos
    # (serão usadas no relatório final — Parte 5)
    todas_pontuacoes    = []
    todos_resultados    = []

    for i in range(len(dados_missao)):
        ciclo = dados_missao[i]

        resultados, pontuacao, classificacao, recomendacoes = analisar_ciclo_completo(ciclo)

        exibir_ciclo(
            numero_ciclo  = i + 1,
            ciclo         = ciclo,
            resultados    = resultados,
            pontuacao     = pontuacao,
            classificacao = classificacao,
            recomendacoes = recomendacoes
        )

        todas_pontuacoes.append(pontuacao)
        todos_resultados.append(resultados)

    return todas_pontuacoes, todos_resultados




# ============================================================
# FUNÇÕES DE ANÁLISE GLOBAL DA MISSÃO
# ============================================================

def analisar_tendencia(todas_pontuacoes):
    primeira = todas_pontuacoes[0]
    ultima   = todas_pontuacoes[-1]

    if ultima > primeira:
        return "A missão apresentou tendência de PIORA ao longo dos ciclos."
    elif ultima < primeira:
        return "A missão apresentou tendência de MELHORA ao longo dos ciclos."
    else:
        return "A missão permaneceu ESTÁVEL em relação ao ciclo inicial."


def identificar_area_mais_afetada(todos_resultados):
    pontuacao_por_area = [0, 0, 0, 0, 0]

    for resultados_ciclo in todos_resultados:
        for i in range(5):
            pontuacao_por_area[i] += resultados_ciclo[i][1]

    indice_maior = pontuacao_por_area.index(max(pontuacao_por_area))
    area_mais_afetada = areas_monitoradas[indice_maior]

    return pontuacao_por_area, area_mais_afetada



def gerar_relatorio_final(todas_pontuacoes, todos_resultados):
    print()
    print()
    linha_dupla()
    print ("         RELATÓRIO FINAL DA MISSÃO É.D.E.N.")
    linha_dupla()

    print(f"Missão : {NOME_MISSAO}")
    print(f"Equipe : {NOME_EQUIPE}")
    print(f"Total de ciclos analisados: {len(dados_missao)}")
    print()

    # Médias por variável
    medias = []
    for col in range(5):
        valores = [dados_missao[linha][col] for linha in range(len(dados_missao))]
        medias.append(sum(valores) / len(valores))

    unidades = ["°C", "%", "%", "%", "%"]
    print("Médias por área:")
    for i in range(5):
        print(f"  {areas_monitoradas[i]}: {medias[i]:.1f}{unidades[i]}")

    print()

    # Ciclo mais crítico
    maior_pontuacao  = max(todas_pontuacoes)
    ciclo_critico    = todas_pontuacoes.index(maior_pontuacao) + 1
    risco_medio      = sum(todas_pontuacoes) / len(todas_pontuacoes)
    ciclos_criticos  = sum(1 for p in todas_pontuacoes if p >= 6)

    print(f"Ciclo mais crítico      : Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco: {maior_pontuacao} / 10")
    print(f"Risco médio da missão   : {risco_medio:.2f}")
    print(f"Ciclos em estado crítico: {ciclos_criticos}")
    print()

    # Tendência
    tendencia = analisar_tendencia(todas_pontuacoes)
    print("Tendência da missão:")
    print(f"  {tendencia}")
    print()

    # Pontuação acumulada por área
    pontuacao_por_area, area_mais_afetada = identificar_area_mais_afetada(todos_resultados)
    print("Pontuação acumulada por área:")
    for i in range(5):
        print(f"  {areas_monitoradas[i]}: {pontuacao_por_area[i]} pontos")

    print()
    print(f"Área mais afetada: {area_mais_afetada}")
    print()

    # Classificação final — baseada na média de risco
    classificacao_final = classificar_ciclo(round(risco_medio))
    print(f"Classificação final da missão: {classificacao_final}")
    print()

    # Conclusão narrativa
    print("Conclusão:")
    if classificacao_final == "MISSÃO CRÍTICA":
        print("  A biocápsula É.D.E.N. enfrentou condições severas durante a missão.")
        print("  O sistema de controle interveio nos momentos críticos, mas a equipe")
        print("  deve revisar os protocolos de energia e estabilidade antes da próxima fase.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        print("  A missão apresentou instabilidade relevante em alguns ciclos.")
        print("  A tentativa de recuperação no ciclo final foi parcialmente bem-sucedida.")
        print("  Manter plano de contingência ativo e monitorar áreas em atenção.")
    else:
        print("  A biocápsula É.D.E.N. operou dentro dos parâmetros esperados.")
        print("  As plantas estão em condições adequadas para a próxima fase da missão.")

    linha_dupla()


# ============================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================

if __name__ == "__main__":
    todas_pontuacoes, todos_resultados = executar_missao()
    gerar_relatorio_final(todas_pontuacoes, todos_resultados)