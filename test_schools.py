import schools


def test_parseschoolschooldata():
    with open("output/div.html") as file:
        data = file.read()
        school_data = schools.parseschooldata(data)
        assert len(school_data) == 5
        assert "Mount Holly Elementary" in school_data


def test_empty_string_parseschooldata():
    school_data = schools.parseschooldata("")
    assert school_data == tuple()


def test_random_data_parseschooldata():
    school_data = schools.parseschooldata("random stuff")
    assert school_data == tuple()


def test_getschools():
    with open("output/div.html") as file:
        data = file.read()
        school_list = schools.get_schools(data)
        assert len(school_list) == 53
        assert "Berkeley County School District" in school_list


def test_empty_string_getschools():
    school_list = schools.get_schools("")
    assert len(school_list) == 0


def test_invalid_string_getschools():
    school_list = schools.get_schools("Hello World")
    assert len(school_list) == 0


def test_getheaders():
    with open("output/div2.html") as file:
        data = file.read()
        assert len(schools.gettableheader(data)) == 7
        assert "Student Close Contacts" in schools.gettableheader(data)


def test_getemptyheaders():
    assert schools.gettableheader("") == tuple()
    assert schools.gettableheader("random") == tuple()
