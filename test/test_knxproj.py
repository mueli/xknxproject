from xknxproject import XKNXProj

from . import RESOURCES_PATH
from .conftest import assert_stub


def test_parse_project_ets5():
    """Test parsing of ETS5 project."""
    knxproj = XKNXProj(RESOURCES_PATH / "xknx_test_project.knxproj", "test")
    project = knxproj.parse()
    assert_stub(project, "xknx_test_project.json")


def test_parse_project_modules():
    """Test parsing of ETS5 project including 2 identical devices with module definitions."""
    knxproj = XKNXProj(
        RESOURCES_PATH / "module-definition-test.knxproj",
        language_code="de-DE",
    )
    project = knxproj.parse()
    assert_stub(project, "module-definition-test.json")
