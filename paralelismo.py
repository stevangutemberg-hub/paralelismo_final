import pandas as pd
import numpy as np
import time
import multiprocessing as mp
import os

# ============================================
# CONFIGURAÇÃO
# ============================================

ARQUIVO = "mta_sbway.csv"
LISTA_PROCESSOS = [2, 4, 8, 12]

# Chunk grande para garantir trabalho pesado por processo
# Ajuste para baixo se der MemoryError (ex: 50000)
CHUNKSIZE = 100000


# ============================================
# FUNÇÃO: DETECTA COLUNAS
# ============================================

def detectar_colunas(colunas):

    if "station" in colunas:
        col_estacao = "station"
    elif "station_complex" in colunas:
        col_estacao = "station_complex"
    elif "stop_name" in colunas:
        col_estacao = "stop_name"
    else:
        return None, None, None

    if "ridership" in colunas:
        col_pass = "ridership"
    elif "entries" in colunas:
        col_pass = "entries"
    elif "passengers" in colunas:
        col_pass = "passengers"
    else:
        return None, None, None

    if "transit_timestamp" in colunas:
        col_time = "transit_timestamp"
    elif "datetime" in colunas:
        col_time = "datetime"
    elif "timestamp" in colunas:
        col_time = "timestamp"
    else:
        col_time = None

    return col_estacao, col_pass, col_time


# ============================================
# FUNÇÃO: TRABALHO PESADO DE CPU
# Garante carga real por chunk para que
# múltiplos núcleos façam diferença visível
# ============================================

def trabalho_pesado(chunk, col_pass):
    valores = chunk[col_pass].values.astype(float)

    for _ in range(30):
        _ = np.convolve(valores[:500], np.ones(50) / 50, mode="valid")
        _ = np.sort(valores)
        _ = np.percentile(valores, [10, 25, 50, 75, 90, 95, 99])
        _ = np.corrcoef(valores[:1000], np.roll(valores[:1000], 10))
        _ = np.fft.fft(valores[:1024])

    return True


# ============================================
# FUNÇÃO WORKER: PROCESSA UM CHUNK
# ============================================

def processar_chunk(args):
    idx, chunk_dict = args
    chunk = pd.DataFrame(chunk_dict)

    chunk.columns = chunk.columns.str.strip().str.lower()
    colunas = chunk.columns

    col_estacao, col_pass, col_time = detectar_colunas(colunas)
    if col_estacao is None:
        return None

    chunk = chunk.drop_duplicates()
    chunk = chunk.dropna(subset=[col_estacao, col_pass])
    chunk[col_pass] = pd.to_numeric(chunk[col_pass], errors="coerce")
    chunk = chunk.dropna(subset=[col_pass])

    if chunk.empty:
        return None

    # ---- CARGA PESADA DE CPU ----
    trabalho_pesado(chunk, col_pass)

    movimento_estacoes = (
        chunk.groupby(col_estacao)[col_pass]
        .sum()
        .to_dict()
    )

    movimento_horarios = {}
    possiveis_atrasos = []
    possiveis_riscos = []

    if col_time:
        chunk[col_time] = pd.to_datetime(chunk[col_time], errors="coerce")
        chunk = chunk.dropna(subset=[col_time])
        chunk["hora"] = chunk[col_time].dt.hour

        movimento_horarios = (
            chunk.groupby("hora")[col_pass]
            .sum()
            .to_dict()
        )

        media = chunk[col_pass].mean()

        atrasos = chunk[chunk[col_pass] > media * 2]
        if len(atrasos) > 0:
            possiveis_atrasos = (
                atrasos[[col_estacao, col_pass]]
                .head(5)
                .to_dict("records")
            )

        riscos = chunk[chunk[col_pass] > media * 3]
        if len(riscos) > 0:
            possiveis_riscos = (
                riscos[[col_estacao, col_pass]]
                .head(5)
                .to_dict("records")
            )

    return {
        "estacoes": movimento_estacoes,
        "horarios": movimento_horarios,
        "atrasos": possiveis_atrasos,
        "riscos": possiveis_riscos,
        "col_estacao": col_estacao,
        "col_pass": col_pass,
    }


# ============================================
# FUNÇÃO: COMBINA RESULTADOS PARCIAIS
# ============================================

def combinar_resultados(lista_resultados):

    movimento_estacoes = {}
    movimento_horarios = {}
    possiveis_atrasos = []
    possiveis_riscos = []
    col_estacao = None
    col_pass = None

    for res in lista_resultados:
        if res is None:
            continue

        col_estacao = res.get("col_estacao", col_estacao)
        col_pass = res.get("col_pass", col_pass)

        for estacao, total in res["estacoes"].items():
            movimento_estacoes[estacao] = (
                movimento_estacoes.get(estacao, 0) + total
            )

        for hora, total in res["horarios"].items():
            movimento_horarios[hora] = (
                movimento_horarios.get(hora, 0) + total
            )

        possiveis_atrasos.extend(res["atrasos"])
        possiveis_riscos.extend(res["riscos"])

    return (
        movimento_estacoes,
        movimento_horarios,
        possiveis_atrasos,
        possiveis_riscos,
        col_estacao,
        col_pass,
    )


