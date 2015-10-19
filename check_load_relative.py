#! /usr/bin/python
import sys, os, multiprocessing

core_number=multiprocessing.cpu_count()
average=os.getloadavg()
print 'relative load is {0}%'.format((average[2]/core_number)*100)
