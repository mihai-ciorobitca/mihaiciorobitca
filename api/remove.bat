@echo off

REM Remove Pingendo code from HTML files using PowerShell
for /r %%f in (*.html) do (
    powershell -Command "(Get-Content '%%f' -Raw) -replace '<pingendo.*?</pingendo>', '' | Set-Content '%%f'"
)