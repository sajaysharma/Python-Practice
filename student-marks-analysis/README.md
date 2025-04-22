# Student Marks Analysis Project

This project generates and analyzes student marks data using NumPy and Matplotlib. It includes functionality for generating random student marks, analyzing the data, and visualizing the results.

## Project Structure

```
student-marks-analysis
├── data
│   └── students.csv          # CSV file containing student marks data
├── src
│   ├── generate_data.py      # Script to generate random student marks data
│   ├── analyze_data.py       # Script to analyze student marks data
│   └── plot_data.py          # Script to visualize student performance
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

### Generating Data

To generate the student marks data, run the following command:

```
python src/generate_data.py
```

This will create a `students.csv` file in the `data` directory with random student marks.

### Analyzing Data

To analyze the generated student marks data, use the following command:

```
python src/analyze_data.py
```

This script will load the data from `students.csv` and perform various analyses, such as calculating averages and identifying trends.

### Plotting Data

To visualize the analyzed data, run:

```
python src/plot_data.py
```

This will create various plots to represent student performance based on the analyzed data.

## Dependencies

This project requires the following Python packages:

- NumPy
- Matplotlib

Make sure to install these packages before running the scripts.

## License

This project is licensed under the MIT License.