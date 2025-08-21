#!/usr/bin/env python3
"""
Sistema Info - Raccoglie informazioni dettagliate sul sistema
"""
import platform
import psutil
import socket
import uuid
import subprocess
import os
import time
from datetime import datetime

def get_system_info():
    """Informazioni generali del sistema"""
    try:
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.now() - boot_time
        
        return {
            'sistema': platform.system(),
            'release': platform.release(),
            'versione': platform.version(),
            'architettura': platform.architecture()[0],
            'macchina': platform.machine(),
            'processore': platform.processor(),
            'hostname': socket.gethostname(),
            'dominio': socket.getfqdn(),
            'avvio_sistema': boot_time.strftime("%Y-%m-%d %H:%M:%S"),
            'uptime_giorni': uptime.days,
            'uptime_ore': uptime.seconds // 3600,
            'utente_corrente': os.getlogin() if hasattr(os, 'getlogin') else 'N/A'
        }
    except Exception as e:
        return {'errore': str(e)}

def get_cpu_detailed_info():
    """Informazioni dettagliate CPU"""
    try:
        cpu_freq = psutil.cpu_freq()
        cpu_times = psutil.cpu_times()
        
        info = {
            'nome_processore': platform.processor(),
            'architettura': platform.machine(),
            'core_fisici': psutil.cpu_count(logical=False),
            'core_logici': psutil.cpu_count(logical=True),
            'utilizzo_percentuale': psutil.cpu_percent(interval=1),
            'utilizzo_per_core': psutil.cpu_percent(interval=1, percpu=True)
        }
        
        if cpu_freq:
            info.update({
                'frequenza_corrente_mhz': round(cpu_freq.current, 2),
                'frequenza_minima_mhz': round(cpu_freq.min, 2),
                'frequenza_massima_mhz': round(cpu_freq.max, 2)
            })
        
        # Statistiche utilizzo CPU
        info.update({
            'tempo_utente': cpu_times.user,
            'tempo_sistema': cpu_times.system,
            'tempo_idle': cpu_times.idle,
            'interrupts': getattr(cpu_times, 'interrupt', 0),
            'context_switches': psutil.cpu_stats().ctx_switches if hasattr(psutil, 'cpu_stats') else 'N/A'
        })
        
        return info
    except Exception as e:
        return {'errore': str(e)}

def get_memory_detailed_info():
    """Informazioni dettagliate memoria"""
    try:
        virtual = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        return {
            'memoria_virtuale': {
                'totale_gb': round(virtual.total / (1024**3), 2),
                'disponibile_gb': round(virtual.available / (1024**3), 2),
                'utilizzata_gb': round(virtual.used / (1024**3), 2),
                'libera_gb': round(virtual.free / (1024**3), 2),
                'percentuale_utilizzata': virtual.percent,
                'buffer_gb': round(getattr(virtual, 'buffers', 0) / (1024**3), 2),
                'cache_gb': round(getattr(virtual, 'cached', 0) / (1024**3), 2)
            },
            'memoria_swap': {
                'totale_gb': round(swap.total / (1024**3), 2),
                'utilizzata_gb': round(swap.used / (1024**3), 2),
                'libera_gb': round(swap.free / (1024**3), 2),
                'percentuale_utilizzata': swap.percent,
                'swap_in': swap.sin,
                'swap_out': swap.sout
            }
        }
    except Exception as e:
        return {'errore': str(e)}

def get_disk_detailed_info():
    """Informazioni dettagliate dischi"""
    try:
        disks = []
        
        # Informazioni partizioni
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info = {
                    'device': partition.device,
                    'mountpoint': partition.mountpoint,
                    'fstype': partition.fstype,
                    'opts': partition.opts,
                    'totale_gb': round(usage.total / (1024**3), 2),
                    'utilizzato_gb': round(usage.used / (1024**3), 2),
                    'libero_gb': round(usage.free / (1024**3), 2),
                    'percentuale_utilizzata': round((usage.used / usage.total) * 100, 2)
                }
                disks.append(disk_info)
            except PermissionError:
                continue
        
        # Statistiche I/O disco
        disk_io = psutil.disk_io_counters()
        io_stats = {}
        if disk_io:
            io_stats = {
                'letture': disk_io.read_count,
                'scritture': disk_io.write_count,
                'bytes_letti': disk_io.read_bytes,
                'bytes_scritti': disk_io.write_bytes,
                'tempo_lettura_ms': disk_io.read_time,
                'tempo_scrittura_ms': disk_io.write_time
            }
        
        return {
            'partizioni': disks,
            'statistiche_io': io_stats
        }
    except Exception as e:
        return {'errore': str(e)}

