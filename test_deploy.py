import os

def test_routes_running():
    result_code = os.system('node_modules/.bin/cypress run --config video=false')
    assert(result_code == 0)