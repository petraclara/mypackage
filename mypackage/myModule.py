def top_n(list, n):
    """ Return the top n items in an array, desc order.

    Args:
        list(array): list or array-like object
        n(int): num of items to return
    
    Return:
        array: top n items ,desc order

    Egs:
        >>> top_n([8,3,2,7,4],3)
        [8,7,3]
    """
    for i in range(n):
        for j in range(len(list)-1-i):

            if list[j] > list[j+1]: # if the item is bigger than the next item
                list[j],list[j+1] = list[j+1],list[j] #swap the two

#get last two items
top_n = list[-n:]

#retun in desc order
return top_n[::-1]

    