import pdfkit
from django.http import HttpResponse
from django.template.loader import get_template

from flower.models import Product


def download_catalog(request):
    template = get_template("download_catalog.html")
    pdf_template = template.render({'products': Product.objects.all()})

    pdf = pdfkit.from_string(
        pdf_template,
        False,
        options={"enable-local-file-access": ""})
    response = HttpResponse(
        pdf,
        content_type='application/pdf'
    )
    filename = 'catalog_products.pdf'
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response
