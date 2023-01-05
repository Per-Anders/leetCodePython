def rescueBoats(people, limit):
    people.sort()
    left = 0 
    right = len(people)-1
    boats = 0 
    while (left <= right):
        if (left == right):
            boats += 1
            break
        if (people[left] + people[right] <= limit):
            left += 1
        right -= 1
        boats += 1
    return boats


print(rescueBoats([2, 1, 3, 4], 4))
             
                