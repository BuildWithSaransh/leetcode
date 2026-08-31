class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = x
        digit_sum =0
        while x > 0:
            digit_sum += x % 10
            x //= 10
        if temp % digit_sum == 0:
            return digit_sum
        else:
             return -1
