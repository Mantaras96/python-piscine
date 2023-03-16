class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if not filename:
            raise ValueError("No filename given")
        if header not in [True, False]:
            raise ValueError("Header must be True or False")
        if not isinstance(skip_top, int) or skip_top < 0:
            raise ValueError("skip_top must be a positive integer")
        if not isinstance(skip_bottom, int) or skip_bottom < 0:
            raise ValueError("skip_bottom must be a positive integer")
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.full_data = []
        self.file = None


    def __enter__(self):
        self.file_obj = open(self.filename, mode="r", encoding="utf-8")
        for line in self.file_obj:
            self.full_data.append(list(map(str.strip, line.split(self.sep))))
        if all(len(elem) == len(self.full_data[0]) for elem in self.full_data):
            return self
        else:
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.full_data = []
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        start = self.skip_top
        end = len(self.full_data) - self.skip_bottom
        if self.header:
            return self.full_data[ start + 1 : end ]
        else:
            return self.full_data[ start : end ]
        
    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if not self.header:
            return None
        else:
            return self.full_data[0]