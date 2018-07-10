import threading
import time

def worker(num):
	print 'In worker'
	if num == 1:
		time.sleep(3)
	print 'Worker: %s' % num
	return

t = threading.Thread(target=worker, args=(1,))
t.start()

t = threading.Thread(target=worker, args=(2,))
t.start()