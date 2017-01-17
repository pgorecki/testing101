

class Comment:
    def __init__(self, email, comment):
        self.email = email
        self.comment = comment


class BlogPost:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments(self):
        return self.comments


# TODO: blog posts stops accepting comments after 24hrs
