import csv
import argparse
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='+', type=argparse.FileType('r', encoding='utf-8-sig'))
    parser.add_argument('--fees',
                        action='store_true',
                        help="only add fees")
    args = parser.parse_args()

    transactions = []
    for f in args.infile:
        for line in csv.DictReader(f):

            # The single line has a gross payment and a fee payment, so we need to split those apart
            tstamp = time.strptime('{Date} {Time}'.format(**line), '%m/%d/%Y %H:%M:%S')

            # This is the "gross" payment
            if not args.fees:
                transactions.append((
                    tstamp,
                    '{Type} for {Item Title} from {Name}'.format(**line),
                    line['Gross'].replace(',', '')
                ))

            if line['Fee'] != '0.00':
                transactions.append((
                    tstamp,
                    '{Type} for {Item Title} from {Name} (PayPal fees)'.format(**line),
                    line['Fee'].replace(',', '')
                ))

    with open('QuickBooksOutput.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['Date', 'Description', 'Amount'])
        writer.writeheader()

        for txn in sorted(transactions, key=lambda l: time.mktime(l[0])):
            writer.writerow({
                'Date': time.strftime('%m/%d/%Y', txn[0]),
                'Description': txn[1],
                'Amount': txn[2]
            })


if __name__ == '__main__':
    main()
