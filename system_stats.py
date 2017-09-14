import psutil

class System_Stats:
    def __init__(self):
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
        self.cpu_info_blob['tasks'] = len(psutil.pids())

        self.cpu_info_blob['pid_info_blob'] = {p.pid: p.info for p in psutil.process_iter(attrs=['name', 'username'])}

        print "pid number and associated name added to cpu_info_blob"
        
        return self

sys_1 = System_Stats()
sys_1.cpu_info()
sys_1.pid_info()

# print sys_1.cpu_info_blob

# cpu percentages for each core
# Number of tasks, number of threads running
# Load Average
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