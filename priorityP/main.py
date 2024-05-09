class Process:
    def __init__(self, processID, arrivalTime, burstTime, priority):
        self.processID = processID
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.priority = priority
        self.arrived = False
        self.executionRemaining = burstTime

n = int(input("Enter the number of processes: "))

processes = []
for i in range(n):
    print(f"Process number: {i}")
    processID = int(input("Enter process ID: "))
    burstTime = int(input("Enter burst time: "))
    priority = int(input("Enter priority: "))
    arrivalTime = int(input("Enter arrival time: "))
    processes.append(Process(processID, arrivalTime, burstTime, priority))

for i in range(n):
    min_proc = i
    for j in range(i + 1, n):
        if processes[min_proc].arrivalTime > processes[j].arrivalTime:
            min_proc = j
    processes[i], processes[min_proc] = processes[min_proc], processes[i]

for i in range(n):
    min_proc = i
    for j in range(i + 1, n):
        if processes[min_proc].arrivalTime > processes[j].arrivalTime:
            min_proc = j
        elif processes[min_proc].arrivalTime == processes[j].arrivalTime:
            if processes[min_proc].priority > processes[j].priority:
                min_proc = j
            elif processes[min_proc].priority == processes[j].priority:
                if processes[min_proc].processID > processes[j].processID:
                    min_proc = j
print()
for process in processes:
    print(process.processID)

averageWaitingTime = 0.0
averageTurnAroundTime = 0.0
averageCompletionTime = 0.0
idleTime = 0

arrived = []
count = 0
min = 0

arrived.append(processes[0])
processes[0].arrived = True
print()
timeQuanta = int(input("Enter time quanta: "))
print()
priorityOrder = int(input("If lower priority number == higher priority, enter 0. Else enter 1 or above."))
print()
while arrived:
    min = 0
    # Find the highest priority process and execute it
    min = 0
    if not priorityOrder:
        for i in range(len(arrived)):
            if arrived[min].priority > arrived[i].priority:
                min = i
    else:
        for i in range(len(arrived)):
            if arrived[min].priority < arrived[i].priority:
                min = i

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

for i in range(n):
    min_proc = i
    for j in range(i + 1, n):
        if processes[min_proc].processID > processes[j].processID:
            min_proc = j
    processes[i], processes[min_proc] = processes[min_proc], processes[i]

print("PID PRI AT BT TAT CT WT")
for process in processes:
    print(process.processID, process.priority, process.arrivalTime, process.burstTime, process.turnAroundTime, process.completionTime,
          process.waitingTime)
    averageCompletionTime += process.completionTime
    averageWaitingTime += process.waitingTime
    averageTurnAroundTime += process.turnAroundTime

averageCompletionTime, averageWaitingTime, averageTurnAroundTime = averageCompletionTime / n, averageWaitingTime / n, averageTurnAroundTime / n
print(
    f"Average completion time, average waiting time and average turn around time are respectively {averageCompletionTime}, {averageWaitingTime}, and {averageTurnAroundTime}")
