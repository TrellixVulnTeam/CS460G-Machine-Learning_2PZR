# NOTES FOR DOCUMENTATION WRITE-UP:
# Assumptions:
#   943 users
#   1682 movies
#   column 1 - user, 2 - movie, 3 - rating
#   if user has not seen one of the movies, I set a default rating of 0
# Slow runtime

import math
import time
from tqdm import tqdm

# --------------------------------------- FUNCTIONS --------------------------------------- #


# output list of cosine similarities for each piece of data
def cosine_similarity(person_num, movie_num, training_data):
    start = time.time()
    person_ratings_data = []  # create list for each user and their rating for each movie
    similarity_ratios = []

    # for each user
    for i in range(1, 944):

        temp = [0]*1683  # index 0 = user, 1-1682 = rating of each movie (default value = 0)
        temp[0] = i

        # create a list with a rating for each movie
        for row in training_data:
            if int(row[0]) == i:
                 temp[int(row[1])] = int(row[2])

        # print(temp)
        person_ratings_data.append(temp)

    print(time.time() - start)

    # store given user's data (number and ratings)
    given_info = person_ratings_data[person_num - 1]
    # print(given_info)

    iteration = 0
    # go through list of each user and their ratings
    for info in person_ratings_data:

        dot_product = 0  # numerator
        magnitude = 0   # denominator
        current_magnitude = 0
        given_magintude = 0
        iteration += 1

        # don't calculate cosine similarity between given person and themself
        # don't calculate cosine similarity if user has not seen given movie (keep it set at 0)
        if info[0] != person_num and info[movie_num] != 0:

            # for each movie rating
            for index in range(1, 1683):

                # can't calculate similarity of movie user is trying to find rating of
                if index != movie_num:

                    dot_product += info[index] * given_info[index]
                    current_magnitude += info[index] * info[index]
                    given_magintude += given_info[index] * given_info[index]

            # calculate magnitude of current person and given person
            magnitude = math.sqrt(current_magnitude) * math.sqrt(given_magintude)

            t = []
            t.append(iteration)

            if magnitude != 0:
                t.append(dot_product / magnitude)
            else:
                t.append(0)
            similarity_ratios.append(t)

        # USE 0 AS PLACEHOLDER
        else:
            t = []
            t.append(iteration)
            t.append(0)
            similarity_ratios.append(t)

    return similarity_ratios, person_ratings_data


# output list of 'k' highest similarities (data of user with highest similarities)
def top_similarities(k, cosine_similarities):

    # print(cosine_similarities[cosine_similarities[:,1].argsort()])
    # print(sorted(cosine_similarities, key=lambda x: (x[1])))
    top = []
    top.append(sorted(cosine_similarities, key=lambda x: (x[1]))[-3:])
    # print(top)

# ----------------------------------------- MAIN ----------------------------------------- #

# open training data file
training_file = open("data/u1-base.base", "r")
training_file_contents = training_file.read()

# store each row in a list
training_rows = []
for line in training_file_contents.splitlines():
    training_rows.append(line.split())


# open training data file
test_file = open("data/u1-test.test", "r")
test_file_contents = test_file.read()

# TEST DATA
# store each row in a list
test_rows = []
for line in test_file_contents.splitlines():
    test_rows.append(line.split())

for i in tqdm(test_rows):

    # calculate cosine similarity for each piece of data in training
    similarities, user_data = cosine_similarity(int(i[0]), int(i[1]), training_rows)
    # print(similarities)
    input("hi")

    # find the k nearest neighbors
    k = 3
    nearest_neighbors = top_similarities(k, similarities)


# user = input("User: ")
# movie = input("Movie: ")
# similarities, user_data = cosine_similarity(int(user), int(movie), training_rows)
# # print(similarities)
# k = 3
# nearest_neighbors = top_similarities(k, similarities)


# TODO:

# for now k = 3

# create function k_nearest_neighbors(k, similarities)
# find highest 3 cosine similarities and their info - person & ratings (person = index + 1)

# create function predicted_rating(highest_similarities, highest_info)