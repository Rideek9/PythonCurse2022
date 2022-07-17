class Queue:
    def __init__(self, fifo =[]):
        self.fifo = fifo

    def show(self):
        print('Queue: ', self.fifo)

    def is_empty(self):
        return len(self.fifo) == 0

    def put(self,item):
        self.fifo.append(item)

    def get(self):
        return self.fifo.pop(0)


def main():
    q = Queue([3,4,2,1,9,6])
    q.show()
    print(q.is_empty())
    q.put(99)
    q.show()
    print(q.get())
    q.show()



if __name__ == '__main__':
    main()