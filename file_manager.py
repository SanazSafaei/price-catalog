
class FileManager():
    """converting csv files to dict objects, using first-line as keys."""

    def __init__(self, address: str) -> None:
        """opening file and get the first line to define columns."""

        self.file = open(address, 'r', encoding="utf-8")
        self.generate_headline()

    def get_row_data(self) -> dict | None:
        """reading each line of file and convert it to dict."""
        row = self.file.readline()  #skip \n character
        if '\n' in row:
            row = row[:-1]  #skip \n character

        if row == '':
            self.file.close()
            return None
        row = row.split(';')
        data_object = {}
        for headline, data in zip(self.headlines, row):
            data_object[headline] = data

        return data_object

    def get_all_data(self) -> list: # is it needed?
        """returns a list of objects from file's data."""

        data = []

        while row := self.get_row_data():
            data.append(row)

        return row

    def generate_headline(self) -> None:
        """generating dict's keys from the first line of fifle."""
        first_line = self.file.readline()
        if '\n' in first_line:
            first_line = first_line[:-1]  #skip \n character

        if first_line == '':
            self.file.close()
            self.headlines = None
            return

        self.headlines = first_line.split(';')

