from elasticsearch import AsyncElasticsearch, Elasticsearch

from infrastructure.config.app import APP_OPTIONS

frame_index_alias = "frames"

es = Elasticsearch(
    hosts=APP_OPTIONS.elasticsearch_options.hosts,
    sniff_on_start=APP_OPTIONS.elasticsearch_options.sniff_on_start,
    sniff_on_connection_fail=APP_OPTIONS.elasticsearch_options.sniff_on_connection_fail,
    snifffer_timeout=APP_OPTIONS.elasticsearch_options.sniff_timeout_in_sec,
    sniff_timeout=10,
    http_compress=APP_OPTIONS.elasticsearch_options.http_compress
)


asyncElasticClient = AsyncElasticsearch(
    hosts=APP_OPTIONS.elasticsearch_options.hosts,
    sniff_on_start=APP_OPTIONS.elasticsearch_options.sniff_on_start,
    sniff_on_connection_fail=APP_OPTIONS.elasticsearch_options.sniff_on_connection_fail,
    snifffer_timeout=APP_OPTIONS.elasticsearch_options.sniff_timeout_in_sec,
    sniff_timeout=10,
    http_compress=APP_OPTIONS.elasticsearch_options.http_compress
)