import multiprocessing as mp
import time

def trabalho(intervalo):
    inicio, fim = intervalo

    total = 0

    for i in range(inicio, fim):
        x = float(i)

        # carga computacional pesada
        for _ in range(100):
            x = (x * 1.0000001) ** 1.0000001

        total += x

    return total


def executar(n_processos):

    TOTAL = 5_000_000

    tamanho_bloco = TOTAL // n_processos

    tarefas = []

    for i in range(n_processos):

        inicio = i * tamanho_bloco

        if i == n_processos - 1:
            fim = TOTAL
        else:
            fim = (i + 1) * tamanho_bloco

        tarefas.append((inicio, fim))

    inicio_tempo = time.time()

    with mp.Pool(processes=n_processos) as pool:
        resultados = pool.map(trabalho, tarefas)

    tempo_total = time.time() - inicio_tempo

    return sum(resultados), tempo_total


if __name__ == "__main__":

    mp.freeze_support()

    lista_processos = [1, 2, 4, 8, 12]

    tempos = {}

    print("=" * 50)
    print("TESTE DE PARALELIZAÇÃO")
    print("=" * 50)

    print("Núcleos lógicos detectados:", mp.cpu_count())

    for n in lista_processos:

        print(f"\nExecutando com {n} processos...")

        _, tempo = executar(n)

        tempos[n] = tempo

        print(f"Tempo: {tempo:.2f} segundos")

    print("\n" + "=" * 50)
    print("COMPARATIVO DE DESEMPENHO")
    print("=" * 50)

    tempo_base = tempos[1]

    print(f"{'Processos':<12}{'Tempo(s)':<12}{'Speedup':<12}")

    for n in lista_processos:

        speedup = tempo_base / tempos[n]

        print(f"{n:<12}{tempos[n]:<12.2f}{speedup:<12.2f}")
