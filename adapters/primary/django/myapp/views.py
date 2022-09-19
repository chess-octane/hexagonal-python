from datetime import datetime
from django.views.generic import View
from django.http.response import JsonResponse

from corebusiness.use_cases.SubmitLoanApplicationUseCase import SubmitLoanApplicationUseCase
from corebusiness.ports.primary.ISubmitLoanApplication import LoanApplicationInfo

from adapters.secondary.django_orm.LoanApplicationRepositoryDjangoORM import LoanApplicationRepositoryDjangoORM
from adapters.secondary.django_orm.CustomerRepositoryDjangoORM import CustomerRepositoryDjangoORM

# Try using Psycopg here as well.
# from adapters.secondary.psycopg.LoanApplicationRepositoryPsycopg import LoanApplicationRepositoryPsycopg
# from adapters.secondary.psycopg.CustomerRepositoryPsycopg import CustomerRepositoryPsycopg

class ApplicationView(View):
    def post(self, request, *args, **kwargs):
        # TODO: use automatic dependency injection
        submit_app_use_case = SubmitLoanApplicationUseCase(
            customer_repository=CustomerRepositoryDjangoORM(),
            loan_application_repository=LoanApplicationRepositoryDjangoORM(),
        )

        application_info = LoanApplicationInfo(
            customer_ssn=request.POST['customer_ssn'],
            customer_name=request.POST['customer_name'],
            application_date=datetime.now().isoformat(),
        )

        result = submit_app_use_case.handle(application_info=application_info)

        return JsonResponse({
            "success": result.success,
            "application_id": result.application_id,
        })
