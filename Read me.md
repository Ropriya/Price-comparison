# E-Pharmacy Price Comparison System

## Overview
A Streamlit-based web application that helps users compare medicine prices across multiple online pharmacies in India. The system uses Google Shopping API to fetch real-time prices and displays the best deals with interactive visualizations.

## Features
- **Real-time Price Comparison**: Fetches current medicine prices from various online sources
- **Best Price Identification**: Automatically identifies and highlights the lowest price option
- **Multiple Options Display**: Shows user-specified number of price options
- **Visual Comparisons**: Provides bar chart and pie chart visualizations
- **Direct Purchase Links**: Includes clickable links to buy from each source
- **Medicine Image Display**: Shows product thumbnail for reference

## Technology Stack
- **Python 3.x**
- **Streamlit**: Web application framework
- **SerpAPI**: Google Shopping search integration
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Ropriya/e-pharmacy-price-comparison.git
cd e-pharmacy-price-comparison
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Add E-Pharmacy logo**
- Place your logo image as `E-pharmacy logo.png` in the project root directory

4. **Configure API Key**
- Get your SerpAPI key from [serpapi.com](https://serpapi.com/)
- Replace the API key in `app.py`:
```python
"api_key": "YOUR_API_KEY_HERE"
```

## Usage

1. **Run the application**
```bash
streamlit run app.py
```

2. **Enter medicine details**
   - Input the medicine name in the sidebar
   - Specify the number of price options to display
   - Click "Price compair" button

3. **View results**
   - Browse through different price options
   - Check the "Best option" section for lowest price
   - Review bar chart and pie chart comparisons
   - Click on purchase links to buy

## Application Interface

### Sidebar
- Medicine name input field
- Number of options input field
- Price comparison button
- Medicine thumbnail display

### Main Content
- **Option sections**: Displays each price option with:
  - Company/Source name
  - Medicine title
  - Price
  - Buy link
- **Best option section**: Highlights the lowest price offer
- **Chart comparison**: Bar chart showing price distribution
- **Pie chart**: Visual price breakdown by company

## Dependencies

```
google_search_results==2.4.2
pandas==2.2.3
serpapi==0.1.5
streamlit==1.35.0
google-serp-api
googlesearch-python
matplotlib
```

## File Structure
```
e-pharmacy-price-comparison/
│
├── app.py                    # Main application file
├── requirements.txt          # Project dependencies
├── E-pharmacy logo.png       # Application logo
└── README.md                # Project documentation
```

## Key Functions

### `compare(med_name)`
- Fetches medicine prices using Google Shopping API
- Parameters: Medicine name
- Returns: Shopping results with prices, sources, and links

## Features Breakdown

### Price Comparison
- Searches across multiple online pharmacy sources
- Displays prices in Indian Rupees (₹)
- Automatically filters and sorts results

### Best Price Detection
- Compares all fetched prices
- Identifies the lowest price option
- Highlights best deal for user convenience

### Visual Analytics
- **Bar Chart**: Easy comparison of prices across sources
- **Pie Chart**: Proportional view of price distribution

## Limitations
- Requires active internet connection
- API rate limits may apply
- Results depend on SerpAPI availability
- Limited to Indian market (gl="in" parameter)

## Future Enhancements
- Add filters for medicine type/category
- Include user reviews and ratings
- Add price history tracking
- Implement medicine alternatives suggestion
- Add notification for price drops
- Multi-language support

## Troubleshooting

### Common Issues

**API Key Error**
- Verify your SerpAPI key is valid
- Check API usage limits

**No Results Found**
- Check medicine name spelling
- Try alternative medicine names
- Verify internet connection

**Image Not Displaying**
- Ensure `E-pharmacy logo.png` exists in root directory
- Check file name and path

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## License
This project is open-source and available for educational purposes.

## Author
**Rohit Ranjan**
- GitHub: [github.com/Ropriya](https://github.com/Ropriya)
- LinkedIn: [linkedin.com/in/contact-rohit-ranjan](https://linkedin.com/in/contact-rohit-ranjan)

## Disclaimer
This tool is for informational purposes only. Always verify medicine details and prices before purchase. Consult healthcare professionals for medical advice.
