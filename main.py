from facebook_scraper import get_posts

my_dict = {'cookies': '.\cookies.json'}

for posts in get_posts('beaverconfessions',pages=1, **my_dict):
    print(posts['text'])
    print('\n\n')



