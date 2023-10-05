from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from numpy import array
def mapping1(values_x, a):
    return a * values_x


values_x1 = array([270.3, 256.3, 241.2, 227.5, 212.3, 197.8, 183.0, 169.3, 154.2, 140.2, 0])
values_x2 = array([176.4, 166.5, 156.4, 147.3, 138, 128.5, 119.1, 109.9, 100.5, 90.7, 0])
values_x3 = array([108.9, 103.1, 97.2, 91.4, 85.5, 79.6, 68, 63.3, 56.6, 0])
values_y1 = array([149, 141, 133, 125, 117, 109, 101, 93, 85, 77, 0])
values_y2 = array([149, 141, 133, 125, 117, 109, 101, 93, 85, 77, 0])
values_y3 = array([150, 142, 134, 126, 118, 110, 94, 86, 78, 0])
values_y1*=4
values_y2*=4
values_y3*=4
print(*values_y2[-2::-1],sep=" & ")
args, covar = curve_fit(mapping1, values_x1, values_y1)
a1 = args[0]
y_fit1 = a1 * values_x1
args, covar = curve_fit(mapping1, values_x2, values_y2)
a2 = args[0]
y_fit2 = a2 * values_x2
args, covar = curve_fit(mapping1, values_x3, values_y3)
a3= args[0]
y_fit3 = a3 * values_x3
plt.figure(figsize=(12, 7))
plt.plot(values_x1, values_y1, 'o', alpha=0.7, label="20 см", mew=4)
plt.plot(values_x1, y_fit1,'-.', label="k="+str(round(a1,4)))
plt.plot(values_x2, values_y2, 'v', alpha=0.7, label="30 см", mew=4)
plt.plot(values_x2, y_fit2,'-', label="k="+str(round(a2,4)))
plt.plot(values_x3, values_y3, 'D', alpha=0.7, label="50 см", mew=4)
plt.plot(values_x3, y_fit3,":", label="k="+str(round(a3,4)))
plt.legend()
plt.ylabel("$V_B$, мВ")
plt.xlabel("$I_a$, мА")
plt.xlim(0, 300)
plt.ylim(0, 700)
plt.show()