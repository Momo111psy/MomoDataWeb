# Navigate to project
cd C:\Users\rashi\MomoDataWeb

# Run the scraper first to get fresh data
python momo_scraper.py

# Push to GitHub
git add dubai_leads_sample.csv
git commit -m "Auto-Update: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
git push origin main

Write-Host "Website is now updated with real data!" -ForegroundColor Green
