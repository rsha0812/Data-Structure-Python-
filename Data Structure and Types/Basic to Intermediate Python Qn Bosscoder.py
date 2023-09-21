'''
Qn 1: Write a program that converts given number of days into years, weeks, and days.
'''
#Code: 
def days_to_years_weeks_days(days):
    # Calculate the number of years
    years = days // 365
    # Calculate the remaining days
    remaining_days = days % 365
    # Calculate the number of weeks
    weeks = remaining_days // 7
    # Calculate the remaining days
    remaining_days = remaining_days % 7
    
    return years, weeks, remaining_days

# Input the number of days
days_input = int(input("Enter the number of days: "))

# Call the function to convert days to years, weeks, and days
years, weeks, remaining_days = days_to_years_weeks_days(days_input)

# Display the result
print(f"{days_input} days is equal to {years} years, {weeks} weeks, and {remaining_days} days.")


'''
Qn2 : Create a program that takes sentence as input and count number of words in it.
'''
# Code: 
def count_words(sent): 
    cnt = 0
    lst = sent.split(" ")
    print(lst)
    for i in lst: 
        cnt += 1
    return cnt
    
print(count_words("I am a Girl"))


########################## Variables and Data Types#########################

'''
Q1: Reversing the string and palindrome. 
'''
# Code: 
def rev_string(s):
    s = s.replace(" ","").lower()
    return s[::-1]
    
print(rev_string("Help"))

def is_palindrome(s): 
    s = s.replace(" ","").lower()
    return s == s[::-1]

print(is_palindrome("mom"))

'''
Q2 : Given list of names, concate them into single string seperated by spaces.
'''
# Code: 
lst = ['pooja','dum','neem','rukh']
strng = (" ").join(lst)
print(strng)


'''
Q3 : write a program to check if given string is a pangram or not.(Contains all letter of alphabet)
'''
# Code: 
def is_pangram(sentence):
    # Create a set to store the unique letters in the sentence
    unique_letters = set()

    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is an alphabet letter (a to z or A to Z)
        if 'a' <= char <= 'z':
            unique_letters.add(char)
        elif 'A' <= char <= 'Z':
            # Convert uppercase letters to lowercase and add to the set
            unique_letters.add(char.lower())

    # Check if the set of unique letters contains all 26 letters of the alphabet
    return len(unique_letters) == 26

# Input the sentence to check
sentence = input("Enter a sentence: ")

# Call the function to check if it's a pangram
if is_pangram(sentence):
    print("The given sentence is a pangram.")
else:
    print("The given sentence is not a pangram.")


'''
Q4 : write a program to convert given number of minutes into hours and minutes. 
'''
# Code: 

def hour_minute(num): 
    
    hour = num // 60 
    remain_min = num % 60
    
    return hour , remain_min
    
# Input the number of minutes
minutes_input = int(input("Enter the number of minutes: "))

# Call the function to convert minutes to hours and minutes
hours, remain_min = hour_minute(minutes_input)

# Display the result
print(f"{minutes_input} minutes is equal to {hours} hours and {remain_min}")

'''
Q5 : Create a function to count number of vowels in given string.    
'''
# Code: 

def count_vowel(s): 
    cnt = 0
    vowels = set("aeiou")
    for i in s:
        if i in vowels:
            cnt += 1
    return cnt 
    
print(count_vowel("neem"))


##########################Control Flows and Loops and Functions########################

'''
Q1: Check leap year or not?  
'''
# Code: 

def is_leapyear(year): 
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Given year {year} is leap year")
    else: 
        print(f"Given year {year} is not leap year")
              
is_leapyear(2022)
is_leapyear(2012)


'''
Q2 : Write a program to generate fibonnaci series upto given number of terms
'''
# Code: 
# 1,1,2,3,5
def fibonnaci_series(n): 
    fib_series = [1,1]
    
    while len(fib_series) < 5: 
        new_elem = fib_series[-1] + fib_series[-2]
        fib_series.append(new_elem)
    return fib_series
        
print(fibonnaci_series(5))


'''
Q4 : Given a list of names, print all names starting with the
letter 'A'.
'''
# Code: 
def name_list(lst): 
    for i in lst: 
        if i.startswith("A"): 
            print(i)
            
name_list(["Anjali","Arman","Pooja"])


'''
Q5: Implement a program that prints the multiplication table
of a given number
'''
# Code: 
def multiplication(n): 
    
    for i in range(1,11): 
        ans = n * i
        print(n, "*" , i , "=" , ans , end = "\n")
        
