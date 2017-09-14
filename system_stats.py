import psutil
import os

class System_Stats:
    def __init__(self):
        self.running = 0
        self.cpu_info_blob = {
            "cpu_count": psutil.cpu_count() 
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
    
    def memory_usage(self):
        memory = pprint_ntuple(psutil.virtual_memory())
        swap =  pprint_ntuple(psutil.swap_memory())
        print memory
        print swap
        
    def bytes2human(n):
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


def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))


sys_1 = System_Stats()
# sys_1.cpu_info()
# sys_1.pid_info()
# sys_1.cpu_load_avg()
sys_1.memory_usage()

# print sys_1.cpu_info_blob

# cpu percentages for each core - DONE
# Number of tasks - DONE
# number of processes running - DONE
# Load Average - DONE
# Mem usage 
# Swap usage
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