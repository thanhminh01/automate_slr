class Dokument:
    def __init__(self, DOI, raw_data):
        self.DOI = DOI
        self.raw_data = raw_data
        self.token_count = ""
        # For bias
        self.rob_sqa = ""
        self.rob = ""
        self.rob2_sqa = ""
        self.rob2 = ""
        # For synthesis
        self.eligibility =""
        self.codes = ""
        self.themes = ""
