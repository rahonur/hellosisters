from model import db, User,Blog,Comment,connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

# USE THE CLASS NAMES NOT TABLE

def create_blog(title, overview):
    """Create and return a new blog."""

    blog=Blog(title=title,
                  overview=overview)

    db.session.add(blog)
    db.session.commit()

    return blog


def create_comment(user,response):
    """Create and return a new comment."""

    comment=Comment(user=user, response=response)

    db.session.add(comment)
    db.session.commit()

    return comment


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
