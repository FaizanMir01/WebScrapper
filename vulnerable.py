import openpyxl
import subprocess

def run_sqlmap(url):
    try:
        # Run SQLMap as a subprocess
        process = subprocess.Popen(['sqlmap', '-u', url, '--batch'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # Check the output for indications of SQL injection vulnerabilities
        if "sql injection" in output.decode().lower():
            print(f"SQL Injection vulnerability found at {url}")
            # You can parse and print more detailed information from SQLMap output if needed
        else:
            print(f"No SQL Injection vulnerability found at {url}")
    except Exception as e:
        print(f"Error scanning {url} for SQL injection: {e}")

def main():
    # Load Excel file
    wb = openpyxl.load_workbook('test1.xlsx')
    sheet = wb.active

    # Iterate over rows and run SQLMap for each URL
    for row in sheet.iter_rows(values_only=True):
        if row[0]:  # Assuming URLs are in the first column
            url = row[0]
            run_sqlmap(url)

if __name__ == "__main__":
    main()
