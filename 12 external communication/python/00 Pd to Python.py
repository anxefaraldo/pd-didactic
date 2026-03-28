import time

import threading

#!pip install python-osc
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.dispatcher import Dispatcher

class OscReceiver(threading.Thread):

    def __init__(self, ip, receive_from_port, quit_event, address_list=["/clock*"], address_handler_list=[None]):
        """
        Constructor for OscReceiver CLASS

        :param ip:                      ip address that pd uses to send messages to python
        :param receive_from_port:       port  that pd uses to send messages to python
        :param quit_event:              a Threading.Event object, for finishing the receiving process
        :param address_list:            list of osc addresses that need to be assigned a specific handler
        :param address_handler_list:    the handlers for a received osc message
        """

        # we want the OscReceiver to run in a separate concurrent thread
        # hence it is a child instance of the threading.Thread class
        super(OscReceiver, self).__init__()

        # connection parameters
        self.ip = ip
        self.receiving_from_port = receive_from_port

        # dispatcher is used to assign a callback to a received osc message
        self.dispatcher = Dispatcher()

        # assign each handler to it's corresponding message
        for ix, address in enumerate(address_list):
            self.dispatcher.map(address, address_handler_list[ix])

        # you can have a default_handler for messages that don't have dedicated handlers
        self.dispatcher.set_default_handler(self.default_handler)

        # python-osc method for establishing the UDP communication with pd
        self.server = BlockingOSCUDPServer((self.ip, self.receiving_from_port), self.dispatcher)

        # used from outside the class/thread to signal finishing the process
        self.quit_event = quit_event

    def run(self):
        # When you start() an instance of the class, this method starts running
        print("running --- waiting for data")

        # Counter for the number messages are received
        count = 0

        # Keep waiting of osc messages (unless the you've quit the receiver)
        while not self.quit_event.is_set():

            # handle_request() waits until a new message is received
            # Messages are buffered! so if each loop takes a long time, messages will be stacked in the buffer
            # uncomment the sleep(1) line to see the impact of processing time
            self.server.handle_request()
            count = (count+1)                           # Increase counter
            #time.sleep(1)

    def default_handler(self, address, *args):
        # handler for osc messages with no specific defined decoder/handler
        print(f"DEFAULT {address}: {args}")

    def get_ip(self):
        return self.ip

    def get_receiving_from_port(self):
        return self.receiving_from_port

    def get_server(self):
        return self.server

    def change_ip_port(self, ip, port):
        self.ip = ip
        self.receiving_from_port = port
        self.server = BlockingOSCUDPServer(self.ip, self.receiving_from_port)


if __name__ == '__main__':
    # used to quit osc_receiver
    quit_event = threading.Event()

    ##################################################################
    ##################################################################
    ########### OSC MESSAGE HANDLERS #################################
    ##################################################################
    ##################################################################
    #  Values received from sliders or numboxes will be stored/updated
    #       in the dedicated lists: slider_values and num_box_values
    #       if you need more than 10 sliders, increase the length of
    #       the default lists in lines 96-98
    #
    #  The methods slider_message_handler and num_box_message_handler
    #       are in charge of updating the slider_values and num_box_values
    #       lists using the corresponding received osc messages

    # Lists for storing slider and nbox values
    slider_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    num_box_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # define the dedicated handler for a specific message
    def slider_message_handler(address, *args):
        # handler for messages starting with /slider/[slider_id]
        slider_id = address.split("/")[-1]
        slider_values[int(float(slider_id))] = args[0]

    def num_box_message_handler(address, *args):
        # handler for messages starting with /nbox/[nbox_id]
        nbox_id = address.split("/")[-1]
        num_box_values[int(float(nbox_id))] = args[0]

    # Creat an OSCREceiver instance using the above params and handlers
    address_list = ["/slider*", "/nbox*"]
    address_handler_list = [slider_message_handler, num_box_message_handler]

    osc_receiver_from_pd = OscReceiver(ip="127.0.0.1", receive_from_port=1415, quit_event=quit_event,
                                       address_list=address_list, address_handler_list=address_handler_list)

    osc_receiver_from_pd.start()

    ##################################################################
    ##################################################################
    ########### MAIN CODE HERE #######################################
    ##################################################################
    ##################################################################

    while (1):
        time.sleep(1)
        print("sliders: ", slider_values, "nbox: ", num_box_values)

    # Don't change the following lines

    # Wait for 60 seconds then quit the receiver
    time.sleep(1)

    # Note: after setting the quit_event, at least one message should be received for quitting to happen
    quit_event.set()
