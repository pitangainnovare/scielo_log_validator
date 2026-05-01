PATTERN_Y_M_D = r'\d{4}-\d{2}-\d{2}'

PATTERN_YMD = r'\d{4}\d{2}\d{2}'

PATTERN_PAPERBOY = r'^\d{4}-\d{2}-\d{2}[\w|\.]*\.log\.gz$'

# https://github.com/matomo-org/matomo-log-analytics/blob/4.x-dev/import_logs.py
PATTERN_COMMON_LOG_FORMAT = (
    r'(?P<ip>[\w*.:-]+)\s+\S+\s+(?P<userid>\S+)\s+\[(?P<date>.*[^\-\+\s])\s*(?P<timezone>[+-]?\d{4})\]\s+'
    r'"(?P<method>\S+)\s+(?P<path>.*?)\s+\S+"\s+(?P<status>\d+)\s+(?P<length>\S+)'
)

PATTERN_COMMON_LOG_FORMAT_WITH_IP_LIST = (
    r'(?P<ip>[\w*.:-]+)\s(?P<ip_list>[\w*.:,\s-]+)\s+(?P<userid>\S+)\s+\[(?P<date>.*[^\-\+\s])\s*(?P<timezone>[+-]?\d{4})\]\s+'
    r'"(?P<method>\S+)\s+(?P<path>.*?)\s+\S+\"\s+(?P<status>\d+)\s+(?P<length>\S+)'
)

# https://github.com/matomo-org/matomo-log-analytics/blob/4.x-dev/import_logs.py
PATTERN_NCSA_EXTENDED_LOG_FORMAT = (
    PATTERN_COMMON_LOG_FORMAT + r'\s+"(?P<referrer>.*?)"\s+"(?P<user_agent>.*?)"'
)

PATTERN_NCSA_EXTENDED_LOG_FORMAT_WITH_IP_LIST = (
    PATTERN_COMMON_LOG_FORMAT_WITH_IP_LIST + r'\s+"(?P<referrer>.*?)"\s+"(?P<user_agent>.*?)"'
)

# Pattern designed to capture rows that begin with the domain name
PATTERN_NCSA_EXTENDED_LOG_FORMAT_DOMAIN = (
    r'(?P<domain>.*?)\s' + PATTERN_COMMON_LOG_FORMAT + r'\s+"(?P<referrer>.*?)"\s+"(?P<user_agent>.*?)"'
)

PATTERN_NCSA_EXTENDED_LOG_FORMAT_DOMAIN_WITH_IP_LIST = (
    r'(?P<domain>.*?)\s' + PATTERN_COMMON_LOG_FORMAT_WITH_IP_LIST + r'\s+"(?P<referrer>.*?)"\s+"(?P<user_agent>.*?)"'
)

PATTERN_BUNNYCDN_LOG_FORMAT = (
    r'^(?P<cache>HIT|MISS|BYPASS|EXPIRED|STALE)\|'
    r'(?P<status>\d{3})\|'
    r'(?P<unix_ts>\d{7}|\d{10})\|'
    r'(?P<length>\d+)\|'
    r'(?P<zone>\d+)\|'
    r'(?P<ip>[a-fA-F0-9:.]+)\|'
    r'(?P<referrer>[^|]*)\|'
    r'(?P<path>[^|]+)\|'
    r'(?P<country>[A-Z0-9]{2,3})\|'
    r'(?P<user_agent>[^|]*)\|'
    r'(?P<request_id>[a-f0-9]{32})\|'
    r'(?P<iq>[A-Z]{2})'
    r'(?:\|(?P<shield_status>[^|]+))?$'
)