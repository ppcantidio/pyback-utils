import pytest
import unittest
from pyback.rest.responses.metadata import Metadata
from opentelemetry import trace


@pytest.mark.asyncio
async def test_metadata():
    with trace.get_current_span():        
        
        metadata = Metadata(service_name="pyback")
        
        assert metadata.trace_id is not None
        assert metadata.service_name == "pyback"
        assert metadata.details is None