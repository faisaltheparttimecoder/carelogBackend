from zendesk.lib.ticket_extractor import extract_tickets_created_by_month, extract_status_count_tickets, extract_top_creators
from zendesk.lib.ticket_extractor import extract_top_product_components, extract_ticket_created_solved_by_current_year
from zendesk.lib.ticket_extractor import extract_priority_tickets_for_year, extract_ticket_by_version
from zendesk.lib.ticket_extractor import extract_ticket_by_kb, extract_ticket_by_environment


def qdict_to_dict(qdict):
    """
    Convert a Django QueryDict to a Python dict.

    Single-value fields are put in directly, and for multi-value fields, a list
    of all values is stored at the field's key.
    """
    return {k: v[0] if len(v) == 1 else v for k, v in qdict.lists()}


def method_mapper(method, request):
    url_parameters = qdict_to_dict(request.GET)
    org_id = url_parameters['org_id']
    from_date = url_parameters['fromDate']
    end_date = url_parameters['endDate']
    switcher = {
        "status_count": extract_status_count_tickets(org_id, from_date, end_date),
        "tickets_created_by_month": extract_tickets_created_by_month(org_id),
        "top_creators": extract_top_creators(org_id, from_date, end_date),
        "top_product_components": extract_top_product_components(org_id, from_date, end_date),
        "ticket_created_solved": extract_ticket_created_solved_by_current_year(org_id),
        "priority_tickets": extract_priority_tickets_for_year(org_id),
        "ticket_by_version": extract_ticket_by_version(org_id, from_date, end_date),
        "ticket_by_environment": extract_ticket_by_environment(org_id, from_date, end_date),
        "ticket_by_kb": extract_ticket_by_kb(org_id, from_date, end_date)
    }
    return switcher.get(method, "Method is yet not implemented")
