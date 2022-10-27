"""
created by: thibault defeyter
created at: 2022/10/28
licene: MIT

unit testing of beerbox users domain
"""


from datetime import datetime

import pytest

from beerbox.domain.users import InMemoryUserRepository
from beerbox.domain.users import User
from beerbox.domain.users import UserAlreadyExist
from beerbox.domain.users import UserDoesNotExist


@pytest.fixture(name="user", scope="session")
def fixture_user():
    """expose a host fixture"""
    return User(
        created_at=datetime(2020, 1, 1),
        modified_at=datetime(2020, 1, 1),
        public_id="id",
        username="user",
    )


def test_repository_add_user(user):
    """test adding a user to the in memory repository"""
    repository = InMemoryUserRepository()
    repository.add_user(user)
    assert repository.storage == {user.public_id: user}


def test_repository_add_user__already_exist(user):
    """test adding a user to the in memory repository"""
    repository = InMemoryUserRepository(storage={user.public_id: user})
    with pytest.raises(UserAlreadyExist):
        repository.add_user(user)


def test_repository_get_users__empty():
    """test getting nothing from in memory repository"""
    repository = InMemoryUserRepository()
    assert not repository.get_users()


def test_repository_get_users__full(user):
    """test fetching users from in memory repository"""
    repository = InMemoryUserRepository(storage={user.public_id: user})
    assert repository.get_users() == [user]


def test_repository_get_user__does_not_exist(user):
    """test getting nothing from in memory repository"""
    repository = InMemoryUserRepository(storage={user.public_id: user})
    with pytest.raises(UserDoesNotExist):
        repository.get_user(public_id="does-not-exist")


def test_repository_get_user__exists(user):
    """test getting nothing from in memory repository"""
    repository = InMemoryUserRepository(storage={user.public_id: user})
    assert repository.get_user(public_id=user.public_id) == user
