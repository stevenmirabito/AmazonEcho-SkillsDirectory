# Computer Science House
# WebNews Reader for Amazon Echo
# Written By: Marc Billow
# mbillow@csh.rit.edu

from csh import webnews
import news_key


def count_readable(unread_dict):
    total = int(unread_dict['normal'])
    replies = int(unread_dict['in_reply'])

    if total > 0 and replies > 0:
        return "There are currently {} unread posts, {} in response to posts you have made.".format(total, replies)
    elif total > 0 and replies == 0:
        return "There are currently {} unread posts.".format(total)
    else:
        return "There are no new WebNews posts."


def unread_readable(activity_dict):
    unread_posts = []
    text_to_read = "Those posts are "
    for post in activity_dict:
        if int(post['unread_count']) > 0:
            unread_posts.append('{post_title} in {newsgroup}'.format(
                post_title=post['thread_parent']['subject'],
                newsgroup=post['thread_parent']['newsgroup']))
    if unread_posts:
        for formatted_post in unread_posts:
            # If the current item is not the last item in the list and is not the only item.
            if formatted_post is not unread_posts[len(unread_posts)-1] and len(unread_posts) > 1:
                text_to_read += "{}, ".format(formatted_post)
            # If the current item is the only element in the list.
            elif len(unread_posts) == 1:
                text_to_read = "That post is {}.".format(formatted_post)
            # Reached the last element.
            elif formatted_post == unread_posts[len(unread_posts)-1] and len(unread_posts) > 1:
                text_to_read += "and {}.".format(formatted_post)
        return text_to_read
    else:
        return ""


def check_webnews():
    # Create the connection to the WebNews server.
    news = webnews.Webnews(news_key.api_key, news_key.agent_id)
    # Format final text and store it.
    text_to_read = "{} {}".format(count_readable(news.get_unread_counts()), unread_readable(news.activity()))
    return text_to_read, True

# For testing purposes, running the Python file, executes return_all()

if __name__ == "__main__":
    print check_webnews()[0]

