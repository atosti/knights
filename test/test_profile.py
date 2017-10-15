import profile 
def test_constructor_name():
    value = profile.Profile("name","username","password",{},0)
    expected = "name"
    assert expected == value.name
 
def test_constructor_username():
    value = profile.Profile("name","username","password",{},0)
    expected = "username"
    assert expected == value.username 
    
def test_constructor_password():
    value = profile.Profile("name","username","password",{},0)
    expected = "password"
    assert expected == value.password 

def test_constructor_skill_dict():
    value = profile.Profile("name","username","password",{},0)
    expected = {}
    assert expected == value.skill_dict 

def test_constructor_combat_level():
    value = profile.Profile("name","username","password",{},0)
    expected = 0
    assert expected == value.combat_level 


def test_profile_equality():
 value = profile.Profile("name","username","password",{},0)
 expected = profile.Profile("","","",{},0)
 expected.name = "name"
 expected.username = "username"
 expected.password = "password"
 expected.skill_dict = {}
 expected.combat_level = 0
 
 assert expected == value
 
def test_fetch_skills():
    p = profile.Profile("name","Karma","password",{},0)
    value = p.request_skills()
    expected = 34
    assert expected == len(value['raw_skill_list'])

def test_process_skills():
    p = profile.Profile("name","Karma","password",{},0)
    raw_skills = p.request_skills()['raw_skill_list']
    processed_skills = p.process_skills(raw_skills)
    value = len(processed_skills)
    expected = 24
    assert expected == value
    
def test_set_name():
    p = profile.Profile("name","username","password",{},0)
    p.set_name("test name")
    value = p.get_name()
    expected = "test name"
    assert expected == value

def test_set_password():
    p = profile.Profile("name","username","password",{},0)
    p.set_password("test pass")
    value = p.get_password()
    expected = "test pass"
    assert expected == value
    
def test_set_username():
    p = profile.Profile("name","username","password",{},0)
    p.set_username("test username")
    value = p.get_username()
    expected = "test username"
    assert expected == value