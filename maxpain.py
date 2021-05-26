import re
import os
import logging
#import numpy
import numpy as np
import csv,sys
import matplotlib.pyplot as plt

class intri:
	def __init__(self, spr, s, inv, oint, cas):
		self.sp = spr
		self.str = s
		self.iv = inv
		self.oi = oint
		self.cash = cas

class s:
	def __init__(self, s, ci, pi):
		self.st = s
		self.callint = ci
		self.putint = pi
		
class cs:
	def __init__(self, s, cc, pc):
		self.st = s
		self.ccash = cc
		self.pcash = pc
		
class u:
	def __init__(self, u, st, cvi, pvi, ci, pi, ccas, pcas):
		self.ur = u
		self.str = st
		self.civ = cvi
		self.piv = pvi
		self.coi = ci
		self.poi = pi
		self.ccash = ccas
		self.pcash = pcas

fp = 0.0029
rel_tol = 1e-05
abs_tol = 1e-08

fig = plt.figure()


FORMAT = "%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename="./optstoch.log")
logger = logging.getLogger(__name__)

try:
	path='./CME/'+sys.argv[1]+'/2021/'

	csv_reader1 = csv.reader(open(path+sys.argv[1]+"_JS_"+sys.argv[2]+"_settle_" + sys.argv[3] + ".csv"), delimiter=' ')
	ci = []
	for l in csv_reader1:
		if l[0]!="Total":
			ci.append(s(l[0],l[2],l[4]))

	cas = []
	st = []
	cc = []
	pc = []
	for index1 in range(0,len(ci)):
		c = []
		for index2 in range(0,len(ci)):
			ur = ci[index1].st
			piv = float(ci[index2].st) - float(ci[index1].st)
			civ = float(ci[index1].st) - float(ci[index2].st)
			if (piv < 0):
				piv = 0
			if (civ < 0):
				civ = 0
			
			pcash = piv * float(ci[index2].putint)
			ccash = civ * float(ci[index2].callint)
			c.append(u(ur,ci[index2].st,civ,piv,ci[index2].callint,ci[index2].putint,ccash,pcash))
		ccash = 0
		pcash = 0
		for i in range(0,len(c)):
			#print c[i].cash
			ccash += c[i].ccash
			pcash += c[i].pcash
		cas.append(cs(ci[index1].st,ccash,pcash))
		st.append(int(ci[index1].st))
		cc.append(float(ccash))
		pc.append(float(pcash))
	ax1 = fig.add_subplot(111)
	ax1.bar(st, cc, color='r', label='c')
	ax1.bar(st, pc, color='b', label='p')
	leg = ax1.legend()
	plt.xticks(np.arange(min(st), max(st)+1, 25.0))
	plt.xticks(rotation=45)
	plt.show()

except OSError as e:
    print "oserror"+str(e)
except NameError as e:
    print "nameerror"+str(e)
except TypeError as e:
    print "typeerror"+str(e)
except SyntaxError as e:
    print "syntaxerror"+str(e)
except NotImplementedError as e:
    print "nierror"+str(e)
except IOError as e:
    print "ioerror"+str(e)
except AssertionError as e:
    print "assertionerror"+str(e)
except ArithmeticError as e:
    print "arytherror"+str(e)
except AttributeError as e:
    print "attributeerror"+str(e)
except EOFError as e:
    print "eoferror"+str(e)
except EnvironmentError as e:
    print "enverror"+str(e)
except FloatingPointError as e:
    print "flpointerror"+str(e)
except KeyError as e:
    print "keyerror"+str(e)
except ValueError as e:
    print "valueerror"+str(e)
except:
    print "error"