def get_network_info():
    """Informazioni di rete"""
    try:
        interfaces = []
        
        # Interfacce di rete
        net_if_addrs = psutil.net_if_addrs()
        net_if_stats = psutil.net_if_stats()
        
        for interface_name, addresses in net_if_addrs.items():
            interface_info = {
                'nome': interface_name,
                'indirizzi': [],
                'attiva': False,
                'velocita_mbps': 0
            }
            
            for addr in addresses:
                addr_info = {
                    'famiglia': str(addr.family),
                    'indirizzo': addr.address,
                    'netmask': getattr(addr, 'netmask', None),
                    'broadcast': getattr(addr, 'broadcast', None)
                }
                interface_info['indirizzi'].append(addr_info)
            
            # Statistiche interfaccia
            if interface_name in net_if_stats:
                stats = net_if_stats[interface_name]
                interface_info['attiva'] = stats.isup
                interface_info['velocita_mbps'] = stats.speed
                interface_info['mtu'] = stats.mtu
            
            interfaces.append(interface_info)
        
        # Statistiche traffico di rete
        net_io = psutil.net_io_counters()
        traffic_stats = {}
        if net_io:
            traffic_stats = {
                'bytes_inviati': net_io.bytes_sent,
                'bytes_ricevuti': net_io.bytes_recv,
                'pacchetti_inviati': net_io.packets_sent,
                'pacchetti_ricevuti': net_io.packets_recv,
                'errori_in': net_io.errin,
                'errori_out': net_io.errout,
                'drop_in': net_io.dropin,
                'drop_out': net_io.dropout
            }
        
        return {
            'interfacce': interfaces,
            'statistiche_traffico': traffic_stats
        }
    except Exception as e:
        return {'errore': str(e)}

