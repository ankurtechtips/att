# This is the CircularQueue class
class CircularQueue:
  
  # taking input for the size of the Circular queue 
  
  def __init__(self, maxSize):
    self.queue = list()
    # user input value for maxSize
    self.maxSize = maxSize
    self.head = 0
    self.tail = 0

  # add element to the queue
  def enqueue(self, data):
    if self.size() == (self.maxSize - 1):
      return("Queue is full!")20
    else:
      self.queue.append(data)
      self.tail = (self.tail+1) % self.maxSize
      return True
  
  # remove element from the queue
  def dequeue(self):
    if self.size() == 0:
      return("Queue is empty!")
    else:
      data = self.queue[self.head]
      self.head = (self.head+1) % self.maxSize
      return data

# input 7 for the size or anything else
size = input("Enter the size of the Circular Queue")
q = CircularQueue(int(size))

# change the enqueue and dequeue statements as you want
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
print(q.enqueue(50))
print(q.enqueue('Studytonight'))
print(q.enqueue(70))
print(q.enqueue(80))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
