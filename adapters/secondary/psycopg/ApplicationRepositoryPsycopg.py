from corebusiness.exceptions.ApplicationNotFoundExeption import ApplicationNotFoundException
from corebusiness.ports.secondary.IApplicationRepository import IApplicationRepository
from corebusiness.entities.Application import Application

from .db import get_connection


class ApplicationRepositoryPsycopg(IApplicationRepository):
    def save_application(self, application: Application) -> Application:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO myapp_application (date, customer_id) VALUES (%s, %s) RETURNING id", [application.date, application.customer_id])
            application_id = cursor.fetchone()[0]
            cursor.close()

        return Application(
            id=application_id,
            date=application.date,
            customer_id=application.customer_id,
        )

    def get_application(self, application_id: str) -> Application:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, date, customer_id FROM myapp_application WHERE id=%s", [application_id])
            application_row = cursor.fetchone()
            cursor.close()

        if not application_row:
            raise ApplicationNotFoundException()

        application = Application(
            id=application_row[0],
            date=application_row[1],
            customer_id=application_row[2],
        )

        return application
