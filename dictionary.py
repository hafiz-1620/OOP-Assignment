Course_info={
    "CSE101":{
        "Course_Name":"Introduction to Programming",
        "Credits":3,
        "Instructor":"Dr. Alice"
    },
    "CSE102":{
        "Course_Name":"Data Structures",
        "Credits":4,
        "Instructor":"Dr. Bob"
    },
    "CSE103":{
        "Course_Name":"Database Systems",
        "Credits":3,
        "Instructor":"Dr.Carol"
    }
}
#Update the instructor's name 
Course_info["CSE102"]["Instructor"]="Dr. Bob Jr."
#Add new course
Course_info["CSE104"]={"Course_Name":"Algorithms",
        "Credits":4,
        "Instructor":"Dr. Dave"}
#Remove Course
Course_info.pop("CSE101")
#Loop through the dictionary
for x, courses in Course_info.items():
  print(x)

  for y in courses:
    print(y + ':', courses[y])