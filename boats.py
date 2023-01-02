# https://www.udemy.com/course/leetcode-in-python-50-algorithms-coding-interview-questions/learn/lecture/17338822#overview
people = [2,1,3,4]
limit = 4

def rescueBoats(people, limit):
    people.sort()
    left = 0
    right = len(people)-1
    boats = 0

    while (left <= right):
        if(left == right):
            boats+=1
            break
        if(people[left] + people[right]<=limit):
            left+=1

        right-=1
        boats+=1


    return boats


print(rescueBoats(people, limit))