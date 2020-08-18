'''

#- Shpjegoni me detaje si llogaritet vlera qe printohet, pse ndryshon kur i nderrojme vendet dekoratoreve, dhe si
#eshte rradha e aplikimit te funksioneve qe cojne ne printimin e vleres perfundimtare.

def decorator1(f):
  def inner(x):
    return f(x + 1)
  return inner

def decorator2(f):
  def inner(x):
    return f(x ** 2)
  return inner

@decorator1
@decorator2

# Ne kete rast programi do te printoje 9 sepse ne fillim kryhet funksioni i pare
# me parameter 2 (2+1=3)  dhe pastaj rezultati ngrihet ne katrore (3 ** 2 = 9)


#decorator2
#decorator1

# Ne kete rastin tjeter programi do te printoje 5 sepse ne fillim parametri 2
#ngrihet ne katror (2 ** 2 = 4) dhe rezultati shtohet me 1 (4+1=5)



def f(x): # funksioni qe dekorohet, thjesht kthen argumentin qe merr
  return x

print(f(2))

'''


