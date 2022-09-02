from mock import MagicMock

from corebusiness.entities.Application import Application
from corebusiness.entities.Customer import Customer
from corebusiness.ports.primary.ISubmitApplication import ApplicationInfo
from corebusiness.use_cases.SubmitApplicationUseCase import SubmitApplicationUseCase

customer_repository_mock = MagicMock()
application_repository_mock = MagicMock()


class TestSubmitApplicationUseCase:
    # SUT => Subject Under Test
    sut = SubmitApplicationUseCase(
        customer_repository=customer_repository_mock,
        application_repository=application_repository_mock,
    )

    def setup_class(self):
        customer_repository_mock.reset_mock()
        application_repository_mock.reset_mock()

    def test_existing_user_can_submit_application(self):
        application_info = ApplicationInfo('2233', 'John Doe', '2022-01-01T00:00:00')
        saved_application = Application(1, application_info.application_date, 2)
        saved_customer = Customer(9, application_info.customer_name, application_info.customer_ssn)

        # configure repository methods to return an expected value
        customer_repository_mock.get_customer = MagicMock(return_value=saved_customer)
        application_repository_mock.save_application = MagicMock(return_value=saved_application)

        result = self.sut.handle(application_info)

        # assert the result is as expected
        assert result.application_id == saved_application.id
        assert result.success is True

        # assert the repository methods were called with the expected parameters
        customer_repository_mock.get_customer.assert_called_once_with(application_info.customer_ssn)
        application_repository_mock.save_application.assert_called_once()
        assert application_repository_mock.save_application.call_args.args[0].id is None
        assert application_repository_mock.save_application.call_args.args[0].date == application_info.application_date
        assert application_repository_mock.save_application.call_args.args[0].customer_id == saved_customer.id