multiplication(5)

'''
Q6 : Write a program that calculates the factorial of a given
number.
'''
 # Code: 
 
def factorial(n): 
    if n == 1: 
        return n 
    else: 
        return n  * factorial(n-1)
    
print(factorial(5))


'''
Q7 : Create a loop that prints all prime numbers between 1 and
50.
'''

# Code: 
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

# Loop through numbers from 1 to 50 and print prime numbers
print("Prime numbers between 1 and 50:")
for number in range(1, 51):
    if is_prime(number):
        print(number)


'''
Q8:  Calculate the sum of digits of a given number.
'''
## Code: 
def digit_sum(x): 
    digit = str(x)
    total_sum = 0
    for i in digit: 
        total_sum += int(i)
    return total_sum
    
print(digit_sum(7234))

'''
Q9:  Create a function that takes a list of strings and returns
the list sorted alphabetically.
'''
## Code: 
def sort_list(lst): 
    sorted_list = sorted(lst)
    return sorted_list
print(sort_list(["I","am","girl","or","boy"]))

'''
Q10:  Write a function that takes two lists and returns their
intersection (common elements).
'''
## Code: 
def common_element(lst1,lst2): 
    com_ele_lst = []
    
    for i in lst1: 
        for j in lst2: 
            if i==j:
                com_ele_lst.append(i)
    return com_ele_lst
    
    
print(common_element([1,2,3,4,5,6],[4,5,6,7,8,9]))

########################## String Manipulation ########################
'''
Q1: Write a program that takes a sentence as input and
counts the number of words in it.
'''
## Code: 
def number_of_words(sent): 
    lst = sent.split(" ")
    word_cnt = len(lst)
    return word_cnt
print(number_of_words("I am a girl or a boy"))


'''
Q2:  Given a string, write a function to remove all vowels from
it and return the modified string.
'''
## Code: 
def remove_vowel(strng): 
    vowel = set("aeiou")
    for char in strng: 
        if char in vowel: 
            strng = strng.replace(char,"")
    return strng
    
print(remove_vowel("datedertyuio"))


'''
Q3:  Write a Python program to find the length of the longest
word in a sentence.
'''
## Code: 
def longest_word(sent): 
    lst = sent.split()
    max_len_word = 0
    cnt = 0 
    for char in lst: 
        cnt = len(char)
        if cnt > max_len_word: 
            max_len_word = cnt 
            
    return max_len_word

print(longest_word("I am a girl or a boy"))

'''
Q4: Write a function to remove all duplicate characters from a
given string.
'''
## Code: 
def remove_duplicate(strng): 
    unique_strng = set()
    result_string = ""
    for char in strng: 
        if char not in unique_strng:
            unique_strng.add(char)
            result_string += char
    
    return result_string

print(remove_duplicate("madamestdt"))

########################## Lists and Tuples ########################

'''
Q1: Given two lists of numbers, concatenate them into a
single list.
'''
## Code: 
def concat_lists(list1,list2): 
    final_list = list(set(list1+list2))  ## To remove Duplicate/Common element.
    return final_list
    
print(concat_lists([1,2,3,4],[1,5,4,6]))

'''
Q2: Given a list of words, find the word with the maximum
length and its length.
'''
## Code: 

def max_len_word(lst): 
    max_len  = 0
    max_len_wrd = ""
    for wrd in lst: 
        length = len(wrd)
        if length > max_len: 
            max_len = length 
            max_len_wrd = wrd 
    return max_len,max_len_wrd

print(max_len_word(["I","am","girl","or","boy"])) 


'''
Q3: Write a Python program to count the occurrences of each
element in a given list.
'''
## Code: 

def element_occurence(lst): 
    new_list = {}
    
    for wrd in range(0,len(lst)):
        if lst[wrd] in new_list: 
            new_list[lst[wrd]] += 1
        else: 
            new_list[lst[wrd]] = 1
            
    return new_list

print(element_occurence(["a","deer","run","a","run","boy","a"]))


'''
Q4: Create a function that takes a list of strings and returns
the list sorted by the length of the strings.
'''
## Code: 
def sorted_list(lst): 
    final_lst = sorted(lst, key = lambda x: len(x))
    return final_lst
    
print(sorted_list(["a","boy","or","girl","run"]))


'''
Q5: Write a program that checks if a given list is sorted in
ascending order
'''
## Code: 
def is_lst_sorted(lst): 
    sorted_lst = sorted(lst)
    print(sorted_lst)
    if lst == sorted_lst: 
        return True 
    else: 
        return False 
        
