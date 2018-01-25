"""Provides all the generic data related to the address."""

COUNTRIES_ISO = {
    'iso2': [
        'AD',
        'AE',
        'AF',
        'AG',
        'AI',
        'AL',
        'AM',
        'AN',
        'AO',
        'AQ',
        'AR',
        'AS',
        'AT',
        'AU',
        'AW',
        'AX',
        'AZ',
        'BA',
        'BB',
        'BD',
        'BE',
        'BF',
        'BG',
        'BH',
        'BI',
        'BJ',
        'BL',
        'BM',
        'BN',
        'BO',
        'BR',
        'BS',
        'BT',
        'BV',
        'BW',
        'BY',
        'BZ',
        'CA',
        'CC',
        'CD',
        'CF',
        'CG',
        'CH',
        'CI',
        'CK',
        'CL',
        'CM',
        'CN',
        'CO',
        'CR',
        'CU',
        'CV',
        'CX',
        'CY',
        'CZ',
        'DE',
        'DJ',
        'DK',
        'DM',
        'DO',
        'DZ',
        'EC',
        'EE',
        'EG',
        'EH',
        'ER',
        'ES',
        'ET',
        'FI',
        'FJ',
        'FK',
        'FM',
        'FO',
        'FR',
        'GA',
        'GB',
        'GD',
        'GE',
        'GF',
        'GG',
        'GH',
        'GI',
        'GL',
        'GM',
        'GN',
        'GP',
        'GQ',
        'GR',
        'GS',
        'GT',
        'GU',
        'GW',
        'GY',
        'HK',
        'HM',
        'HN',
        'HR',
        'HT',
        'HU',
        'ID',
        'IE',
        'IL',
        'IM',
        'IN',
        'IO',
        'IQ',
        'IR',
        'IS',
        'IT',
        'JE',
        'JM',
        'JO',
        'JP',
        'KE',
        'KG',
        'KH',
        'KI',
        'KM',
        'KN',
        'KP',
        'KR',
        'KW',
        'KY',
        'KZ',
        'LA',
        'LB',
        'LC',
        'LI',
        'LK',
        'LR',
        'LS',
        'LT',
        'LU',
        'LV',
        'LY',
        'MA',
        'MC',
        'MD',
        'ME',
        'MF',
        'MG',
        'MH',
        'MK',
        'ML',
        'MM',
        'MN',
        'MO',
        'MP',
        'MQ',
        'MR',
        'MS',
        'MT',
        'MU',
        'MV',
        'MW',
        'MX',
        'MY',
        'MZ',
        'NA',
        'NC',
        'NE',
        'NF',
        'NG',
        'NI',
        'NL',
        'NO',
        'NP',
        'NR',
        'NU',
        'NZ',
        'OM',
        'PA',
        'PE',
        'PF',
        'PG',
        'PH',
        'PK',
        'PL',
        'PM',
        'PN',
        'PR',
        'PS',
        'PT',
        'PW',
        'PY',
        'QA',
        'RE',
        'RO',
        'RS',
        'RU',
        'RW',
        'SA',
        'SB',
        'SC',
        'SD',
        'SE',
        'SG',
        'SH',
        'SI',
        'SJ',
        'SK',
        'SL',
        'SM',
        'SN',
        'SO',
        'SR',
        'SS',
        'ST',
        'SV',
        'SY',
        'SZ',
        'TC',
        'TD',
        'TF',
        'TG',
        'TH',
        'TJ',
        'TK',
        'TL',
        'TM',
        'TN',
        'TO',
        'TR',
        'TT',
        'TV',
        'TW',
        'TZ',
        'UA',
        'UG',
        'UM',
        'US',
        'UY',
        'UZ',
        'VA',
        'VC',
        'VE',
        'VG',
        'VI',
        'VN',
        'VU',
        'WF',
        'WS',
        'YE',
        'YT',
        'ZA',
        'ZM',
        'ZW',
    ],
    'iso3': [
        'AND',
        'ARE',
        'AFG',
        'ATG',
        'AIA',
        'ALB',
        'ARM',
        'ANT',
        'AGO',
        'ATA',
        'ARG',
        'ASM',
        'AUT',
        'AUS',
        'ABW',
        'ALA',
        'AZE',
        'BIH',
        'BRB',
        'BGD',
        'BEL',
        'BFA',
        'BGR',
        'BHR',
        'BDI',
        'BEN',
        'BLM',
        'BMU',
        'BRN',
        'BOL',
        'BRA',
        'BHS',
        'BTN',
        'BVT',
        'BWA',
        'BLR',
        'BLZ',
        'CAN',
        'CCK',
        'COD',
        'CAF',
        'COG',
        'CHE',
        'CIV',
        'COK',
        'CHL',
        'CMR',
        'CHN',
        'COL',
        'CRI',
        'CUB',
        'CPV',
        'CXR',
        'CYP',
        'CZE',
        'DEU',
        'DJI',
        'DNK',
        'DMA',
        'DOM',
        'DZA',
        'ECU',
        'EST',
        'EGY',
        'ESH',
        'ERI',
        'ESP',
        'ETH',
        'FIN',
        'FJI',
        'FLK',
        'FSM',
        'FRO',
        'FRA',
        'GAB',
        'GBR',
        'GRD',
        'GEO',
        'GUF',
        'GGY',
        'GHA',
        'GIB',
        'GRL',
        'GMB',
        'GIN',
        'GLP',
        'GNQ',
        'GRC',
        'SGS',
        'GTM',
        'GUM',
        'GNB',
        'GUY',
        'HKG',
        'HMD',
        'HND',
        'HRV',
        'HTI',
        'HUN',
        'IDN',
        'IRL',
        'ISR',
        'IMN',
        'IND',
        'IOT',
        'IRQ',
        'IRN',
        'ISL',
        'ITA',
        'JEY',
        'JAM',
        'JOR',
        'JPN',
        'KEN',
        'KGZ',
        'KHM',
        'KIR',
        'COM',
        'KNA',
        'PRK',
        'KOR',
        'KWT',
        'CYM',
        'KAZ',
        'LAO',
        'LBN',
        'LCA',
        'LIE',
        'LKA',
        'LBR',
        'LSO',
        'LTU',
        'LUX',
        'LVA',
        'LBY',
        'MAR',
        'MCO',
        'MDA',
        'MNE',
        'MAF',
        'MDG',
        'MHL',
        'MKD',
        'MLI',
        'MMR',
        'MNG',
        'MAC',
        'MNP',
        'MTQ',
        'MRT',
        'MSR',
        'MLT',
        'MUS',
        'MDV',
        'MWI',
        'MEX',
        'MYS',
        'MOZ',
        'NAM',
        'NCL',
        'NER',
        'NFK',
        'NGA',
        'NIC',
        'NLD',
        'NOR',
        'NPL',
        'NRU',
        'NIU',
        'NZL',
        'OMN',
        'PAN',
        'PER',
        'PYF',
        'PNG',
        'PHL',
        'PAK',
        'POL',
        'SPM',
        'PCN',
        'PRI',
        'PSE',
        'PRT',
        'PLW',
        'PRY',
        'QAT',
        'REU',
        'ROU',
        'SRB',
        'RUS',
        'RWA',
        'SAU',
        'SLB',
        'SYC',
        'SDN',
        'SWE',
        'SGP',
        'SHN',
        'SVN',
        'SJM',
        'SVK',
        'SLE',
        'SMR',
        'SEN',
        'SOM',
        'SUR',
        'SSD',
        'STP',
        'SLV',
        'SYR',
        'SWZ',
        'TCA',
        'TCD',
        'ATF',
        'TGO',
        'THA',
        'TJK',
        'TKL',
        'TLS',
        'TKM',
        'TUN',
        'TON',
        'TUR',
        'TTO',
        'TUV',
        'TWN',
        'TZA',
        'UKR',
        'UGA',
        'UMI',
        'USA',
        'URY',
        'UZB',
        'VAT',
        'VCT',
        'VEN',
        'VGB',
        'VIR',
        'VNM',
        'VUT',
        'WLF',
        'WSM',
        'YEM',
        'MYT',
        'ZAF',
        'ZMB',
        'ZWE',
    ],
    'numeric': [
        '020',
        '784',
        '004',
        '028',
        '660',
        '008',
        '051',
        '530',
        '024',
        '010',
        '032',
        '016',
        '040',
        '036',
        '533',
        '248',
        '031',
        '070',
        '052',
        '050',
        '056',
        '854',
        '100',
        '048',
        '108',
        '204',
        '652',
        '060',
        '096',
        '068',
        '076',
        '044',
        '064',
        '074',
        '072',
        '112',
        '084',
        '124',
        '166',
        '180',
        '140',
        '178',
        '756',
        '384',
        '184',
        '152',
        '120',
        '156',
        '170',
        '188',
        '192',
        '132',
        '162',
        '196',
        '203',
        '276',
        '262',
        '208',
        '212',
        '214',
        '012',
        '218',
        '233',
        '818',
        '732',
        '232',
        '724',
        '231',
        '246',
        '242',
        '238',
        '583',
        '234',
        '250',
        '266',
        '826',
        '308',
        '268',
        '254',
        '831',
        '288',
        '292',
        '304',
        '270',
        '324',
        '312',
        '226',
        '300',
        '239',
        '320',
        '316',
        '624',
        '328',
        '344',
        '334',
        '340',
        '191',
        '332',
        '348',
        '360',
        '372',
        '376',
        '833',
        '356',
        '086',
        '368',
        '364',
        '352',
        '380',
        '832',
        '388',
        '400',
        '392',
        '404',
        '417',
        '116',
        '296',
        '174',
        '659',
        '408',
        '410',
        '414',
        '136',
        '398',
        '418',
        '422',
        '662',
        '438',
        '144',
        '430',
        '426',
        '440',
        '442',
        '428',
        '434',
        '504',
        '492',
        '498',
        '499',
        '663',
        '450',
        '584',
        '807',
        '466',
        '104',
        '496',
        '446',
        '580',
        '474',
        '478',
        '500',
        '470',
        '480',
        '462',
        '454',
        '484',
        '458',
        '508',
        '516',
        '540',
        '562',
        '574',
        '566',
        '558',
        '528',
        '578',
        '524',
        '520',
        '570',
        '554',
        '512',
        '591',
        '604',
        '258',
        '598',
        '608',
        '586',
        '616',
        '666',
        '612',
        '630',
        '275',
        '620',
        '585',
        '600',
        '634',
        '638',
        '642',
        '688',
        '643',
        '646',
        '682',
        '090',
        '690',
        '736',
        '752',
        '702',
        '654',
        '705',
        '744',
        '703',
        '694',
        '674',
        '686',
        '706',
        '740',
        '728',
        '678',
        '222',
        '760',
        '748',
        '796',
        '148',
        '260',
        '768',
        '764',
        '762',
        '772',
        '626',
        '795',
        '788',
        '776',
        '792',
        '780',
        '798',
        '158',
        '834',
        '804',
        '800',
        '581',
        '840',
        '858',
        '860',
        '336',
        '670',
        '862',
        '092',
        '850',
        '704',
        '548',
        '876',
        '882',
        '887',
        '175',
        '710',
        '894',
        '716',
    ],
}

