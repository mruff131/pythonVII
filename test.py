a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

new_list = a_text.split()

# print(new_list)


# unique_words = {}

# unique_words['In'] = 1
# unique_words['In'] += 1
# print(unique_words)

def countDict(ur_list):
    
    unique_words = {}
    
    for word in ur_list:
        if word in unique_words: #checks key
            unique_words[word] += 1
        else:
            unique_words[word] = 1
    return unique_words

print(countDict(new_list))