import copy
from zendesk.models import TicketAttribute, Organisation
from common.utilities import find_between
from django.db import connection


def dict_fetch_all(cursor):
    """
    Return all rows from a cursor as a dict
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetch_all_by_month(cursor):
    """
    We need the data in this format
    data = [
        Month: "jan", "type1": value , "type2": value,
        Month: "feb", "type1": value , "type2": value,
        ......
    ]
    do the below code helps to build the dictionary on that method
    """
    collectors = []
    is_the_data_empty = True
    cursor_fetch = cursor.fetchall()
    types = [rows[0] for rows in cursor_fetch]

    # built a template of dictionary
    for col in cursor.description:
        temp_collector = {}
        if col[0] != 'Type':
            temp_collector['month'] = col[0]
            for type in types:
                temp_collector[type] = ''
            collectors.append(temp_collector)

    # Now populate the row
    for rows in cursor_fetch:
        type = None
        index = 0
        for row in rows:
            if index == 0:
                type = row
            else:
                if row > 0:
                    is_the_data_empty = False
                collectors[index-1][type] = row
            index = index + 1

    return [{
        'collectors': collectors,
        'is_the_data_empty': is_the_data_empty
    }]


def run_query(sql, by_month=False):
    """
    Run the raw sql and return the result
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.close()
    if by_month:
        return dict_fetch_all_by_month(cursor)
    else:
        return dict_fetch_all(cursor)


def extract_ticket_attributes(search_string):
    collector = {}
    org_id = find_between(search_string, 'organization:', ' updated')
    ticket_attributes = TicketAttribute.objects.filter(org_id=Organisation.objects.get(org_id=org_id))
    for attribute in ticket_attributes:
        collector['zd' + str(attribute.org_id.id) + str(attribute.ticket_id) + 'hot'] = attribute.hot
        collector['zd' + str(attribute.org_id.id) + str(attribute.ticket_id) + 'patch'] = attribute.patch
    return collector


def extract_status_count_tickets(org_id):
    sql = """  
    SELECT 
        status, COUNT(*) "total"
    FROM
        zendesk_ticket
    WHERE
        org_id_id = """ + org_id + """
    GROUP BY 1
    ORDER BY 1 
    """
    return run_query(sql)


def extract_tickets_created_by_month(org_id):
    sql = """
    SELECT Year(created) Type
      ,ifnull(ROUND(sum(case when month(created) = 1 then 1 end)), 0) Jan
      ,ifnull(ROUND(sum(case when month(created) = 2 then 1 end)), 0) Feb
      ,ifnull(ROUND(sum(case when month(created) = 3 then 1 end)), 0) Mar
      ,ifnull(ROUND(sum(case when month(created) = 4 then 1 end)), 0) Apr
      ,ifnull(ROUND(sum(case when month(created) = 5 then 1 end)), 0) May
      ,ifnull(ROUND(sum(case when month(created) = 6 then 1 end)), 0) Jun
      ,ifnull(ROUND(sum(case when month(created) = 7 then 1 end)), 0) Jul
      ,ifnull(ROUND(sum(case when month(created) = 8 then 1 end)), 0) Aug
      ,ifnull(ROUND(sum(case when month(created) = 9 then 1 end)), 0) Sep
      ,ifnull(ROUND(sum(case when month(created) = 10 then 1 end)), 0) Oct
      ,ifnull(ROUND(sum(case when month(created) = 11 then 1 end)), 0) Nov
      ,ifnull(ROUND(sum(case when month(created) = 12 then 1 end)), 0) "Dec"
    FROM zendesk_ticket
    WHERE  org_id_id = """ + org_id + """
    AND created >= DATE_SUB(now(), INTERVAL 2 YEAR)
    GROUP BY Year(created)
    ORDER BY 1
    """
    return run_query(sql, True)


def extract_top_creators(org_id, from_date, end_date):
    sql = """
    SELECT 
        submitter label, COUNT(*) total
    FROM
        zendesk_ticket
    WHERE
        org_id_id = """ + org_id + """
    AND created >= '""" + from_date + """'
    AND created <= '""" + end_date + """'
    GROUP BY 1
    ORDER BY 2 desc
    LIMIT 10 
    """
    return run_query(sql)


def extract_top_product_components(org_id, from_date, end_date):
    sql = """
    SELECT 
        CASE
          WHEN product_component LIKE 'to_be_filled_%' THEN 'unknown'
          WHEN product_component LIKE '%csr%' THEN 'csr'
          ELSE REPLACE(product_component, '_', ' ')
        END label,
        COUNT(*) total
    FROM
        zendesk_ticket
    WHERE
        org_id_id = """ + org_id + """
    AND created >= '""" + from_date + """'
    AND created <= '""" + end_date + """'
    GROUP BY 1
    ORDER BY 2 desc
    LIMIT 10
    """
    return run_query(sql)