SHORTENED_ADDRESS_FMT = [
    'cs',
    'da',
    'de',
    'de-at',
    'de-ch',
    'el',
    'es',
    'fi',
    'is',
    'nl',
    'nl-be',
    'no',
    'sv',
]

CONTINENT_CODES = ['AF', 'NA', 'OC', 'AN', 'AS', 'EU', 'SA']

CALLING_CODES = [
    '+1',
    '+7',
    '+20',
    '+27',
    '+30',
    '+31',
    '+32',
    '+33',
    '+34',
    '+36',
    '+39',
    '+40',
    '+41',
    '+43',
    '+44',
    '+44',
    '+44',
    '+44',
    '+45',
    '+46',
    '+47',
    '+48',
    '+49',
    '+51',
    '+52',
    '+53',
    '+54',
    '+55',
    '+56',
    '+56',
    '+57',
    '+58',
    '+60',
    '+61',
    '+61',
    '+61',
    '+62',
    '+63',
    '+64',
    '+64',
    '+64',
    '+65',
    '+66',
    '+77',
    '+81',
    '+82',
    '+84',
    '+86',
    '+90',
    '+91',
    '+92',
    '+93',
    '+94',
    '+95',
    '+98',
    '+211',
    '+212',
    '+213',
    '+216',
    '+218',
    '+220',
    '+221',
    '+222',
    '+223',
    '+224',
    '+225',
    '+226',
    '+227',
    '+228',
    '+229',
    '+230',
    '+231',
    '+232',
    '+233',
    '+234',
    '+235',
    '+236',
    '+237',
    '+238',
    '+239',
    '+240',
    '+241',
    '+242',
    '+243',
    '+244',
    '+245',
    '+246',
    '+246',
    '+247',
    '+248',
    '+249',
    '+250',
    '+251',
    '+252',
    '+253',
    '+254',
    '+255',
    '+255',
    '+256',
    '+257',
    '+258',
    '+260',
    '+261',
    '+262',
    '+262',
    '+263',
    '+264',
    '+265',
    '+266',
    '+267',
    '+268',
    '+269',
    '+290',
    '+291',
    '+297',
    '+298',
    '+299',
    '+350',
    '+351',
    '+352',
    '+353',
    '+354',
    '+355',
    '+356',
    '+357',
    '+358',
    '+359',
    '+370',
    '+371',
    '+372',
    '+373',
    '+374',
    '+375',
    '+376',
    '+377',
    '+378',
    '+379',
    '+380',
    '+381',
    '+382',
    '+383',
    '+385',
    '+386',
    '+387',
    '+389',
    '+420',
    '+421',
    '+423',
    '+500',
    '+500',
    '+501',
    '+502',
    '+503',
    '+504',
    '+505',
    '+506',
    '+507',
    '+508',
    '+509',
    '+590',
    '+590',
    '+590',
    '+591',
    '+592',
    '+593',
    '+594',
    '+595',
    '+596',
    '+596',
    '+597',
    '+598',
    '+670',
    '+672',
    '+672',
    '+673',
    '+674',
    '+675',
    '+676',
    '+677',
    '+678',
    '+679',
    '+680',
    '+681',
    '+682',
    '+683',
    '+685',
    '+686',
    '+687',
    '+688',
    '+689',
    '+690',
    '+691',
    '+692',
    '+800',
    '+808',
    '+850',
    '+852',
    '+853',
    '+855',
    '+856',
    '+870',
    '+878',
    '+880',
    '+881',
    '+886',
    '+960',
    '+961',
    '+962',
    '+963',
    '+964',
    '+965',
    '+966',
    '+967',
    '+968',
    '+970',
    '+971',
    '+972',
    '+973',
    '+974',
    '+975',
    '+976',
    '+977',
    '+992',
    '+993',
    '+994',
    '+995',
    '+996',
    '+998',
    '+1242',
    '+1246',
    '+1264',
    '+1268',
    '+1268',
    '+1284',
    '+1340',
    '+1345',
    '+1441',
    '+1473',
    '+1649',
    '+1664',
    '+1670',
    '+1671',
    '+1684',
    '+1721',
    '+1758',
    '+1767',
    '+1784',
    '+1808',
    '+1808',
    '+1849',
    '+1868',
    '+1869',
    '+1869',
    '+1876',
    '+1939',
    '+2908',
    '+4779',
    '+4779',
    '+5399',
    '+5993',
    '+5994',
    '+5997',
    '+5997',
    '+5999',
    '+8810',
    '+8813',
    '+8817',
    '+8818',
    '+35818',
    '+88213',
    '+88216',
    '+90392',
    '+99534',
    '+99544',
]

