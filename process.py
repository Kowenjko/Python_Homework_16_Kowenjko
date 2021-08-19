
import tracemalloc
import time
from multiprocessing import Pool
import base


def main():
    p = Pool()
    p.map(base.create_person, [i+1 for i in range(0, base.copy)])


if __name__ == "__main__":

    program = ["Mode - process"]
    base.write_csv('data.csv', 'w', program)

    tracemalloc.start()
    start = time.time()

    main()

    base.print_txt('Process', start)

    print('Process')
    print("Curent %d, Peak %d" % tracemalloc.get_traced_memory())
    print(f"All done! {format(time.time()-start)}")
