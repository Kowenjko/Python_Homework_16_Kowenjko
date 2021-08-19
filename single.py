import tracemalloc
import time
import base


program = ["Mode - single"]
base.write_csv('data.csv', 'w', program)

tracemalloc.start()
start = time.time()

for i in range(0, base.copy):
    base.create_person(i+1)


base.print_txt('Single', start)


print('Single')
print("Curent %d, Peak %d" % tracemalloc.get_traced_memory())
print(f"All done! {format(time.time()-start)}")
