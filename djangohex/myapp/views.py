from datetime import datetime
from django.views.generic import View
from django.http.response import JsonResponse

from corebusiness.use_cases.SubmitApplicationUseCase import SubmitApplicationUseCase
from corebusiness.ports.primary.ISubmitApplication import ApplicationInfo

from .adapters.ApplicationRepository import ApplicationRepository
from .adapters.CustomerRepository import CustomerRepository


class ApplicationView(View):
    def post(self, request, *args, **kwargs):
        submit_app_use_case = SubmitApplicationUseCase(
            customer_repository=CustomerRepository(),
            application_repository=ApplicationRepository(),
        )

        application_info = ApplicationInfo(
            customer_ssn=request.POST['customer_ssn'],
            customer_name=request.POST['customer_name'],
            application_date=datetime.now().isoformat(),
        )

        result = submit_app_use_case.handle(application_info=application_info)

        return JsonResponse({
            "success": result.success,
            "application_id": result.application_id,
        })