COORDINATE_RANGE = {
    'default': {'lat': [-90, 90], 'long': [-180, 180]},
    'ar': {'lat': [-54.8, -22.10236], 'long': [-72.3508, -53.64581]},
    'ke': {'lat': [-4.47166, 3.93726], 'long': [33.97559, 41.85688]},
    'mc': {'lat': [43.73333, 43.73976], 'long': [7.41667, 7.42732]},
    'bt': {'lat': [26.80069, 27.90372], 'long': [89.09951, 91.55424]},
    'ro': {'lat': [43.66667, 48.18333], 'long': [20.48333, 28.86667]},
    'nz': {'lat': [-46.56069, -35.22676], 'long': [-176.55973, 178.00417]},
    'sr': {'lat': [5.06667, 5.95], 'long': [-56.98333, -54.05]},
    'mh': {'lat': [4.58199, 11.34735], 'long': [162.33733, 171.73502]},
    'jo': {'lat': [29.52667, 32.69833], 'long': [35.00778, 36.83113]},
    'om': {'lat': [17.01505, 26.17993], 'long': [54.09237, 59.52889]},
    'mg': {'lat': [-25.3, -12.2787], 'long': [43.66667, 50.27876]},
    'sn': {'lat': [12.5579, 16.51293], 'long': [-17.47581, -12.1743]},
    'mf': {'lat': [18.06667, 18.06667], 'long': [-63.08333, -63.08333]},
    'dj': {'lat': [11.10861, 11.96306], 'long': [42.37389, 43.29056]},
    'lv': {'lat': [55.88333, 57.89752], 'long': [21.01667, 28.12165]},
    'af': {'lat': [30.15, 37.46572], 'long': [61.06667, 72.318]},
    'et': {'lat': [4.05, 14.277], 'long': [34.53333, 42.8]},
    'vc': {'lat': [13.01102, 13.2879], 'long': [-61.26667, -61.1302]},
    'ly': {'lat': [24.1989, 32.94701], 'long': [9.50072, 25.08653]},
    'ir': {'lat': [25.2919, 39.6482], 'long': [44.7653, 61.4949]},
    'mw': {'lat': [-16.91995, -9.70237], 'long': [32.88019, 35.5]},
    'tr': {'lat': [35.9025, 42.02683], 'long': [25.90902, 44.5742]},
    'so': {'lat': [-0.35817, 11.87037], 'long': [42.22091, 51.0773]},
    'dk': {'lat': [54.76906, 57.72093], 'long': [8.24402, 14.70664]},
    've': {'lat': [4.60226, 11.6956], 'long': [-72.55212, -61.11025]},
    'ee': {'lat': [57.77781, 59.47667], 'long': [22.50389, 28.19028]},
    'sz': {'lat': [-27.21667, -25.96667], 'long': [31.13333, 31.95]},
    'ba': {'lat': [42.71197, 45.18497], 'long': [15.77806, 19.29256]},
    'no': {'lat': [58.0274, 70.66336], 'long': [5.0328, 29.74943]},
    'md': {'lat': [45.68417, 48.43], 'long': [27.085, 29.95861]},
    'cv': {'lat': [14.86667, 17.18561], 'long': [-25.07243, -22.9]},
    'be': {'lat': [49.56652, 51.46791], 'long': [2.59368, 6.25749]},
    'gl': {'lat': [60.71667, 69.21667], 'long': [-53.6735, -46.03333]},
    'bg': {'lat': [41.38333, 44.11667], 'long': [22.68361, 28.33333]},
    'rw': {'lat': [-2.59667, -1.49984], 'long': [28.9075, 30.5427]},
    'gb': {'lat': [50.10319, 60.15456], 'long': [-7.64133, 1.75159]},
    'mt': {'lat': [35.82583, 36.07222], 'long': [14.20361, 14.56701]},
    'sl': {'lat': [7.24611, 9.58893], 'long': [-13.28972, -10.37135]},
    'mp': {'lat': [14.96823, 15.21233], 'long': [145.61998, 145.7545]},
    'kz': {'lat': [40.66667, 54.90521], 'long': [46.84705, 84.87144]},
    'ls': {'lat': [-30.40001, -28.76659], 'long': [27.23744, 29.06751]},
    'lt': {'lat': [54.01667, 56.31667], 'long': [21.06861, 26.41667]},
    'tc': {'lat': [21.46122, 21.46122], 'long': [-71.14188, -71.14188]},
    'bs': {'lat': [20.94982, 26.86667], 'long': [-79.3, -72.96667]},
    'is': {'lat': [63.93311, 66.07475], 'long': [-23.13498, -14.39484]},
    'in': {'lat': [8.09008, 34.55765], 'long': [68.82655, 96.12882]},
    'gq': {'lat': [-1.40139, 3.75], 'long': [5.6325, 11.33528]},
    'hu': {'lat': [45.85499, 48.39492], 'long': [16.27358, 22.68096]},
    'ms': {'lat': [16.70555, 16.79183], 'long': [-62.21729, -62.21058]},
    'cy': {'lat': [34.68406, 35.59719], 'long': [32.42451, 34.37916]},
    'la': {'lat': [14.11726, 21.68372], 'long': [100.41302, 106.83184]},
    'ca': {'lat': [42.11679, 63.74697], 'long': [-135.05375, -52.70931]},
    'az': {'lat': [38.45598, 41.72626], 'long': [45.36561, 50.32476]},
    'bw': {'lat': [-26.05, -17.81667], 'long': [21.78333, 27.84296]},
    'yt': {'lat': [-12.95361, -12.69982], 'long': [45.05819, 45.27938]},
    'cr': {'lat': [8.60327, 10.95173], 'long': [-85.5851, -82.946]},
    'cx': {'lat': [-10.42172, -10.42172], 'long': [105.67912, 105.67912]},
    'gg': {'lat': [49.45981, 49.45981], 'long': [-2.53527, -2.53527]},
    'wf': {'lat': [-14.31096, -13.28163], 'long': [-178.16551, -176.17453]},
    'ss': {'lat': [3.86512, 9.53342], 'long': [27.40019, 33.59168]},
    'jp': {'lat': [24.34478, 45.40944], 'long': [124.15717, 145.575]},
    'fr': {'lat': [41.59101, 51.03457], 'long': [-4.65, 9.45]},
    'dz': {'lat': [22.785, 36.92917], 'long': [-8.14743, 8.46667]},
    'je': {'lat': [49.18804, 49.18804], 'long': [-2.10491, -2.10491]},
    'tm': {'lat': [35.27992, 42.32773], 'long': [52.95517, 66.04656]},
    'lr': {'lat': [4.3782, 8.42194], 'long': [-11.3671, -7.71081]},
    'py': {'lat': [-27.4, -21.04153], 'long': [-60.03333, -54.30694]},
    'ag': {'lat': [17.02741, 17.63333], 'long': [-61.87466, -61.77046]},
    'bn': {'lat': [4.58361, 4.94029], 'long': [114.2312, 115.06667]},
    'ps': {'lat': [31.25997, 32.50847], 'long': [34.25952, 35.45]},
    'tt': {'lat': [10.13333, 11.25], 'long': [-61.68333, -60.58333]},
    'nf': {'lat': [-29.05459, -29.05459], 'long': [167.96628, 167.96628]},
    'gh': {'lat': [4.86992, 11.0616], 'long': [-2.58404, 0.98789]},
    'ie': {'lat': [51.58666, 55.13333], 'long': [-9.70264, -6.04944]},
    'tj': {'lat': [36.72484, 40.66992], 'long': [67.60931, 73.96674]},
    'sc': {'lat': [-4.76667, -4.61667], 'long': [55.41667, 55.51667]},
    'kp': {'lat': [37.90889, 42.95722], 'long': [124.39806, 130.46222]},
    'gs': {'lat': [-54.28111, -54.28111], 'long': [-36.5092, -36.5092]},
    'eh': {'lat': [27.09611, 27.1418], 'long': [-13.41583, -13.18797]},
    'tz': {'lat': [-11.36667, -1.14389], 'long': [29.62667, 40.33333]},
    'bd': {'lat': [20.86382, 26.33338], 'long': [88.15638, 92.30153]},
    'ch': {'lat': [45.83203, 47.69732], 'long': [6.07544, 9.83723]},
    'st': {'lat': [0.33654, 1.63726], 'long': [6.72732, 7.41783]},
    'iq': {'lat': [29.97421, 37.14871], 'long': [40.28586, 48.47309]},
    'lk': {'lat': [5.94851, 9.81667], 'long': [79.79528, 81.84198]},
    'kr': {'lat': [33.25333, 38.37881], 'long': [126.10863, 129.365]},
    'sa': {'lat': [16.57946, 31.67252], 'long': [35.69014, 50.20833]},
    'am': {'lat': [39.20755, 41.17244], 'long': [43.84528, 46.40576]},
    'cu': {'lat': [20.02472, 23.15917], 'long': [-84.28173, -74.15181]},
    'do': {'lat': [17.9, 19.84826], 'long': [-71.85022, -68.40431]},
    'cd': {'lat': [-11.76667, 4.279], 'long': [12.9484, 30.25224]},
    'sm': {'lat': [43.90451, 43.96897], 'long': [12.4185, 12.49798]},
    'sk': {'lat': [47.76356, 49.43503], 'long': [17.02188, 22.18136]},
    'mu': {'lat': [-20.51667, -16.60329], 'long': [57.37056, 63.41667]},
    'nl': {'lat': [50.77083, 53.35917], 'long': [3.57361, 7.10833]},
    'gr': {'lat': [35.01186, 41.50306], 'long': [19.91975, 28.2225]},
    'ws': {'lat': [-13.93375, -13.51963], 'long': [-172.63784, -171.53122]},
    'ax': {'lat': [60.09726, 60.09726], 'long': [19.93481, 19.93481]},
    'ky': {'lat': [19.27647, 19.36667], 'long': [-81.41667, -81.2542]},
    'sj': {'lat': [70.9221, 78.22334], 'long': [-8.7187, 15.64689]},
    'rs': {'lat': [42.55139, 46.102792], 'long': [18.98472, 22.58611]},
    'pw': {'lat': [3.00488, 8.08228], 'long': [131.12168, 134.71725]},
    'gf': {'lat': [4.847, 5.65919], 'long': [-54.03333, -52.26667]},
    'ai': {'lat': [18.21704, 18.21704], 'long': [-63.05783, -63.05783]},
    'kg': {'lat': [39.83895, 42.89106], 'long': [69.5276, 78.39362]},
    'cg': {'lat': [-4.77609, 1.61804], 'long': [11.8125, 18.05981]},
    'nu': {'lat': [-19.05952, -19.05952], 'long': [-169.91867, -169.91867]},
    'gd': {'lat': [12.04903, 12.48292], 'long': [-61.74849, -61.45597]},
    'mm': {'lat': [12.43954, 25.38641], 'long': [92.89835, 98.60028]},
    'cc': {'lat': [-12.15681, -12.15681], 'long': [96.82251, 96.82251]},
    'pk': {'lat': [24.3539, 35.91869], 'long': [61.74681, 75.16683]},
    'pf': {'lat': [-17.75, -8.91093], 'long': [-151.44482, -140.09972]},
    'pm': {'lat': [46.77914, 47.0975], 'long': [-56.38139, -56.1773]},
    'vg': {'lat': [18.42693, 18.43882], 'long': [-64.62079, -64.60382]},
    'si': {'lat': [45.50526, 46.83694], 'long': [13.52639, 16.45091]},
    'bl': {'lat': [17.89618, 17.89618], 'long': [-62.84978, -62.84978]},
    'uz': {'lat': [37.22417, 43.76833], 'long': [58.90372, 72.76177]},
    'mz': {'lat': [-25.96553, -11.31667], 'long': [31.99528, 40.73583]},
    'gi': {'lat': [36.14474, 36.14474], 'long': [-5.35257, -5.35257]},
    'bi': {'lat': [-4.1348, -2.5845], 'long': [29.1248, 30.5528]},
    'bb': {'lat': [13.06667, 13.28333], 'long': [-59.65, -59.45]},
    'kn': {'lat': [17.11667, 17.41473], 'long': [-62.84858, -62.56667]},
    'fj': {'lat': [-18.14161, -12.5], 'long': [177.05, 179.38333]},
    'cl': {'lat': [-53.15483, -18.4746], 'long': [-73.81622, -68.93015]},
    'th': {'lat': [5.77434, 20.43353], 'long': [97.96852, 105.22908]},
    'id': {'lat': [-10.1718, 5.88969], 'long': [95.31644, 140.71813]},
    'li': {'lat': [47.06667, 47.23799], 'long': [9.5, 9.54678]},
    'me': {'lat': [41.92936, 43.3567], 'long': [18.5375, 20.16652]},
    'ru': {'lat': [41.28413, 71.69002], 'long': [19.90929, 177.5103]},
    'at': {'lat': [46.52694, 48.81667], 'long': [9.6, 16.94504]},
    'ua': {'lat': [44.41886, 52.18903], 'long': [22.20555, 40.13222]},
    'gy': {'lat': [3.38333, 8.2], 'long': [-59.8, -57.13333]},
    'cz': {'lat': [48.73881, 51.00369], 'long': [12.19499, 18.76458]},
    'bf': {'lat': [9.88333, 14.4429], 'long': [-4.93417, 1.78838]},
    'ph': {'lat': [4.66115, 20.44865], 'long': [117.04868, 126.56]},
    'mv': {'lat': [-0.6, 6.62207], 'long': [72.89437, 73.56667]},
    'qa': {'lat': [24.99611, 26.12933], 'long': [50.78583, 51.60337]},
    'pe': {'lat': [-18.01465, -3.48139], 'long': [-81.27194, -69.04167]},
    'ci': {'lat': [4.42295, 10.48115], 'long': [-8.42592, -2.80003]},
    'mk': {'lat': [41.03143, 42.20194], 'long': [20.52421, 22.89056]},
    'ye': {'lat': [12.64881, 16.94021], 'long': [42.95452, 54.01895]},
    'mx': {'lat': [14.53588, 32.62781], 'long': [-117.06583, -86.73105]},
    'mq': {'lat': [14.46733, 14.83292], 'long': [-61.13333, -60.83883]},
    'uy': {'lat': [-34.96667, -30.27522], 'long': [-58.41667, -53.38583]},
    'pt': {'lat': [32.63333, 42.07892], 'long': [-28.7, -6.75719]},
    'ni': {'lat': [11.1236, 14.74189], 'long': [-87.17336, -83.04175]},
    'cn': {'lat': [18.24306, 52.33333], 'long': [75.98951, 134.28917]},
    'es': {'lat': [27.7567, 43.68333], 'long': [-17.93394, 4.2899]},
    'im': {'lat': [54.15, 54.32273], 'long': [-4.48333, -4.38526]},
    'as': {'lat': [-14.33583, -11.05528], 'long': [-171.08833, -169.51444]},
    'us': {'lat': [19.50139, 64.85694], 'long': [-161.75583, -68.01197]},
    'za': {'lat': [-34.53215, -22.35131], 'long': [17.8865, 32.03768]},
    'lu': {'lat': [49.48056, 49.86778], 'long': [5.88056, 6.44194]},
    'vu': {'lat': [-19.55, -13.88333], 'long': [167.16235, 169.26667]},
    'ma': {'lat': [23.68477, 35.76727], 'long': [-15.95798, -1.22855]},
    'dm': {'lat': [15.23333, 15.58333], 'long': [-61.46667, -61.26667]},
    'ki': {'lat': [1.3278, 1.3673], 'long': [172.92105, 173.12415]},
    'pl': {'lat': [49.29899, 54.79086], 'long': [14.24712, 23.89251]},
    'mo': {'lat': [22.20056, 22.20056], 'long': [113.54611, 113.54611]},
    'tg': {'lat': [6.13748, 10.86225], 'long': [0.20762, 1.5919]},
    'sg': {'lat': [1.28967, 1.28967], 'long': [103.85007, 103.85007]},
    'ec': {'lat': [-4.38181, 1.28626], 'long': [-90.3138, -76.89528]},
    'kh': {'lat': [10.48291, 14.18175], 'long': [102.5625, 107.18811]},
    'fm': {'lat': [5.32479, 9.51638], 'long': [138.12167, 163.00781]},
    'pa': {'lat': [7.76667, 9.55276], 'long': [-82.86206, -77.53507]},
    'de': {'lat': [47.40724, 54.9079], 'long': [5.98815, 14.98853]},
    'il': {'lat': [29.55805, 33.20733], 'long': [34.57149, 35.57212]},
    'cf': {'lat': [3.52494, 10.28488], 'long': [15.13926, 26.49211]},
    'vi': {'lat': [17.72751, 18.3419], 'long': [-64.9307, -64.74698]},
    'bo': {'lat': [-22.08659, -10.83676], 'long': [-68.85063, -57.76667]},
    'kw': {'lat': [28.63917, 29.4425], 'long': [47.65806, 48.27472]},
    'al': {'lat': [39.87556, 42.07694], 'long': [19.44139, 20.99]},
    'sh': {'lat': [-37.06757, -7.93333], 'long': [-14.41667, -5.71675]},
    'hn': {'lat': [13.11667, 16.31759], 'long': [-89.18333, -83.77222]},
    'fk': {'lat': [-51.7, -51.7], 'long': [-57.85, -57.85]},
    'ae': {'lat': [23.14355, 25.78953], 'long': [52.73056, 56.34199]},
    'cm': {'lat': [2.38333, 12.5717], 'long': [8.8724, 15.23288]},
    're': {'lat': [-21.37839, -20.88231], 'long': [55.27071, 55.79629]},
    'nc': {'lat': [-22.28333, -20.91687], 'long': [164.86582, 167.88333]},
    'na': {'lat': [-28.55, -17.46667], 'long': [13.83998, 24.26667]},
    'aw': {'lat': [12.51667, 12.61667], 'long': [-70.06667, -69.95]},
    'ge': {'lat': [41.26458, 43.38111], 'long': [40.07944, 46.27667]},
    'ga': {'lat': [-2.93323, 2.07597], 'long': [8.78151, 13.67533]},
    'gu': {'lat': [13.26584, 13.53605], 'long': [144.65852, 144.88855]},
    'ug': {'lat': [-1.28538, 3.66088], 'long': [29.65, 34.66659]},
    'tk': {'lat': [-9.38516, -8.54212], 'long': [-172.51591, -171.24675]},
    'bm': {'lat': [32.2949, 32.2949], 'long': [-64.78303, -64.78303]},
    'td': {'lat': [8.26681, 21.35494], 'long': [14.1539, 22.84308]},
    'mn': {'lat': [43.57083, 50.23139], 'long': [89.9625, 114.53264]},
    'pn': {'lat': [-25.06597, -25.06597], 'long': [-130.10147, -130.10147]},
    'tw': {'lat': [22.00417, 25.12825], 'long': [118.31833, 121.753]},
    'tf': {'lat': [-49.35, -49.35], 'long': [70.21667, 70.21667]},
    'lc': {'lat': [13.71667, 14.06667], 'long': [-61.0566, -60.88786]},
    'sv': {'lat': [13.22028, 14.33333], 'long': [-89.92972, -87.84389]},
    'zw': {'lat': [-22.21667, -16.51667], 'long': [25.83066, 32.69781]},
    'sb': {'lat': [-10.71667, -8.10303], 'long': [156.84186, 165.83333]},
    'se': {'lat': [55.37514, 67.85572], 'long': [11.1712, 23.15645]},
    'br': {'lat': [-33.69111, 2.81972], 'long': [-72.89583, -34.80861]},
    'np': {'lat': [26.4831, 29.84121], 'long': [80.33333, 88.09436]},
    'gn': {'lat': [7.75624, 12.5311], 'long': [-14.6, -8.64869]},
    'zm': {'lat': [-17.84194, -8.76234], 'long': [22.68138, 33.1782]},
    'fi': {'lat': [59.83333, 68.90596], 'long': [21.37596, 30.93276]},
    'mr': {'lat': [15.15895, 22.71873], 'long': [-17.03465, -7.2535]},
    'sy': {'lat': [32.61889, 37.07279], 'long': [35.79011, 40.91854]},
    'tn': {'lat': [32.92967, 37.27442], 'long': [7.87765, 11.21965]},
    'eg': {'lat': [24.09082, 31.5084], 'long': [25.51965, 34.89005]},
    'by': {'lat': [51.7905, 55.9058], 'long': [23.68775, 32.0514]},
    'gw': {'lat': [11.28333, 12.48389], 'long': [-16.16583, -14.21667]},
    'hk': {'lat': [22.22623, 22.45007], 'long': [113.97157, 114.26667]},
    'vn': {'lat': [9.17682, 22.82333], 'long': [103.02301, 109.32094]},
    'ng': {'lat': [4.31506, 13.72918], 'long': [2.73333, 14.21731]},
    'tl': {'lat': [-9.31286, -8.47111], 'long': [124.38333, 127.0025]},
    'sd': {'lat': [10.55, 21.06667], 'long': [22.44725, 37.729]},
    'pr': {'lat': [17.9658, 18.50078], 'long': [-67.2499, -65.30099]},
    'bh': {'lat': [26.06861, 26.25722], 'long': [50.50389, 50.65417]},
    'bj': {'lat': [6.28036, 11.86819], 'long': [1.26651, 3.38327]},
    'va': {'lat': [41.90236, 41.90236], 'long': [12.45332, 12.45332]},
    'ad': {'lat': [42.46372, 42.5676], 'long': [1.49129, 1.5975]},
    'nr': {'lat': [-0.55085, -0.50803], 'long': [166.92384, 166.95813]},
    'ht': {'lat': [18.19331, 19.9389], 'long': [-74.42167, -71.72397]},
    'er': {'lat': [13.00917, 15.77792], 'long': [37.59067, 42.73944]},
    'bz': {'lat': [16.09835, 18.39375], 'long': [-89.13917, -87.9659]},
    'km': {'lat': [-12.34639, -11.38472], 'long': [43.25506, 44.53194]},
    'lb': {'lat': [33.11806, 34.54278], 'long': [35.13972, 36.21806]},
    'gm': {'lat': [13.20194, 13.56667], 'long': [-16.73389, -14.2]},
    'fo': {'lat': [61.55557, 62.24398], 'long': [-7.19389, -6.58901]},
    'au': {'lat': [-43.00311, -12.46113], 'long': [113.6594, 153.61194]},
    'ao': {'lat': [-17.06667, -5.55], 'long': [12.15222, 22.22466]},
    'co': {'lat': [-4.21528, 12.58472], 'long': [-81.70056, -67.48588]},
    'ml': {'lat': [11.08943, 18.44111], 'long': [-11.44448, 3.14111]},
    'ck': {'lat': [-21.20778, -21.20778], 'long': [-159.775, -159.775]},
    'tv': {'lat': [-8.52425, -6.10819], 'long': [176.31472, 179.19417]},
    'gp': {'lat': [15.88346, 16.47206], 'long': [-61.78783, -61.27414]},
    'it': {'lat': [36.71703, 46.99623], 'long': [7.05809, 18.37819]},
    'gt': {'lat': [13.9274, 17.06606], 'long': [-92.19298, -88.59444]},
    'my': {'lat': [1.24722, 6.8837], 'long': [99.8432, 118.61119]},
    'to': {'lat': [-21.33333, -15.9544], 'long': [-175.2018, -173.79616]},
    'hr': {'lat': [42.64807, 46.38444], 'long': [13.52389, 19.37694]},
    'ne': {'lat': [11.88435, 17.0187], 'long': [0.75306, 13.10921]},
    'jm': {'lat': [17.81007, 18.49358], 'long': [-78.17356, -76.40927]},
    'pg': {'lat': [-10.31509, -2.0341], 'long': [141.26667, 155.56598]},
}
