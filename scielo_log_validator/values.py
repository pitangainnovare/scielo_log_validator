COLLECTION_FILE_NAME_IDENTIFIERS = {
    '_scielo.ar': 'arg',
    '_scielo.bo': 'bol',
    '_scielo.1.br': 'scl',
    '_scielo.2.br': 'scl',
    '_scielo.cl': 'chl',
    '_scielo.co': 'col',
    '_scielo.cr': 'cru',
    '_scielo.cu': 'cub',
    '_scielo.ec': 'ecu',
    '_scielo.mx': 'mex',
    '_scielo.py': 'pry',
    '_scielo.pe': 'per',
    '_scielo.pt': 'prt',
    '_scielo.sp.1': 'ssp',
    '_scielo.sp.2': 'ssp',
    '_scielo.za': 'sza',
    '_scielo.es': 'esp',
    '_scielo.uy': 'ury',
    '_scielo.ven': 'ven',
    '_caribbean.scielo.org.1': 'wid',
    '_caribbean.scielo.org.2': 'wid',
    '_scielo.data': 'dat',
    '_scielo.preprints': 'pre',
    '_scielo.pepsic': 'psi',
    '_scielo.revenf': 'rev',
    '_scielo.ss': 'sss',
}

PATTERN_Y_M_D = r'\d{4}-\d{2}-\d{2}'

PATTERN_YMD = r'\d{4}\d{2}\d{2}'

PATTERN_PAPERBOY = r'^\d{4}-\d{2}-\d{2}[\w|\.]*\.log\.gz$'

# https://github.com/matomo-org/matomo-log-analytics/blob/4.x-dev/import_logs.py
PATTERN_COMMON_LOG_FORMAT = (
    r'(?P<ip>[\w*.:-]+)\s+\S+\s+(?P<userid>\S+)\s+\[(?P<date>.*?)\s+(?P<timezone>.*?)\]\s+'
    r'"(?P<method>\S+)\s+(?P<path>.*?)\s+\S+"\s+(?P<status>\d+)\s+(?P<length>\S+)'
)

PATTERN_COMMON_LOG_FORMAT_WITH_IP_LIST = (
    r'(?P<ip>[\w*.:-]+)\s(?P<ip_list>[\w*.:,\s-]+)\s+(?P<userid>\S+)\s+\[(?P<date>.*?)\s+(?P<timezone>.*?)\]\s+'
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
