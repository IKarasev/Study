# 2. Знакомство с интерфейсом MXDR

## Фильтры по разделу «Алерты»

| Фильтр   | Описание    | Пример |
|--------------- | --------------- | --- |
| `company_name: «*»`   | поиск по компании | [пример](https://xdr.facct.ru/attacks/alerts?tab=new&search=company_name:+%22F.A.C.C.T.+Demo%22)   |
| `appliance_name: «*»`   | поиск по устройству/модулю (NTA, MDP, EDR) | [пример](https://xdr.facct.ru/attacks/alerts?tab=new&search=appliance_name:+%22FACCT+Demo+NTA+1000%22) |
| `reason: «*»`   | поиск по имени сигнатуры | [пример](https://xdr.facct.ru/attacks/alerts?tab=new&search=reason:+%22CURRENT_EVENTS+Balada+Domain+in+DNS+Lookup+(rdntocdns+.com)%22)   |
| `sid: *`   |  поиск по номеру сигнатуры | [пример](https://xdr.facct.ru/attacks/alerts?tab=all&search=sid:+1005172)   |
| `ioc.event.domains: «*»` | поиск по домену | [пример](https://xdr.facct.ru/attacks/alerts?search=+ioc.event.domains:+%22ndm2398asdlw.shop%22&tab=all) |
| `ioc.event.ip_addresses: «*»` | поиск по ip | [пример](https://xdr.facct.ru/attacks/alerts?search=+ioc.event.ip_addresses:+%2294.124.205.83%22&tab=all) |
| `sha1: «*» / sha256: «*» / md5: «*»` | поиск по хэшу файла (sha1, sha256, md5) | [пример](https://xdr.facct.ru/attacks/alerts?search=+ioc.event.ip_addresses:+%2294.124.205.83%22&tab=all) |
| `target_hostname: «*»` | поиск по задействованному хосту | [пример](https://xdr.facct.ru/attacks/alerts?search=target_hostname:+%22facct-demo.local%5C%5Cwin-3%22&tab=all) |
| `file_name: «*»` | поиск по имени файла | [пример](https://xdr.facct.ru/attacks/alerts?search=file_name:+%22*PingCastleAutoUpdater*%22&tab=all) |

### Комплексный запрос

https://xdr.facct.ru/investigation/network?t=now-1d&t=now&tab=session&search=company_name:+%22F.A.C.C.T.+Demo%22+AND+ip:+%5b%22185.125.190.49%22,+%2291.189.91.49%22

## Фильтры по разделу «Сетевые соединения»

| Наименование | Пример |
| -- | -- |
| Пример поиска по ip | [пример](https://xdr.facct.ru/investigation/network?t=now-1d&t=now&tab=session&search=company_name:+%22F.A.C.C.T.+Demo%22+AND+ip:+%5b%22185.125.190.49%22,+%2291.189.91.49%22) |
| Пример поиска с фильтрацией доменов | [пример](https://xdr.facct.ru/investigation/network?t=2024-09-05T14:00:00.000%2B03:00&t=2024-09-05T16:59:59.999%2B03:00&tab=dns&search=company_name:+%22F.A.C.C.T.+Demo%22+AND+domain:+%22*5crljypc.ru%22+AND+NOT+domain:+%5b%22*ubuntu.com%22,+%22*google.com%22,+%22*mxdr.ru%22,+%22*tcp.local%22,+%22*microsoft.com%22,+%22*facct.ru%22,+%22*windowsupdate.com%22,+%22*demo.local%22,+%22*office.com%22,+%22*cloudflare-dns.com%22) |
| Пример комплексного запроса по ip и исключенных доменов | [пример](https://xdr.facct.ru/investigation/network?t=2024-09-05T14:00:00.000%2B03:00&t=2024-09-05T16:59:59.999%2B03:00&tab=dns&search=company_name:+%22F.A.C.C.T.+Demo%22+AND+NOT+domain:+%5b%22*ubuntu.com%22,+%22*google.com%22,+%22*mxdr.ru%22,+%22*tcp.local%22,+%22*microsoft.com%22,+%22*facct.ru%22,+%22*windowsupdate.com%22,+%22*demo.local%22,+%22*office.com%22,+%22*cloudflare-dns.com%22%5d+AND+ip:+192.168.1.5) |

## Фильтры по разделу «События с хостов»


| Фильтр   | Описание    | Пример |
|--------------- | --------------- | --- |
| `Header.HostName: *`<br>`Header.MachineId: *` | поиск событий с определенного хоста | [пример](https://xdr.facct.ru/investigation/huntpoint-events?t=now-1d&t=now&tab=alerts&search=Header.HostName:+%22facct-demo.local%5C%5Cwin-3%22+AND+Header.MachineId:+%225F37AD45-AC22-1D54-0395-6D60845D754A%22)   |
| `filename: «**»` | поиск по имени файла | [пример](https://xdr.facct.ru/investigation/huntpoint-events?t=now-1w&t=now&tab=alerts&search=Header.HostName:+%22facct-demo.local%5C%5Cwin-3%22+AND+filename:+%22*PingCastle*%22+AND+sha1:*)   |
| `sha1: «*» / sha256: «*» / md5: «*»` | поиск по хэшу файла (sha1, sha256, md5) | [пример](https://xdr.facct.ru/investigation/huntpoint-events?t=now-1w&t=now&tab=alerts&search=Header.HostName:+%22facct-demo.local%5C%5Cwin-3%22+AND+filename:+%22*PingCastle*%22+AND+sha1:*)   |
| `Payload.FileZone.ZoneIdString: *` | поиск источника загрузки файла | [пример](https://xdr.facct.ru/investigation/huntpoint-events?tab=all&search=company_name:+%22F.A.C.C.T.+Demo%22+AND+filename:+%22*john-1.9.0-jumbo*%22+AND+Payload.FileZone.ZoneIdString:+*)   |
| `Payload.CommandLine: "* *"` | поиск по исполняемым командам | [пример1](https://xdr.facct.ru/investigation/huntpoint-events?tab=all&search=machine_id:+6E569CE0-9CA8-19F1-76EF-7773F3609066+AND+Payload.CommandLine:+%22*whoami*%22)<br>[пример2](https://xdr.facct.ru/investigation/huntpoint-events?tab=all&search=company_name:+%22F.A.C.C.T.+Demo%22++AND+Payload.CommandLine:+%22*cmd+/c+tasklist+/FI*%22+AND++Header.Type:+%2220%22)   |


