import multiprocessing as mp
import os, random, time


def pm(task_id, task_quere):
    task = [0, '']
    task_type = random.sample(['Level A Task', 'Level B Task', 'Level C Task', 'Level S Task'], k=1)
    task[0] = task_id
    task[1] = task_type
    print('PM 接到一項', task[1], '編號', task[0])
    task_quere.put(task)


def worker(worker_id, task_quere):
    while True:
        task = list(task_quere.get())
        time.sleep(random.randrange(2))
        print('Worker', worker_id, '處理了一項', task[1], '編號', task[0], 'PID=', os.getpid())
        task_quere.task_done()


def main():
    task_quere = mp.JoinableQueue()

    worker1 = mp.Process(target=worker, args=(1, task_quere))
    worker1.daemon = True
    worker1.start()

    worker2 = mp.Process(target=worker, args=(2, task_quere))
    worker2.daemon = True
    worker2.start()

    # worker3 = mp.Process(target=worker, args=(3, task_quere))
    # worker3.daemon = True
    # worker3.start()

    for id in range(100):
        pm(id, task_quere)
    task_quere.join()
    print('Done fool')


if __name__ == '__main__':
    main()