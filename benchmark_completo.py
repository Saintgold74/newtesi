#!/usr/bin/env python3
"""
Benchmark Completo - Esegue tutti i benchmark e genera un report finale
"""
import time
import sys
import os
from datetime import datetime

# Import dei moduli benchmark
try:
    from benchmark_cpu import run_cpu_benchmark
    from benchmark_ram import run_memory_benchmark
    from benchmark_disk import run_disk_benchmark
    from sistema_info import print_system_report, get_system_info
except ImportError as e:
    print(f"Errore nell'importazione dei moduli: {e}")
    print("Assicurati che tutti i file benchmark_*.py e sistema_info.py siano presenti.")
    sys.exit(1)

def print_header():
    """Stampa intestazione del benchmark"""
    print("=" * 80)
    print("SUITE BENCHMARK COMPLETA")
    print("=" * 80)
    print(f"Avviata il: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Informazioni sistema di base
    sys_info = get_system_info()
    print(f"Sistema: {sys_info.get('sistema', 'N/A')} {sys_info.get('release', 'N/A')}")
    print(f"Processore: {sys_info.get('processore', 'N/A')}")
    print(f"Architettura: {sys_info.get('architettura', 'N/A')}")
    print()

def run_all_benchmarks():
    """Esegue tutti i benchmark in sequenza"""
    print_header()
    
    # Risultati benchmark
    results = {}
    
    print("FASE 1: REPORT SISTEMA")
    print("=" * 50)
    try:
        print_system_report()
    except Exception as e:
        print(f"Errore nel report sistema: {e}")
    
    input("\nPremi INVIO per continuare con i benchmark delle prestazioni...")
    
    # Benchmark CPU
    print("\n" + "=" * 80)
    print("FASE 2: BENCHMARK CPU")
    print("=" * 80)
    try:
        start_time = time.time()
        cpu_score = run_cpu_benchmark()
        cpu_time = time.time() - start_time
        results['cpu'] = {
            'score': cpu_score,
            'time': cpu_time,
            'status': 'completato'
        }
    except Exception as e:
        print(f"Errore benchmark CPU: {e}")
        results['cpu'] = {
            'score': 0,
            'time': 0,
            'status': 'errore',
            'error': str(e)
        }
    
    input("\nPremi INVIO per continuare con il benchmark della memoria...")
    
    # Benchmark RAM
    print("\n" + "=" * 80)
    print("FASE 3: BENCHMARK MEMORIA")
    print("=" * 80)
    try:
        start_time = time.time()
        ram_score = run_memory_benchmark()
        ram_time = time.time() - start_time
        results['ram'] = {
            'score': ram_score,
            'time': ram_time,
            'status': 'completato'
        }
    except Exception as e:
        print(f"Errore benchmark RAM: {e}")
        results['ram'] = {
            'score': 0,
            'time': 0,
            'status': 'errore',
            'error': str(e)
        }
    
    input("\nPremi INVIO per continuare con il benchmark del disco...")
    
    # Benchmark Disco
    print("\n" + "=" * 80)
    print("FASE 4: BENCHMARK DISCO")
    print("=" * 80)
    try:
        start_time = time.time()
        disk_score = run_disk_benchmark()
        disk_time = time.time() - start_time
        results['disk'] = {
            'score': disk_score,
            'time': disk_time,
            'status': 'completato'
        }
    except Exception as e:
        print(f"Errore benchmark disco: {e}")
        results['disk'] = {
            'score': 0,
            'time': 0,
            'status': 'errore',
            'error': str(e)
        }
    
    return results

def calculate_overall_score(results):
    """Calcola punteggio complessivo"""
    total_score = 0
    valid_scores = 0
    
    weights = {
        'cpu': 0.4,    # 40%
        'ram': 0.3,    # 30%  
        'disk': 0.3    # 30%
    }
    
    for component, weight in weights.items():
        if component in results and results[component]['status'] == 'completato':
            total_score += results[component]['score'] * weight
            valid_scores += weight
    
    if valid_scores > 0:
        return total_score / valid_scores * (valid_scores / sum(weights.values()))
    else:
        return 0

def get_performance_rating(score):
    """Determina rating prestazioni basato sul punteggio"""
    if score >= 2000:
        return "ECCELLENTE", "🟢"
    elif score >= 1500:
        return "MOLTO BUONO", "🟡"
    elif score >= 1000:
        return "BUONO", "🟠"
    elif score >= 500:
        return "DISCRETO", "🔴"
    else:
        return "SCARSO", "⚫"

def print_final_report(results):
    """Stampa report finale"""
    print("\n" + "=" * 80)
    print("REPORT FINALE BENCHMARK")
    print("=" * 80)
    
    # Dettaglio risultati per componente
    print("\nRISULTATI PER COMPONENTE:")
    print("-" * 50)
    
    for component, data in results.items():
        component_name = component.upper()
        if data['status'] == 'completato':
            rating, emoji = get_performance_rating(data['score'])
            print(f"{component_name}:")
            print(f"  Punteggio: {data['score']:.0f}")
            print(f"  Rating: {rating} {emoji}")
            print(f"  Tempo esecuzione: {data['time']:.1f} secondi")
        else:
            print(f"{component_name}:")
            print(f"  Status: ERRORE ❌")
            if 'error' in data:
                print(f"  Errore: {data['error']}")
        print()
    
    # Punteggio complessivo
    overall_score = calculate_overall_score(results)
    overall_rating, overall_emoji = get_performance_rating(overall_score)
    
    print("PUNTEGGIO COMPLESSIVO:")
    print("-" * 50)
    print(f"Punteggio Totale: {overall_score:.0f}")
    print(f"Rating Generale: {overall_rating} {overall_emoji}")
    
    # Tempo totale
    total_time = sum(data['time'] for data in results.values())
    print(f"Tempo Totale Benchmark: {total_time:.1f} secondi")
    
    # Raccomandazioni
    print("\nRACCOMANDAZIONI:")
    print("-" * 50)
    
    if 'cpu' in results and results['cpu']['status'] == 'completato':
        cpu_score = results['cpu']['score']
        if cpu_score < 800:
            print("🔴 CPU: Prestazioni limitate. Considera un upgrade del processore.")
        elif cpu_score < 1200:
            print("🟡 CPU: Prestazioni discrete. Adeguate per uso quotidiano.")
        else:
            print("🟢 CPU: Ottime prestazioni per qualsiasi utilizzo.")
    
    if 'ram' in results and results['ram']['status'] == 'completato':
        ram_score = results['ram']['score']
        if ram_score < 600:
            print("🔴 RAM: Prestazioni memoria limitate. Considera più RAM o RAM più veloce.")
        elif ram_score < 1000:
            print("🟡 RAM: Prestazioni memoria discrete.")
        else:
            print("🟢 RAM: Ottime prestazioni memoria.")
    
    if 'disk' in results and results['disk']['status'] == 'completato':
        disk_score = results['disk']['score']
        if disk_score < 500:
            print("🔴 DISCO: Prestazioni storage lente. Considera un SSD.")
        elif disk_score < 800:
            print("🟡 DISCO: Prestazioni storage discrete.")
        else:
            print("🟢 DISCO: Ottime prestazioni storage.")
    
    # Uso consigliato
    print(f"\nUSO CONSIGLIATO SISTEMA (Rating: {overall_rating}):")
    print("-" * 50)
    
    if overall_score >= 2000:
        print("✅ Gaming ad alta risoluzione")
        print("✅ Editing video/3D professionale")
        print("✅ Sviluppo software complesso")
        print("✅ Calcolo scientifico")
        print("✅ Multitasking intensivo")
    elif overall_score >= 1500:
        print("✅ Gaming 1080p")
        print("✅ Editing video base")
        print("✅ Sviluppo software")
        print("✅ Multitasking")
        print("❌ Gaming 4K")
    elif overall_score >= 1000:
        print("✅ Uso ufficio")
        print("✅ Navigazione web")
        print("✅ Streaming video")
        print("✅ Sviluppo leggero")
        print("❌ Gaming pesante")
    elif overall_score >= 500:
        print("✅ Uso base quotidiano")
        print("✅ Navigazione web")
        print("❌ Multitasking intensivo")
        print("❌ Gaming")
    else:
        print("✅ Uso molto leggero")
        print("❌ Multitasking")
        print("❌ Applicazioni pesanti")

def save_results_to_file(results):
    """Salva risultati in un file di testo"""
    try:
        filename = f"benchmark_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("RISULTATI BENCHMARK SISTEMA\n")
            f.write("=" * 50 + "\n")
            f.write(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Sistema info
            sys_info = get_system_info()
            f.write("INFORMAZIONI SISTEMA:\n")
            for key, value in sys_info.items():
                f.write(f"{key}: {value}\n")
            f.write("\n")
            
            # Risultati benchmark
            f.write("RISULTATI BENCHMARK:\n")
            for component, data in results.items():
                f.write(f"\n{component.upper()}:\n")
                f.write(f"  Score: {data['score']:.0f}\n")
                f.write(f"  Status: {data['status']}\n")
                f.write(f"  Time: {data['time']:.2f}s\n")
                if 'error' in data:
                    f.write(f"  Error: {data['error']}\n")
            
            # Punteggio complessivo
            overall_score = calculate_overall_score(results)
            overall_rating, _ = get_performance_rating(overall_score)
            f.write(f"\nPUNTEGGIO COMPLESSIVO:\n")
            f.write(f"Score: {overall_score:.0f}\n")
            f.write(f"Rating: {overall_rating}\n")
        
        print(f"\nRisultati salvati in: {filename}")
        
    except Exception as e:
        print(f"Errore nel salvataggio: {e}")

def main():
    """Funzione principale"""
    try:
        # Controllo dipendenze
        print("Controllo dipendenze...")
        import psutil
        print("✅ psutil disponibile")
        
        # Esegui benchmark
        results = run_all_benchmarks()
        
        # Report finale
        print_final_report(results)
        
        # Salva risultati
        save_choice = input("\nVuoi salvare i risultati in un file? (s/n): ")
        if save_choice.lower() in ['s', 'si', 'sì', 'y', 'yes']:
            save_results_to_file(results)
        
        print("\n" + "=" * 80)
        print("BENCHMARK COMPLETATO!")
        print("=" * 80)
        
    except KeyboardInterrupt:
        print("\n\nBenchmark interrotto dall'utente.")
    except Exception as e:
        print(f"\nErrore durante l'esecuzione: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()