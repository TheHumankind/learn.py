from multiprocessing import cpu_count, Process
import time

start = time.perf_counter()

def counter(num):
    count = 0
    while count < num:
        count += 1
    print(count)

def main():

    print(cpu_count())

    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    b.join()
    a.join()
    c.join()
    d.join()
    print('finished in ', time.perf_counter() - start, ' seconds')

if __name__ == '__main__':
    main()