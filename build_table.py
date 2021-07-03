from terminaltables import AsciiTable


def build_table(table_headers, table_strings, results_count, table_title):
    table_content = (table_headers,)
    for table_string in table_strings[:results_count]:
        table_content = table_content + (table_string,)
    table = AsciiTable(table_content, table_title)
    table.inner_row_border = True
    table.justify_columns[2] = "right"
    return table.table
