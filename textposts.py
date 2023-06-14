import praw
from dotenv import dotenv_values

env = dotenv_values()
client_id = env["CLIENT_ID"]
client_secret = env["CLIENT_SECRET"]
user_agent = env["USER_AGENT"]
username = env["USERNAME"]
password = env["PASSWORD"]

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

for post in reddit.user.me().submissions.new(limit=None):
    if isinstance(post, praw.models.Submission) and not post.is_self:
        try:
            post.edit(env["TEXT"])
            print(f"Post edited: {post.id}")
        except praw.exceptions.APIException:
            print(f"{post.id} could not be edited.")
            post.delete()
            print(f"Post deleted: {post.id}")
    else:
        post.delete()
        print(f"Non-text post deleted: {post.id}")

print("All posts edited/deleted.")
