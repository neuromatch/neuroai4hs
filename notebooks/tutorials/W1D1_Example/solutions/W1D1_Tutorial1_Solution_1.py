def square(x):
  """Square every element of an array.

  Args:
    x (ndarray): numbers to square

  Returns:
    ndarray: the squares
  """
  return x ** 2


x = np.linspace(-3, 3, 61)
plt.plot(x, square(x))
plt.xlabel("x")
plt.ylabel("x squared")
plt.show()
