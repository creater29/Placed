# Placed

A job placement app that scrapes multiple job boards, extracts required skills using NLP, classifies experience level with machine learning, and allows flexible filtering and categorization of jobs.

## Features

- **Multi-site Scraping:** Configurable selectors for scraping multiple job boards.
- **Skill Extraction:** Utilizes NLP to extract required skills from job descriptions.
- **Experience Level Classification:** Categorizes jobs based on experience level.
- **Flexible Categorization:** Filter jobs by any extracted attribute.
- **Polite Scraping:** Supports delays between requests to avoid overloading sources.
- **Machine Learning:** Uses ML for advanced skill and experience classification.
- **User Interface (planned):** For easy filtering and visualization.
- **Scheduled Scraping (planned):** For regular, automatic job data updates.

## Getting Started

### Prerequisites

- Python 3.x
- (Dependencies to be listed here if requirements.txt/environment.yml is available)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/creater29/Placed.git
   cd Placed
   ```
2. (Install dependencies here if requirements.txt/environment.yml is available)

### Usage

- To run the core scraping/processing:
   ```bash
   python main.py
   ```
- To start the user interface (if implemented):
   ```bash
   python interface.py
   ```
- For machine learning components:
   ```bash
   python ml_components.py
   ```
- To run the dashboard (if HTML-based):
   - Open `dashboard.html` in your browser.

## Configuration

- Selectors for job boards and scraping behavior can be configured in the code.
- Job filters and ML model choices are customizable in their respective modules.

## Roadmap

- [ ] Multi-site scraping
- [ ] NLP skill extraction
- [ ] Experience level classification
- [ ] Improved ML for skill/experience
- [ ] User interface for filtering/visualization
- [ ] Scheduled scraping

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

(Choose a license and add here, e.g., MIT, Apache 2.0, etc.)

## Acknowledgements

- [spaCy](https://spacy.io/) or [NLTK](https://www.nltk.org/) for NLP (if used)
- [scikit-learn](https://scikit-learn.org/) for ML (if used)
