def create_queue():
    queue = []
    return queue

def enqueue(queue:list, item:int):
    queue.append(item)
    print(f'This item {item} has been added on the queue')

def check_empty(queue):
    return len(queue)== 0

def dequeue(queue):
    if check_empty(queue):
        return 'Queue is just empty'
    return queue.pop(0)

queue = create_queue()
enqueue(queue,12)
enqueue(queue,2)
enqueue(queue,21)
enqueue(queue,29)
print(queue)
dequeue(queue)
print(queue)


