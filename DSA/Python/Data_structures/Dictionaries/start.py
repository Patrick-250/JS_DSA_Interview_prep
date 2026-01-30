#below dict define the agents names(as keys) and they uses(as values)
agents={
"course_generator":"used to generate the course based on student request",
"quiz_generator":"used to generate quizzes for the students based on the course",
"quiz_grader":"used to grade quizzes submitted by the students"

}

role_of_course_generator=agents["course_generator"] 
role_of_quiz_generator=agents["quiz_generator"] 
role_of_quiz_grader=agents["quiz_grader"] 

if __name__=="__main__":
    print(role_of_course_generator)
    print(role_of_quiz_generator)
    print(role_of_quiz_grader)