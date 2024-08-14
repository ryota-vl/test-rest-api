from pytest import mark


@mark.testomatio('@T418c3493')
@mark.smoke
def test_create_post(session):
    response = session.post(
        '/posts', json={'title': 'foo', 'body': 'bar', 'userId': 1})
    assert response.ok
    assert response.json()['title'] == 'foo'
    assert response.json()['body'] == 'bar'
    assert response.json()['userId'] == 1


@mark.testomatio('@Tca30bc2d')
def test_delete_post(session):
    response = session.delete('/posts/1')
    assert response.ok
    assert response.json() == {}


@mark.testomatio('@T6579fee9')
def test_put_post(session):
    response = session.put(
        '/posts/1', json={'title': 'foo', 'body': 'bar', 'userId': 1})
    assert response.ok
    assert response.json()['title'] == 'foo'
    assert response.json()['body'] == 'bar'
    assert response.json()['userId'] == 1


@mark.testomatio('@Tf83280b0')
def test_patch_post(session):
    response = session.patch(
        '/posts/1', json={'title': 'foo', 'body': 'bar', 'userId': 1})
    assert response.ok
    assert response.json()['title'] == 'foo'
    assert response.json()['body'] == 'bar'
    assert response.json()['userId'] == 1
