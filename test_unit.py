

def test_encode_decode_access_token():
    from app_utils import create_access_token
    from datetime import timedelta
    input_data_create_access_token = {"sub": "cuongld"}
    access_token_expires = timedelta(minutes=10)
    access_token = create_access_token(data=input_data_create_access_token, expires_delta=access_token_expires)
    from app_utils import decode_access_token
    decoded_access_token = decode_access_token(data=access_token)
    assert decoded_access_token['sub'] == input_data_create_access_token['sub']



