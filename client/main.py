import asyncio
import connect
import configloader
import os
import gb
configloader.init()
for root, dirs, files in os.walk('plugins'):
    for i in files:
        if not i=='__init__.py':__import__('plugins.'+i.split('.')[0])
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(gb.var['await']))