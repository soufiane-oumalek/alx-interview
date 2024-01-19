#!/usr/bin/python3
'''The minimum operations'''


def minOperations(n):
  '''method that calculates the fewest number of operations'''

  if not isinstance(n, int) or n <= 0:
      return 0

  operations = 0
  current_length = 1
  clipboard = 0

  while current_length < n:
      if n % current_length == 0:
          clipboard = current_length
          operations += 2
      current_length += clipboard
      operations += 1

  return operations - 1
