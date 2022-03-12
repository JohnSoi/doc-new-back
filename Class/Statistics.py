from datetime import datetime, timedelta

from sqlalchemy import and_
from sqlalchemy.orm import Session

from Constants.models import CARD_TYPE, PATIENT_TYPE
from Models.Patient import Patient
from Platform.Helpers import HttpQuery
from app import engine


class Statistic:
    ALLOWED_PERIOD = ['half_year', 'month', 'year', 'all']

    def patient(self, filter_params: dict = None):
        period = 'half_year'
        date_start = None

        if filter_params and filter_params.get('period') and filter_params.get('period') in self.ALLOWED_PERIOD:
            period = filter_params.get('period')

        if period == 'half_year':
            date_start = datetime.today() - timedelta(days=6 * 365 / 12)
        elif period == 'year':
            date_start = datetime.today() - timedelta(days=365)

        query = '''
            SELECT 
                "type",
                COUNT("id") AS "Count",
                CONCAT(RIGHT(CONCAT('00', EXTRACT(MONTH FROM "date_create")), 2), '-', 
                       EXTRACT(year FROM "date_create")) AS "Date",
                EXTRACT(MONTH FROM "date_create") AS "Month",
                EXTRACT(year FROM "date_create") AS "Year"
            FROM 
                "patients" 
            WHERE 
                 (
                    (
                        {0} IS NOT NULL 
                         AND "date_create" > {0}::date
                    ) 
                     OR {0} IS NULL 
                )
            GROUP BY 
                "Date", "type", "Month", "Year"
	        ORDER BY 
	            "Year", "Month"
        '''

        query = query.format(date_start.strftime("""'%d.%m.%Y'""") if date_start else 'NULL')

        result = engine.engine.execute(query).fetchall()

        month_human_name = {
            1: 'янв.',
            2: 'февр.',
            3: 'март',
            4: 'апр.',
            5: 'май',
            6: 'июнь',
            7: 'июль',
            8: 'авг.',
            9: 'сент.',
            10: 'окт.',
            11: 'нояб.',
            12: 'дек.'
        }

        result_data = {}
        dates = []
        for row in result:
            date_statistic = '{} {}'.format(month_human_name.get(int(row[2].split('-')[0])),
                                            row[2].split('-')[1][2:])
            if date_statistic not in dates:
                dates.append(date_statistic)
            type_name = PATIENT_TYPE.get(int(row[0]))

            if type_name in result_data:
                result_data[type_name][date_statistic] = row[1]
            else:
                result_data[type_name] = {date_statistic: row[1]}

        all_result = {}
        for date in dates:
            for type_patient in result_data:
                result_data.get(type_patient)[date] = result_data.get(type_patient).get(date, 0)
                if date in all_result:
                    all_result[date] += result_data.get(type_patient)[date]
                else:
                    all_result[date] = result_data.get(type_patient)[date]

        results = {
            'labels': dates,
            'datasets': []
        }

        i = 0
        for key in result_data:
            Statistic._get_chart_data(dates, result_data.get(key), results, index_color=i, label=key)
            i += 1

        Statistic._get_chart_data(dates, all_result, results, index_color=-1, label='Все')

        return HttpQuery.HttpQueryHelpers.json_response(data=results)

    @staticmethod
    def _get_chart_data(dates: list, chart_data: dict, results: dict, *, label: str, index_color: int):
        background_color = ['#fa070732', '#fa07e232', '#1c07fa32', '#07fa8532']
        data = []

        for date in dates:
            data.append(chart_data.get(date))

        results['datasets'].append({'label': label, 'data': data, 'backgroundColor': background_color[index_color]})
