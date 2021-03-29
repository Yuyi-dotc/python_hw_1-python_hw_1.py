from typing import Iterator, List, TypeVar

T = TypeVar("T")


def get_hello_world() -> str:
    """Task 1

    Returns:
        "Hello, world!" string
    """
    return "Hello, world!"

def check_ticket(ls0):
	ls1, ls2 = ls0[:3], ls0[3:]
	s1, s2 = sum(ls1), sum(ls2)
	return s1 == s2


def get_nearest_happy_ticket(current_ticket: str) -> str:
    result, first, second_1, second_2, buffer = "", "", "", "", ""
    ls_0, check_1, check_2 = list(map(int, current_ticket)), [], []
    if check_ticket(ls_0):
        return current_ticket
    ls_1, ls_2 = ls_0[:3], ls_0[3:]
    flag_1, flag_2 = False, False
    count_1, count_2 = 0, 0
    for i in ls_2:
        second_1 += str(i)
        second_2 += str(i)
    for j in ls_1:
        first += str(j)
    buffer = first + second_1
    result = first + second_2

    check_1 = list(map(int, buffer))
    while check_ticket(check_1) is not True:
        count_1 += 1
        buffer = ""
        second_1 = int(second_1)
        second_1 -= 1

        if second_1 < 0:
            flag_1 = True
            break

        second_1 = str(second_1)
        while len(second_1) < 3:
            second_1 = "0" + second_1

        buffer = first + second_1
        check_1 = list(map(int, buffer))

    check_2 = list(map(int, result))
    while check_ticket(check_2) is not True:
        count_2 += 1
        result = ""
        second_2 = int(second_2)
        second_2 += 1

        if second_2 > 999 and flag_2 is not True:
            second_2 = str(second_2)
            second_2 = 0 * 3
            first = int(first)
            first += 1
            first = str(first)
            flag_2 = True

        second_2 = str(second_2)
        while len(second_2) < 3:
            second_2 = "0" + second_2

        result = first + second_2
        check_2 = list(map(int, result))

    if flag_1 is False:
        if count_1 < count_2:
            return buffer
        else:
            return result
    return result

   


def get_fizz_buzz(n: int):
    buffer0, final_list = [], [] 
    for i in range(1, n+ 1):
	a = str(i)
	f, b = 'Fizz", "Buzz"
        if i % 3 != 0:
            f = ""
        else:
            a = ""

        if i % 5 != 0:
            b = ""
        else:
            a = ""

        buffer0.append(a + f + b)

    for i in buffer0:
        if i.isdigit():
            i = int(i)
        final_list.append(i)

    return final_list
	
            




   


def get_value(value: int, repeats: int) -> int:
    """Task 4

    Args:
        value: value to repeat
        repeats: number of repeats

    Returns:
        square of repeated value
    """
    return int(str(value)*repeats)**2

def longest_common_prefix(my_str) -> str:
    curb, minstr = [], strs[0]
    minlen, maxpre = len(strs[0])
    flag = TRUE
    for i in strs[1:]:
	if len(i) < minlen:
	    minlen = len(i)
	    minstr = i
    if len(strs) != 1:
	strs.remove(minstr)
	curb.extend(strs)
    else:
	curb.extend(strs)
    
    for i in range(len(minstr)):
	for j in curb :
	    if j[i] != minstr[i]:
		flag = FALSE
	if flag :
		maxpre += j[i]
	else:
		break
    return maxpre








def password_strength(password: str) -> str:
    islow, ishigh, isnum = FALSE, FALSE, FALSE
    islen, isunique, isanna = FALSE, FALSE, FALSE
    annaset = ("Anna", "AnnA", "AnNa", "AnNA",
                "ANna", "ANnA", "ANNa", "ANNA",
                "anna", "annA", "anNa", "anNA",
                "aNna", "aNnA", "aNNa", "aNNA")
    annaset = set(annaset)
    passwordset = set(password)
    if len(passwordset) < 4:
        isunique = TRUE

    for i in password:
        if i.islower():
            islow = TRUE
        if i.isupper():
            ishigh = TRUE
        if i.isdigit():
            isnum = TRUE
    if len(password) >= 8:
        islen = TRUE

    for i in annaset:
        if i in password:
            isanna = TRUE

    if islow and ishigh and isnum and islen and not isanna and not isunique:
        return("strong")
    else:
        return("weak")


def is_perfect(num: int) -> bool:
    if num == 1 :
	return False
    sum_div = 0
    for i in range(num -1, 1, -1):
	if num % i ==0 :
		sum_div += i
    return num == sum_div + 1


def ispalindrome(line):
    return line == line[::-1]

    



def addition_upto_palindrome(line: str) -> int:
    if ispalindrome (line):
	return 0
    
	c1, c2, i = 0, 0, 0
    rline = line[::-1]
    pline = rline[:-1]
    rpline = rline[1:]
    while TRUE:
        line += rpline[i]
	c1 += 1
	i += 1
	if i == len(rpline):
	    i = 0
	if c1 > 1000:
	    break
	if ispalindrome(line):
	    break
    
    i = 0
    while TRUE :
	rline += pline[i]
	c2 += 1
	i += 1
	if i == len(pline):
	    i = 0
	if c2 > 1000:
	    break
	if ispalindrome(rline):
		break
    return min(c1, c2)	

    




def caesar_encrypt(message: str, n: int) -> str:
    text = []
    for ch in message:
	if ch >= 'a' and ch <= 'z':
	    text.append(chr((ord(ch) - ord("a") + n + 26) % 26 + ord("a")))
	elif ch >= 'A' and ch <= 'Z':
	    text.append(chr((ord(ch) - ord("A") + n + 26) % 26 + ord("A")))
	else:
	    text.append(ch)
    return ''.join(text)
	
	    

    


def parse_color(color: str) -> [int]:
    """Task 10

    Args:
        color: color string to parse

    Returns:
        parsed color – RGB values list

    """


# BONUS TASKS GO BRR


def transpose(matrix: List[list]) -> List[list]:
    """Bonus task
    Args:
        matrix: rectangular matrix

    Return:
        transposed matrix
    """

def uniq(sequence: List[T]) -> Iterator[T]:
    """Bonus task
    Args:
        sequence: arbitrary sequence of comparable elements

    Return:
        generator of elements of `sequence` in the same order without duplicates
    """


def dict_merge(*dicts: dict) -> dict:
    """Bonus task
    Args:
        dicts: flat dictionaries to be merged

    Returns:
        merged dictionary
    """


def product(lhs: List[int], rhs: List[int]) -> int:
    """Bonus task
    Args:
        rhs: first factor
        lhs: second factor

    Returns:
        scalar product
    """
