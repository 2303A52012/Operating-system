li = list(map(int, input("Enter the list items (space separated): ").split(" ")))
n = len(li)
memory = []
hit = 0
fault = 0
max_memory_size = int(input("Enter the size of the memory: ")) 
print("List items are:", li)
for i in range(n):
    print(f"\nIteration {i+1}: Processing item {li[i]}")
    if li[i] in memory: 
        hit += 1
        print(f"Page {li[i]} is already in memory (Hit)")
    else: 
        fault += 1
        print(f"Page {li[i]} caused a fault (Fault)")
        if len(memory) < max_memory_size:
            memory.append(li[i]) 
        else:
            memoryidx = []
            for item in memory:
                if item in li[i+1:]:
                    memoryidx.append(li[i+1:].index(item))
                else:
                    memoryidx.append(float('inf'))
            item_to_replace = memory[memoryidx.index(max(memoryidx))]
            print(f"Removing page {item_to_replace} from memory")
            memory.remove(item_to_replace)
            memory.append(li[i])
    print("Current memory state:", memory)
print(f"\nFinal Results:\nHit  = {hit}\nFault = {fault}")
print(f"\nFinal Results:\nHit rate = {hit / float(n)}\nFault rate = {fault / float(n)}")