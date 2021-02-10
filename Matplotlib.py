import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[5,6,7,8],color="red",label="first")
plt.plot([5,6,7,8],color="blue",label="second")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("First plot")
plt.legend()
plt.show()
