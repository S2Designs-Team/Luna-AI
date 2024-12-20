import pickle
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import asyncio

async def main(memory_dump_file_path):
    # Carica lo snapshot dal file .pkl
    with open(memory_dump_file_path, "rb") as f:
        snapshot = pickle.load(f)

    # Puoi esplorare le informazioni nello snapshot. Ecco alcune opzioni:

    # 1. Mostrare la statistica sulle allocazioni
    print("Mostra le allocazioni più significative:")
    top_stats = snapshot.statistics('lineno')
    for stat in top_stats[:10]:  # Mostra le prime 10 righe con maggiore allocazione
        print(stat)

    # 2. Estrai dati per il grafico
    labels = [f"{stat.traceback[0]}" for stat in top_stats]  # Primo file e linea
    sizes = [stat.size / 1024 for stat in top_stats]  # Conversione in KB
    
    try:
        # 3. Visualizzare un grafico delle allocazioni, utile se hai installato `matplotlib`
    
        # Crea un grafico a barre
        plt.figure(figsize=(10, 6))
        plt.barh(labels, sizes, color='skyblue')
        plt.xlabel("Dimensione (KB)")
        plt.ylabel("File e Linea")
        plt.title("Top 10 allocazioni di memoria")
        plt.tight_layout()
        plt.show()

        # (Facoltativo) Grafico a torta
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Distribuzione della memoria tra le prime 10 allocazioni")
        plt.show()


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

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(sys.argv) != 2:
        print("Usage Help: python startLunaAI.py [gui|console]")
        sys.exit(1)

    par_memory_dump_file_path = sys.argv[1].lower()
    
    try:
        asyncio.run(main(par_memory_dump_file_path))
        
    except Exception as app_exception:
        print(f"An unexpected error occurred: {app_exception}")