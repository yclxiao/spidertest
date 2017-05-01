# -*- coding: UTF-8 -*-

# import cPickle as p
import pickle as p

shoplist = ['apple', 'mango', 'carrot']

f = file('shoplist.data','w')
p.dump(shoplist,f)
f.close()

f2 = file('shoplist.data')
storedlist = p.load(f2)
print storedlist
