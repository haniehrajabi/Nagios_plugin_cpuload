import nagiosplugin
import commands
import re,multiprocessing
import argparse

class Load(nagiosplugin.Resource):

    def __init__(self, percpu=False):
        self.percpu = percpu

    def cpus(self):
        #cpus = int(subprocess.check_output(['nproc']))
        cpus=multiprocessing.cpu_count()

        return cpus

    def probe(self):
        #_log.info('reading load from /proc/loadavg')
        with open('/proc/loadavg') as loadavg:
            load = loadavg.readline().split()[0:3]
        cpus = self.cpus() if self.percpu else 1
        load = [float(l) / cpus for l in load]
        for i, period in enumerate([1, 5, 15]):
            yield nagiosplugin.Metric('load%d' % period, load[i], min=0,
                                      context='load')
