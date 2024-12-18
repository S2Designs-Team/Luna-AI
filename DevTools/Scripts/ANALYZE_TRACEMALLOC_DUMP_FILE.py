import tracemalloc

# Carica il file di dump
snapshot = tracemalloc.load_snapshot("memory_dump.pkl")

# Puoi esplorare le informazioni nello snapshot. Ecco alcune opzioni:

# 1. Mostrare la statistica sulle allocazioni
print("Mostra le allocazioni più significative:")
top_stats = snapshot.statistics('lineno')
for stat in top_stats[:10]:  # Mostra le prime 10 righe con maggiore allocazione
    print(stat)

# 2. Analizzare la memoria utilizzata da un modulo specifico
print("\nMostra le allocazioni per modulo specifico (es. `yaml`):")
yaml_stats = snapshot.statistics('module')
for stat in yaml_stats:
    if 'yaml' in stat.traceback[0].filename:
        print(stat)

# 3. Analizzare i dettagli dello snapshot
print("\nDettagli dello snapshot:")
snapshot_stats = snapshot.statistics('traceback')
for stat in snapshot_stats[:10]:
    print(stat)

# 4. Visualizzare un grafico delle allocazioni, utile se hai installato `matplotlib`
try:
    import matplotlib.pyplot as plt
    import numpy as np

    # Creare un grafico per analizzare l'uso della memoria
    allocations = [stat.size for stat in top_stats]
    labels = [str(stat.traceback) for stat in top_stats]
    indices = np.arange(len(allocations))

    plt.bar(indices, allocations)
    plt.xticks(indices, labels, rotation=90)
    plt.xlabel('Allocazioni di memoria')
    plt.ylabel('Dimensione (bytes)')
    plt.title('Distribuzione dell\'uso della memoria')
    plt.show()

except ImportError:
    print("matplotlib non trovato, impossibile visualizzare il grafico.")