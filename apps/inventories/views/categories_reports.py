"""Categories reports."""

# Django
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.utils import timezone

# xhtml2pdf
from xhtml2pdf import pisa

# Models
from apps.inventories.models import Category

# Utilities
from apps.utils.reports import link_callback


def render_pdf_categories_view(request):
    template_path = 'core/base/crud/reports/model_list_printer.html'
    report_name = 'categorias'
    
    today = timezone.now()
    categories = Category.objects.filter(active=True)

    title_cols = ('Nombre',)

    data = [ [category.name,] for category in categories ]

    context = {
        'title_header': 'Categorías de productos', 
        'title_cols': title_cols,
        'data': data, 
        'today': today, 
        'request': request
    }

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="{}.pdf"'.format(report_name)

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpRespon
    return response