def get_processes_info(limit=10):
    """Informazioni sui processi (top processi per utilizzo CPU/memoria)"""
    try:
        processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status']):
            try:
                proc_info = proc.info
                proc_info['cpu_percent'] = proc.cpu_percent()
                processes.append(proc_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # Ordina per utilizzo CPU
        top_cpu = sorted(processes, key=lambda x: x['cpu_percent'] or 0, reverse=True)[:limit]
        
        # Ordina per utilizzo memoria
        top_memory = sorted(processes, key=lambda x: x['memory_percent'] or 0, reverse=True)[:limit]
        
        return {
            'totale_processi': len(processes),
            'top_cpu': top_cpu,
            'top_memory': top_memory
        }
    except Exception as e:
        return {'errore': str(e)}

def get_windows_specific_info():
    """Informazioni specifiche per Windows"""
    try:
        info = {}
        
        # Versione Windows
        try:
            result = subprocess.run(['systeminfo'], capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'OS Name' in line:
                        info['os_name'] = line.split(':', 1)[1].strip()
                    elif 'OS Version' in line:
                        info['os_version'] = line.split(':', 1)[1].strip()
                    elif 'System Type' in line:
                        info['system_type'] = line.split(':', 1)[1].strip()
                    elif 'Total Physical Memory' in line:
                        info['total_physical_memory'] = line.split(':', 1)[1].strip()
                    elif 'Available Physical Memory' in line:
                        info['available_physical_memory'] = line.split(':', 1)[1].strip()
        except:
            pass
        
        # Informazioni WMI (se disponibile)
        try:
            import wmi
            c = wmi.WMI()
            
            # Informazioni CPU
            for cpu in c.Win32_Processor():
                info['cpu_name'] = cpu.Name
                info['cpu_cores'] = cpu.NumberOfCores
                info['cpu_threads'] = cpu.NumberOfLogicalProcessors
                break
            
            # Informazioni memoria
            for memory in c.Win32_PhysicalMemory():
                if 'memory_modules' not in info:
                    info['memory_modules'] = []
                info['memory_modules'].append({
                    'capacity_gb': round(int(memory.Capacity) / (1024**3), 2),
                    'speed_mhz': memory.Speed,
                    'manufacturer': memory.Manufacturer
                })
        except ImportError:
            pass
        except Exception:
            pass
        
        return info
    except Exception as e:
        return {'errore': str(e)}

def get_hardware_temps():
    """Informazioni temperature hardware (se disponibili)"""
    try:
        temps = {}
        
        if hasattr(psutil, 'sensors_temperatures'):
            sensors = psutil.sensors_temperatures()
            for name, entries in sensors.items():
                temps[name] = []
                for entry in entries:
                    temp_info = {
                        'label': entry.label or 'N/A',
                        'current': entry.current,
                        'high': entry.high,
                        'critical': entry.critical
                    }
                    temps[name].append(temp_info)
        
        return temps
    except Exception as e:
        return {'errore': str(e)}

def get_battery_info():
    """Informazioni batteria (per laptop)"""
    try:
        battery = psutil.sensors_battery()
        if battery:
            return {
                'percentuale': battery.percent,
                'in_carica': battery.power_plugged,
                'tempo_rimasto_sec': battery.secsleft if battery.secsleft != psutil.POWER_TIME_UNLIMITED else 'Illimitato'
            }
        return {'disponibile': False}
    except Exception as e:
        return {'errore': str(e)}

def print_system_report():
    """Stampa report completo del sistema"""
    print("=" * 80)
    print("REPORT SISTEMA COMPLETO")
    print("=" * 80)
    print(f"Generato il: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Informazioni sistema
    print("INFORMAZIONI SISTEMA")
    print("-" * 50)
    sys_info = get_system_info()
    for key, value in sys_info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    # CPU
    print("\n" + "="*50)
    print("INFORMAZIONI CPU")
    print("-" * 50)
    cpu_info = get_cpu_detailed_info()
    for key, value in cpu_info.items():
        if key == 'utilizzo_per_core':
            print(f"{key.replace('_', ' ').title()}: {[f'{x:.1f}%' for x in value]}")
        else:
            print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Memoria
    print("\n" + "="*50)
    print("INFORMAZIONI MEMORIA")
    print("-" * 50)
    mem_info = get_memory_detailed_info()
    
    print("MEMORIA VIRTUALE:")
    for key, value in mem_info['memoria_virtuale'].items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    
    print("\nMEMORIA SWAP:")
    for key, value in mem_info['memoria_swap'].items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    
    # Dischi
    print("\n" + "="*50)
    print("INFORMAZIONI DISCHI")
    print("-" * 50)
    disk_info = get_disk_detailed_info()
    
    print("PARTIZIONI:")
    for i, disk in enumerate(disk_info['partizioni']):
        print(f"  Disco {i+1}:")
        for key, value in disk.items():
            print(f"    {key.replace('_', ' ').title()}: {value}")
        print()
    
    if disk_info['statistiche_io']:
        print("STATISTICHE I/O:")
        for key, value in disk_info['statistiche_io'].items():
            print(f"  {key.replace('_', ' ').title()}: {value:,}")
    
    # Rete
    print("\n" + "="*50)
    print("INFORMAZIONI RETE")
    print("-" * 50)
    net_info = get_network_info()
    
    print("INTERFACCE DI RETE:")
    for interface in net_info['interfacce']:
        print(f"  {interface['nome']}:")
        print(f"    Attiva: {interface['attiva']}")
        print(f"    Velocità: {interface['velocita_mbps']} Mbps")
        for addr in interface['indirizzi'][:2]:  # Mostra solo i primi 2 indirizzi
            print(f"    Indirizzo: {addr['indirizzo']}")
        print()
    
    if net_info['statistiche_traffico']:
        print("STATISTICHE TRAFFICO:")
        for key, value in net_info['statistiche_traffico'].items():
            print(f"  {key.replace('_', ' ').title()}: {value:,}")
    
    # Processi
    print("\n" + "="*50)
    print("PROCESSI (TOP 5)")
    print("-" * 50)
    proc_info = get_processes_info(5)
    
    print(f"Totale processi: {proc_info['totale_processi']}")
    
    print("\nTOP CPU:")
    for proc in proc_info['top_cpu']:
        print(f"  {proc['name']} (PID: {proc['pid']}) - CPU: {proc['cpu_percent']:.1f}%")
    
    print("\nTOP MEMORIA:")
    for proc in proc_info['top_memory']:
        print(f"  {proc['name']} (PID: {proc['pid']}) - RAM: {proc['memory_percent']:.1f}%")
    
    # Temperature (se disponibili)
    temps = get_hardware_temps()
    if temps and not 'errore' in temps:
        print("\n" + "="*50)
        print("TEMPERATURE HARDWARE")
        print("-" * 50)
        for sensor, readings in temps.items():
            print(f"{sensor}:")
            for reading in readings:
                print(f"  {reading['label']}: {reading['current']}°C")
    
    # Batteria (se disponibile)
    battery = get_battery_info()
    if battery.get('disponibile', True) and not 'errore' in battery:
        print("\n" + "="*50)
        print("INFORMAZIONI BATTERIA")
        print("-" * 50)
        for key, value in battery.items():
            if key != 'disponibile':
                print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Windows specific
    if platform.system() == 'Windows':
        win_info = get_windows_specific_info()
        if win_info and not 'errore' in win_info:
            print("\n" + "="*50)
            print("INFORMAZIONI WINDOWS")
            print("-" * 50)
            for key, value in win_info.items():
                if key != 'memory_modules':
                    print(f"{key.replace('_', ' ').title()}: {value}")
            
            if 'memory_modules' in win_info:
                print("\nMODULI MEMORIA:")
                for i, module in enumerate(win_info['memory_modules']):
                    print(f"  Modulo {i+1}:")
                    for key, value in module.items():
                        print(f"    {key.replace('_', ' ').title()}: {value}")

if __name__ == "__main__":
    try:
        print_system_report()
    except KeyboardInterrupt:
        print("\nReport interrotto dall'utente")
    except Exception as e:
        print(f"Errore durante la generazione del report: {e}")