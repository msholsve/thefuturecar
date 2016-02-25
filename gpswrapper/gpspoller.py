__author__ = 'Max'


# GPSPpller is a (thread) object that constantly updates a global variable
# (in this case gpsd) with the current GPS data. The core software can now access the current
# location through the global variable 'gpsd'. For example: gpsd.fix.latitude

from gps import *
import os
import threading


gpsd = None  # seting the global variable


class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd  # bring it in scope
        gpsd = gps(mode=WATCH_ENABLE)  # starting the stream of info
        self.current_value = None
        self.running = True  # setting the thread running to true

    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next()  # this will continue to loop and grab EACH set of gpsd info to clear the buffer


# Example on how to use a GpsPoller object:
#
# if __name__ == '__main__':
#     gpsp = GpsPoller()  # create a GpsPoller thread
#     try:
#         gpsp.start()  # start the thread
#         print("Thread starting, please wait...")
#         while True:
#             # it may take a second or two to get good data
#             time.sleep(2)
#
#             os.system('clear')
#
#             print(" GPS reading") # Note, the data bellow is only some of the avalialbe GPS data
#             print("----------------------------------------")
#             print("latitude       " + str(gpsd.fix.latitude)) # Example: (latitude     63.431156667)
#             print("longitude      " + str(gpsd.fix.longitude)) # Example: ('longitude  10.393918333)
#             print("time utc       " + str(gpsd.utc)) # Example: (time utc    2016-02-25T00:40:03.000Z)
#             print("altitude (m)   " + str(gpsd.fix.altitude)) # Example (altitude (m)   47.5)
#             print("speed (m/s)    " + str(gpsd.fix.speed)) # Example (speed (m/s)   0.134)
#             print("mode           " + str(gpsd.fix.mode)) # mode 1 = No satellite fix, mode 2 = 2D fix, mode 3 = 3D fix
#             print
#             print("Satellites (total of " + str(len(gpsd.satellites)) + " in view)") #Prints out satalites in view/used
#             for i in gpsd.satellites:
#                 print("\t" + str(i))
#
#             time.sleep(2)  # set to whatever
#
#     except (KeyboardInterrupt, SystemExit):  # when you press ctrl+c
#         print
#         "\nKilling Thread..."
#         gpsp.running = False
#         gpsp.join()  # wait for the thread to finish what it's doing
#     print
#     "Done.\nExiting."