import csv
import sys


def is_url_string(url_string):
    return url_string.startswith("http://") or url_string.startswith("https://")


def convert_url_string_to_markdonw_link(url_string):
    if not is_url_string(url_string):
        return url_string
    link_text = url_string[url_string.find("://") + 3 : -1]
    link_text = (
        url_string[url_string.find("www") + 4 : -1] if "www" in link_text else link_text
    )
    index = link_text.find("/")
    link_text = link_text[:index] if index != -1 else link_text
    return f"[{link_text}]({url_string})"


def convert_csv_to_markdown_table(csv_file_path):
    markdown_table = ""
    with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        # Create the header row
        print(headers)
        markdown_table += "| " + " | ".join(headers) + " |\n"
        # Create the separator row
        markdown_table += "|---" * len(headers) + "|\n"
        # Create each data row
        for row in csv_reader:
            row = map(convert_url_string_to_markdonw_link, row)
            markdown_table += "| " + " | ".join(row) + " |\n"
    return markdown_table


def save_table_to_file(markdown_table, file_path):
    with open(file_path, "w") as file:
        file.write(markdown_table)


if __name__ == "__main__":
    args = sys.argv[1:]
    csv_file_path = args[0]
    output_file_path = args[1]
    markdown_table = convert_csv_to_markdown_table(csv_file_path)
    save_table_to_file(markdown_table, output_file_path)
