#!/usr/bin/env python3
"""
Benchmark RAM - Test delle prestazioni della memoria
"""
import time
import random
import psutil
import gc
import sys

def get_memory_info():
    """Raccoglie informazioni sulla memoria"""
    mem = psutil.virtual_memory()
    return {
        'total_gb': round(mem.total / (1024**3), 2),
        'available_gb': round(mem.available / (1024**3), 2),
        'used_gb': round(mem.used / (1024**3), 2),
        'percent_used': mem.percent,
        'free_gb': round(mem.free / (1024**3), 2)
    }

def memory_allocation_test(size_mb=500, iterations=10):
    """Test allocazione e deallocazione memoria"""
    print(f"Test allocazione memoria: {size_mb}MB x {iterations} iterazioni")
    
    allocation_times = []
    deallocation_times = []
    
    for i in range(iterations):
        # Allocazione
        start_time = time.time()
        data = bytearray(size_mb * 1024 * 1024)  # Alloca size_mb MB
        alloc_time = time.time() - start_time
        allocation_times.append(alloc_time)
        
        # Riempimento memoria con dati random
        fill_start = time.time()
        for j in range(0, len(data), 4096):  # Ogni 4KB
            data[j:j+4096] = random.getrandbits(4096 * 8).to_bytes(4096, 'little')
        fill_time = time.time() - fill_start
        
        # Deallocazione
        dealloc_start = time.time()
        del data
        gc.collect()
        dealloc_time = time.time() - dealloc_start
        deallocation_times.append(dealloc_time)
        
        print(f"  Iterazione {i+1}: Alloc={alloc_time*1000:.2f}ms, "
              f"Fill={fill_time*1000:.2f}ms, Dealloc={dealloc_time*1000:.2f}ms")
    
    avg_alloc = sum(allocation_times) / len(allocation_times)
    avg_dealloc = sum(deallocation_times) / len(deallocation_times)
    
    return avg_alloc, avg_dealloc

def memory_throughput_test(size_mb=1000):
    """Test throughput lettura/scrittura memoria"""
    print(f"Test throughput memoria: {size_mb}MB")
    
    # Allocazione blocco di memoria
    data = bytearray(size_mb * 1024 * 1024)
    
    # Test scrittura sequenziale
    print("  Test scrittura sequenziale...")
    start_time = time.time()
    for i in range(len(data)):
        data[i] = i % 256
    write_time = time.time() - start_time
    write_speed = size_mb / write_time  # MB/s
    
    # Test lettura sequenziale
    print("  Test lettura sequenziale...")
    start_time = time.time()
    total = 0
    for byte in data:
        total += byte
    read_time = time.time() - start_time
    read_speed = size_mb / read_time  # MB/s
    
    # Test accesso casuale
    print("  Test accesso casuale...")
    random_indices = [random.randint(0, len(data)-1) for _ in range(100000)]
    
    start_time = time.time()
    for idx in random_indices:
        data[idx] = random.randint(0, 255)
    random_write_time = time.time() - start_time
    
    start_time = time.time()
    total = 0
    for idx in random_indices:
        total += data[idx]
    random_read_time = time.time() - start_time
    
    # Pulizia
    del data
    gc.collect()
    
    return {
        'sequential_write_speed': write_speed,
        'sequential_read_speed': read_speed,
        'random_write_time': random_write_time,
        'random_read_time': random_read_time
    }

def memory_pattern_test():
    """Test pattern di accesso memoria"""
    print("Test pattern di accesso...")
    
    size = 50 * 1024 * 1024  # 50MB
    data = bytearray(size)
    
    patterns = {
        'linear': lambda i, s: i % s,
        'stride_2': lambda i, s: (i * 2) % s,
        'stride_4': lambda i, s: (i * 4) % s,
        'stride_8': lambda i, s: (i * 8) % s,
        'random': lambda i, s: random.randint(0, s-1)
    }
    
    results = {}
    iterations = 1000000
    
    for pattern_name, pattern_func in patterns.items():
        print(f"  Testing {pattern_name} pattern...")
        start_time = time.time()
        
        for i in range(iterations):
            idx = pattern_func(i, size)
            data[idx] = (data[idx] + 1) % 256
        
        elapsed = time.time() - start_time
        results[pattern_name] = iterations / elapsed  # accessi per secondo
    
    del data
    gc.collect()
    
    return results

