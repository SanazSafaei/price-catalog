
class FileManager():

    def __init__(self, address: str) -> None:
        self.file = open(address, 'r')
        self.generate_headline()

    def get_row_data(self) -> dict:
        row = self.file.readline()[:-1] #skip \n character
        if(row == ''):
            self.file.close()
            return {}
        row = row.split(';')
        data_object = {}
        for headline,data in zip(self.headlines, row):
            data_object[headline] = data

        return data_object
    

    def generate_headline(self) -> None:
        first_line = self.file.readline()[:-1] #skip \n character

        if(first_line == ''):
            self.file.close()
            self.headlines = None
            return

        self.headlines = first_line.split(';')

