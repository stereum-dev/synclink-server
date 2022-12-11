import requests
import pytest
import configparser

# Configure pytest
def pytest_configure(config):
    pytest.api_url = get_conftest_setting('api_url','http://localhost:5051')
    pytest.api_unavailable = api_unavailable()
    # Uncomment the below to stop ALL tests if the Consensus Server is down
    # if pytest.api_unavailable:
    #     pytest.exit(f'FATAL - API unavailable: {pytest.api_url}')

# Use this to "skipif" individual tests that require an available API
def api_unavailable(api_url = None):
    if "status" not in api_unavailable.__dict__ : api_unavailable.status = None
    if api_unavailable.status != None:
        return api_unavailable.status
    try:
        api_url = api_url if api_url != None else pytest.api_url
        request = requests.get(api_url, timeout = 5)
        api_unavailable.status = False
    except requests.exceptions.ConnectionError:
        api_unavailable.status = True
    return api_unavailable.status

# Get conftest setting if either conftest.dev.ini or conftest.ini exists
# Note that the keys in "conftest.dev.ini" will overwrite "conftest.ini"
# The mentioned order above is mandatory and the file format is fixed:
# [conftest]
# key = value 
def get_conftest_setting(key,default=None):
    bn = "conftest"
    ext = "ini"
    dev = "dev"
    filename = f"{bn}.{ext}"
    filename_dev = f"{bn}.{dev}.{ext}"
    config = configparser.ConfigParser()
    try:
        config.read([filename,filename_dev])
    except:
        pass
    if not "conftest" in config:
        return default
    return config["conftest"][key] if key in config["conftest"] else default