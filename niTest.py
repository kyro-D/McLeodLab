import nidaqmx.system
from time import sleep


from nidaqmx.constants import (LineGrouping)

system = nidaqmx.system.System.local()
for device in system.devices:
    print device


with nidaqmx.Task() as task:
    task.do_channels.add_do_chan(
        'Dev1/port1/line3',
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

    try:
        task.write(True, auto_start=True)
        
        print 'success'
    except nidaqmx.DaqError as e:
        print 'error ' , e
        
    sleep(5)
    try:
        task.write(False, auto_start=True)
        print 'success'
    except nidaqmx.DaqError as e:
        print 'error', e
    
