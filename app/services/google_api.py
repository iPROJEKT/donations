import copy
from datetime import datetime

from aiogoogle import Aiogoogle

from app.core import const
from app.core.config import settings


async def get_spreadsheet_body(
    locale: str = const.LOCALE,
    sheet_type: str = const.SHEERTYPE,
    sheet_id: int = const.SHEERTID,
    title: str = const.SHEET_TITLE,
    row_count: int = const.ROW_COUNT,
    column_count: int = const.COLUMN_COUNT,
    body: dict = const.SPREADSHEET_BODY
) -> dict:
    body['properties']['title'] = const.SPREADSHEET_TITLE.format(
        datetime.now().strftime(
            const.FORMAT
        )
    )
    body['properties']['locale'] = locale
    body['sheets'][0]['properties']['sheetType'] = sheet_type
    body['sheets'][0]['properties']['sheetId'] = sheet_id
    body['sheets'][0]['properties']['title'] = title
    body['sheets'][0]['properties']['gridProperties']['rowCount'] = row_count
    body['sheets'][0]['properties']['gridProperties']['columnCount'] = column_count
    return body


async def spreadsheets_create(
    wrapper_services: Aiogoogle
) -> str:
    service = await wrapper_services.discover('sheets', 'v4')
    return await wrapper_services.as_service_account(
        service.spreadsheets.create(json=await get_spreadsheet_body())
    )['spreadsheetId']


async def set_user_permissions(
    spreadsheet_id: str,
    wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': const.TYPE,
        'role': const.ROLE,
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields=const.FILDS_FOR_SERVIS_ACCOUNT
        )
    )


async def spreadsheets_update_value(
    spreadsheet_id: str,
    charity_projects: list,
    wrapper_services: Aiogoogle
) -> None:
    table = copy.deepcopy(const.TABLE_VALUES)
    table[0] = [const.A1, datetime.now().strftime(const.FORMAT)]
    service = await wrapper_services.discover('sheets', 'v4')
    for project in charity_projects:
        new_row = [
            str(project.name),
            str(project.close_date - project.create_date),
            str(project.description)
        ]
        table.append(new_row)
    update_body = {
        'majorDimension': const.TABLE_UPDATA,
        'values': table
    }
    if len(table) > const.ROW_COUNT:
        raise ValueError(const.ROW_COUNT_ERROR)
    if len(table) > const.COLUMN_COUNT:
        raise ValueError(const.COLUMN_COUNT_ERROR)
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=const.RANGE,
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
