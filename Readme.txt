Vedic Maths is ancient system of mathematics formulated over many centruies by sages of India.

Sanskrit is the language in which all the explanations and functions are defined.

To memorize the functions much easier, it has been written as simple suthras.

These methods are performance efficient and simplify the maths.

These library is being written to showcase the maths to newer generation. 

Every method has information about suthras and what it means and how its devised.

Hope it helps the developers and wider community is welcome to improve on it.

Karthik Srinivasan


Compliment:

print(VedicM.compliment('5670',True))

Output:
Entering the world of Vedic Maths
Sutra is : Nikhilam Navatascarmam Dasatah
Meaning : All from nine and last from ten
4330

If no details on the methods needed:
print(VedicM.compliment('5670',False))

Output:
4330

Subtraction:

print(VedicM.subtract('4826495','3717871',True))

Output:

	Entering the world of Vedic Maths
	Sutra is : Nikhilam Navatascarmam Dasatah
	Meaning : All from nine and last from ten
	There is no carry over in this method
	1. Do normal subtraction when the numerator digit is bigger than lower digit
	2. Go to complements when the lower digit is bigger than upper digit
	3.First time complement has to be from 10 and later on with 9
	4. When the numerator digit is bigger again, come out of complement and subtract extra 1 and later start the new complement from 10 for subsequent digits
	1108624



Multiply 11:
print(VedicM.mul11('795213',True) )  

Output:
	Sutra is : Antyayoreva
	Meaning : Only the last two digits
	Add only the last two digits at a time from base10. We dont need to do any multiplication
	8747343

Multiply 12:
print(VedicM.mul12('26154',True) ) 

Output:   
	Entering the world of Vedic Maths
	Sutra is : Sopaantyadvayamantyam
	Meaning : The ultimate and twice the penultimate
	Add only the last digit with twice the penultimate at a time from base10. We dont need to do any multiplication
	313848

Multiply 9,99,99...infinity:

print(VedicM.mul9('482649534595734983493434989834321342532668578697454351481293048120348','999999999999999999999999999999999999999999999999999999999999999999999','True'))
 
Output:

	Entering the world of Vedic Maths
	Sutra is : Nikhilam Navatascarmam Dasatah
	Meaning : All from nine and last from ten
	Subtract 1 from the multiplicand
	Obtain complement of the multiplicand
	concatenate the values together
	482649534595734983493434989834321342532668578697454351481293048120347517350465404265016506565010165678657467331421302545648518706951879652
