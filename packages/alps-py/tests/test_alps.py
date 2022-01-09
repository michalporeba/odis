from alps import Alps 

def test_root_is_alps():
    data = Alps().to_data()
    assert 1 == len(data.keys())
    assert None != data['alps']