def extract_ticket_created_solved_by_current_year(org_id):
    sql = """
    SELECT "Created" Type
      ,ifnull(ROUND(sum(case when month(created) = 1 then 1 end)), 0) Jan
      ,ifnull(ROUND(sum(case when month(created) = 2 then 1 end)), 0) Feb
      ,ifnull(ROUND(sum(case when month(created) = 3 then 1 end)), 0) Mar
      ,ifnull(ROUND(sum(case when month(created) = 4 then 1 end)), 0) Apr
      ,ifnull(ROUND(sum(case when month(created) = 5 then 1 end)), 0) May
      ,ifnull(ROUND(sum(case when month(created) = 6 then 1 end)), 0) June
      ,ifnull(ROUND(sum(case when month(created) = 7 then 1 end)), 0) July
      ,ifnull(ROUND(sum(case when month(created) = 8 then 1 end)), 0) Aug
      ,ifnull(ROUND(sum(case when month(created) = 9 then 1 end)), 0) Sep
      ,ifnull(ROUND(sum(case when month(created) = 10 then 1 end)), 0) Oct
      ,ifnull(ROUND(sum(case when month(created) = 11 then 1 end)), 0) Nov
      ,ifnull(ROUND(sum(case when month(created) = 12 then 1 end)), 0) "Dec"
    FROM zendesk_ticket
    WHERE org_id_id = """ + org_id + """
    AND created >= DATE_FORMAT(NOW() ,'%Y-01-01')
    union
    SELECT "Closed" Type
      ,ifnull(ROUND(sum(case when month(updated) = 1 then 1 end)), 0) Jan
      ,ifnull(ROUND(sum(case when month(updated) = 2 then 1 end)), 0) Feb
      ,ifnull(ROUND(sum(case when month(updated) = 3 then 1 end)), 0) Mar
      ,ifnull(ROUND(sum(case when month(updated) = 4 then 1 end)), 0) Apr
      ,ifnull(ROUND(sum(case when month(updated) = 5 then 1 end)), 0) May
      ,ifnull(ROUND(sum(case when month(updated) = 6 then 1 end)), 0) June
      ,ifnull(ROUND(sum(case when month(updated) = 7 then 1 end)), 0) July
      ,ifnull(ROUND(sum(case when month(updated) = 8 then 1 end)), 0) Aug
      ,ifnull(ROUND(sum(case when month(updated) = 9 then 1 end)), 0) Sep
      ,ifnull(ROUND(sum(case when month(updated) = 10 then 1 end)), 0) Oct
      ,ifnull(ROUND(sum(case when month(updated) = 11 then 1 end)), 0) Nov
      ,ifnull(ROUND(sum(case when month(updated) = 12 then 1 end)), 0) "Dec"
    FROM zendesk_ticket
    WHERE org_id_id = """ + org_id + """
    AND status in ('closed', 'solved')
    AND updated >= DATE_FORMAT(NOW() ,'%Y-01-01')
    """
    return run_query(sql, True)


def extract_priority_tickets_for_year(org_id):
    sql = """
    SELECT priority "Type"
      ,ifnull(ROUND(sum(case when month(created) = 1 then 1 end)), 0) Jan
      ,ifnull(ROUND(sum(case when month(created) = 2 then 1 end)), 0) Feb
      ,ifnull(ROUND(sum(case when month(created) = 3 then 1 end)), 0) Mar
      ,ifnull(ROUND(sum(case when month(created) = 4 then 1 end)), 0) Apr
      ,ifnull(ROUND(sum(case when month(created) = 5 then 1 end)), 0) May
      ,ifnull(ROUND(sum(case when month(created) = 6 then 1 end)), 0) June
      ,ifnull(ROUND(sum(case when month(created) = 7 then 1 end)), 0) July
      ,ifnull(ROUND(sum(case when month(created) = 8 then 1 end)), 0) Aug
      ,ifnull(ROUND(sum(case when month(created) = 9 then 1 end)), 0) Sep
      ,ifnull(ROUND(sum(case when month(created) = 10 then 1 end)), 0) Oct
      ,ifnull(ROUND(sum(case when month(created) = 11 then 1 end)), 0) Nov
      ,ifnull(ROUND(sum(case when month(created) = 12 then 1 end)), 0) "Dec"
    FROM zendesk_ticket
    WHERE org_id_id = """ + org_id + """
    AND created >= DATE_FORMAT(NOW() ,'%Y-01-01')
    GROUP BY 1
    """
    return run_query(sql, True)


def extract_ticket_by_version(org_id, from_date, end_date):
    sql = """
    SELECT 
        CASE
            WHEN product_version LIKE 'to_be_filled_%' THEN 'unknown'
            ELSE product_version
        END label,
        COUNT(*) total
    FROM
        zendesk_ticket
    WHERE
        org_id_id = """ + org_id + """
    AND created >= '""" + from_date + """'
    AND created <= '""" + end_date + """'
    GROUP BY 1
    """
    return run_query(sql)


def extract_ticket_by_environment(org_id, from_date, end_date):
    sql = """
    SELECT 
        CASE
            WHEN environment LIKE 'instance_%' THEN substr(environment,10)
            WHEN environment LIKE 'to_be_filled_%' THEN 'Unknown'
            ELSE environment
        END label,
        COUNT(*) total
    FROM
        zendesk_ticket
    WHERE
        org_id_id = """ + org_id + """
    AND created >= '""" + from_date + """'
    AND created <= '""" + end_date + """'
    GROUP BY 1
    """
    return run_query(sql)


def extract_ticket_by_kb(org_id, from_date, end_date):
    sql = """
        SELECT 
        CASE
            WHEN kb='kb_n_a' THEN 'Not Applicable'
            WHEN kb='kb_doc_exists' THEN 'Doc Exists'
            WHEN kb='kb_needed' THEN 'Doc Needed'
            WHEN kb='kb_exists' THEN 'Doc Exists'
            WHEN kb LIKE 'to_be_filled_%' THEN 'Unknown'
            ELSE kb
        END label,
        COUNT(*) total
    FROM
       zendesk_ticket
    WHERE
        org_id_id = """ + org_id + """
    AND created >= '""" + from_date + """'
    AND created <= '""" + end_date + """'
    GROUP BY 1
    """
    return run_query(sql)
