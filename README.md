# Test_Tenzor
Пункт 5 Тестового задания, Использование сторонних инструментов.
Для реализвации "красивых" отчетов о проведенном тестировании используется Allure.

Версия pyton - 3.9

Инструкция по установке и запуску тестов.

1. Установить Scoop ( https://scoop.sh/ ) 
1.1 В консоли PowerShell ввести "Set-ExecutionPolicy RemoteSigned -scope CurrentUser"
1.2 Ввести "Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')"
2. Ввести "scoop install allure" (Необходимо наличие java для дальнейшей работы)
3. Открыть проект в среде PyCharm
4. Установить библиотеки ( pip install -r requirements.txt ) и перезапустить проект(!)
5. В среде PyCharm открыть терминал и ввести "pytest --alluredir reportsallure" для непосредственного запуска тестов
6. После завершения ввести "allure serve reportsallure" для просмотра отчета 

