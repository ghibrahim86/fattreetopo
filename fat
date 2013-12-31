#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Creating Fat-Tree Topology using Mininet'''

from mininet.topo import Topo


class FatTreeTopo(Topo):

    "Fat-Tree Topology topology of k core switches"

    def __init__(self, k=2, hconf=None, lconf=None, **opts):
        """
        Init.
            k: number of core switches.
            hconf: host configuration options
            lconf: link configuration options
        """

        super(FatTreeTopo, self).__init__(**opts)
        self.k = k

        if hconf is None:
            hconf = {}

        if lconf is None:
            lconf = {}

        aggregation_nodes = []
        for i in range(k):
            a1 = self.addSwitch('a%d' % (2 * i + 1))
            a2 = self.addSwitch('a%d' % (2 * i + 2))
            aggregation_nodes.append(a1)
            aggregation_nodes.append(a2)
            e1 = self.addSwitch('e%d' % (2 * i + 1))
            e2 = self.addSwitch('e%d' % (2 * i + 2))
            self.addLink(a1, e1, **lconf)
            self.addLink(a2, e2, **lconf)
            self.addLink(a1, e2, **lconf)
            self.addLink(a2, e1, **lconf)
            h1 = self.addHost('h%d' % (4 * i + 1), **hconf)
            h2 = self.addHost('h%d' % (4 * i + 2), **hconf)
            h3 = self.addHost('h%d' % (4 * i + 3), **hconf)
            h4 = self.addHost('h%d' % (4 * i + 4), **hconf)
            self.addLink(e1, h1, **lconf)
            self.addLink(e1, h2, **lconf)
            self.addLink(e2, h3, **lconf)
            self.addLink(e2, h4, **lconf)

        for i in range(1, k + 1):
            c = self.addSwitch('c%d' % i)
            for a in aggregation_nodes:
                self.addLink(c, a, **lconf)


def simpleTest():
    from mininet.net import Mininet
    from mininet.link import TCLink
    from mininet.util import dumpNodeConnections
    lconf = {'bw': 10, 'delay': '5ms'}
    topo = FatTreeTopo(k=2, lconf=lconf)
    net = Mininet(topo, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    net.stop()

if __name__ == '__main__':
    from mininet.log import setLogLevel
    setLogLevel('info')
    simpleTest()
