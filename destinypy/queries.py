class PagedQuery():

    def __init__(self,
        itemsPerPage: int,
        currentPage: int,
        requestContinuationToken: str
    ):
        self.itemsPerPage = itemsPerPage
        self.currentPage = currentPage
        self.requestContinuationToken = requestContinuationToken