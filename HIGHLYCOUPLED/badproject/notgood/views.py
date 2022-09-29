from datetime import datetime
from django.views.generic import View
from django.http.response import JsonResponse
from notgood.models import Customer, Application


class ApplicationView(View):
    def post(self, request, *args, **kwargs):
        # 1. get or create the customer

        try:
            saved_customer = Customer.objects.filter(customer_ssn=request.POST["customer_ssn"])
        except Customer.DoesNotExist:
            saved_customer = Customer(customer_name=request.POST["customer_name"], customer_ssn=request.POST["customer_ssn"])
            try:
                saved_customer.full_clean()
                saved_customer.save()
            except Exception:
                return JsonResponse({
                    "success": False,
                    "application_id": None
                })

        # 2. save the application
        application = Application(application_date=datetime.now(), customer=saved_customer)

        try:
            application.full_clean()
            application.save()
        except Exception:
            return JsonResponse({
                "success": False,
                "application_id": None
            })

        # 3. return the application result
        return JsonResponse({
            "success": True,
            "application_id": application.id,
        })
