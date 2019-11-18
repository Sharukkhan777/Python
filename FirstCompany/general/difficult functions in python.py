# difficult functions in python
#------------------------------------------------------------------------------
# enumerate functions
# check whether the memory address are same 
'''
The enumerate() function adds a counter to an iterable.
So for each element in cursor, a tuple is produced with (counter, element); the for loop binds that to row_number and row, respectively.
'''
elements = ('foo', 'bar', 'baz')
for elem in elements:
    print elem

foo
bar
baz
for count, elem in enumerate(elements):
    print count, elem
>>>
0 foo
1 bar
2 baz
'''
By default, enumerate() starts counting at 0 but if you give it a second integer argument, it'll start from that number instead:
'''
for count, elem in enumerate(elements, 42):
    print count, elem
>>>
42 foo
43 bar
44 baz

#------------------------------------------------------------------------------



















