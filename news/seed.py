import csv 
from news.models import Post, Comment, UserProfile 

'''
to run
1) python3 manage.py shell
2) from news.seed import seed
3) save ?
'''
# 
# open the file with information we want to seed from 
with open("news/seed.txt", encoding='latin-1') as seed_file:

    "this seeds a DB from a file using csv reader"
    # use csv reader to split the each line in the file by tab or comma
    reader = csv.reader(seed_file, delimiter="\t")

    for row in reader:
        # print each row for testing
        print (row)  
            # for each line create an object in the db
        _, created = Post.objects.get_or_create(
            # give each part of the db object a positional from the seed file 
            title = row[0],
            link = row [1],
            content = row[2],
            )
        






# from faker import Factory
# from news.models import Post, Comment, UserProfile

# '''
# to run
# 1) python3 manage.py shell
# 2) from news.seed import seed_from_fake
# 3) seed_from_fake()
# '''

# def seed_from_fake():
#     "This seeds a DB with fake text, using the faker"
#     # create a fake factory
#     fake = Factory.create()

#     # print is as sanity check
#     print(fake.text())

#     # open or make text file
#     text_file = open("Output.txt", "w")

#     # 50 times
#     for i in range(50):
#         # make some fake text
#         fake_text = fake.text() # this just gives stupid fake text 

#         # split the text up to make a title and post 
#         title = fake_text[:49]
#         text = fake_text

#         # seed the db with the test you just created
#         post = Post(
#           title=fake_text, 
#           text=text
#           )
#         post.save()




# def seed_from_file():
#     "This seeds the db from a tab seperated file without using csv reader"
#     # open text file for reading
#     with open("posts/Output.txt", "r") as seed_file:

#     # iterate across each line
#         for line in seed_file:
#             # split on tab
#             split = line.split("  ")
#             # first part is title
#             title = split[0].strip(' \n')
#             # second part is text
#             text = split[1].strip(' \n')
#             # make post object with text and title
#             post = Post(title=title, text=text)
#             # save to db
#             post.save()




# def write_text_seed_file():
#     "this creates a file with random fake text"
#     fake = Factory.create()

#     # print is as sanity check
#     print(fake.text())

#     # open or make text file
#     text_file = open("Output.txt", "w")

#     # 50 times
#     for i in range(50):
#         # make some fake text
#         fake_text = fake.text()

#         # split the text up to make a title and post 
#         title = fake_text[:49]
#         text = fake_text

#         # create lines with tabs in between te created title and post
#         line = title + "\t" + text + "\n"
#         # write each new line to the file
#         text_file.write(line)

#     text_file.close()



