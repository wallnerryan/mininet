#Credit to Brandon Heller (brandonh@stanford.edu), his original example was build on for this.
#Author: Ryan Wallner (ryan.wallner1@marist.edu)

#Four fully meshed switches in an "any-to-any" topology plus a host for each switch:

#   host --- switch --- switch --- host
#	                     |     X    |
#   host --- switch --- switch --- host
  
from mininet.topo import Topo, Node

class FoursTopo( Topo ):

    def __init__( self, enable_all = True ):
        # Add default members to class.
        super( FoursTopo, self ).__init__()

        # Set Node IDs for switches
        leftSwitch = 1
        bottomLeftSwitch = 2
        rightSwitch = 3
        bottomRightSwitch = 4
        
        #Set Node IDs for hosts
        leftTopHost = 5
        rightTopHost = 6
        bottomLeftHost = 7
        bottomRightHost = 8
       	
	switch = Node( is_switch=True ) 
	host = Node( is_switch=False )

 	 # Add nodes
  	self.add_node( leftSwitch, switch )
  	self.add_node( rightSwitch, switch )
  	self.add_node( bottomLeftSwitch, switch)
  	self.add_node( bottomRightSwitch, switch)
        
   	self.add_node( leftTopHost, host )
   	self.add_node( rightTopHost, host )
   	self.add_node( bottomLeftHost, host )
   	self.add_node( bottomRightHost, host )

   	# Add edges
   	self.add_edge( leftTopHost, leftSwitch )
   	self.add_edge( rightSwitch, rightTopHost )
   	self.add_edge( bottomLeftHost, bottomLeftSwitch )
   	self.add_edge( bottomRightSwitch, bottomRightHost )
        
   	#Switch Edges to support full mesh
   	self.add_edge( leftSwitch, rightSwitch )
 	self.add_edge( bottomLeftSwitch, bottomRightSwitch )
	self.add_edge( bottomLeftSwitch, rightSwitch )
	self.add_edge( leftSwitch, bottomRightSwitch )
	self.add_edge( rightSwitch, bottomRightSwitch )
	self.add_edge( leftSwitch, bottomLeftSwitch )
	
	#verify mesh	
	switches = []
	switches.append(leftSwitch) 
	switches.append(rightSwitch)
	switches.append(bottomLeftSwitch) 
	switches.append(bottomRightSwitch)
	for switch in switches:
		for connectingSwitch in switches:
			if switch == connectingSwitch:
				print 'Destination to itself'
			else:
				ports = self.port(switch, connectingSwitch)
				print 'Source SW: %s Destination SW: %s have ports (outport, inport) %s' % (str(switch),str(connectingSwitch),ports)
	print "Edge Object {Source dpid: Dest dpid} Tuples"
	print self.ports


        # Consider all switches and hosts 'on'
        self.enable_all()


topos = { '4s4htopo': ( lambda: FoursTopo() ) }
