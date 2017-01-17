from example2 import BlogPost, Comment


def test_can_add_comments():
    post = BlogPost("Hello world!", "This is my first article. Let me know what you think...")
    post.add_comment(Comment("alice@example.com", "Congrats!"))
    assert len(post.get_comments()) == 1
    post.add_comment(Comment("bob@example.com", "I like it too"))
    assert len(post.get_comments()) == 2



