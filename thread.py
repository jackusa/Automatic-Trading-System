 # -*- coding: utf-8 -*-

import os, time, random, threading
from multiprocessing import Process, Pool, Queue

def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

while False:
	if __name__=='__main__':
		print  'Process (%s) start...' % (os.getpid())
		pid = os.fork()

		if pid ==0:
			print 'I am child process (%s) and my parent process is (%s)' % (os.getpid(), os.getppid())
		else:
			print 'I %s just created a child process(%s)' % (os.getpid(), pid)


while False:
	if __name__=='__main__':
	    print 'Parent process %s.' % os.getpid()
	    p = Process(target=run_proc, args=('test',))
	    print 'Process will start.'
	    p.start()
	    p.join()
	    print 'Process end.'



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