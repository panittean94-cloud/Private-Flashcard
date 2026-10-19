@echo off
chcp 65001 > nul
echo ========================================================
echo   ⚡ FunE Flashcard System - Push to GitHub Utility
echo ========================================================
echo.

cd /d "c:\Users\thana\Desktop\Private-Flashcard"

echo [1/3] Adding all updated files...
git add .

echo [2/3] Committing changes...
git commit -m "feat: complete master exam collection with 72 flashcards, circuit diagrams, and full solutions"

echo [3/3] Pushing to GitHub (panittean94-cloud/Private-Flashcard)...
git push origin main

echo.
echo ========================================================
if %ERRORLEVEL% EQU 0 (
    echo   ✅ SUCCESS! All flashcards and Excel pushed to GitHub.
    echo   🌐 Web App: https://panittean94-cloud.github.io/Private-Flashcard/
) else (
    echo   ❌ Error during push. Please check your network or credentials.
)
echo ========================================================
pause
