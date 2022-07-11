# 2010 or later
# born in 1991 or later
# 41 courses

for n in range(int(input())):
    name, school, born, courses = input().split(" ")
    school_start = int(school.split("/")[0])
    year_born = int(born.split("/")[0])
    
    if school_start > 2009 or year_born > 1990:
        print(name +" eligible")
        continue
    if int(courses) > 40:
        print(name +" ineligible")
    else:
        print(name +" coach petitions")