class Synthesis:
    # For storing research topic and eligible documents of the research topic for synthesis
    def __init__(self, topic, eligible_documents=None):
        if eligible_documents is None:
            eligible_documents = []
        self.topic = topic
        self.eligible_documents = eligible_documents
        self.themes = None

    def add_eligible_document(self, document):
        self.eligible_documents.append(document)