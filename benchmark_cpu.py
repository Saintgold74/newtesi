#!/usr/bin/env python3
"""
Benchmark CPU - Test delle prestazioni del processore
"""
import time
import math
import multiprocessing as mp
import platform
import psutil

def cpu_stress_test(duration=10):
    """Test di stress CPU per un determinato periodo"""
    print(f"Avvio test CPU per {duration} secondi...")
    start_time = time.time()
    iterations = 0
    
    while time.time() - start_time < duration:
        # Operazioni matematiche intensive
        for i in range(1000):
            math.sqrt(i ** 2 + math.sin(i) * math.cos(i))
            math.factorial(20)
        iterations += 1000
    
    end_time = time.time()
    elapsed = end_time - start_time
    ops_per_second = iterations / elapsed
    
    return ops_per_second, iterations, elapsed

def prime_calculation_test(max_num=100000):
    """Test calcolo numeri primi"""
    print(f"Test calcolo primi fino a {max_num}...")
    start_time = time.time()
    
    primes = []
    for num in range(2, max_num + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    return len(primes), elapsed

def multi_core_test():
    """Test utilizzo multi-core"""
    print("Test multi-core...")
    cpu_count = mp.cpu_count()
    print(f"CPU disponibili: {cpu_count}")
    
    def worker_task(n):
        result = 0
        for i in range(n * 100000, (n + 1) * 100000):
            result += math.sqrt(i)
        return result
    
    # Test single-core
    start_time = time.time()
    single_result = sum(worker_task(i) for i in range(cpu_count))
    single_time = time.time() - start_time
    
    # Test multi-core
    start_time = time.time()
    with mp.Pool(cpu_count) as pool:
        multi_result = sum(pool.map(worker_task, range(cpu_count)))
    multi_time = time.time() - start_time
    
    speedup = single_time / multi_time if multi_time > 0 else 0
    
    return single_time, multi_time, speedup

def get_cpu_info():
    """Raccoglie informazioni sulla CPU"""
    try:
        cpu_freq = psutil.cpu_freq()
        return {
            'processor': platform.processor(),
            'architecture': platform.architecture()[0],
            'cores_physical': psutil.cpu_count(logical=False),
            'cores_logical': psutil.cpu_count(logical=True),
            'frequency_current': cpu_freq.current if cpu_freq else 'N/A',
            'frequency_max': cpu_freq.max if cpu_freq else 'N/A',
            'frequency_min': cpu_freq.min if cpu_freq else 'N/A'
        }
    except:
        return {
            'processor': platform.processor(),
            'architecture': platform.architecture()[0],
            'cores_physical': 'N/A',
            'cores_logical': 'N/A',
            'frequency_current': 'N/A',
            'frequency_max': 'N/A',
            'frequency_min': 'N/A'
        }

def run_cpu_benchmark():
    """Esegue tutti i test CPU"""
    print("=" * 60)
    print("BENCHMARK CPU")
    print("=" * 60)
    
    # Informazioni CPU
    cpu_info = get_cpu_info()
    print("\nINFORMAZIONI CPU:")
    print("-" * 40)
    for key, value in cpu_info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    print(f"\nUtilizzo CPU corrente: {psutil.cpu_percent(interval=1)}%")
    
    # Test stress CPU
    print("\n" + "=" * 40)
    print("TEST STRESS CPU")
    print("=" * 40)
    ops_per_sec, total_ops, elapsed = cpu_stress_test(10)
    print(f"Operazioni totali: {total_ops:,}")
    print(f"Tempo trascorso: {elapsed:.2f} secondi")
    print(f"Operazioni per secondo: {ops_per_sec:,.0f}")
    
    # Test calcolo primi
    print("\n" + "=" * 40)
    print("TEST CALCOLO NUMERI PRIMI")
    print("=" * 40)
    primes_count, prime_time = prime_calculation_test(50000)
    print(f"Primi trovati: {primes_count}")
    print(f"Tempo impiegato: {prime_time:.2f} secondi")
    print(f"Primi per secondo: {primes_count/prime_time:.0f}")
    
    # Test multi-core
    print("\n" + "=" * 40)
    print("TEST MULTI-CORE")
    print("=" * 40)
    single_time, multi_time, speedup = multi_core_test()
    print(f"Tempo single-core: {single_time:.2f} secondi")
    print(f"Tempo multi-core: {multi_time:.2f} secondi")
    print(f"Speedup: {speedup:.2f}x")
    
    # Calcolo punteggio
    base_score = 1000
    cpu_score = (ops_per_sec / 10000) * base_score
    prime_score = (primes_count / prime_time) * 10
    multi_score = speedup * 200
    
    total_score = (cpu_score + prime_score + multi_score) / 3
    
    print("\n" + "=" * 40)
    print("PUNTEGGI")
    print("=" * 40)
    print(f"Punteggio CPU Stress: {cpu_score:.0f}")
    print(f"Punteggio Primi: {prime_score:.0f}")
    print(f"Punteggio Multi-core: {multi_score:.0f}")
    print(f"PUNTEGGIO TOTALE CPU: {total_score:.0f}")
    
    return total_score

if __name__ == "__main__":
    try:
        run_cpu_benchmark()
    except KeyboardInterrupt:
        print("\nBenchmark interrotto dall'utente")
    except Exception as e:
        print(f"Errore durante il benchmark: {e}")