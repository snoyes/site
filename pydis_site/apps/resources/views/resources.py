from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from pydis_site.apps.resources.utils import RESOURCE_TABLE, get_resources_from_search

RESOURCE_META_TAGS = {k: list(v) for k, v in RESOURCE_TABLE.items()}


def format_checkbox_options(options: str) -> list[str]:
    """Split up the comma separated query parameters for checkbox options into a list."""
    return options.split(",")[:-1] if options else []


def resource_view(request: HttpRequest) -> HttpResponse:
    """View for resources index page."""
    checkbox_options = {
        a: set(format_checkbox_options(request.GET.get(b)))
        for a, b in (
            ('topics', 'topicOption'),
            ('type', 'typeOption'),
            ('payment_tiers', 'paymentOption'),
            ('complexity', 'complexityOption'),
        )
    }

    return render(
        request,
        template_name="resources/resources.html",
        context={
            "checkboxOptions": checkbox_options,
            "topics": sorted(RESOURCE_META_TAGS.get("topics")),
            "tag_types": sorted(RESOURCE_META_TAGS.get("type")),
            "payment_tiers": sorted(RESOURCE_META_TAGS.get("payment_tiers")),
            "complexities": sorted(RESOURCE_META_TAGS.get("complexity")),
            "resources": get_resources_from_search(checkbox_options)
        }
    )
