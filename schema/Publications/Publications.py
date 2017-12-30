import jsl, json, requests

# Create a Manifest Class
class Publications(jsl.Document):
    class Options(object):
        additional_properties = True
    class init(jsl.Document):
        init = jsl.StringField()        
    # Manifest properties
    init = jsl.DocumentField(init, as_ref=True, required=True)
    countries = ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BV", "BR", "IO", "BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES", "LK", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN", "VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]
    languages = ["aar", "abk", "ace", "ach", "ada", "ady", "afa", "afh", "afr", "ain", "aka", "akk", "alb (B)", "sqi (T)", "ale", "alg", "alt", "amh", "ang", "anp", "apa", "ara", "arc", "arg", "arm (B)", "hye (T)", "arn", "arp", "art", "arw", "asm", "ast", "ath", "aus", "ava", "ave", "awa", "aym", "aze", "bad", "bai", "bak", "bal", "bam", "ban", "baq (B)", "eus (T)", "bas", "bat", "bej", "bel", "bem", "ben", "ber", "bho", "bih", "bik", "bin", "bis", "bla", "bnt", "tib (B)", "bod (T)", "bos", "bra", "bre", "btk", "bua", "bug", "bul", "bur (B)", "mya (T)", "byn", "cad", "cai", "car", "cat", "cau", "ceb", "cel", "cze (B)", "ces (T)", "cha", "chb", "che", "chg", "chi (B)", "zho (T)", "chk", "chm", "chn", "cho", "chp", "chr", "chu", "chv", "chy", "cmc", "cnr", "cop", "cor", "cos", "cpe", "cpf", "cpp", "cre", "crh", "crp", "csb", "cus", "wel (B)", "cym (T)", "dak", "dan", "dar", "day", "del", "den", "ger (B)", "deu (T)", "dgr", "din", "div", "doi", "dra", "dsb", "dua", "dum", "dut (B)", "nld (T)", "dyu", "dzo", "efi", "egy", "eka", "gre (B)", "ell (T)", "elx", "eng", "enm", "epo", "est", "ewe", "ewo", "fan", "fao", "per (B)", "fas (T)", "fat", "fij", "fil", "fin", "fiu", "fon", "fre (B)", "fra (T)", "frm", "fro", "frr", "frs", "fry", "ful", "fur", "gaa", "gay", "gba", "gem", "geo (B)", "kat (T)", "gez", "gil", "gla", "gle", "glg", "glv", "gmh", "goh", "gon", "gor", "got", "grb", "grc", "grn", "gsw", "guj", "gwi", "hai", "hat", "hau", "haw", "heb", "her", "hil", "him", "hin", "hit", "hmn", "hmo", "hrv", "hsb", "hun", "hup", "iba", "ibo", "ice (B)", "isl (T)", "ido", "iii", "ijo", "iku", "ile", "ilo", "ina", "inc", "ind", "ine", "inh", "ipk", "ira", "iro", "ita", "jav", "jbo", "jpn", "jpr", "jrb", "kaa", "kab", "kac", "kal", "kam", "kan", "kar", "kas", "kau", "kaw", "kaz", "kbd", "kha", "khi", "khm", "kho", "kik", "kin", "kir", "kmb", "kok", "kom", "kon", "kor", "kos", "kpe", "krc", "krl", "kro", "kru", "kua", "kum", "kur", "kut", "lad", "lah", "lam", "lao", "lat", "lav", "lez", "lim", "lin", "lit", "lol", "loz", "ltz", "lua", "lub", "lug", "lui", "lun", "luo", "lus", "mac (B)", "mkd (T)", "mad", "mag", "mah", "mai", "mak", "mal", "man", "mao (B)", "mri (T)", "map", "mar", "mas", "may (B)", "msa (T)", "mdf", "mdr", "men", "mga", "mic", "min", "mis", "mkh", "mlg", "mlt", "mnc", "mni", "mno", "moh", "mon", "mos", "mul", "mun", "mus", "mwl", "mwr", "myn", "myv", "nah", "nai", "nap", "nau", "nav", "nbl", "nde", "ndo", "nds", "nep", "new", "nia", "nic", "niu", "nno", "nob", "nog", "non", "nor", "nqo", "nso", "nub", "nwc", "nya", "nym", "nyn", "nyo", "nzi", "oci", "oji", "ori", "orm", "osa", "oss", "ota", "oto", "paa", "pag", "pal", "pam", "pan", "pap", "pau", "peo", "phi", "phn", "pli", "pol", "pon", "por", "pra", "pro", "pus", "qaa-qtz", "que", "raj", "rap", "rar", "roa", "roh", "rom", "rum (B)", "ron (T)", "run", "rup", "rus", "sad", "sag", "sah", "sai", "sal", "sam", "san", "sas", "sat", "scn", "sco", "sel", "sem", "sga", "sgn", "shn", "sid", "sin", "sio", "sit", "sla", "slo (B)", "slk (T)", "slv", "sma", "sme", "smi", "smj", "smn", "smo", "sms", "sna", "snd", "snk", "sog", "som", "son", "sot", "spa", "srd", "srn", "srp", "srr", "ssa", "ssw", "suk", "sun", "sus", "sux", "swa", "swe", "syc", "syr", "tah", "tai", "tam", "tat", "tel", "tem", "ter", "tet", "tgk", "tgl", "tha", "tig", "tir", "tiv", "tkl", "tlh", "tli", "tmh", "tog", "ton", "tpi", "tsi", "tsn", "tso", "tuk", "tum", "tup", "tur", "tut", "tvl", "twi", "tyv", "udm", "uga", "uig", "ukr", "umb", "und", "urd", "uzb", "vai", "ven", "vie", "vol", "vot", "wak", "wal", "war", "was", "wen", "wln", "wol", "xal", "xho", "yao", "yap", "yid", "yor", "ypk", "zap", "zbl", "zen", "zgh", "zha", "znd", "zul", "zun", "zxx", "zza"]
    authors = jsl.ArrayField()
    contentType = jsl.StringField()
    country = jsl.StringField(enum=countries)
    edition = jsl.StringField()
    language = jsl.StringField(enum=languages)
    publication = jsl.StringField()
    publisher = jsl.StringField()

# Add the global properties to the definitions
def add_global(manifest):
    url = 'https://raw.githubusercontent.com/whatevery1says/manifest/master/schema/global/global.json'
    manifest['definitions'] = json.loads(requests.get(url).text)
    del manifest['properties']['init']
    return manifest

# Add the requirements, global and manifest-specific
def add_requirements(manifest):
    manifest['required'] = ['_id', 'namespace', 'path'] # Global
    manifest['required'] = manifest['required'] + ['date', 'publication', 'publisher']
    return manifest

# Set manifest-specific definitions
def set_manifest_definitions(manifest):
#     manifest['definitions'][''][''] = ''
    return manifest

# Get the manifest as a dict
def get_manifest(schema):
    schema = json.dumps(schema, indent=4).replace('__main__.', '')
    schema = json.loads(schema)
    return schema

# Build the manifest
def build_manifest(schema):
    manifest = get_manifest(schema)
    manifest = add_global(manifest)
    manifest = add_requirements(manifest)
    manifest = set_manifest_definitions(manifest)
    return manifest

manifest = build_manifest(Publications.get_schema(ordered=True))
print(json.dumps(manifest, indent=4))
