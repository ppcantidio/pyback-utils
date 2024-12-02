import unittest

import pytest

from pyback.pgsql.pgsql_async_client import PGCredentials, PGSQLAsyncClient


@pytest.mark.asyncio
@unittest.mock.patch(
    "pyback.pgsql.pgsql_async_client.create_async_engine", new=unittest.mock.AsyncMock
)
async def test_connect(*args, **kwargs):
    db = PGSQLAsyncClient(
        PGCredentials(
            username="username",
            password="password",
            database="database",
            host="host",
            port=5432,
        )
    )
    async with db.connect() as conn:
        assert conn is not None
