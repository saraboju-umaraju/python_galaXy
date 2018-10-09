#!/usr/bin/python3
import threading
thobj = threading.Thread(target=print , args=['cat','sat','nat'] , kwargs={'sep':'&'})
thobj.start()
