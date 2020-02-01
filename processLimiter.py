#!/usr/bin/python
import psutil, subprocess, time

######################

#define your process limits here, name: cpu%
processLimits = {
    "stockfish_11": 10,
    "komodo_10":    10
}

sleepTime = 60 #seconds, how long to wait before checking for new processes

######################

def findProcesses(name):
    results = []
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = proc.pid
            if (processName == name):
                results.append(processID)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return results

def limitProcess(pID, pName):
    limit = processLimits[pName]
    #print("Limiting " + str(pName) + " with pID " + str(pID) + " to " + str(limit) + "% CPU usage")
    subprocess.run(["cpulimit", "--pid="+str(pID), "--limit="+str(limit), "--quiet", "--background", "--lazy"])

def main():
    alreadyLimited = []
    
    while (True):
        #Find process IDs by name and limit them if they're not already limited
        for processName in processLimits:
            processIDs = findProcesses(processName)
            for pID in processIDs:
                if pID not in alreadyLimited:
                    limitProcess(pID, processName)
                    alreadyLimited.append(pID)

        #Clean out dead processes
        alreadyLimited[:] = [x for x in alreadyLimited if psutil.pid_exists(x)]

        time.sleep(sleepTime)

if __name__ == '__main__':
    main()
