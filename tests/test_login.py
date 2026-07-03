
def test_login(login):
    
    assert "dashboard" in login.url.lower()
