#输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printListFromTailToHead(listNode):
    # write code here
    a = listNode
    aal = []
    while True:
        if a.next != None:
            aal.append(a.val)
            print(aal)
            a = a.next
        else:
            aal.append(a.val)
            print(aal)
            break
    aal.reverse()
    return aal

