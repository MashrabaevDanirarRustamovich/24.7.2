from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_ge_all_pets_with_valid_key(filter=''):
    _auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(_auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0
