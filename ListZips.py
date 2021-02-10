list1 = [1, 2, 3, 4, 5]
list2 = ["one", "two", "three", "four", "five"] # we can also use many number of list

zipped = list(zip(list1, list2)) # zipping the list

print(zipped) # if the no.of elements in all the list satisfies the number of elements in all list it prints out otherwise not

unzipped = list(zip(*zipped)) # unzipping the list

print(unzipped)

for l1, l2 in zip(list1, list2):
    print(l1, end=" ")
    print(l2)

items = ["Apple", "Banana", "Oranges"]
counts = [3, 6, 4]
prices = [0.99, 0.25, 0.50]

sentences = []
for (item, count, price) in zip(items, counts, prices):
    item, count, price = str(item), str(count), str(price)
    sentence = "I bought " + count + " " + item + "s at " + "cents each."
    sentences.append(sentence)
print('''
'''.join(sentences))
