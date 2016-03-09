from faker import Factory
from news.models import Post, Comment, UserProfile

'''
to run
1) python3 manage.py shell
2) from news.seed import seed_from_fake
3) seed_from_fake()
'''

def seed_from_fake():
    "This seeds a DB with fake text, using the faker"
    # create a fake factory
    fake = Factory.create()

    # print is as sanity check
    print(fake.text())

    # open or make text file
    text_file = open("Output.txt", "w")

    # 50 times
    for i in range(50):
        # make some fake text
        fake_text = fake.text() # this just gives stupid text 
        # # print fake text
        # print(fake_text[:49])
        # # print seperator
        # print("_____________")
        # make new post

        # split the text up to make a title and post 
        title = fake_text[:49]
        text = fake_text

        post = Post(title=fake_text, text=text)
        post.save()



def seed_from_file():
    "This seeds the db from a tab seperated file without using csv reader"
    # open text file for reading
    with open("posts/Output.txt", "r") as seed_file:

    # iterate across each line
        for line in seed_file:
            # split on tab
            split = line.split("  ")
            # first part is title
            title = split[0].strip(' \n')
            # second part is text
            text = split[1].strip(' \n')
            # make post object with text and title
            post = Post(title=title, text=text)
            # save to db
            post.save()




def write_text_seed_file():
    "this creates a file with random fake text"
    fake = Factory.create()

    # print is as sanity check
    print(fake.text())

    # open or make text file
    text_file = open("Output.txt", "w")

    # 50 times
    for i in range(50):
        # make some fake text
        fake_text = fake.text()
        # # print fake text
        # print(fake_text[:49])
        # # print seperator
        # print("_____________")
        # make new post
        title = fake_text[:49]
        text = fake_text
        line = title + "\t" + text + "\n"
        text_file.write(line)

    text_file.close()