#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Creating Linear Topology using Mininet'''

from mininet.topo import Topo


class LinearTopo(Topo):

    "Linear topology of k switches, with one host per switch."

    def __init__(self, k=2, hconf=None, lconf=None, **opts):
        """
        Init.
            k: number of switches (and hosts)
            hconf: host configuration options
            lconf: link configuration options
        """

        super(LinearTopo, self).__init__(**opts)
        self.k = k

        if hconf is None:
            hconf = {}

        if lconf is None:
            lconf = {}

        lastSwitch = None
        for i in range(1, k+1):
            host = self.addHost('h%d' % i, **hconf)
            switch = self.addSwitch('s%d' % i)
            self.addLink(host, switch, **lconf)
            if lastSwitch:
                self.addLink(switch, lastSwitch, **lconf)
            lastSwitch = switch


def simpleTest():
    from mininet.net import Mininet
    from mininet.link import TCLink
    from mininet.util import dumpNodeConnections
    lconf = {'bw': 10, 'delay': '5ms'}
    topo = LinearTopo(k=3, lconf=lconf)
    net = Mininet(topo, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    from mininet.log import setLogLevel
    setLogLevel('info')
    simpleTest()
