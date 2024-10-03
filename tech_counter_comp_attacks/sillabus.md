# Технологии противодействия компьютерным атакам

Формат сдачи: **Зачет в формате лабораторной работы**

## Модули

1. [Основные принципы работы аналитика blue team](./01_Осн_принципы_раб_аналитика_blue_team.md)
1. [Компетенции аналитиков второй и третьей линии SOC](./02_Комп_аналитиков_2_3_линии_SOC.md)
1. [Основы мониторинга событий и построения SOC](./03_Основы_мон_соб_постр_SOC.md)
1. [Практическое изучение платформы MXDR](./04_Практическое_изучение_платформы_MXDR.md)

## Содержание дисциплины

<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Модуль</th>
            <th>Содержание дисциплины</th>
            <th>Баллы</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Основные принципы работы аналитика blue team</td>
            <td>
                <p><strong>
                    <ul>
                        <li>Основные термины и модели</li>
                        <li>Процессы в команде ИБ и моделирование угроз</li>
                        <li>Основные принципы логирования и мониторинга</li>
                        <li>Синтаксис Suricata</li>
                        <li>Основы реагирования на инциденты</li>
                        <li>Поиск устойчивых индикаторов компрометации, основы проактивного поиска угроз</li>
                    </ul>
                </strong></p>
                <p>
                    <ul>
                        <li>Классификация событий</li>
                        <li>Понятие кибератаки, инцидента и алерта</li>
                        <li>Модели Cyber KillChain, MitreAtt&ck</li>
                        <li>Пирамида боли Дэвида Бьянко</li>
                        <li>Основы детектирования и обработки событий</li>
                        <li>Основные подходы к мониторингу и фильтрации событий</li>
                        <li>Основные действия, порядки применения и структура написания правил</li>
                        <li>Альтернативные варианты созданию правил</li>
                        <li>Работа с отчетами</li>
                        <li>Правила формирования гипотез</li>
                    </ul>
                </p>
            </td>
            <td>14</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Компетенции аналитиков второй и третьей линии SOC</td>
            <td>
                <p><strong>
                    <ul>
                        <li>Цифровая криминалистика ОС Windows, ОЗУ, ОС Linux в рамках работы SOC</li>
                        <li>Основы анализа вредоносного программного обеспечения</li>
                        <li>Проактивный поиск угроз и масштабирование</li>
                    </ul>
                </strong></p>
                <p>
                    <ul>
                        <li>Основные артефакты и принципы их исследования</li>
                        <li>Специализированное программное обеспечение для исследования артефактов</li>
                        <li>Базовые принципы анализа ВПО</li>
                        <li>Анализ вредоносных скриптов</li>
                        <li>Анализ вредоносных офисных документов</li>
                        <li>Анализ ВПО с использованием песочниц и специализированного ПО</li>
                        <li>Использование программных решений для масштабирования логирования</li>
                    </ul>
                </p>
            </td>
            <td>20</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Основы мониторинга событий и построения SOC</td>
            <td>
                <p><strong>
                    <ul>
                        <li>Введение</li>
                        <li>Теоретические и методические основы мониторинга событий</li>
                        <li>Основные термины</li>
                        <li>Основы построения SOC</li>
                    </ul>
                </strong></p>
                <p>
                    <ul>
                        <li>Основы современной киберпреступности</li>
                        <li>История SOC</li>
                        <li>Взаимодействие команды SOC с другими командами</li>
                        <li>Обзор компонентов MXDR</li>
                        <li>Интерфейс MXDR</li>
                    </ul>
                </p>
            </td>
            <td>7</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Практическое изучение платформы MXDR</td>
            <td>
                <p><strong>
                    <ul>
                        <li>Изучение интерфейса MXDR</li>
                        <li>Работа с инцидентами</li>
                        <li>Практические основы работы с инцидентами с использованием программных сред</li>
                    </ul>
                </strong></p>
                <p>
                    <ul>
                        <li>Практическая работа с модулем NTA</li>
                        <li>Практическая работа с модулем MDP</li>
                        <li>Практическая работа с модулем EDR</li>
                        <li>Интерфейс ASM</li>
                    </ul>
                </p>
            </td>
            <td>28</td>
        </tr>
    </tbody>
</table>

## Система оценивания

Успешное освоение дисциплины предполагает:
- выполнение учебных заданий (текущая аттестация);
- сдачу зачета (итоговая аттестация).

Для допуска к экзамену необходимо выполнить все лабораторные работы.
- Максимальный балл, который можно получить в течение семестра, — 69 баллов.
- Максимальный балл за экзамен — 31 баллов.

## Рекомендуемые источники

- [OISF (2020, 11 сентября). Suricata User](https://docs.suricata.io/_/downloads/en/suricata-6.0.0-rc1/pdf/)
- [Осепов Б., Массерле А. (2021, 17 марта). Матрица ATT&CK. Как устроен язык описания угроз и как его используют](https://xakep.ru/2021/03/17/mitre-att-ck/)
- Johansen G. Digital Forensics and Incident Response. М.: Packt Publishing, 2017. 324 c.
- Sammons J. The Basics of Digital Forensics: The Primer for Getting Started in Digital Forensics. M.: Elsevier, 2012. 208 c.
- Luttgens J.T., Pepe M., Mandia K. Incident Response & Computer Forensics. M.: McGraw Hill Professional, 2014. 544 c.
- [Msuhanov M. (2021, 10 марта). $STANDARD_INFORMATION vs. $FILE_NAME](https://dfir.ru/2021/01/10/standard_information-vs-file_name/)
- [Harrison A. (2019, 1 октября). Available Artifacts - Evidence of Execution](https://blog.1234n6.com/2018/10/available-artifacts-evidence-of.html)
- [Бирюков А. (2023, 14 ноября). И снова про SIEM](https://habr.com/ru/companies/otus/articles/773430/)
- [Основной репозиторий правил SIGMA](https://github.com/SigmaHQ/sigma)
- [Hioureas V. (2018, 20 февраля) Encryption 101: a malware analyst’s primer](https://www.malwarebytes.com/blog/news/2018/02/encryption-101-malware-analysts-primer)
- Skulkin O. Windows Forensics Cookbook M.: Packt Publishing, 2017. 274 c.
- Ostrovskaya S., Skulkin O. Practical Memory Forensics, 2022. 304 c.
- [Berba P. (2022, 7 февраля). Hunting for Persistence in Linux: System Generators](https://pberba.github.io/security/2022/02/07/linux-threat-hunting-for-persistence-systemd-generators/)
