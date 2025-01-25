def count_substring(string, sub_string):
    nsubs = len(sub_string)
    occur = 0
    for s in range(len(string)-nsubs+1):
        print(string[s:s+nsubs])
        if sub_string == string[s:s+nsubs]:
            occur += 1
    return occur
         

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)