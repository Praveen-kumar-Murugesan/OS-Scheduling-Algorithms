from tkinter import *

class Process:
    def __init__(self, processID, burstTime, arrivalTime):
        self.processID = processID
        self.burstTime = burstTime
        self.arrivalTime = arrivalTime
        self.waitingTime = 0
        self.turnAroundTime = 0
        self.completionTime = 0

n = int(input("Enter the number of processes: "))
processes = []
for i in range(n):
    print("Process number:", i + 1)
    processID = int(input("Enter process ID for process: "))
    burstTime = int(input("Enter burst time for process: "))
    arrivalTime = float(input("Enter arrival time for process: "))
    processes.append(Process(processID, burstTime, arrivalTime))

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

print("Process IDs will be printed inside brackets [].")
for process in processes:
    if process.arrivalTime > counter:
        print(counter, "[-]", end=" ")
        idleTime += process.arrivalTime - counter
        counter = process.arrivalTime
    print(counter, f"[{process.processID}]", end=" ")
    counter += process.burstTime
    process.completionTime = counter
    process.turnAroundTime = process.completionTime - process.arrivalTime
    process.waitingTime = process.turnAroundTime - process.burstTime
print(counter)

print(f"The idle time for this program was {idleTime}")

print("PID AT BT TAT CT WT")
for process in processes:
    print(process.processID, process.arrivalTime, process.burstTime, process.turnAroundTime, process.completionTime, process.waitingTime)
    averageCompletionTime += process.completionTime
    averageWaitingTime += process.waitingTime
    averageTurnAroundTime += process.turnAroundTime

averageCompletionTime, averageWaitingTime, averageTurnAroundTime = averageCompletionTime/n, averageWaitingTime/n, averageTurnAroundTime/n
print(f"Average completion time, average waiting time and average turn around time are respectively {averageCompletionTime}, {averageWaitingTime}, and {averageTurnAroundTime}")