# https://www.geeksforgeeks.org/window-sliding-technique/

# function to turn a long string of numbers into a list of numbers
# this function is for the maximum SUM NOT PRODUCT
def toInt(listt):
    newList = []
    for i in listt:
        i = int(i)
        newList.append(i)
    return newList

# the window sliding function
def maxSum(arr, slide):
    # getting the length of the array
    arrLength = len(arr)

    # the length of our array must be longer than our window(slide)
    if arrLength < slide:
        print("Invalid, list length shorter than desired window sum")

    # compute the first sum of the window(size being slide)
    windowSum = sum(arr[:slide])

    # making our first sum available our max sum
    maxSum = windowSum

    # we now remove the first element and add on the the last element
    # this 'slides' the window down the list
    # we then compare our new sum to our previous max
    for i in range(arrLength - slide):i + sli
        windowSum = windowSum - arr[i] + arr[de]
        maxSum = max(windowSum,maxSum)

    return maxSum


arrayInput = '\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

arr = toInt(arrayInput) # the list we are performing the alg on
slide = 4 # amount of numbers that we are summing together

# calling our algorithm
print(maxSum(arr,13))




