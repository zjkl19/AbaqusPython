# -*- coding: utf-8 -*-
"""


@author: ldn
"""

aDict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}  
print('-----------dict-------------')  
for d in aDict:  
    print("%s:%s" %(d, aDict[d]))  
  
print('-----------item-------------')   
for (k,v) in aDict.items():  
    print('%s:%s' %(k, v))  
#效率最高  
print('------------iteritems---------')  
for k,v in aDict.items():  
    print('%s:%s' % (k, v))  
#最笨的方法  
print('---------iterkeys---------------')  
for k in aDict.keys():  
    print('%s:%s' % (k, aDict[k])) 
  
print('------------iterkeys, itervalues----------')  
for k,v in zip(aDict.keys(), aDict.values()):  
    print('%s:%s' % (k, v) )
