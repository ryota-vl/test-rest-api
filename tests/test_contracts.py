from pytest import mark


@mark.testomatio('@Tdf158c31')
@mark.smoke
def test_posts(session):
    response = session.get('/posts')
    assert response.ok


@mark.testomatio('@Tfa2718ee')
@mark.smoke
def test_posts_25(session):
    response = session.get('/posts/25')
    assert response.ok


@mark.testomatio('@Td90681f2')
@mark.smoke
def test_albums(session):
    response = session.get('/albums')
    assert response.ok
