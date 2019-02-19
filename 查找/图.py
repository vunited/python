from collections import deque

def person_is_seller(name):
    #return name[-1] == 'm'

    # 创建一个队列
    # 散列表是无序的

    graph={}
    graph["you"] = ["alice", "bob", 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    search_queue = deque()
    # 将你的邻居都加入到这个搜索队列中
    search_queue += graph[name]
    searched=[]
    #只要队列不空
    while search_queue:
        #就取出其中的第一个人
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person+"is a mango seller")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False

person_is_seller('you')