# nutrition

I was volunteering at a food bank one day and wanted to see what nutrition was being handed out to clients.

I know tools like https://www.myfitnesspal.com/ exist and have nice user interfaces but the data is manually keyed in and perhaps not as complete as I would like. I wanted to see numbers that come from a definitive source and built http://www.tom.ae-web.ca for this purpose.

Data is pulled from the Canadian nutrient file and shows up to 152 nutrients.

You can see my working version at http://www.tom.ae-web.ca or construct your own.

***

Instructions:

download Canadian nutrient file in CSV format

https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/nutrient-data/canadian-nutrient-file-2015-download-files.html

run python script "create.py" based on CSV file inputs

move output files "labels.js" and "data.js" into ./js/ folder

open "index.html" in web browser



