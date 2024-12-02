import unittest
import unittest.mock
from typing import Type

import pytest

from pyback.rest.errors import BadRequest, BaseError, Forbidden, NotFound, Unauthorized
from pyback.rest.handlers.base_error_handler import base_error_exception_handler


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "exc,status_code",  # Corrigido: parâmetros devem ser passados como uma única string
    [
        (BadRequest("Error message"), 400),
        (Unauthorized("Error message"), 401),
        (Forbidden("Error message"), 403),
        (NotFound("Error message"), 404),
        (Exception("Error message"), 500),
    ],
)
async def test_base_error_exception_handler(exc: Type[BaseError], status_code: int):
    response = await base_error_exception_handler(request=unittest.mock.Mock(), exc=exc)

    assert response.status_code == status_code

@pytest.mark.asyncio
async def test_add_handlers():
    app = unittest.mock.Mock()
    app.add_exception_handler = unittest.mock.Mock()

    from pyback.rest.handlers import add_handlers

    add_handlers(app)

    app.add_exception_handler.assert_any_call(BaseError, base_error_exception_handler)
    app.add_exception_handler.assert_any_call(Exception, base_error_exception_handler)