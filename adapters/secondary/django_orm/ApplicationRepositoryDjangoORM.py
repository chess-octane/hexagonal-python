from corebusiness.exceptions.ApplicationNotFoundExeption import ApplicationNotFoundException
from corebusiness.ports.secondary.IApplicationRepository import IApplicationRepository
from corebusiness.entities.Application import Application

from adapters.primary.django.myapp.models import Application as ApplicationModel


class ApplicationRepositoryDjangoORM(IApplicationRepository):
    def save_application(self, application: Application) -> Application:
        application_instance = ApplicationModel.objects.create(
            date=application.date,
            customer_id=application.customer_id
        )
        return Application(
            id=application_instance.id,
            date=application_instance.date,
            customer_id=application_instance.customer_id,
        )

    def get_application(self, application_id: str) -> Application:
        application_instance = ApplicationModel.objects.filter(pk=application_id).first()

        if not application_instance:
            raise ApplicationNotFoundException()

        return Application(
            id=application_instance.id,
            date=application_instance.date,
            customer_id=application_instance.customer_id,
        )
