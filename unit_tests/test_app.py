# Include the directory above where my_app is located
import sys
sys.path.append("..")
import my_app

def test_running():
    my_app.main()
    assert isinstance(my_app, object)




