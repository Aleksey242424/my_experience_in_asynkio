import asyncio

def get_docs():
    docs = '''
async это маркер для питона что функция возвращает не обычные значения, а корутину
    
await нужен для передачи управления обратно в event loop, когда корутина встречает операцию требующую ожидания.
Технический это выглядит так,"Я сейчас буду ждать результат этой операции - пока я жду можешь выполнять другие операции"
    '''
    return docs


#синхронная функция, вернёт 777
def sync_func():
    return 777


#асинхронная функция, вернёт объект корутины (<coroutine object async_func at 0x7f823f8b2610>)
async def async_func():
    ...

async def main():
    print(get_docs())
    print(sync_func())
    print(async_func())

    
asyncio.run(main())


