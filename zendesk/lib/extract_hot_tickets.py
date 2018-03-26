from zendesk.models import HotTicket
from common.utilities import find_between


def extract_hot_ticket(search_string):
    collector = {}
    org_id = find_between(search_string, 'organization:', ' updated')
    hot_tickets = HotTicket.objects.filter(org_id=org_id)
    for hot_ticket in hot_tickets:
        collector['zd' + str(hot_ticket.org_id) + str(hot_ticket.ticket_id)] = hot_ticket.hot
    return collector
