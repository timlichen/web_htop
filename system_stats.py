import psutil
import os

class System_Stats:
    def __init__(self):
        self.running = 0
        self.cpu_info_blob = {
            "cpu_count": psutil.cpu_count() 
        }
        self.memory_info_blob = {
            "memory" : {},
            "swap" : {}
        }
        self.disk_info_blob = {
        }

    def cpu_info(self):
        for x in range(self.cpu_info_blob['cpu_count'] - 1):
            cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
            self.cpu_info_blob['cpu_1'] = cpu_percent[0]
            self.cpu_info_blob['cpu_2'] = cpu_percent[1]
            self.cpu_info_blob['cpu_3'] = cpu_percent[2]
            self.cpu_info_blob['cpu_4'] = cpu_percent[3]
        
        print "cpu_percentages added to cpu_info_blob"
        return self

    def pid_info(self):
        self.running = 0

        self.cpu_info_blob['tasks'] = len(psutil.pids())

        self.cpu_info_blob['pid_info_blob'] = {p.pid: {"pid_name":p.info, "cpu_percent": 0.0 } for p in psutil.process_iter(attrs=['name', 'username'])}

        
        for pid, name in self.cpu_info_blob['pid_info_blob'].iteritems():
            p = psutil.Process(pid)
            proc_cpu_usage = p.cpu_percent(interval=0.1)
        
            if proc_cpu_usage > 0.0:
                self.running += 1
                self.cpu_info_blob['pid_info_blob'][pid]['cpu_percent'] = proc_cpu_usage
    
    def cpu_load_avg(self):
        self.cpu_info_blob['load_avg'] = os.getloadavg()
            
        print "pid number and associated name added to cpu_info_blob"
        
        return self
        
    def bytes2human(self, n):
        # http://code.activestate.com/recipes/578019
        # >>> bytes2human(10000)
        # '9.8K'
        # >>> bytes2human(100001221)
        # '95.4M'
        symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return '%.1f%s' % (value, s)
        return "%sB" % n


    def pprint_ntuple(self, nt):
        mem_blob = {}
        for name in nt._fields:
            value = getattr(nt, name)
            if name != 'percent':
                value = self.bytes2human(value)
            mem_blob[name.capitalize()] = value 
        
        return mem_blob
    
    def memory_usage(self):
        self.memory_info_blob["memory"] = self.pprint_ntuple(psutil.virtual_memory())
        self.memory_info_blob["swap"] = self.pprint_ntuple(psutil.swap_memory())

        return self
    
    def disk_info_blob_make(self):
        self.disk_usage()
        self.disk_io()
        print self.disk_info_blob

    
    def disk_usage(self):
        partitions = psutil.disk_partitions()
        for part in partitions:
            self.disk_info_blob[str(part[1])] = self.pprint_ntuple(psutil.disk_usage(str(part[1])))
    
    def disk_io(self):
        for phys_disk, io in psutil.disk_io_counters(perdisk=True, nowrap=True):
            self.disk_info_blob[phys_disk] = io

        

        
    


sys_1 = System_Stats()
# sys_1.cpu_info()
# sys_1.pid_info()
# sys_1.cpu_load_avg()
# sys_1.memory_usage()
# print sys_1.memory_info_blob
sys_1.disk_info_blob_make()

# print sys_1.cpu_info_blob

###########
# PHASE 1 #
###########

# cpu percentages for each core - DONE
# Number of tasks - DONE
# number of processes running - DONE
# Load Average - DONE
# Mem usage - DONE
# Swap usage - DONE
# Network stats
# Disk Stats

# The pid table should include
## PID
## User
## PRI
## NI
## VIRT 
## RES
## SHR
## S
## CPU Percentage
## MEM %
## Time +
## Command

# Features should include
# Search
# Sorting
# Kill
# Nice -
# Nice +
# Process Tree

###########
# PHASE 2 #
###########

# Memory alerts
# Disk alerts
# Use sockets to monitor multiple systems and report back to a server
# Create web interface to view multiple stats

# END