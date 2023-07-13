from django.http import HttpResponse

from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 321,
            "customer_name": "Maxs Forocca",
            "amount": 1999.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            return HttpResponse(pdf, content_type = ' application/pdf')
        return HttpResponse("No Encontrado")
    # videotime = 10:25

"""
def generate_view(request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 321,
            "customer_name": "Maxs Forocca",
            "amount": 1999.99,
            "today": "Today",
        }
        html = template.render(context)
        return HttpResponse(html)
"""