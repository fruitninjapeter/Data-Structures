import random
import time


def selection_sort(alist):
    count = 0
    for i in range(len(alist)-1, 0, -1):    # n - 1 passes,
        maxpos = 0
        for j in range(1, i+1):
            count += 1
            if alist[j] > alist[maxpos]:
                maxpos = j
        temp = alist[i]
        alist[i] = alist[maxpos]
        alist[maxpos] = temp
    return count

def insertion_sort(alist):
    count = 0
    for i in range(1, len(alist)):
        current = alist[i]
        pos = i - 1
        count += 1
        while pos > 0 and alist[pos] > current:    # if current is less than previous position
            alist[pos+1] = alist[pos]
            pos = pos-1
            if pos > i-1:
                count += 1
        alist[pos+1] = current
    return count


def main():
    # Give the random number generator a seed, so the same sequence of
    # random numbers is generated at each run
    random.seed(1234)
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 1000)
    start_time = time.time()
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)


if __name__ == '__main__':
    main()