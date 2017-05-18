from vk import API, Session
from functools import reduce
from json import load, dump

with open('result.json', 'w') as result:
    dump(list((lambda api, groups: set.intersection(*map((lambda g: set(reduce(lambda a, o: a + api.groups.getMembers(group_id=g, offset=o)['users'], range(0, api.groups.getMembers(group_id=g)['count'], 1000), []))), groups)))(API(Session()), load(open('groups.json')))), result)
