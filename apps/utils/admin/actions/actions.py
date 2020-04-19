"""Actions admin."""

# Django
from django.contrib import messages
from django.http import HttpResponse

# Utilities
import csv


class ActionDownloadData:
    """Action download data."""

    def download_data_csv(model_admin, request, queryset):
        """Download data in csv for any models."""
        
        if not queryset.count() > 0:
            level = messages.WARNING
            msg = 'No hay datos para descargar.'
            return model_admin.message_user(request, msg, level)
        else:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(model_admin.model._meta.model_name)
            writer = csv.writer(response)

            # Write header
            writer.writerow(
                [field_name for field_name in queryset[0].get_dict_fields_and_values()] # Name fields           
            )

            for row_model in queryset:
                writer.writerow(
                    [field_value for field_value in row_model.get_dict_fields_and_values().values()] # Value Fields
                )

        return response
    download_data_csv.short_description = "Descargar datos en CSV"

