a = '''Strings in python are surrounded by either single quotation marks, or double quotation marks.'''

#---string Arrey er moto kaj kore so Sring er vitore loop posible

'''multi-line string likar jonno kuno variable e {triple qute(''use kora hoy'')}'''

# string er index number print

print(a[29])

#-------------string er length ber kora------

print(len(a))
#-----------------string e e for loop lagano
# for a in a:
#     print(a)

b = '''Since strings are arrays, we can loop through the characters in a string, with a for loop'''
print(b)
print(len(b))

'''loop'''


# for b in b:
#     print(b)
    
#--------------------------------------
'''-------------STRING ER MODDE {AKKAS}ACE KINA CHECK KORTE HOLE AIVABE LOOP LAGANO JAY---------'''

if "ok" in b:
    print("ace re vai ace") 
else:
    print(" nai re vai")   
#--------------------------------
 
if "ok" not in b:
    print('nai re vai nai')   
#-------------------------------------------------------------------

''' --------------- SLICING KORA SREING ER -------------------''' 

A = b[26:61]
print(A)

''' -------------------- STRING BORO-HATER ---- CHOTO-HATER KORA---------------  '''

# R = b.upper()
# R = b.lower()
R = b.strip()   # strip er sahajje line er suruter space kata hoy--{Remove white space}


print(R)
