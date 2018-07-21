"""
1.1
Is Unique
Implement an algorithm, to determine if a sing has all unique characters. What if you can't use additional data suctures?
"""



"""
Solution 1: O(n), assuming alphabet of size n.
"""

def isUnique(s):
  dct = {}
  for l in s:
    if l in dct:
      return False
    else:
      dct[l] = 1
  return True

# print(isUnique('theLazyDog'))
# print(isUnique('hello world'))


"""
Solution 2: Assuming sorting is in place, O(nlogn) assuming alphabet of size n and Python's sorting is efficient
"""

def isUniqueSorted(s):
  s = ''.join(sorted(s))
  for i in range(0, len(s)-1):
    if s[i] == s[i+1]:
      return False
  return True


# print(isUniqueSorted('theLazyDog'))
# print(isUniqueSorted('hello world'))


"""
Solution 3: Assuming sorting is not in place.
O(n^2) assuming alphabet of size n
"""


def isUniqueInPlace(s):
  for i in range (0, len(s)):
    for j in range (0, len(s)):
      if s[i] == s[j] and i != j:
        return False
  return True

# print(isUniqueInPlace('theLazyDog'))
# print(isUniqueInPlace('hello world'))


"""
1.2
Check Permutations:
Given two sings, write a method to decide if one is a permutation of another
"""



"""
Solution 1: O(nlogn)
"""

def isPermutation(sA,sB):
  if len(sA) != len(sB):
    return False
  sA = ''.join(sorted(sA))
  sB = ''.join(sorted(sB))
  for i in range (0, len(sA)):
    if sA[i] != sB[i]:
      return False
  return True

# print(isPermutation('hello', 'elloh'))
# print(isPermutation('hello', 'ellxh'))


"""
Solution 2: My O(n) solution using dictionaries
"""

class FreqPair:
  def __init__(self,a = 0, b = 0):
    self.a = a
    self.b = b

  def isEqual(self):
    if self.a == self.b:
      return True
    return False


def isPerm(strA, strB):
  if len(strA) != len(strB):
    return False
  dct = {}
  for l in strA:
    if l not in dct:
      dct[l] = FreqPair()
    dct[l].a += 1
  for l in strB:
    if l not in dct:
      dct[l] = FreqPair()
    dct[l].b += 1
  for key, val in dct.items():
    if not val.isEqual():
      return False
  return True


# print(isPerm('hello', 'elloh'))
# print(isPerm('hello', 'ellxh'))


"""
Solution 3: Another O(n) solution
"""

def isPermuted(strA, strB):
  if len(strA) != len(strB):
    return False
  d = {}
  for l in strA:
    if l in d:
      d[l] += 1
    else:
      d[l] = 1
  for l in strB:
    if l in d:
      if d[l] == 0:
        return False
      d[l] -= 1
    else:
      return False
  # The below code is not technically necessary, but it may not be immediately obvious!
  # for key, val in d.items():
  #   if val > 0:
  #     return False
  return True



# print(isPermuted('hello', 'elloh'))
# print(isPermuted('hello', 'ellxh'))



"""
1.3
URLify:
'Mr John Smith' => 'Mr%20John%20Smith'
"""

def URLify(s):
  return '%20'.join(s.split(' '))

# print(URLify('hello  world'))



def URLifyAgain(s):
  resList = []
  for l in s:
    if l == ' ':
      resList.append('%20')
    else:
      resList.append(l)
  return ''.join(resList)

# print(URLifyAgain('hello  world'))



"""
1.4 Is Permutation of Palindrome
Tact Coa is a permutation of Taco Cat which is a palindrome.
Spaces don't matter
"""

def isPalindromePerm(s):
  s = ''.join(s.split(' ')).lower()
  d= {}

  for l in s:
    if l not in d:
      d[l] = 0
    d[l] += 1

  nOdd = 0

  for key, val in d.items():
    if val%2:
      nOdd += 1
      if nOdd > 1:
        return False
  if len(s) % 2 == 0 and nOdd == 0:
    return True
  if len(s) % 2 == 1 and nOdd == 1:
    return True
  return False


# print(isPalindromePerm('taco cat'))
# print(isPalindromePerm('Aaco CTT'))
# print(isPalindromePerm('Aaco CaT'))
# print(isPalindromePerm('AABBBC'))
# print(isPalindromePerm('AA BBBBB CCDD'))


"""
1.5 One Away
A string is one away if either one character is different, or if one of the strings is missing a character.
"""

def isOneAway(strA,strB):
  a = len(strA)
  b = len(strB)

  if abs(a-b) > 1:
    return False


  # If the string are the same length check collision count.

  if a == b:
    collisions = 0
    for i in range(0,a):
      if strA[i] != strB[i]:
        collisions += 1
        if collisions > 1:
          return False
    return True

  # if the strings are

  else:
    if a < b:
      s = strA
      l = strB
    else:
      s = strB
      l = strA

    for i in range(0,len(s)):
      if s[i] != l[i]:
        for j in range (0, len(s)-i):
          if s[i+j] != l[i+j+1]:
            return False
    return True


# print(isOneAway('hello','hezzo'))
# print(isOneAway('hello','hell'))
# print(isOneAway('z',''))



"""
1.6 Compress Strings
aaabbbccd -> a3b3c2d1
ab -> ab because it's shorter than a1b1
"""


def compressString(s):
  counter = 0
  activeLetter = ''
  compressed =''

  for i in range(0, len(s)):
    if s[i] != activeLetter:
      activeLetter = s[i]
      counter = 1
      compressed += activeLetter
    else:
      counter += 1
    if i == len(s) - 1 or s[i] != s[i+1]:
      compressed += str(counter)
      if len(compressed) >= len(s):
        return s
  return compressed

# print(compressString('The quick                                                                                  brown fox jumps over the lazy dog'))
# print(compressString('The quick brown fox jumps over the lazy dog'))
# print(compressString('abcdeee'))
# print(compressString('abcdeeeeeeee'))
# print(compressString('abcdeeeeeeee'))



"""
1.6 Given a matrix, turn it 90deg
"""

class Matrix:
  def __init__(self, m, n):
    self.rows = m
    self.cols = n
    self.data = [[0]*n]*m

def rotateMatrix(M):
  K = Matrix(M.cols, M.rows)
  for i in range(0, M.cols):
    for j in range (0, M.rows):
      K.data[i][j] = M.data[j][M.rows - i - 1]
  return K

M = Matrix(3,5)
K = rotateMatrix(M)
print(K.data)
