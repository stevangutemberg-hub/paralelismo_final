import pandas as pd
import time

# ============================================
# INÍCIO
# ============================================

inicio = time.time()

arquivo = "mta_sbway.csv"

print("======================================")
print("ANÁLISE SERIAL - METRÔ DE NY")
print("======================================")

print("\nCriando leitor do CSV...")

# ============================================
# LEITOR SERIAL EM CHUNKS
# ============================================

reader = pd.read_csv(
    arquivo,
    chunksize=20000,
    encoding="latin1",
    on_bad_lines="skip",
    engine="python"
)

print("Reader criado com sucesso!")

# ============================================
# ESTRUTURAS PARA RESULTADOS
# ============================================

movimento_estacoes = {}
movimento_horarios = {}
possiveis_atrasos = []
possiveis_riscos = []

# ============================================
# PROCESSAMENTO SERIAL
# ============================================

for i, chunk in enumerate(reader):

    print(f"\nChunk {i+1} carregado...")

    # ----------------------------------------
    # PADRONIZA NOMES
    # ----------------------------------------

    chunk.columns = (
        chunk.columns
        .str.strip()
        .str.lower()
    )

    colunas = chunk.columns

    # ----------------------------------------
    # DETECTA COLUNAS
    # ----------------------------------------

    # ESTAÇÃO
    if "station" in colunas:
        COL_ESTACAO = "station"

    elif "station_complex" in colunas:
        COL_ESTACAO = "station_complex"

    elif "stop_name" in colunas:
        COL_ESTACAO = "stop_name"

    else:
        continue

    # PASSAGEIROS
    if "ridership" in colunas:
        COL_PASS = "ridership"

    elif "entries" in colunas:
        COL_PASS = "entries"

    elif "passengers" in colunas:
        COL_PASS = "passengers"

    else:
        continue

    # DATA/HORA
    if "transit_timestamp" in colunas:
        COL_TIME = "transit_timestamp"

    elif "datetime" in colunas:
        COL_TIME = "datetime"

    elif "timestamp" in colunas:
        COL_TIME = "timestamp"

    else:
        COL_TIME = None

    # ----------------------------------------
    # LIMPEZA
    # ----------------------------------------

    chunk = chunk.drop_duplicates()

    chunk = chunk.dropna(
        subset=[COL_ESTACAO, COL_PASS]
    )

    # converte passageiros
    chunk[COL_PASS] = pd.to_numeric(
        chunk[COL_PASS],
        errors="coerce"
    )

    chunk = chunk.dropna(subset=[COL_PASS])

    # ----------------------------------------
    # ESTAÇÕES MAIS MOVIMENTADAS
    # ----------------------------------------

    agrupado_estacoes = (
        chunk.groupby(COL_ESTACAO)[COL_PASS]
        .sum()
    )

    for estacao, total in agrupado_estacoes.items():

        if estacao not in movimento_estacoes:
            movimento_estacoes[estacao] = total

        else:
            movimento_estacoes[estacao] += total

    # ----------------------------------------
    # HORÁRIOS MAIS MOVIMENTADOS
    # ----------------------------------------

    if COL_TIME:

        chunk[COL_TIME] = pd.to_datetime(
            chunk[COL_TIME],
            errors="coerce"
        )

        chunk = chunk.dropna(subset=[COL_TIME])

        chunk["hora"] = chunk[COL_TIME].dt.hour

        agrupado_hora = (
            chunk.groupby("hora")[COL_PASS]
            .sum()
        )

        for hora, total in agrupado_hora.items():

            if hora not in movimento_horarios:
                movimento_horarios[hora] = total

            else:
                movimento_horarios[hora] += total

        # ------------------------------------
        # POSSÍVEIS ATRASOS
        # ------------------------------------

        media = chunk[COL_PASS].mean()

        atrasos = chunk[
            chunk[COL_PASS] > media * 2
        ]

        if len(atrasos) > 0:

            possiveis_atrasos.append(
                atrasos[
                    [COL_ESTACAO, COL_PASS]
                ].head(5)
            )

        # ------------------------------------
        # POSSÍVEIS RISCOS / ACIDENTES
        # ------------------------------------

        riscos = chunk[
            chunk[COL_PASS] > media * 3
        ]

        if len(riscos) > 0:

            possiveis_riscos.append(
                riscos[
                    [COL_ESTACAO, COL_PASS]
                ].head(5)
            )

# ============================================
# RESULTADOS FINAIS
# ============================================

print("\n======================================")
print("TOP 10 ESTAÇÕES MAIS MOVIMENTADAS")
print("======================================")

top_estacoes = (
    pd.Series(movimento_estacoes)
    .sort_values(ascending=False)
    .head(10)
)

print(top_estacoes)

# --------------------------------------------

print("\n======================================")
print("HORÁRIOS MAIS MOVIMENTADOS")
print("======================================")

top_horarios = (
    pd.Series(movimento_horarios)
    .sort_values(ascending=False)
)

print(top_horarios.head(10))

# --------------------------------------------

print("\n======================================")
print("POSSÍVEIS ATRASOS DETECTADOS")
print("======================================")

if len(possiveis_atrasos) > 0:

    atrasos_df = pd.concat(possiveis_atrasos)

    print(atrasos_df.head(20))

else:
    print("Nenhum possível atraso detectado.")

# --------------------------------------------

print("\n======================================")
print("POSSÍVEIS RISCOS / SUPERLOTAÇÃO")
print("======================================")

if len(possiveis_riscos) > 0:

    riscos_df = pd.concat(possiveis_riscos)

    print(riscos_df.head(20))

else:
    print("Nenhum possível risco detectado.")

# ============================================
# ESTAÇÃO CAMPEÃ
# ============================================

estacao_campea = top_estacoes.idxmax()
total = top_estacoes.max()

print("\n======================================")
print("ESTAÇÃO MAIS MOVIMENTADA")
print("======================================")

print(f"Estação: {estacao_campea}")
print(f"Total de passageiros: {total}")

# ============================================
# TEMPO FINAL
# ============================================

fim = time.time()

print("\n======================================")
print(f"TEMPO TOTAL: {fim - inicio:.2f} segundos")