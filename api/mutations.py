from datetime import date
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Post

@convert_kwargs_to_snake_case
def createPost_resolver(obj, info, title, description):
    try:
        today = date.today()
        post = Post(
            title=title,
            description=description,
            created_at=today.strftime("%b-%d-%Y")
        )
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": ["Incorrect date format provided.  Date should be in format dd-mm-yyy"]
        }
    return payload

@convert_kwargs_to_snake_case
def update_post_resolver(obj, info, id, title, description):
    try:
        post = Post.query.get(id)
        if post:
            post.title = title
            post.description = description
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }