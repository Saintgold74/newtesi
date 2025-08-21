#!/usr/bin/env python3
"""
Benchmark Disco - Test delle prestazioni di storage
"""
import time
import os
import tempfile
import random
import string
import shutil
import psutil

def get_disk_info():
    """Raccoglie informazioni sui dischi"""
    disk_info = []
    
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                'device': partition.device,
                'mountpoint': partition.mountpoint,
                'fstype': partition.fstype,
                'total_gb': round(usage.total / (1024**3), 2),
                'used_gb': round(usage.used / (1024**3), 2),
                'free_gb': round(usage.free / (1024**3), 2),
                'percent_used': round((usage.used / usage.total) * 100, 2)
            })
        except PermissionError:
            continue
    
    return disk_info

def sequential_write_test(test_dir, file_size_mb=100, chunk_size_kb=64):
    """Test scrittura sequenziale"""
    print(f"Test scrittura sequenziale: {file_size_mb}MB (chunk: {chunk_size_kb}KB)")
    
    test_file = os.path.join(test_dir, "sequential_write_test.dat")
    chunk_size = chunk_size_kb * 1024
    total_bytes = file_size_mb * 1024 * 1024
    chunks_needed = total_bytes // chunk_size
    
    # Genera dati casuali
    test_data = os.urandom(chunk_size)
    
    start_time = time.time()
    
    with open(test_file, 'wb') as f:
        for i in range(chunks_needed):
            f.write(test_data)
            f.flush()
            os.fsync(f.fileno())  # Forza scrittura su disco
    
    end_time = time.time()
    elapsed = end_time - start_time
    speed_mbps = file_size_mb / elapsed
    
    # Pulizia
    os.remove(test_file)
    
    return speed_mbps, elapsed

