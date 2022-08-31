import abc
from abc import abstractmethod
from ...entities.Application import Application


class IApplicationRepository(abc.ABC):
    @abstractmethod
    def save_application(self, application: Application) -> Application:
        raise NotImplementedError()

    @abstractmethod
    def get_application(self, application_id: str) -> Application:
        """
        This might throw ApplicationNotFoundException
        """
        raise NotImplementedError()
