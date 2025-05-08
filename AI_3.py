def selectionSort(arr): 
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i + 1, len(arr)): 
            if arr[j] < arr[min_idx]: 
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap outside the inner loop 
    return arr 

print("Sorted Array:", selectionSort([10, 89, 56, 45, 34, 65, 15, 76])) 

# --- Job Scheduling --- 
profit = [15, 27, 10, 100, 150] 
jobs = ["j1", "j2", "j3", "j4", "j5"] 
deadline = [2, 3, 3, 3, 4] 

# Zip and sort based on profit descending 
profitNJobs = list(zip(profit, jobs, deadline)) 
profitNJobs.sort(key=lambda x: x[0], reverse=True) 

# Find maximum deadline to size the slot array 
max_deadline = max(deadline) 
slot = [0] * (max_deadline + 1)  # Slot[0] is unused 
ans = ["null"] * (max_deadline + 1) 
total_profit = 0 

for job in profitNJobs: 
    for j in range(job[2], 0, -1):  # j = deadline to 1 
        if slot[j] == 0: 
            slot[j] = 1 
            ans[j] = job[1] 
            total_profit += job[0] 
            break 

# Filter out "null" entries and print results 
scheduled_jobs = [job for job in ans[1:] if job != 'null'] 
print("Jobs scheduled buddy:", scheduled_jobs) 
print("Total Profit:", total_profit) 