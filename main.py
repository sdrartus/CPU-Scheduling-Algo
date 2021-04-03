import FCFS as fcfs
import SJF as sjf
import SRTF as srtf
import priority as pr
import Robin as r
import MLQ as mlq

while True:
    print("[1] First Come First Serve (FCFS)")
    print("[2] Shortest-Job-First (SJF) Scheduling")
    print("[3] Shortest Remaining Time")
    print("[4] Priority Scheduling")
    print("[5] Round Robin Scheduling")
    print("[6] Multilevel Queue Scheduling")
    choice = int(input("Choose What CPU Scheduling Algorithm to Use: "))
    if choice == 1:
        processList = []
        n = int(input("How many processes?"))
        for i in range(0, n):
            process = int(input("Enter process: "))
            processList.append(process)
        print("***********")
        burstTime = []
        for i in range(0, n):
            burst = int(input("Enter burst time:"))
            burstTime.append(burst)
        print("***********")
        arrTime = []
        for i in range(0, n):
            arrival = int(input("Enter arrival time:"))
            arrTime.append(arrival)
        fcfs.avgTime(processList, n, burstTime, arrTime)
        print("----------------")
    elif choice == 2:
        sjf.main()
        print("----------------")
    elif choice == 3:
        srtf.main()
        print("----------------")
    elif choice == 4:
        pr.main()
        print("----------------")
    elif choice == 5:
        r.main()
        print("----------------")
    elif choice == 6:
        mlq.main()
        print("----------------")
    else:
        print("Program terminated")
        break