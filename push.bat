@echo off
chcp 65001 >nul
echo ========================================
echo   Paper Daily GitHub Push Script
echo ========================================
echo.
cd /d "%~dp0"
echo [1/4] Copying daily reports...
set DATE=%date:~0,4%-%date:~5,2%-%date:~8,2%
if exist "C:\Users\miclo\.qclaw\workspace\paper-pipeline\output\readable\paper_report_%DATE%.html" (
    copy "C:\Users\miclo\.qclaw\workspace\paper-pipeline\output\readable\paper_report_%DATE%.html" "daily_reports\%DATE%-arXiv.html" /Y
    echo [OK] Report copied: %DATE%-arXiv.html
)
echo.
echo [2/4] Staging files...
git add .
echo.
echo [3/4] Committing...
git commit -m "feat: Daily update - %DATE%"
echo.
echo [4/4] Pushing to GitHub...
git push origin main
echo.
echo ========================================
echo   Done! Check https://miclover0.github.io/paper-daily/
echo ========================================
pause
