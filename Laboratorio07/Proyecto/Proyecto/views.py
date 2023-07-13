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
            response = HttpResponse(pdf, content_type = 'application/pdf')
            filename = "Invoice_%s.pdf" %("321123")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("No Encontrado")
    

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