from pytest import mark
from schemas.schemas import (validate_json, post_schema,
                             comment_schema, album_schema, user_schema)


def test_posts_schema(session):
    response = session.get('/posts')
    for post in response.json():
        result = validate_json(post, post_schema)
        assert result[0], f'post id = {[post["id"]]} ' + result[1]


@mark.smoke
def test_post_1_schema(session):
    response = session.get('/posts/1')
    result = validate_json(response.json(), post_schema)
    assert result[0], result[1]


@mark.smoke
def test_user_1_schema(session):
    response = session.get('/users/1')
    result = validate_json(response.json(), user_schema)
    assert result[0], result[1]


def test_album_1_schema(session):
    response = session.get('/albums/1')
    result = validate_json(response.json(), album_schema)
    assert result[0], result[1]


def test_comment_1_schema(session):
    response = session.get('/comments/1')
    result = validate_json(response.json(), comment_schema)
    assert result[0], result[1]