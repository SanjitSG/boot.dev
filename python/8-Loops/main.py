# integer -> integer
# calculates xp based on current level and previous level xp
# total xp = current xp + (5 * level)

'''
examples:
level current-xp   required
1     0            5 
2     5(5+0)       10 = (5 * level)
3     15(15+10)    15 = (5 * 3)
4     30(15+10+5)  20 = (5 * 4)

next = prevous xp + (5*level)
'''
def calculate_experience_points(level):
  xp = 0
  
  for i in range(1 , level, 1):
    xp += i * 5

  return xp 

