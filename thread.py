 # -*- coding: utf-8 -*-

import os, time, random, threading, multiprocessing
from multiprocessing import Process, Pool, Queue

def run_proc(name):
    print ("Run child process %s (%s)..." % (name, os.getpid()))

def long_time_task(name):
    print ('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print ('Task %s runs %0.2f seconds.' % (name, (end - start)))

def write(q):
    for value in ['A', 'B', 'C']:
        print ('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print ('Get %s from queue.' % value)

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

def loop():
    x = 0
    while True:
        x = x ^ 1

# if __name__=='__main__':
#      print ('Process (%s) start...' % (os.getpid()))
#      pid = os.fork()
# if pid ==0:
#      print ('I am child process (%s) and my parent process is (%s)' % (os.getpid(), os.getppid()))
# else:
#      print ('I %s just created a child process(%s)' % (os.getpid(), pid))



# if __name__=='__main__':
#      print（'Parent process %s.' %os.getpid())
#      p = Process(target=run_proc, args=('test',))
#      print（'Process will start.'）
#      p.start()
#      p.join()
#      print（'Process end.'）

# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done.'


# if __name__=='__main__':

#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))

#     pw.start()

#     pr.start()

#     pw.join()

#     pr.terminate()

# if __name__=='__main__':
#     print ('thread %s is running...' % threading.current_thread().name)
#     t = threading.Thread(target=loop, name='LoopThread')
#     t.start()
#     t.join()
#     print('thread %s ended.' % threading.current_thread().name)

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()