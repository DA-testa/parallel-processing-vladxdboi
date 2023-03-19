# python3

def parallel_processing(n, m, data):
    output = []
    next_t = [0] * n
    av_threads = list(range(n))
    for indx, thread in enumerate(data):
        next_thrd = min(av_threads, key=lambda i: next_t[i])
        output.append((next_thrd, next_t[next_thrd]))
        next_t[next_thrd] += thread
        if next_t[next_thrd] == next_t[next_thrd-1]:
            av_threads.pop(av_threads.index(next_thrd))
            av_threads.append(next_thrd)
        
    return output

def main():

    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    print("Job schedule:")
    for i, (thread_num, start_time) in result:
        print(thread_num,start_time)

if __name__ == "__main__":
    main()
