from start import agents
# print(agents)

#really no pre defined method to call on a dictionary to add a new key value pair
#we just do dictionary[key]=value; O(1)

agents["retake_generator"]="uses the previous quizzes to generate a retake quiz with the same difficulty level for students with F grade"

# print(agents) #retake_generator agent added

#same works on updating the value; O(1)
agents["retake_generator"]="uses the previous quizzes to generate a retake quiz with the same difficulty level for students with D grade and below"
# print(agents) # #retake_generator agent role(value) updated