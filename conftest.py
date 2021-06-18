# -*- coding:utf-8 -*-
# author：Zzzsy

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )

    parser.addoption(
        "--devices", action="store", default="dev", help="env：表示测试环境，默认dev环境"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

@pytest.fixture()
def devices(request):
    return request.config.getoption("--devices")


