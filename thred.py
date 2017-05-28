import os

print  'Process (%s) start...' % (os.getpid())
pid = os.fork()

if pid ==0:
	print 'child Process (%s) and parent process (%s)' % (os.getpid(), os.getppid())
else:
	print 'The %s just create a child process(%s)' % (os.getpid(), pid)

