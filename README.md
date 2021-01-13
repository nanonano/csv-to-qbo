csv-to-qbo
==========

Converts CSV exports from Paypal to a CSV format that QuickBooks Online understands.

Paypal Download
---------------

1. In your Paypal account, browse to the Activity → All transactions -> Download.
2. Select the CSV Format and either download a time range or use the Last Download to Present option. Either way, you'll end up with a CSV file (probably called `Download.CSV`).

Convert
-------

1. Run `python paypal2qbo.py Download.CSV` (note that if you have multiple CSV files from Paypal you can add specify them all). The script will output a file named `QuickBooksOutput.csv`.
2. If you only want to output the fees do `python paypal2qbo.py --fees Download.CSV`.

QuickBooks Online Upload
------------------------

1. In your Quickbooks Online account, go to the account you want to import transactions into.
2. Click the arrow next to the "Update" button in the upper right and select "File Upload".
3. Click the Browse button and find the `QuickBooksOutput.csv` file generated above.
