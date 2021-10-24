import numpy as np



def generateQuestions(user_vector, feature_vector, maxQuestions):
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    
    features = []
    #Finding 2 features to tests
    for i in range(len(user_vector)):
        new_list = np.concatenate((user_vector[:i], user_vector[i+1:]))
        closest_value = min(new_list, key=lambda list_value : abs(list_value - user_vector[i]))
        # print(abs(closest_value-user_vector[i]), feature_vector[i],  feature_vector[np.where(user_vector==closest_value)[0][0]])
        newLocation = np.where(user_vector==closest_value)
        features.append((abs(closest_value-user_vector[i]), feature_vector[i],  feature_vector[newLocation[0][0]], i, newLocation[0][0]))
    features = sorted(features, key=lambda t: t[0])[1::2]
    # print(features)

    def getMul(value):
        return 0.05 * abs(sigmoid(user_vector[i]) - 0.5) #A ML model can be used

    numQuestionsSuggested = sum([ i[0] <= 0.05 for i in features])
    numQuestions = min(maxQuestions, numQuestionsSuggested)
    numQuestions = max(3, numQuestionsSuggested)
    # print(numQuestions)

    for i in range(numQuestions):
        print("Between an event about ", features[i][1].upper(), " and ", features[i][2].upper(), " which are you more interested in attending?" )
        newPref = input()
        firstFeatVal = user_vector[features[i][3]]
        secondFeatVal = user_vector[features[i][4]]

        if(newPref == '8'):
            firstFeatVal *= 1 + getMul(firstFeatVal)
            secondFeatVal *= 1 + getMul(secondFeatVal)
        elif(newPref == '2'):
            firstFeatVal *= 1 - getMul(firstFeatVal)
            secondFeatVal *= 1 - getMul(secondFeatVal)
        elif(newPref == '4'):
            firstFeatVal *= 1 + getMul(firstFeatVal)
        elif(newPref == '6'):
            secondFeatVal *= 1 + getMul(secondFeatVal)

    events = input("What are some other types of events you recently want to attend?\n  ")
    events = events.split(" ")
    for eventCat in events:
        index = np.where(feature_vector == eventCat)[0]
        if (index.size != 0):
            user_vector[index[0]] *= 1 + getMul(user_vector[index[0]])

    return user_vector


np.set_printoptions(precision=None, suppress=True) 
feature_vector = np.array(['research', 'workshop', 'tech', 'science', 'med', 'law', 'env', 'engineering', 'coding', 'sports']) 
    #Saturday / Weekend - Virtual, non-virtual categories (locations, categorical vars)
    #Hard-category -> only search on the subspace
user_vector = np.array([22, -0.373, 0.467, -0.238, 0.190, 0.93, 0.23, -0.28, -0.012, 0.419, 0.319])
UID = user_vector[0]
maxQuestions = 3

print(user_vector)
user_vector = generateQuestions(user_vector[1:], feature_vector, maxQuestions)
user_vector = np.insert(user_vector, 0, UID)
print(user_vector)