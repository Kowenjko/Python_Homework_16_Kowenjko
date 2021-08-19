import csv
import tracemalloc
import time
import threading
import base


program = ["Mode - thread"]
base.write_csv('data.csv', 'w', program)

threads = []
tracemalloc.start()
start = time.time()

for i in range(0, base.copy):
    thread = threading.Thread(target=base.create_person, args=(i+1,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

base.print_txt('Thread', start)

print('Thread')
print("Curent %d, Peak %d" % tracemalloc.get_traced_memory())
print(f"All done! {format(time.time()-start)}")