def sequential_read_test(test_dir, file_size_mb=100, chunk_size_kb=64):
    """Test lettura sequenziale"""
    print(f"Test lettura sequenziale: {file_size_mb}MB (chunk: {chunk_size_kb}KB)")
    
    test_file = os.path.join(test_dir, "sequential_read_test.dat")
    chunk_size = chunk_size_kb * 1024
    total_bytes = file_size_mb * 1024 * 1024
    chunks_needed = total_bytes // chunk_size
    
    # Crea file di test
    test_data = os.urandom(chunk_size)
    with open(test_file, 'wb') as f:
        for i in range(chunks_needed):
            f.write(test_data)
    
    # Test lettura
    start_time = time.time()
    
    with open(test_file, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
    
    end_time = time.time()
    elapsed = end_time - start_time
    speed_mbps = file_size_mb / elapsed
    
    # Pulizia
    os.remove(test_file)
    
    return speed_mbps, elapsed

def random_access_test(test_dir, file_size_mb=50, num_operations=1000):
    """Test accesso casuale"""
    print(f"Test accesso casuale: {file_size_mb}MB, {num_operations} operazioni")
    
    test_file = os.path.join(test_dir, "random_access_test.dat")
    file_size_bytes = file_size_mb * 1024 * 1024
    
    # Crea file di test
    with open(test_file, 'wb') as f:
        f.write(os.urandom(file_size_bytes))
    
    # Test scritture casuali
    write_times = []
    with open(test_file, 'r+b') as f:
        for i in range(num_operations // 2):
            position = random.randint(0, file_size_bytes - 4096)
            data = os.urandom(4096)  # 4KB block
            
            start_time = time.time()
            f.seek(position)
            f.write(data)
            f.flush()
            write_time = time.time() - start_time
            write_times.append(write_time)
    
    # Test letture casuali
    read_times = []
    with open(test_file, 'rb') as f:
        for i in range(num_operations // 2):
            position = random.randint(0, file_size_bytes - 4096)
            
            start_time = time.time()
            f.seek(position)
            f.read(4096)
            read_time = time.time() - start_time
            read_times.append(read_time)
    
    avg_write_time = sum(write_times) / len(write_times)
    avg_read_time = sum(read_times) / len(read_times)
    
    # IOPS (Input/Output Operations Per Second)
    write_iops = 1 / avg_write_time if avg_write_time > 0 else 0
    read_iops = 1 / avg_read_time if avg_read_time > 0 else 0
    
    # Pulizia
    os.remove(test_file)
    
    return {
        'write_iops': write_iops,
        'read_iops': read_iops,
        'avg_write_time_ms': avg_write_time * 1000,
        'avg_read_time_ms': avg_read_time * 1000
    }

def small_files_test(test_dir, num_files=1000, file_size_bytes=4096):
    """Test creazione/lettura molti file piccoli"""
    print(f"Test file piccoli: {num_files} file da {file_size_bytes} bytes")
    
    test_subdir = os.path.join(test_dir, "small_files_test")
    os.makedirs(test_subdir, exist_ok=True)
    
    # Test creazione
    test_data = os.urandom(file_size_bytes)
    create_start = time.time()
    
    for i in range(num_files):
        file_path = os.path.join(test_subdir, f"test_{i:06d}.dat")
        with open(file_path, 'wb') as f:
            f.write(test_data)
    
    create_time = time.time() - create_start
    create_rate = num_files / create_time
    
    # Test lettura
    read_start = time.time()
    
    for i in range(num_files):
        file_path = os.path.join(test_subdir, f"test_{i:06d}.dat")
        with open(file_path, 'rb') as f:
            f.read()
    
    read_time = time.time() - read_start
    read_rate = num_files / read_time
    
    # Test eliminazione
    delete_start = time.time()
    shutil.rmtree(test_subdir)
    delete_time = time.time() - delete_start
    delete_rate = num_files / delete_time
    
    return {
        'create_rate': create_rate,
        'read_rate': read_rate,
        'delete_rate': delete_rate,
        'create_time': create_time,
        'read_time': read_time,
        'delete_time': delete_time
    }

def large_file_test(test_dir, file_size_mb=500):
    """Test con file di grandi dimensioni"""
    print(f"Test file grande: {file_size_mb}MB")
    
    test_file = os.path.join(test_dir, "large_file_test.dat")
    chunk_size = 1024 * 1024  # 1MB chunks
    chunks_needed = file_size_mb
    
    # Test scrittura
    write_start = time.time()
    with open(test_file, 'wb') as f:
        for i in range(chunks_needed):
            f.write(os.urandom(chunk_size))
            if i % 50 == 0:  # Sync ogni 50MB
                f.flush()
                os.fsync(f.fileno())
    
    write_time = time.time() - write_start
    write_speed = file_size_mb / write_time
    
    # Test copia
    copy_file = os.path.join(test_dir, "large_file_copy.dat")
    copy_start = time.time()
    shutil.copy2(test_file, copy_file)
    copy_time = time.time() - copy_start
    copy_speed = file_size_mb / copy_time
    
    # Pulizia
    os.remove(test_file)
    os.remove(copy_file)
    
    return {
        'write_speed': write_speed,
        'copy_speed': copy_speed,
        'write_time': write_time,
        'copy_time': copy_time
    }

def disk_latency_test(test_dir, num_tests=100):
    """Test latenza disco"""
    print(f"Test latenza disco: {num_tests} operazioni")
    
    latencies = []
    
    for i in range(num_tests):
        test_file = os.path.join(test_dir, f"latency_test_{i}.tmp")
        
        # Misura tempo di creazione + scrittura + sync
        start_time = time.time()
        with open(test_file, 'wb') as f:
            f.write(b'test_data' * 100)  # 900 bytes
            f.flush()
            os.fsync(f.fileno())
        latency = (time.time() - start_time) * 1000  # in ms
        latencies.append(latency)
        
        # Pulizia immediata
        os.remove(test_file)
    
    avg_latency = sum(latencies) / len(latencies)
    min_latency = min(latencies)
    max_latency = max(latencies)
    
    return {
        'avg_latency_ms': avg_latency,
        'min_latency_ms': min_latency,
        'max_latency_ms': max_latency
    }

def run_disk_benchmark():
    """Esegue tutti i test disco"""
    print("=" * 60)
    print("BENCHMARK DISCO")
    print("=" * 60)
    
    # Informazioni dischi
    disk_info = get_disk_info()
    print("\nINFORMAZIONI DISCHI:")
    print("-" * 40)
    for disk in disk_info:
        print(f"Disco: {disk['device']}")
        print(f"  Mount point: {disk['mountpoint']}")
        print(f"  File system: {disk['fstype']}")
        print(f"  Totale: {disk['total_gb']} GB")
        print(f"  Libero: {disk['free_gb']} GB ({100-disk['percent_used']:.1f}%)")
        print()
    
    # Crea directory temporanea per i test
    with tempfile.TemporaryDirectory(prefix="disk_benchmark_") as test_dir:
        print(f"Directory test: {test_dir}")
        
        # Test scrittura sequenziale
        print("\n" + "=" * 40)
        print("TEST SCRITTURA SEQUENZIALE")
        print("=" * 40)
        seq_write_speed, seq_write_time = sequential_write_test(test_dir, 100)
        print(f"Velocità: {seq_write_speed:.2f} MB/s")
        print(f"Tempo: {seq_write_time:.2f} secondi")
        
        # Test lettura sequenziale
        print("\n" + "=" * 40)
        print("TEST LETTURA SEQUENZIALE")
        print("=" * 40)
        seq_read_speed, seq_read_time = sequential_read_test(test_dir, 100)
        print(f"Velocità: {seq_read_speed:.2f} MB/s")
        print(f"Tempo: {seq_read_time:.2f} secondi")
        
        # Test accesso casuale
        print("\n" + "=" * 40)
        print("TEST ACCESSO CASUALE")
        print("=" * 40)
        random_results = random_access_test(test_dir, 50, 500)
        print(f"IOPS Scrittura: {random_results['write_iops']:.0f}")
        print(f"IOPS Lettura: {random_results['read_iops']:.0f}")
        print(f"Latenza Scrittura: {random_results['avg_write_time_ms']:.2f}ms")
        print(f"Latenza Lettura: {random_results['avg_read_time_ms']:.2f}ms")
        
        # Test file piccoli
        print("\n" + "=" * 40)
        print("TEST FILE PICCOLI")
        print("=" * 40)
        small_files = small_files_test(test_dir, 500)
        print(f"Creazione: {small_files['create_rate']:.0f} file/sec")
        print(f"Lettura: {small_files['read_rate']:.0f} file/sec")
        print(f"Eliminazione: {small_files['delete_rate']:.0f} file/sec")
        
        # Test latenza
        print("\n" + "=" * 40)
        print("TEST LATENZA")
        print("=" * 40)
        latency = disk_latency_test(test_dir, 50)
        print(f"Latenza media: {latency['avg_latency_ms']:.2f}ms")
        print(f"Latenza min: {latency['min_latency_ms']:.2f}ms")
        print(f"Latenza max: {latency['max_latency_ms']:.2f}ms")
        
        # Test file grande
        print("\n" + "=" * 40)
        print("TEST FILE GRANDE")
        print("=" * 40)
        large_file = large_file_test(test_dir, 200)
        print(f"Velocità scrittura: {large_file['write_speed']:.2f} MB/s")
        print(f"Velocità copia: {large_file['copy_speed']:.2f} MB/s")
        
        # Calcolo punteggio
        base_score = 1000
        
        # Normalizzazione punteggi (basati su valori tipici)
        write_score = min((seq_write_speed / 100) * base_score, base_score * 2)
        read_score = min((seq_read_speed / 100) * base_score, base_score * 2)
        iops_score = min((random_results['write_iops'] / 1000) * base_score, base_score * 2)
        latency_score = max(base_score - (latency['avg_latency_ms'] * 10), base_score // 10)
        
        total_score = (write_score + read_score + iops_score + latency_score) / 4
        
        print("\n" + "=" * 40)
        print("PUNTEGGI")
        print("=" * 40)
        print(f"Punteggio Scrittura Seq.: {write_score:.0f}")
        print(f"Punteggio Lettura Seq.: {read_score:.0f}")
        print(f"Punteggio IOPS: {iops_score:.0f}")
        print(f"Punteggio Latenza: {latency_score:.0f}")
        print(f"PUNTEGGIO TOTALE DISCO: {total_score:.0f}")
        
        return total_score

if __name__ == "__main__":
    try:
        run_disk_benchmark()
    except KeyboardInterrupt:
        print("\nBenchmark interrotto dall'utente")
    except Exception as e:
        print(f"Errore durante il benchmark: {e}")