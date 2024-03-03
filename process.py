import csv
import json

# Function to extract and transform answers
def transform_answers(input_csv_path, output_csv_path):
    try:
        with open(input_csv_path, mode='r', encoding='utf-8') as infile, \
                open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = ['consis_img', 'consis_text', 'overall']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in reader:
                # Parse the JSON string in 'Answer.taskAnswers'
                task_answers = json.loads(row['Answer.taskAnswers'])[0]
                
                # Map responses to the desired output
                output_row = {
                    'consis_img': task_answers['consis_img'],
                    'consis_text':  task_answers['consis_text'],
                    'overall': task_answers['overall']
                }
                
                # Write the transformed row to the new CSV
                writer.writerow(output_row)
    except Exception as e:
        print(f"An error occurred: {e}")

# Assuming your input CSV file is named 'input.csv'
input_csv_path = 'Batch_5193701_batch_results.csv'
output_csv_path = 'output.csv'

# Transform and write the answers
transform_answers(input_csv_path, output_csv_path)
