from datetime import datetime
from flask import Flask, request

from corebusiness.use_cases.SubmitApplicationUseCase import SubmitApplicationUseCase
from corebusiness.ports.primary.ISubmitApplication import ApplicationInfo

from adapters.secondary.psycopg.ApplicationRepositoryPsycopg import ApplicationRepositoryPsycopg
from adapters.secondary.psycopg.CustomerRepositoryPsycopg import CustomerRepositoryPsycopg

app = Flask(__name__)

@app.route("/application", methods=['POST'])
def submit_application():
    # TODO: use automatic dependency injection
    submit_app_use_case = SubmitApplicationUseCase(
        customer_repository=CustomerRepositoryPsycopg(),
        application_repository=ApplicationRepositoryPsycopg(),
    )

    application_info = ApplicationInfo(
        customer_ssn=request.form['customer_ssn'],
        customer_name=request.form['customer_name'],
        application_date=datetime.now().isoformat(),
    )

    result = submit_app_use_case.handle(application_info=application_info)

    return {
        "success": result.success,
        "application_id": result.application_id,
    }
