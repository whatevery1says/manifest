import jsl, json

# Publications Object
class Publications(jsl.Document):

    class Options(object):
        additional_properties = True            
    
    # Global Properties
    class _id(jsl.Document):
        _id = jsl.StringField(pattern='[a-zA-Z-_]+', required=True)

    class namespace(jsl.Document):
        namespace = jsl.StringField(default='we1sv1.1', required=True)

    class path(jsl.Document):
        path = jsl.StringField(pattern='^,[a-zA-Z-_,]+,$', required=True)

    class description(jsl.Document):
        description = jsl.StringField()

    class notes(jsl.Document):
        class note(jsl.Document):
            note = jsl.StringField()
        notes = jsl.ArrayField(jsl.DocumentField(note, as_ref=True), 
                required=True)

    class date(jsl.Document):
        class daterange(jsl.Document):
            start = jsl.StringField(pattern='DATEFORMAT', required=True)
            end = jsl.StringField(pattern='DATEFORMAT')
        class precisedaterange(jsl.Document):
            start = jsl.DateTimeField(required=True)
            end = jsl.DateTimeField(required=True)
        class normal(jsl.Document):
            normal = jsl.ArrayField(jsl.OneOfField([
                jsl.StringField(pattern='DATEFORMAT'),
                jsl.DocumentField(daterange, as_ref=True)
            ]), required=True)
        class precise(jsl.Document):
            precise = jsl.ArrayField(jsl.OneOfField([
                jsl.DateTimeField(),
                jsl.DocumentField(precisedaterange, as_ref=True)
            ]), required=True)
        options = [
            jsl.StringField(pattern='DATEFORMAT'),
            jsl.DateTimeField(),
            jsl.DocumentField(daterange, as_ref=True),
            jsl.DocumentField(precisedaterange, as_ref=True),
            jsl.DocumentField(normal, as_ref=True),
            jsl.DocumentField(precise, as_ref=True)
        ]

        date = jsl.ArrayField(jsl.OneOfField(options), required=True)

    class group(jsl.Document):
        group = jsl.StringField()

    class label(jsl.Document):
        label = jsl.StringField()

    class title(jsl.Document):
        title = jsl.StringField()

    class altTitle(jsl.Document):
        altTitle = jsl.StringField()

    class refLocation(jsl.Document):
        refLocation = jsl.StringField()

    # Publications Properties
    class authors(jsl.Document):
        options = [
            jsl.StringField(),
            jsl.DocumentField(group, as_ref=True)
        ]
        authors = jsl.ArrayField(jsl.OneOfField(options))

    countries = ['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW']
    languages = ['aar', 'abk', 'ace', 'ach', 'ada', 'ady', 'afa', 'afh', 'afr', 'ain', 'aka', 'akk', 'alb (B)', 'sqi (T)', 'ale', 'alg', 'alt', 'amh', 'ang', 'anp', 'apa', 'ara', 'arc', 'arg', 'arm (B)', 'hye (T)', 'arn', 'arp', 'art', 'arw', 'asm', 'ast', 'ath', 'aus', 'ava', 'ave', 'awa', 'aym', 'aze', 'bad', 'bai', 'bak', 'bal', 'bam', 'ban', 'baq (B)', 'eus (T)', 'bas', 'bat', 'bej', 'bel', 'bem', 'ben', 'ber', 'bho', 'bih', 'bik', 'bin', 'bis', 'bla', 'bnt', 'tib (B)', 'bod (T)', 'bos', 'bra', 'bre', 'btk', 'bua', 'bug', 'bul', 'bur (B)', 'mya (T)', 'byn', 'cad', 'cai', 'car', 'cat', 'cau', 'ceb', 'cel', 'cze (B)', 'ces (T)', 'cha', 'chb', 'che', 'chg', 'chi (B)', 'zho (T)', 'chk', 'chm', 'chn', 'cho', 'chp', 'chr', 'chu', 'chv', 'chy', 'cmc', 'cnr', 'cop', 'cor', 'cos', 'cpe', 'cpf', 'cpp', 'cre', 'crh', 'crp', 'csb', 'cus', 'wel (B)', 'cym (T)', 'cze (B)', 'ces (T)', 'dak', 'dan', 'dar', 'day', 'del', 'den', 'ger (B)', 'deu (T)', 'dgr', 'din', 'div', 'doi', 'dra', 'dsb', 'dua', 'dum', 'dut (B)', 'nld (T)', 'dyu', 'dzo', 'efi', 'egy', 'eka', 'gre (B)', 'ell (T)', 'elx', 'eng', 'enm', 'epo', 'est', 'baq (B)', 'eus (T)', 'ewe', 'ewo', 'fan', 'fao', 'per (B)', 'fas (T)', 'fat', 'fij', 'fil', 'fin', 'fiu', 'fon', 'fre (B)', 'fra (T)', 'fre (B)', 'fra (T)', 'frm', 'fro', 'frr', 'frs', 'fry', 'ful', 'fur', 'gaa', 'gay', 'gba', 'gem', 'geo (B)', 'kat (T)', 'ger (B)', 'deu (T)', 'gez', 'gil', 'gla', 'gle', 'glg', 'glv', 'gmh', 'goh', 'gon', 'gor', 'got', 'grb', 'grc', 'gre (B)', 'ell (T)', 'grn', 'gsw', 'guj', 'gwi', 'hai', 'hat', 'hau', 'haw', 'heb', 'her', 'hil', 'him', 'hin', 'hit', 'hmn', 'hmo', 'hrv', 'hsb', 'hun', 'hup', 'arm (B)', 'hye (T)', 'iba', 'ibo', 'ice (B)', 'isl (T)', 'ido', 'iii', 'ijo', 'iku', 'ile', 'ilo', 'ina', 'inc', 'ind', 'ine', 'inh', 'ipk', 'ira', 'iro', 'ice (B)', 'isl (T)', 'ita', 'jav', 'jbo', 'jpn', 'jpr', 'jrb', 'kaa', 'kab', 'kac', 'kal', 'kam', 'kan', 'kar', 'kas', 'geo (B)', 'kat (T)', 'kau', 'kaw', 'kaz', 'kbd', 'kha', 'khi', 'khm', 'kho', 'kik', 'kin', 'kir', 'kmb', 'kok', 'kom', 'kon', 'kor', 'kos', 'kpe', 'krc', 'krl', 'kro', 'kru', 'kua', 'kum', 'kur', 'kut', 'lad', 'lah', 'lam', 'lao', 'lat', 'lav', 'lez', 'lim', 'lin', 'lit', 'lol', 'loz', 'ltz', 'lua', 'lub', 'lug', 'lui', 'lun', 'luo', 'lus', 'mac (B)', 'mkd (T)', 'mad', 'mag', 'mah', 'mai', 'mak', 'mal', 'man', 'mao (B)', 'mri (T)', 'map', 'mar', 'mas', 'may (B)', 'msa (T)', 'mdf', 'mdr', 'men', 'mga', 'mic', 'min', 'mis', 'mac (B)', 'mkd (T)', 'mkh', 'mlg', 'mlt', 'mnc', 'mni', 'mno', 'moh', 'mon', 'mos', 'mao (B)', 'mri (T)', 'may (B)', 'msa (T)', 'mul', 'mun', 'mus', 'mwl', 'mwr', 'bur (B)', 'mya (T)', 'myn', 'myv', 'nah', 'nai', 'nap', 'nau', 'nav', 'nbl', 'nde', 'ndo', 'nds', 'nep', 'new', 'nia', 'nic', 'niu', 'dut (B)', 'nld (T)', 'nno', 'nob', 'nog', 'non', 'nor', 'nqo', 'nso', 'nub', 'nwc', 'nya', 'nym', 'nyn', 'nyo', 'nzi', 'oci', 'oji', 'ori', 'orm', 'osa', 'oss', 'ota', 'oto', 'paa', 'pag', 'pal', 'pam', 'pan', 'pap', 'pau', 'peo', 'per (B)', 'fas (T)', 'phi', 'phn', 'pli', 'pol', 'pon', 'por', 'pra', 'pro', 'pus', 'qaa-qtz', 'que', 'raj', 'rap', 'rar', 'roa', 'roh', 'rom', 'rum (B)', 'ron (T)', 'rum (B)', 'ron (T)', 'run', 'rup', 'rus', 'sad', 'sag', 'sah', 'sai', 'sal', 'sam', 'san', 'sas', 'sat', 'scn', 'sco', 'sel', 'sem', 'sga', 'sgn', 'shn', 'sid', 'sin', 'sio', 'sit', 'sla', 'slo (B)', 'slk (T)', 'slo (B)', 'slk (T)', 'slv', 'sma', 'sme', 'smi', 'smj', 'smn', 'smo', 'sms', 'sna', 'snd', 'snk', 'sog', 'som', 'son', 'sot', 'spa', 'alb (B)', 'sqi (T)', 'srd', 'srn', 'srp', 'srr', 'ssa', 'ssw', 'suk', 'sun', 'sus', 'sux', 'swa', 'swe', 'syc', 'syr', 'tah', 'tai', 'tam', 'tat', 'tel', 'tem', 'ter', 'tet', 'tgk', 'tgl', 'tha', 'tib (B)', 'bod (T)', 'tig', 'tir', 'tiv', 'tkl', 'tlh', 'tli', 'tmh', 'tog', 'ton', 'tpi', 'tsi', 'tsn', 'tso', 'tuk', 'tum', 'tup', 'tur', 'tut', 'tvl', 'twi', 'tyv', 'udm', 'uga', 'uig', 'ukr', 'umb', 'und', 'urd', 'uzb', 'vai', 'ven', 'vie', 'vol', 'vot', 'wak', 'wal', 'war', 'was', 'wel (B)', 'cym (T)', 'wen', 'wln', 'wol', 'xal', 'xho', 'yao', 'yap', 'yid', 'yor', 'ypk', 'zap', 'zbl', 'zen', 'zgh', 'zha', 'chi (B)', 'zho (T)', 'znd', 'zul', 'zun', 'zxx', 'zza']
    
    # Instantiate all Publications properties
    _id = jsl.DocumentField(_id, as_ref=True, required=True)
    namespace = jsl.DocumentField(namespace, as_ref=True, required=True)
    path = jsl.DocumentField(path, as_ref=True, required=True)
    description = jsl.DocumentField(description, as_ref=True, required=True)
    date = jsl.DocumentField(date, as_ref=True, required=True)
    publication = jsl.StringField(required=True)
    publisher = jsl.StringField(required=True)
    group = jsl.DocumentField(group, as_ref=True)
    label = jsl.DocumentField(label, as_ref=True)
    title = jsl.DocumentField(title, as_ref=True)
    altTitle = jsl.DocumentField(altTitle, as_ref=True)
    refLocation = jsl.DocumentField(refLocation, as_ref=True)
    edition = jsl.StringField()
    contentType = jsl.StringField()
    language = jsl.StringField(enum=countries)
    country = jsl.StringField(enum=countries)
    authors = jsl.ArrayField()
    notes = jsl.DocumentField(notes, as_ref=True)

def get_manifest(schema):
    # Convert ordered dict to json
    manifest = json.dumps(schema, indent=4)
    # Clean up Python artefacts from JSL
    manifest = manifest.replace('__main__.', '')
    # jsonschema validator does not accept lower case booleans
    # This needs to be improved so there are no false positives
    manifest = manifest.replace(': false', ': False')
    manifest = manifest.replace(': true', ': True')
    # Workaround because JSL cannot generate date formats, only datetime
    manifest = manifest.replace('"pattern": "DATEFORMAT"', '"format": "date"')
    return manifest
    
schema = Publications.get_schema(ordered=True)
manifest = get_manifest(schema)
print(manifest)
