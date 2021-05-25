class ElasticSearchOptions(object):
    def __init__(
            self,
            hosts=None,
            sniff_on_start: bool = True,
            sniff_on_connection_fail: bool = True,
            http_compress: bool = True,
            sniff_timeout_in_sec: int = 60
    ):
        if hosts is None:
            hosts = ["http://localhost:9200"]
        self.hosts = hosts
        self.sniff_on_start = sniff_on_start
        self.sniff_on_connection_fail = sniff_on_connection_fail
        self.http_compress = http_compress
        self.sniff_timeout_in_sec = sniff_timeout_in_sec


class AppOptions(object):
    def __init__(self):
        self.project_name = "similarity-api"
        self.elasticsearch_options = ElasticSearchOptions(hosts=["http://localhost:9200"])


APP_OPTIONS = AppOptions()