#!/usr/bin/env python3

# Это объявление корутины
async def my_coroutine():
    return

# А это сам объект корутины
coro = my_coroutine()
print(type(coro)) #<class 'coroutine'>
print(coro) #<coroutine object my_coroutine at 0x7fd0d7c5e610>