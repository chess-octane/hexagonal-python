from datetime import datetime
from flask import Flask, request

from corebusiness.use_cases.SubmitApplicationUseCase import SubmitApplicationUseCase
from corebusiness.ports.primary.ISubmitApplication import ApplicationInfo

from .adapters.ApplicationRepository import ApplicationRepository
from .adapters.CustomerRepository import CustomerRepository

app = Flask(__name__)

@app.route("/application", methods=['POST'])
def submit_application():
    submit_app_use_case = SubmitApplicationUseCase(
        customer_repository=CustomerRepository(),
        application_repository=ApplicationRepository(),
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
