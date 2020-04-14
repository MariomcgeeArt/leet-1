#The problem

#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.


#Restate Problem:
#given an interger as an input determine if it is a palindrome and return true or false 


#Assumptions (all the inputs are intergers)
#clarifying questions(Are the inputs negative or posotive...what about edge cases....are they in a list or an array ?)



#code
# so my solution required me lookingup the slicing method to see how [::-1] meets my needs of an incrimentation to reverse the input and matche the to see if its actually a palindrome becuse prior to this i did not know how to do this...so feeling better about this but still need to brush up on classes again 

def isPalindrome(x: int):
    x = str(x)
    reverse = x[::-1]

    if x == reverse:
        print('Yes {} is a Palindrome!'.format(x))
        return True
    else:
        print("False {} is not a Palindrome!".format(x))
    return 
    """
    :type x: int
    :rtype: bool
    """

    

isPalindrome(404)
isPalindrome(404)
isPalindrome(400)
isPalindrome(-404)
isPalindrome(404404)

