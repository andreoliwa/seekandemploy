# coding=utf-8
"""
Core classes that should be imported and extended by other crawling modules.
"""


class JobOffer:
    """
    A job offer posted in a website.
    """
    def __init__(self):
        pass

    def save(self):
        """
        Save a job offer in the database.
        """
        pass


class JobSite:
    """
    A website with job offers.
    """
    def __init__(self):
        pass

    def crawl(self):
        """
        Crawl the website, extracting job offers.
        This method must NOT be overridden by the inherited class.
        """
        self.search()
        while True:
            for link in self.parse_links():
                self.parse_offers(link)

            for offer in self.parse_offers():
                offer.save()

            if not self.has_next_page():
                break

            self.fetch_next_page()

    def search(self):
        """
        Search a URL in the website.
        This method MUST be overridden by the inherited class.
        """
        pass

    def parse_links(self):
        """
        Parse the search results looking for job links.
        This method MUST be overridden by the inherited class.
        """
        return []

    def has_next_page(self):
        """
        Return True if the search results has yet another page to be parsed.
        This method MUST be overridden by the inherited class.
        """
        return False

    def parse_offers(self, link=''):
        """
        Parse the search results looking for job offers. Some sites display
        job offers after a search, instead of paginated search results.
        This method MUST be overridden by the inherited class.
        """
        return []

    def fetch_next_page(self):
        pass


def main():
    job = JobSite()
    job.crawl()

if __name__ == '__main__':
    main()
