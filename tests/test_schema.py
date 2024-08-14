from pytest import mark
from schemas.schemas import validate_schema, post_schema, comment_schema, album_schema, user_schema


@mark.testomatio('@T2238b4b7')
@mark.smoke
def test_post_schema(session):
    response = session.get('/posts')
    for post in response.json():
        result = validate_schema(post, post_schema)
        assert result[0], f'post id = {[post['id']]} ' + result[1]


@mark.testomatio('@Tc89f80cd')
@mark.smoke
def test_user_1_schema(session):
    response = session.get('/users/1')
    result = validate_schema(response.json(), user_schema)
    assert result[0], result[1]


@mark.testomatio('@Tcbae2102')
def test_album_1_schema(session):
    response = session.get('/albums/1')
    result = validate_schema(response.json(), album_schema)
    assert result[0], result[1]


@mark.testomatio('@Td173004c')
def test_comment_1_schema(session):
    response = session.get('/comments/1')
    result = validate_schema(response.json(), comment_schema)
    assert result[0], result[1]
