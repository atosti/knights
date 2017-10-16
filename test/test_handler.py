import handler
 
def test_default_profile():
    value = profile.Profile('default', '', '', default_skill_map(), '3')
    assert default_profile() == value