print(is_lst_sorted(['a', 'boy', 'girl', 'or', 'run']))


########################## Dictionary and Sets ########################

'''
Q1: Given two dictionaries, merge them into a single
dictionary.
'''
#Code: 
def merge_dict(dict1,dict2): 
    final_dict = {**dict1, **dict2}
    return final_dict

print(merge_dict({1:"a",2:"b"},{3:"c"}))

# Code2: 
dict1 = {1:"a",2:"b"}
dict2 = {3:"c"}
dict1.update(dict2)
print(dict1)

'''
Q2: Write a program that finds the most frequent element in a
list.
'''
#Code: 
def freq_elem(lst): 
    new_list = dict()
    most_freq_elem = []
    for ele in range(0,len(lst)): 
        if lst[ele] in new_list: 
            new_list[lst[ele]] += 1
        else: 
            new_list[lst[ele]] = 1
            

    most_freq_elem = max(new_list , key = lambda x: new_list[x])
    
    return most_freq_elem
    
print(freq_elem([1,2,3,8,8,4,5,7,8,8,8,1,5,6]))


'''
Q3:Implement a function that removes a key-value pair from
a dictionary.
'''
#Code: 
def remove_key_value(dict1): 
    dict1.pop(3)
    return dict1
    
print(remove_key_value({1:"a",2:"b",3:"c"})) #O/P : {1:"a",2:"b"}


'''
Q4:Create a program that checks if two sets have any
elements in common.
'''
#Code: 
def check_common_elem(set_a,set_b):
    common_elements = set_a.intersection(set_b)
    return common_elements
    
print(check_common_elem({1,2,3},{1,2})) 


'''
Q5: Given a list of dictionaries, find the dictionary with the
highest value for a specific key.

Analysis : 
The key function, lambda x: x.get(key, float('-inf')), retrieves the value associated with the specified key for each dictionary. 
If the key is not present in a dictionary, it returns negative infinity (float('-inf')) to ensure that such dictionaries are not chosen as the maximum.
'''
#Code: 
def highest_value_dict(dict_lst,key): 
    if not dict_lst:
        return None
        
    max_dict = max(dict_lst, key=lambda x: x.get(key, float('-inf')))
    
    return max_dict
        
dict_list = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 28}
]

key = "age"
print(highest_value_dict(dict_list,key))


'''
Q6: Given two sets, find the union, intersection, and
difference between them.
'''
#Code: 
set_1 = {1,2,3}
set_2 = {1,2}

## Union : 
union_set = set_1.union(set_2)
print(f"Union of Set1 and Set2 is : {union_set}") ## {1,2,3}

## Intersection: 
intersection_set = set_1.intersection(set_2)
print(f"Intersection of Set1 and Set2 is : {intersection_set}") ## {1,2}

## Difference: 
diff_set = set_1.difference(set_2)
print(f"Difference of Set1 and Set2 is : {diff_set}")  ## {3}


'''
Q7: Create a function that takes a list of dictionaries and sorts
them based on a specified key.  
'''
#Code: 
def sort_dict_lst(dict_lst,key): 
    
    sort_dict = sorted(dict_lst, key = lambda x: x.get(key))
    return sort_dict


dict_list = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 28}
]

key = "age"

print(sort_dict_lst(dict_list,key))


'''
Q8: Write a program that finds the average value of all the
elements in a list of dictionaries 
'''
#Code: 
def average_dict_lst(dict_lst,key): 
    total = 0 
    count = 0 
    
    for dic in dict_list: 
        if key in dic: 
            total += dic[key]
            count += 1
            
    if count ==0 : 
        return None
    else: 
        return total/count 

dict_list = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 28}
]
    
key = "age"

print(average_dict_lst(dict_list,key))


'''
Q9:  Implement a function that takes a list of strings and
returns a set of unique characters present in all strings
'''
#Code: 
def find_common_characters(string_list):
    # Convert the first string to a set of characters
    common_characters = set(string_list[0])
    print(common_characters)
 # Iterate through the remaining strings and find the intersection of characters
    for string in string_list[1:]:
        common_characters &= set(string)
        print(common_characters)
        
    return common_characters

# Example list of strings
input_list = ["apple", "banana", "charry", "date"]

# Call the function to find common characters
common_chars = find_common_characters(input_list)

# Display the result
print("Common characters in all strings:")
print(common_chars) ## {"a"}