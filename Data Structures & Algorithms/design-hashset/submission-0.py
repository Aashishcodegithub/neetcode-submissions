class ListNode:
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = next


class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.map = [ListNode() for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                return   # already exists
            cur = cur.next

        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.map[self.hash(key)].next

        while cur:
            if cur.key == key:
                return True
            cur = cur.next

        return False
