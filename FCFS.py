# FCFS
import gChart as gantt


def waitingTime(processes, nP, bTime, wTime, aTime):
    serviceTime = [0] * nP
    serviceTime[0] = 0
    wTime[0] = 0
    for i in range(1, nP):  # add burst time of prev processes
        serviceTime[i] = (serviceTime[i - 1] + bTime[i - 1])

        wTime[i] = serviceTime[i] - aTime[i]
        if (wTime[i] < 0):
            wTime[i] = 0


def aroundTime(processes, nP, bTime, wTime, tTime):
    for i in range(nP):
        tTime[i] = bTime[i] + wTime[i]


def avgTime(processes, nP, bTime, aTime):
    wTime = [0] * nP
    tTime = [0] * nP

    waitingTime(processes, nP, bTime, wTime, aTime)
    aroundTime(processes, nP, bTime, wTime, tTime)
    print(f"Processes: {format(processes)}")
    print(f"Burst Time: {format(bTime)}")
    print("Arrival Time:")
    for i in range(nP):
        print(aTime[i])
    print("Waiting Time:")
    totalwTime = 0
    totaltTime = 0
    cTime = 0
    pTime = []
    for i in range(nP):
        totalwTime = totalwTime + wTime[i]
        print(wTime[i])
    print("Turn Around Time:")
    for i in range(nP):
        totaltTime = totaltTime + tTime[i]
        print(tTime[i])
    print("Completion Time:")
    for i in range(nP):
        cTime = tTime[i] + aTime[i]
        print(cTime)
    print("------------")
    print("Average Waiting Time: " + str(totalwTime / nP))
    print("Average Turn Around Time: " + str(totaltTime / nP))
    for i in range(nP):
        item = tTime[i] + aTime[i]
        pTime.append(item)
    # print(pTime) # x legends
    # print(cTime) # max x lim
    # print(processes) # y data
    # print(nP) # y legends
    gantt.chart(pTime, cTime, processes, nP, "FCFS")
