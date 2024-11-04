# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
def add_one(num):
  if (num >= 9):
    return num + 1

  total = num + 1
  print(total)

  return add_one(total)

mynewtotal = add_one(0)
print(mynewtotal)


# %%
