from Queue import Queue

def hotPotato(namelist,num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    #print(simqueue.items)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            print(simqueue.items)
        print("出局者为",simqueue.dequeue())

    return simqueue.dequeue()

print(hotPotato(['1','2','3','4','5','6','7'],7))
