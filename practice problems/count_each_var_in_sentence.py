from pprint import pprint
sentence="this is a common interview question"
sen=set(sentence)

sen.remove(' ')

dictionary=({i:sentence.count(i) for i in sen})
pprint(dictionary,width=5)
max1=0
for i in dictionary:
    if dictionary[i]>max1:
        max1=dictionary[i]
print(max1)
dictionary_sorted=sorted(dictionary.items(),key=lambda kv:kv[1],reverse=1)
print(dictionary_sorted[0])
