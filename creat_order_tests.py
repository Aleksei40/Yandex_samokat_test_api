import data
import configuration
import requests
import sendler_stand_request


def test_status_cod():
    assert sendler_stand_request.st_cod.status_code == 200
