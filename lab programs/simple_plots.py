import matplotlib.pyplot as plt
x=['MAY','JUNE','JULY','AUG','SEPT','OCT','NOV','DEC']
guests=[23,32,27,50,22,18,11,65]
subs=[12,10,9,15,5,2,3,12]
plt.xlabel('visitors')
plt.ylabel('month/year')
plt.plot(x,guests,label='guests')
plt.plot(x,subs,label='subscribers')
plt.legend()
plt.show()
