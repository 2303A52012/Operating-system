li = list(map(int, input("Enter the list items (space separated): ").split(" ")))
n = len(li)
memory = []
recent_usage = []
hit = 0
fault = 0
max_memory_size = int(input("Enter the size of the memory: ")) 
print("List items are:", li)
for i in range(n):
    print(f"\nIteration {i+1}: Processing item {li[i]}")
    if li[i] in memory:  
        hit += 1
        print(f"Page {li[i]} is already in memory (Hit)")
        recent_usage.remove(li[i])
        recent_usage.append(li[i])
    else:  
        fault += 1
        print(f"Page {li[i]} caused a fault (Fault)")
        if len(memory) < max_memory_size:
            memory.append(li[i]) 
            recent_usage.append(li[i])
        else:
            lru_page = recent_usage.pop(0)  
            print(f"Removing page {lru_page} from memory (Least Recently Used)")
            memory.remove(lru_page)
            memory.append(li[i])
            recent_usage.append(li[i])
    print("Current memory state:", memory)
    print("Recent usage order:", recent_usage)
print(f"\nFinal Results:\nHit = {hit}\nFault = {fault}")
print(f"\nFinal Results:\nHit rate = {hit / float(n)}\nFault rate = {fault / float(n)}")