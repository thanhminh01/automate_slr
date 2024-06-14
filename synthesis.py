class Synthesis:
    def __init__(self, topic, eligible_documents=None):
        if eligible_documents is None:
            eligible_documents = []
        self.topic = topic
        self.eligible_documents = eligible_documents
        self.synthesis_result = None

    def add_eligible_document(self, document):
        self.eligible_documents.append(document)