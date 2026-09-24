KB = 1024
MB = 1048576
GB = 1073741824

num_entries = input("Please enter the number of entries per second: ")
entry_size = input("Please enter the average number of bytes per entry: ")

num_entries_int = int(num_entries)
entry_size_int = int(entry_size)

kb_size = ((num_entries_int * entry_size_int) * 60) / KB

print("Storage Estimates")
print(f"Per minute: {kb_size}KB")