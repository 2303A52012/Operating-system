li = list(map(int, input("Enter the list items (space separated): ").split(" ")))
n = len(li)
memory = []
hit = 0
fault = 0
max_memory_size = int(input("Enter the size of the memory: ")) 
print("List items are:", li)
for i in li:
    print(f"\nProcessing item: {i}")
    
    if i in memory:  
        hit += 1
        print(f"Page {i} is already in memory (Hit)")
    else:  
        fault += 1
        print(f"Page {i} caused a fault (Fault)")
        
        if len(memory) < max_memory_size:
            memory.append(i)  
            print(f"Added page {i} to memory.\nCurrent memory state: {memory}")
        else:
            removed_page = memory.pop(0)  
            memory.append(i)  
            print(f"Removed page {removed_page} from memory.\nAdded page {i}.\nCurrent memory state: {memory}")
print(f"\nFinal Results:\nHits = {hit}\nFaults = {fault}")
print(f"Hit rate = {hit / float(n):.2f}\nFault rate = {fault / float(n):.2f}")