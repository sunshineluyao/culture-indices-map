# Cultural Values Comparison Dashboard

This repository hosts a Dash application that visualizes comparative analyses of cultural values derived from two sources:

- **Survey Data**: Original survey data by Haerpfer et al. (2022).
- **ChatGPT Simulations**: Responses from ChatGPT simulating an average individual in each country/region.

The dashboard presents differences and absolute differences in traditional vs. secular values and survival vs. self-expression values across various countries and regions.

## Features

- **Interactive Maps**: Explore choropleth maps displaying cultural value differences and absolute differences.
- **Tab Navigation**: Easily switch between different comparative maps using tabs.
- **Responsive Design**: The application is built with Dash and Bootstrap, ensuring compatibility across devices.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd your-repo
   ```

3. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that the `requirements.txt` file includes all necessary packages, such as `pandas`, `dash`, `dash-bootstrap-components`, and `plotly`.

5. **Prepare the Data**:

   Place the `updated_merged_data.csv` file in the `data` directory. Ensure the file is properly formatted and contains the necessary columns for the application to function correctly.

## Usage

Run the application locally:

```bash
python app.py
```

By default, the app will be accessible at `http://127.0.0.1:8050/` in your web browser.

## File Structure

```
your-repo/
├── app.py
├── assets/
│   └── custom_styles.css
├── data/
│   └── updated_merged_data.csv
├── requirements.txt
└── README.md
```

- `app.py`: Main application script.
- `assets/custom_styles.css`: Custom CSS for styling the application.
- `data/updated_merged_data.csv`: Dataset used for generating the visualizations.
- `requirements.txt`: List of Python dependencies.
- `README.md`: This file.

## References

- Haerpfer, C., Inglehart, R., Moreno, A., Welzel, C., Kizilova, K., Diez-Medrano J., Lagos, M., Norris, P., Ponarin, E., & Puranen, B. (eds.). (2022). World Values Survey: Round Seven - Country-Pooled Datafile Version 5.0. Madrid, Spain & Vienna, Austria: JD Systems Institute & WVSA Secretariat. DOI: 10.14281/18241.24
- Inglehart, R., & Welzel, C. (2005). Modernization, cultural change, and democracy: The human development sequence. Cambridge University Press.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

