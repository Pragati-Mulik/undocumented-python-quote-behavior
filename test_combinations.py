# test_combinations.py
# Evaluates 36 combinations each for single quotes and double quotes

import csv

results = []

for quote in ["'", '"']:
    for open_q in range(1, 7):
        for close_q in range(1, 7):
            opening = quote * open_q
            closing = quote * close_q
            expr = opening + "hi" + closing
            try:
                val = eval(expr)
                results.append((quote, open_q, close_q, True, repr(val)))
            except Exception as e:
                results.append((quote, open_q, close_q, False, str(e)))

# Save to CSV
with open("quote_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote_Type", "Opening_Count", "Closing_Count", "Is_Valid", "Output_or_Error"])
    writer.writerows(results)