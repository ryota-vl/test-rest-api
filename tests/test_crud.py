from pytest import mark


@mark.smoke
def test_create_post(session):
    response = session.post('/posts', json={
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    })
    assert response.ok
    payload = response.json()
    assert payload['title'] == 'foo'
    assert payload['body'] == 'bar'
    assert payload['userId'] == 1


def test_update_post(session):
    response = session.put('/posts/1', json={
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    })
    assert response.ok
    payload = response.json()
    assert payload['title'] == 'foo'
    assert payload['body'] == 'bar'
    assert payload['userId'] == 1


def test_delete_post(session):
    response = session.delete('/posts/1')
    assert response.ok
    assert response.json() == {}
