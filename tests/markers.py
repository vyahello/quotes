import _pytest.mark
import pytest

unit: _pytest.mark.MarkDecorator = pytest.mark.unit
param: _pytest.mark.MarkDecorator = pytest.mark.parametrize
web: _pytest.mark.MarkDecorator = pytest.mark.web
api: _pytest.mark.MarkDecorator = pytest.mark.parametrize
