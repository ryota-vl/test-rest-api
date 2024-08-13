from pytest import mark


@mark.smoke
def test_posts(session):
    response = session.get('/posts')
    x = response.elapsed
    assert response.ok
    assert response.elapsed.total_seconds() * 1000 < 300  # < 300 ms
