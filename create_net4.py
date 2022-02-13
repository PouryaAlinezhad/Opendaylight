'Pourya Alinezhad'
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
"""
Instructions to run the topo:
    1. Go to directory where this file is.
    2. run: sudo -E python create_net4.py
The topo has 7 switches and 8 hosts.
"""


class SimpleOVSSwitch(Topo):

    def __init__(self, **opts):
        """Create custom topo."""

        # Initialize topology
        # It uses the constructor for the Topo class
        super(SimpleOVSSwitch, self).__init__(**opts)

        # Add hosts and switches
        h1 = self.addHost('host1', ip="10.0.0.1/24", mac='00:00:00:00:00:01')
        h2 = self.addHost('host2', ip="10.0.0.2/24", mac='00:00:00:00:00:02')
        h3 = self.addHost('host3', ip="10.0.0.3/24", mac='00:00:00:00:00:03')
        h4 = self.addHost('host4', ip="10.0.0.4/24", mac='00:00:00:00:00:04')
        h5 = self.addHost('host5', ip="10.0.0.5/24", mac='00:00:00:00:00:05')
        h6 = self.addHost('host6', ip="10.0.0.6/24", mac='00:00:00:00:00:06')
        h7 = self.addHost('host7', ip="10.0.0.7/24", mac='00:00:00:00:00:07')
        h8 = self.addHost('host8', ip="10.0.0.8/24", mac='00:00:00:00:00:08')

        # Adding switches

        s1, s2,s3,s4,s5,s6,s7= [ self.addSwitch( s ,protocols='OpenFlow13') for s in ( 's1', 's2' , 's3','s4','s5','s6','s7') ]

        # Add links
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s2, s4)
        self.addLink(s2, s5)
        self.addLink(s3, s6)
        self.addLink(s3, s7)

        self.addLink(h1, s4)
        self.addLink(h2, s4)

        self.addLink(h3, s5)
        self.addLink(h4, s5)

        self.addLink(h5, s6)
        self.addLink(h6, s6)

        self.addLink(h7, s7)
        self.addLink(h8, s7)

	
def run():
    c = RemoteController('c', '127.0.0.1', 6633)
    net = Mininet(topo=SimpleOVSSwitch(), switch=OVSKernelSwitch, controller=RemoteController,link=TCLink)
    #net.addController(c)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
