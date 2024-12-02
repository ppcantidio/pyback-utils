import pytest
import unittest
from pyback.telemetry.decorator import telemetry_decorator
from opentelemetry import trace
TARGET_DECORATOR = "pyback.telemetry.decorator"
TARGET_LOGGER_DEBUG = f'{TARGET_DECORATOR}.logger.debug'


@telemetry_decorator
def sample_function():
    return 5

@telemetry_decorator
async def sample_function_async():
    return 5


@unittest.mock.patch(TARGET_LOGGER_DEBUG)
def test_telemetry_decorator(mocked_logger):
    result = sample_function()

    assert result == 5
    mocked_logger.assert_any_call("Executing sample_function function.")


@pytest.mark.asyncio
@unittest.mock.patch(TARGET_LOGGER_DEBUG)
async def test_telemetry_decorator_async(mocked_logger):
    result = await sample_function_async()
    assert result == 5
    
    mocked_logger.assert_any_call("Executing sample_function_async function.")