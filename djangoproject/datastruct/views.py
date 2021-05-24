from django.shortcuts import render
class Stack:
    def __init__(self,lst = None):
        self.lst = lst if lst is not None else []
    def push(self,item):
        self.lst.append(item)
    def pop(self):
        self.lst.pop()
    def peek(self):
        return self.lst[-1]
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return len(self.lst) == 0
    def lststack(self):
        return self.lst
    def find(self,num):
        return self.lst[num]

class Queue:
    def __init__(self,lst = None):
        self.lst = lst if lst is not None else []
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return len(self.lst) == 0
    def top(self):
        return self.lst[0]
    def enQ(self,obj):
        self.lst.append(obj)
    def deQ(self):
        return self.lst.pop(0)
    def show(self):
        return self.lst

class sorting:
    def sortDate(self, num):
        a = []
        for i in num:
            a.append(i.split('_')[0])
        for i in range(len(a)-1, -1, -1):
            for b in range(i):
                if int(a[b].split("/")[0]) > int(a[b+1].split("/")[0]):
                    a[b], a[b+1] = a[b+1], a[b]
                    num[b], num[b+1] = num[b+1], num[b]
        for i in range(len(a)-1, -1, -1):
            for b in range(i):
                if int(a[b].split("/")[1]) > int(a[b+1].split("/")[1]):
                    a[b], a[b+1] = a[b+1], a[b]
                    num[b], num[b+1] = num[b+1], num[b]
        for i in range(len(a)-1, -1, -1):
            for b in range(i):
                if int(a[b].split("/")[2]) > int(a[b+1].split("/")[2]):
                    a[b], a[b+1] = a[b+1], a[b]
                    num[b], num[b+1] = num[b+1], num[b]
        return num