from django.db import connections
import logging

logger = logging.getLogger("app")


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_week_of_month(date):
    from math import ceil
    first_day = date.replace(day=1)
    day_of_month = date.day
    if (first_day.weekday() == 6):
        adjusted_dom = (1 + first_day.weekday()) / 7
    else:
        adjusted_dom = day_of_month + first_day.weekday()
    return int(ceil(adjusted_dom / 7.0))


class Payrolls:
    sql = """
select 
  TZe_PersNr, 
  max(Per_PersNr) PeopleSoftId, 
  max(PIn_PersNrRef) as CalismaId, 
  MAX(Per_Vorname) as ADI, 
  max(Per_Name) as SOYADI, 
  max(Per_Grp1) as Grup1, 
  max(Per_Grp2) as Grup2, 
  max(Per_Grp3) as Grup3, 
  max(Per_Grp4) as Grup4, 
  MIN(
    convert(varchar, TZe_Datum, 104)
  ) AS BaslaTarihi, 
  MAX(
    convert(varchar, TZe_Datum, 104)
  ) as BitisTarihi, 
  format(
    sum(
      iif(
        TZe_ZeitArt = 'NCAL' 
        or TZe_ZeitArt = 'NC', 
        convert(int, TZe_IstZeit)+(
          TZe_IstZeit - convert(int, TZe_IstZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as NCAL, 
  format(
    abs(
      convert(int,min(TZe_SaldoTag))+(min(TZe_SaldoTag)-convert(int,min(TZe_SaldoTag))
      )*5/3),'0.00') as EKSIK,
  format(
    sum(
      iif(
        TZe_AbwArt = 'DESIZ', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as DESIZ, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'UCSIZ', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as UCSIZ, 
   format(
    sum(
      iif(
        TZe_AbwArt = 'UCSPZ', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as UCSPZ, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'MUCSZ', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as MUCSZ, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'KISAC', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as KISAC, 
    format(
    sum(
      iif(
        TZe_AbwArt = 'KISAP', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as KISAP, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'HTAT2', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as HTAT, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'RESTA', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as RESTA, 
  format(
    sum(
      iif(
        TZe_ZeitArt = 'GECEZ', 
        convert(int, TZe_IstZeit)+(
          TZe_IstZeit - convert(int, TZe_IstZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as GECEZ, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'TUTKL', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as TUTKL, 
  format(
    sum(
      iif(
        TZe_ZeitArt = 'FM1' 
        or TZe_ZeitArt = 'FM2' 
        or TZe_ZeitArt = 'FM3', 
        convert(int, TZe_IstZeit)+(
          TZe_IstZeit - convert(int, TZe_IstZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as FMTOP, 
  format(
    sum(
      iif(
        TZe_ZeitArt = 'OFM1' 
        or TZe_ZeitArt = 'OFM2' 
        or TZe_ZeitArt = 'OFM3', 
        convert(int, TZe_IstZeit)+(
          TZe_IstZeit - convert(int, TZe_IstZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as OFMTOP, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'GOREV', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as GOREV, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'YILIZ', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as YILIZ, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'UCRLI', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as UCRLI, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'DOUCS', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as DOUCS, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'EVLEN', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as EVLEN, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'OLUM', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as OLUM, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'DOGUM', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as DOGUM,
  format(
    sum(
      iif(
        TZe_AbwArt = 'DOGPZ', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as DOGPZ,  
  format(
    sum(
      iif(
        TZe_AbwArt = 'SUT', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as SUT, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'HASTA', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as RAPOR, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'HASPZ', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as RAPOR_TATIL, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'SENDK', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as SENDK, 
  format(
    sum(
      iif(
        TZe_AbwArt = 'ARGE', 
        convert(int, TZe_AbwArtZeit)+(
          TZe_AbwArtZeit - convert(int, TZe_AbwArtZeit)
        )* 5 / 3, 
        0
      )
    ), 
    '0.00'
  ) as ARGE 
from 
  TTagZei 
  left join TPerTab on TTagZei.TZe_PersNr = tpertab.Per_PersNr 
  left join TPerInd on TTagZei.TZe_PersNr = TPerInd.PIn_PersNr 
where 
  convert(date, TZe_Datum, 104) between 
  convert(date, '{}', 104) and
  convert(date, '{}', 104)
  {}
group by 
  TZe_PersNr, 
  TZe_Datum;        
    """

    @classmethod
    def query(cls, db, start, end, employees=[], collar_type=None, firm=[]):
        with connections[db].cursor() as cursor:
            # collar_type = B 'beyaz yaka'
            # M 'mavi yaka'
            # tpertab.per_grp3 = ''

            filter = []
            if employees:
                empx = str.join(', ', map(str, employees))
                filter.append(f'and tze_persnr in ({empx})')
            if collar_type:
                filter.append(f"and tpertab.per_grp3 = '{collar_type}'")
            if firm:
                # Convert firm list to string
                firm_str = ", ".join([f"'{f}'" for f in firm])
                filter.append(f"and tpertab.per_grp0 in ({firm_str})")
            fsql = cls.sql.format(
                start.strftime('%d.%m.%Y'),
                end.strftime('%d.%m.%Y'),
                str.join(' ', filter)
            )
            logger.exception(fsql)
            cursor.execute(fsql)
            result = dictfetchall(cursor)
            return result

    @classmethod
    def montly(cls, data, config):
        from datetime import datetime
        # yil ay setleri
        periods = {}
        for dx in data:
            tr_date = datetime.strptime(dx.get('BaslaTarihi'), '%d.%m.%Y')
            key = f'{tr_date.year}-{tr_date.month}'
            if key not in periods:
                periods[key] = {
                    'year': tr_date.year,
                    'month': tr_date.month,
                    'types': {k: [] for k in config.keys()},
                    'totals': {k: 0 for k in config.keys()}

                }

        for dx in data:
            tr_date = datetime.strptime(dx.get('BaslaTarihi'), '%d.%m.%Y')
            key = f'{tr_date.year}-{tr_date.month}'
            ret = cls.reduce(dx, config)
            for r, v in ret.items():
                periods[key]['types'][r].append(v)

        for key, period in periods.items():
            for k, v in period['types'].items():
                period['totals'][k] = sum(v)

        return period

    @classmethod
    def reduce(cls, line, config):
        from decimal import Decimal
        nx = {}
        for key, values in config.items():
            nx[key] = []
            for value in values:
                if value in line and line[value]:
                    if key is 'eksikGunSayisi' and Decimal(line.get(value)):
                      nx[key].append(1)
                      print(key)
                    else:
                      nx[key].append(Decimal(line.get(value)))
        tx = {}
        for key, value in nx.items():
          tx[key] = sum(value)
        return tx

    @classmethod
    def prepare(cls, db, start, end, employees=[], collar_type=None, firm=[]):
        raw = cls.query(
            db,
            start,
            end,
            employees=employees,
            collar_type=collar_type,
            firm=firm
        )
        data = {}
        for item in raw:
            if item['TZe_PersNr'] not in data:
                data[item['TZe_PersNr']] = {
                    'geco': [],
                    'people_soft_id': item.get('PeopleSoftId'),
                    'name': item.get('ADI'),
                    'surname': item.get('SOYADI'),
                    'employee_nr': item['TZe_PersNr'],
                    'group1': item.get('Grup1'),
                    'group2': item.get('Grup2'),
                    'group3': item.get('Grup3'),
                    'group4': item.get('Grup4')
                }

        clear = [
            'PeopleSoftId', 'ADI', 'SOYADI',
            'Grup1', 'Grup2', 'Grup3', 'Grup4'
        ]
        for item in raw:
            per = item.pop('TZe_PersNr')
            for clr in clear:
                if clr in item:
                    item.pop(clr)

            data[per]['geco'].append(
                item
            )

        return list(data.values())
