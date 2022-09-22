import math


def parser(data: list) -> list:
    str_data = []
    for row in data:
        if isinstance(row, int):
            str_data.append(str(row))
        elif isinstance(row, (tuple, list)):
            row_list = []
            counter = 0
            for r in row:
                row_list.insert(counter, str(r))
                counter += 1
            str_data.append(row_list)
        elif isinstance(row, dict):
            row_list = []
            counter = 0
            for key in sorted(row.keys()):
                row_list.insert(counter, str(row[key]))
                counter += 1
            str_data.append(row_list)
        elif isinstance(row, str):
            str_data.append(row)
        else:
            print(f"Unsupported type {type(row)}")
    return str_data


def prettytable(data: list, table_info: str, cell_sep: str = '  |  ', header_separator=True):
    rows = len(data)
    cols = len(data[0])

    col_width = []
    for col in range(cols):
        columns = [data[row][col] for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    separator = "--+--".join('-' * n for n in col_width)

    centre = math.ceil(len(col_width) / 2)
    print(">" * sum(col_width[:centre]) + table_info + "<" * sum(col_width[centre:]) + "\n")
    for i, row in enumerate(range(rows)):
        if i == 1 and header_separator:
            print(separator)

        result = []
        for col in range(cols):
            item = data[row][col].rjust(col_width[col])
            result.append(item)

        print(cell_sep.join(result))

    print("\n\n")
