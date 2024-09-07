from flask import Flask, request, send_file
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def upload_file():
    return open('index.html').read()  # Loads the HTML page

@app.route('/compare', methods=['POST'])
def compare_files():
    # Get uploaded files
    file1 = request.files['file1']
    file2 = request.files['file2']

    # Load Excel files into pandas dataframes
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Compare the two files and find non-common elements
    difference = pd.concat([df1, df2]).drop_duplicates(keep=False)

    # Save the difference to a new Excel file
    output_file = "difference.xlsx"
    difference.to_excel(output_file, index=False)

    # Return the result file to the user
    return send_file(output_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
