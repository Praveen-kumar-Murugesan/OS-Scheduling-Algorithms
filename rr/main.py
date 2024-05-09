class Process:
    def __init__(self, processID, burstTime, arrivalTime):
        self.processID = processID
        self.burstTime = burstTime
        self.arrivalTime = arrivalTime
        self.waitingTime = 0
        self.turnAroundTime = 0
        self.completionTime = 0
        self.executionRemaining = burstTime
        self.arrived = False


n = int(input("Enter the number of processes: "))
processes = []
for i in range(n):
    print("Process number:", i + 1)
    processID = int(input("Enter process ID for process: "))
    burstTime = int(input("Enter burst time for process: "))
    arrivalTime = float(input("Enter arrival time for process: "))
    processes.append(Process(processID, burstTime, arrivalTime))

# Sorting processes by arrival time
for i in range(n):
    min_proc = i
    for j in range(i + 1, n):
        if processes[min_proc].arrivalTime > processes[j].arrivalTime:
            min_proc = j
    processes[i], processes[min_proc] = processes[min_proc], processes[i]

for process in processes:
    print(process.processID, process.burstTime, process.arrivalTime)
counter = 0
averageWaitingTime = 0.0
averageTurnAroundTime = 0.0
averageCompletionTime = 0.0
idleTime = 0

readyQueue = []
count = 0
min = 0

readyQueue.append(processes[0])
processes[0].arrived = True

timeQuanta = int(input("Enter time quanta: "))

while readyQueue:
    proc = readyQueue[0]
    # Execute process for specified time quanta
    # Check if any processes have arrived and add it to the ready queue
    # If execution time is still left, add the process to the end of the queue

    # Accounting for idle time
    if proc.arrivalTime > count:
        print(count, "[-]", end=" ")
        idleTime += proc.arrivalTime - count
        count = proc.arrivalTime

    # If execution remaining is less than time quanta, perform a context switch and update completion time
    # Else perform process normally
    if proc.executionRemaining < timeQuanta:
        print(count, f"[{proc.processID}]", end=" ")
        count += proc.executionRemaining
        for i in range(n):
            if processes[i].processID == proc.processID:
                processes[i].completionTime = count
        proc.executionRemaining = 0
    else:
        print(count, f"[{proc.processID}]", end=" ")
        count += timeQuanta
        proc.executionRemaining -= timeQuanta
        if proc.executionRemaining == 0:
            for i in range(n):
                if processes[i].processID == proc.processID:
                    processes[i].completionTime = count

    # Searching for arrived processes during execution
    for i in range(n):
        if processes[i].arrivalTime <= count and not processes[i].arrived:
            readyQueue.append(processes[i])
            processes[i].arrived = True

    # Updating execution remaining time
    for i in range(n):
        if processes[i].processID == proc.processID:
            processes[i].executionRemaining = proc.executionRemaining
    pr = readyQueue.pop(0)
    if pr.executionRemaining > 0:
        readyQueue.append(pr)
print(count)

for process in processes:
    process.turnAroundTime = process.completionTime - process.arrivalTime
    process.waitingTime = process.turnAroundTime - process.burstTime

print(f"The idle time for this program was {idleTime}")

print("PID AT BT TAT CT WT")
for process in processes:
    print(process.processID, process.arrivalTime, process.burstTime, process.turnAroundTime, process.completionTime,
          process.waitingTime)
    averageCompletionTime += process.completionTime
    averageWaitingTime += process.waitingTime
    averageTurnAroundTime += process.turnAroundTime

averageCompletionTime, averageWaitingTime, averageTurnAroundTime = averageCompletionTime / n, averageWaitingTime / n, averageTurnAroundTime / n
print(
    f"Average completion time, average waiting time and average turn around time are respectively {averageCompletionTime}, {averageWaitingTime}, and {averageTurnAroundTime}")