def memory_cache_test():
    """Test prestazioni cache memoria"""
    print("Test cache memoria...")
    
    # Test diverse dimensioni per testare L1, L2, L3 cache
    cache_sizes = {
        'L1 Cache (32KB)': 32 * 1024,
        'L2 Cache (256KB)': 256 * 1024,
        'L3 Cache (8MB)': 8 * 1024 * 1024,
        'RAM (64MB)': 64 * 1024 * 1024
    }
    
    results = {}
    
    for cache_name, size in cache_sizes.items():
        print(f"  Testing {cache_name}...")
        data = bytearray(size)
        iterations = 1000000
        
        # Riempimento iniziale
        for i in range(size):
            data[i] = i % 256
        
        # Test accesso
        start_time = time.time()
        total = 0
        for i in range(iterations):
            idx = i % size
            total += data[idx]
        elapsed = time.time() - start_time
        
        results[cache_name] = iterations / elapsed
        del data
        gc.collect()
    
    return results

def run_memory_benchmark():
    """Esegue tutti i test memoria"""
    print("=" * 60)
    print("BENCHMARK MEMORIA RAM")
    print("=" * 60)
    
    # Informazioni memoria
    mem_info = get_memory_info()
    print("\nINFORMAZIONI MEMORIA:")
    print("-" * 40)
    for key, value in mem_info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Test allocazione
    print("\n" + "=" * 40)
    print("TEST ALLOCAZIONE MEMORIA")
    print("=" * 40)
    avg_alloc, avg_dealloc = memory_allocation_test(200, 5)
    print(f"Tempo medio allocazione: {avg_alloc*1000:.2f}ms")
    print(f"Tempo medio deallocazione: {avg_dealloc*1000:.2f}ms")
    
    # Test throughput
    print("\n" + "=" * 40)
    print("TEST THROUGHPUT MEMORIA")
    print("=" * 40)
    throughput = memory_throughput_test(500)
    print(f"Velocità scrittura sequenziale: {throughput['sequential_write_speed']:.0f} MB/s")
    print(f"Velocità lettura sequenziale: {throughput['sequential_read_speed']:.0f} MB/s")
    print(f"Tempo accesso casuale scrittura: {throughput['random_write_time']*1000:.2f}ms")
    print(f"Tempo accesso casuale lettura: {throughput['random_read_time']*1000:.2f}ms")
    
    # Test pattern
    print("\n" + "=" * 40)
    print("TEST PATTERN ACCESSO")
    print("=" * 40)
    patterns = memory_pattern_test()
    for pattern, speed in patterns.items():
        print(f"{pattern}: {speed:,.0f} accessi/sec")
    
    # Test cache
    print("\n" + "=" * 40)
    print("TEST CACHE MEMORIA")
    print("=" * 40)
    cache_results = memory_cache_test()
    for cache_level, speed in cache_results.items():
        print(f"{cache_level}: {speed:,.0f} accessi/sec")
    
    # Calcolo punteggio
    base_score = 1000
    alloc_score = (1 / (avg_alloc * 1000)) * base_score  # Più veloce = punteggio più alto
    throughput_score = (throughput['sequential_read_speed'] / 1000) * base_score
    pattern_score = (patterns['linear'] / 1000000) * base_score
    
    total_score = (alloc_score + throughput_score + pattern_score) / 3
    
    print("\n" + "=" * 40)
    print("PUNTEGGI")
    print("=" * 40)
    print(f"Punteggio Allocazione: {alloc_score:.0f}")
    print(f"Punteggio Throughput: {throughput_score:.0f}")
    print(f"Punteggio Pattern: {pattern_score:.0f}")
    print(f"PUNTEGGIO TOTALE RAM: {total_score:.0f}")
    
    return total_score

if __name__ == "__main__":
    try:
        run_memory_benchmark()
    except KeyboardInterrupt:
        print("\nBenchmark interrotto dall'utente")
    except Exception as e:
        print(f"Errore durante il benchmark: {e}")