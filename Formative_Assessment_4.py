#!/usr/bin/env python
# coding: utf-8

# # Programming Set 4
# 
# ## This assignment will test your proficiency in pattern recognition and programming in Python.

# # Bin to Dec (4/4)

# In[146]:


def bin_to_dec(binary_string):
    binary_string = str(binary_string)
    result = 0
    process = binary_string[::-1]
    
    for i in range(len(process)):
        new = int(process[i])*(2**i)
        result += new
    return result


# # Dec to Bin (4/4)

# In[113]:


def dec_to_bin(number):
    number = int(number)
    result = ""
    if number == 0:
        return "0"
    while number != 0:
        remainder = number % 2
        result = str(remainder) + result
        number = number // 2
    return result


# # Telephone Cipher (4/4)

# In[154]:


def telephone_cipher(message):
    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }
    
    message = str(message.upper())
    length = len(message)
    result = ""
    for i in range(length):
        new = str(encoder_dict.get(message[i]))
        if i > 0:
            if result[len(result)-1] == new[0]:
                result += ("_"+ new)
                continue
            else:
                result += new
                continue
        else:
            result += new
            continue
    return result


# # Telephone Decipher (4/4)

# In[ ]:


def telephone_decipher(telephone_string):
    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }

    telephone_string = str(telephone_string)
    result = ""
    length = len(telephone_string)
    skips = 0
    password = True
    for i in range(length):
        if skips > 0:
            skips -= 1
            continue
        
        candidate = telephone_string[i]

        if candidate == "_":
            continue
        if i < length-1:
            if telephone_string[i+1] == telephone_string[i]:
                candidate += telephone_string[i+1]
                skips += 1
            else:
                password = False
                
        if i < length-2 and password:
            if telephone_string[i+2] == telephone_string[i]:
                candidate += telephone_string[i+2]
                skips += 1
            else:
                password = False
        if i < length-3 and password:
            if telephone_string[i+3] == telephone_string[i]:
                candidate += telephone_string[i+3]
                skips += 1
            else:
                password = False

        new = str(decipher_dict.get(candidate))
        result += new
        password = True

    return result

