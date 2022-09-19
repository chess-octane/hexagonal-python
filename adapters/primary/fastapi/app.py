from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

from corebusiness.use_cases.SubmitLoanApplicationUseCase import SubmitLoanApplicationUseCase
from corebusiness.ports.primary.ISubmitLoanApplication import LoanApplicationInfo

from adapters.secondary.psycopg.LoanApplicationRepositoryPsycopg import LoanApplicationRepositoryPsycopg
from adapters.secondary.psycopg.CustomerRepositoryPsycopg import CustomerRepositoryPsycopg

class ApplicationBody(BaseModel):
    customer_ssn: str
    customer_name: str

app = FastAPI()

@app.post("/application")
async def submit_application(body: ApplicationBody):
    # TODO: use automatic dependency injection
    submit_app_use_case = SubmitLoanApplicationUseCase(
        customer_repository=CustomerRepositoryPsycopg(),
        loan_application_repository=LoanApplicationRepositoryPsycopg(),
    )

    application_info = LoanApplicationInfo(
        customer_ssn=body.customer_ssn,
        customer_name=body.customer_name,
        application_date=datetime.now().isoformat(),
    )

    result = submit_app_use_case.handle(application_info=application_info)

    return {
        "success": result.success,
        "application_id": result.application_id,
    }