# ============================================
# FUNÇÃO: EXIBE RESULTADOS
# ============================================

def exibir_resultados(
    movimento_estacoes,
    movimento_horarios,
    possiveis_atrasos,
    possiveis_riscos,
    col_estacao,
    col_pass,
):
    print("\n======================================")
    print("TOP 10 ESTAÇÕES MAIS MOVIMENTADAS")
    print("======================================")
    top_estacoes = (
        pd.Series(movimento_estacoes)
        .sort_values(ascending=False)
        .head(10)
    )
    print(top_estacoes)

    print("\n======================================")
    print("HORÁRIOS MAIS MOVIMENTADOS")
    print("======================================")
    if movimento_horarios:
        top_horarios = (
            pd.Series(movimento_horarios)
            .sort_values(ascending=False)
        )
        print(top_horarios.head(10))
    else:
        print("Sem dados de horário.")

    print("\n======================================")
    print("POSSÍVEIS ATRASOS DETECTADOS")
    print("======================================")
    if possiveis_atrasos:
        atrasos_df = pd.DataFrame(possiveis_atrasos)
        print(atrasos_df.head(20))
    else:
        print("Nenhum possível atraso detectado.")

    print("\n======================================")
    print("POSSÍVEIS RISCOS / SUPERLOTAÇÃO")
    print("======================================")
    if possiveis_riscos:
        riscos_df = pd.DataFrame(possiveis_riscos)
        print(riscos_df.head(20))
    else:
        print("Nenhum possível risco detectado.")

    estacao_campea = top_estacoes.idxmax()
    total = top_estacoes.max()

    print("\n======================================")
    print("ESTAÇÃO MAIS MOVIMENTADA")
    print("======================================")
    print(f"Estação: {estacao_campea}")
    print(f"Total de passageiros: {total}")


# ============================================
# FUNÇÃO: CARREGA CHUNKS DO CSV
# ============================================

def carregar_chunks():
    print(f"\nLendo '{ARQUIVO}' em chunks de {CHUNKSIZE:,} linhas...")
    reader = pd.read_csv(
        ARQUIVO,
        chunksize=CHUNKSIZE,
        encoding="latin1",
        on_bad_lines="skip",
        engine="python",
    )
    chunks = []
    for i, chunk in enumerate(reader):
        chunks.append((i, chunk.to_dict("list")))
        print(f"  Chunk {i+1} carregado ({len(chunk):,} linhas)")
    return chunks


# ============================================
# FUNÇÃO: RODA COM N PROCESSOS
# ============================================

def rodar_paralelo(chunks, n_processos):

    print(f"\n{'='*55}")
    print(f"  RODANDO COM {n_processos} PROCESSOS")
    print(f"{'='*55}")

    inicio = time.time()

    with mp.Pool(processes=n_processos) as pool:
        resultados = pool.map(processar_chunk, chunks)

    (
        movimento_estacoes,
        movimento_horarios,
        possiveis_atrasos,
        possiveis_riscos,
        col_estacao,
        col_pass,
    ) = combinar_resultados(resultados)

    fim = time.time()
    tempo = fim - inicio

    exibir_resultados(
        movimento_estacoes,
        movimento_horarios,
        possiveis_atrasos,
        possiveis_riscos,
        col_estacao,
        col_pass,
    )

    print(f"\n>>> TEMPO COM {n_processos} PROCESSOS: {tempo:.2f} segundos")
    return n_processos, tempo


# ============================================
# EXECUÇÃO PRINCIPAL
# ============================================

if __name__ == "__main__":

    print("======================================")
    print("  ANÁLISE PARALELA - METRÔ DE NY")
    print("======================================")
    print(f"CPUs disponíveis na máquina: {mp.cpu_count()}")

    t0 = time.time()
    chunks = carregar_chunks()
    t1 = time.time()
    print(f"\nTotal de chunks: {len(chunks)}")
    print(f"Tempo de carga do CSV: {t1 - t0:.2f}s")

    tempos = []
    for n in LISTA_PROCESSOS:
        n_proc, tempo = rodar_paralelo(chunks, n)
        tempos.append((n_proc, tempo))

    tempo_base = tempos[0][1]  # 2 processos como base

    print("\n")
    print("=" * 55)
    print("       COMPARATIVO DE DESEMPENHO FINAL")
    print("=" * 55)
    print(f"{'Processos':<15} {'Tempo (s)':<18} {'Speedup vs 2 proc'}")
    print("-" * 55)

    for n_proc, tempo in tempos:
        speedup = tempo_base / tempo
        barra = "█" * int(speedup * 8)
        print(f"{n_proc:<15} {tempo:<18.2f} {speedup:.2f}x  {barra}")

    print("=" * 55)
    melhor = min(tempos, key=lambda x: x[1])
    print(f"\n>>> Melhor configuração: {melhor[0]} processos ({melhor[1]:.2f}s)")
    print(f"    Ganho total: {tempo_base / melhor[1]:.2f}x mais rápido que 2 processos")
