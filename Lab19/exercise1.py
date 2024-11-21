import random

stack_list = [random.randint(1, 10) for i in range(5)]
print(stack_list)
l= len(stack_list)


def push():
         x = int(input("Enter the element to be pushed:"))
         stack_list.append(x)
         return stack_list

def pop():

        if  l == 0:
                print("stack is empty")
                return None
        else:
                return stack_list.pop()



#create queue
def queue():
        queue_list = [random.randint(1, 10) for i in range(5)]
        return queue_list


def enqueue(queue_list, x):

        queue_list.insert(0,x)
        return queue_list

def dequeue(queue_list):

        del queue_list[0]
        return queue_list






def main():
        res = queue()
        print(res)
        x = int(input("Enter the element to be enqueued: "))
        print(enqueue(res, x))
        print(dequeue(res))



        stack_list = [random.randint(1, 10) for i in range(5)]
        print(stack_list)
        res= push()
        print(res)
        res= pop()
        print(res)

if __name__ == "__main__":
    main()