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
        elif processes[min_proc].arrivalTime == processes[j].arrivalTime:
            if processes[min_proc].burstTime > processes[j].burstTime:
                min_proc = j
    processes[i], processes[min_proc] = processes[min_proc], processes[i]

for process in processes:
    print(process.processID, process.burstTime, process.arrivalTime)
counter = 0
averageWaitingTime = 0.0
averageTurnAroundTime = 0.0
averageCompletionTime = 0.0
idleTime = 0

arrived = []
count = 0
min = 0

arrived.append(processes[0])
processes[0].arrived = True

timeQuanta = int(input("Enter time quanta: "))

while arrived:
    # Find element with the minimum burst time in the list
    min = 0
    for i in range(len(arrived)):
        if arrived[min].executionRemaining > arrived[i].executionRemaining != 0:
            min = i
    # Remove process from arrived list and execute it
    # and append processes that have arrived into the list

    proc = arrived[min]
    if proc.arrivalTime > count:
        print(count, "[-]", end=" ")
        idleTime += proc.arrivalTime - count
        count = proc.arrivalTime

    if proc.executionRemaining < timeQuanta:
        print(count, f"[{proc.processID}]", end=" ")
        count += proc.executionRemaining
    else:
        print(count, f"[{proc.processID}]", end=" ")
        count += timeQuanta

    for i in range(n):
        if processes[i].processID == proc.processID:
            processes[i].executionRemaining -= timeQuanta
    for i in range(n):
        if proc.processID == processes[i].processID:
            if proc.executionRemaining <= 0:
                processes[i].completionTime = count

    # Appending arrived processes to the arrived list
    for i in range(n):
        if processes[i].arrivalTime <= count and not processes[i].arrived:
            arrived.append(processes[i])
            processes[i].arrived = True

    # Removing processes that had their execution completed
    tempArrived = []
    for i in range(len(arrived)):
        if arrived[i].executionRemaining > 0:
            tempArrived.append(arrived[i])
    arrived = tempArrived
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
