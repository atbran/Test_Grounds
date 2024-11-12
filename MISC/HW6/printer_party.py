#This function takes a string of pages and returns the total number of pages

#I do not like using one letter var names for a parameter but that is what the assignment says.
# p = pages
def count_pages(p):
    #create list
    pages = []
    parts = p.split(', ')

    for part in parts:
        if '-' in part:
            start, end = part.split('-')
            start = int(start)
            end = int(end)
            #this ensures that no duplicate pages are counted
            for page in range(min(start, end), max(start, end) + 1):
                if page not in pages:
                    pages.append(page)
        else:
            page = int(part)
            if page not in pages:
                pages.append(page)

    return len(pages)


#test cases
print(count_pages('5-7, 2'))
print(count_pages('12-18, 20-20'))
print(count_pages('18-12, 20-20, 5-6'))

print(count_pages('1, 3, 5-5, 7-9'))
print(count_pages('1-3, 3-1'))
print(count_pages('4, 4, 4'))
print(count_pages('2-4, 5-2'))