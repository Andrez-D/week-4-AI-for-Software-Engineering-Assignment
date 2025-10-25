# 🤖 AI in Software Engineering Assignment

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Selenium](https://img.shields.io/badge/Selenium-4.10.0-43B02A.svg)](https://www.selenium.dev/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange.svg)](https://scikit-learn.org/)

> **Building Intelligent Software Solutions** - A comprehensive exploration of AI applications in modern software engineering, demonstrating automated code generation, intelligent testing, and predictive analytics.

---
## Screenshots
<img width="1366" height="768" alt="Screenshot (36)" src="https://github.com/user-attachments/assets/c0453ce6-7692-404b-9e03-6cb111633251" />

<img width="1366" height="768" alt="Screenshot (37)" src="https://github.com/user-attachments/assets/2df788c2-3870-48ff-a471-9a4f2b06e038" />


<img width="1366" height="768" alt="Screenshot (38)" src="https://github.com/user-attachments/assets/dff00c05-d32f-458d-b86a-2d7de03f17e3" />



<img width="1366" height="768" alt="Screenshot (39)" src="https://github.com/user-attachments/assets/7ab6083d-872d-43a2-b871-2fad81b64973" />



<img width="1366" height="768" alt="Screenshot (40)" src="https://github.com/user-attachments/assets/bfc48c66-c075-4501-8d47-7e712829df27" />


<img width="1366" height="768" alt="Screenshot (45)" src="https://github.com/user-attachments/assets/280140ea-4c8d-4c63-8779-cafda0c50abc" />


<img width="1366" height="768" alt="Screenshot (46)" src="https://github.com/user-attachments/assets/2b9b2b76-951d-4590-9e57-51c792696bf5" />


## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 🎯 Overview

This project demonstrates three critical applications of AI in software engineering:

1. **AI-Powered Code Completion**: Comparing manual vs. AI-generated code for efficiency and quality
2. **Automated Testing**: Intelligent test automation using Selenium with AI-enhanced strategies
3. **Predictive Analytics**: Machine learning models for resource allocation and priority prediction

### 🏆 Key Achievements

- ✅ **96.5% accuracy** on predictive analytics (exceeds 85% target)
- ✅ **40x faster** code generation with AI assistance
- ✅ **78% test automation** success rate with intelligent error detection
- ✅ **Comprehensive bias analysis** using IBM AI Fairness 360
- ✅ **Innovative AI tool proposal** (DocuGenius) for automated documentation


## ✨ Features

### Task 1: AI-Powered Code Completion

- 📝 Manual implementation with comprehensive error handling
- 🤖 AI-suggested implementations (5 variations)
- 📊 Performance benchmarking on 50,000 items
- 📈 Detailed comparison analysis (speed, quality, maintainability)

**Key Results:**
- Manual development time: 15-20 minutes
- AI development time: 30 seconds
- AI performance advantage: 8.5% faster execution

### Task 2: Automated Testing with Selenium

- 🧪 9 comprehensive test scenarios
- 🔍 Intelligent element detection with fallback strategies
- 📸 Automatic screenshot capture on failures
- 📋 Detailed JSON test reports
- 🛡️ Security testing (SQL injection, XSS attempts)

**Test Coverage:**
- ✓ Valid credentials
- ✓ Invalid username/password
- ✓ Empty fields
- ✓ SQL injection prevention
- ✓ XSS attack prevention

### Task 3: Predictive Analytics

- 🎯 Random Forest classifier for priority prediction
- 📊 6 comprehensive visualizations
- 🔬 5-fold cross-validation
- 💾 Model persistence for deployment
- 📈 Feature importance analysis

**Model Performance:**
- Accuracy: 96.5%
- Precision: 95.8%
- Recall: 96.2%
- F1-Score: 96.0%
- AUC-ROC: 0.989

### Bonus: DocuGenius AI Tool

- 📚 Automated documentation generation
- 💰 80% time savings on documentation
- 🔄 Real-time synchronization with code changes
- 🌍 Multi-language support (25+ languages)
- 📈 3,000-19,000% ROI for teams

---

## 📂 Project Structure

```
ai-software-engineering/
│
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── .gitignore                         # Git ignore rules
├── LICENSE                            # MIT License
│
├── part1_theory/                      # Theoretical Analysis (30%)
│   ├── theoretical_analysis.md       # Q1-Q3 answers
│   └── case_study_analysis.md        # AIOps analysis
│
├── task1_code_completion/            # Task 1: Code Completion (20%)
│   ├── manual_implementation.py      # Manual sorting function
│   ├── ai_suggested_implementation.py # AI-generated variations
│   ├── comparison_analysis.md        # 200-word comparison
│   └── README.md                     # Task-specific documentation
│
├── task2_automated_testing/          # Task 2: Selenium Testing (20%)
│   ├── selenium_login_test.py        # Main test framework
│   ├── testing_summary.md            # 150-word summary
│   ├── test_results/                 # Test outputs
│   │   ├── screenshots/              # Captured screenshots
│   │   └── reports/                  # JSON test reports
│   └── README.md                     # Task-specific documentation
│
├── task3_predictive_analytics/       # Task 3: ML Model (20%)
│   ├── resource_allocation_model.ipynb # Jupyter notebook
│   ├── data_preprocessing.py         # Data processing script
│   ├── model_evaluation.py           # Evaluation metrics
│   ├── models/                       # Saved models
│   │   ├── priority_prediction_model.pkl
│   │   └── feature_scaler.pkl
│   ├── visualizations/               # Generated charts
│   │   └── task3_predictive_analytics_results.png
│   └── README.md                     # Task-specific documentation
│
├── part3_ethics/                     # Ethical Analysis (10%)
│   ├── ethical_reflection.md         # Bias analysis
│   └── fairness_examples/            # IBM AIF360 examples
│
├── bonus/                            # Innovation Challenge (+10%)
│   ├── ai_tool_proposal.md           # DocuGenius proposal
│   └── architecture_diagram.png      # System architecture
│
├── report/                           # Final Report
│   ├── AI_Software_Engineering_Report.pdf
│   └── presentation_slides.pdf
│
├── docs/                             # Additional Documentation
│   ├── installation_guide.md         # Detailed setup instructions
│   ├── execution_guide.md            # How to run each task
│   ├── troubleshooting.md            # Common issues & solutions
│   └── api_documentation.md          # Code API reference
│
└── tests/                            # Unit tests (optional)
    ├── test_task1.py
    ├── test_task2.py
    └── test_task3.py
```

---

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Google Chrome** - [Download Chrome](https://www.google.com/chrome/)
- **ChromeDriver** - [Download ChromeDriver](https://chromedriver.chromium.org/downloads) (must match Chrome version)

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-software-engineering.git
cd ai-software-engineering

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Verify installation
python -c "import selenium; import sklearn; import pandas; print('✓ All packages installed successfully!')"
```

### ChromeDriver Setup

**Option 1: Automatic (Recommended)**
```python
# Uses webdriver-manager (already in requirements.txt)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

**Option 2: Manual**
```bash
# Download ChromeDriver matching your Chrome version
# https://chromedriver.chromium.org/downloads

# Add to PATH or place in task2_automated_testing/
chmod +x chromedriver  # Mac/Linux only
```

---

## 💻 Usage

### Task 1: Code Completion Analysis

Run manual and AI implementations, then compare results:

```bash
cd task1_code_completion

# Run manual implementation
python manual_implementation.py

# Run AI-suggested versions
python ai_suggested_implementation.py

# View comparison
cat comparison_analysis.md
```

**Expected Output:**
```
TASK 1: MANUAL IMPLEMENTATION - CODE COMPLETION
================================================================================
✓ All steps completed successfully!
- Test cases: 8
- Performance: O(n log n)
- Time: 42.3ms for 50,000 items
```

### Task 2: Automated Testing

Run comprehensive Selenium test suite:

```bash
cd task2_automated_testing

# Run all tests
python selenium_login_test.py

# View test report
cat test_results/reports/test_report_*.json
```

**Expected Output:**
```
🚀 STARTING AUTOMATED TEST SUITE
================================================================================

🧪 TEST: Valid Login
✅ TEST PASSED

🧪 TEST: Invalid Username  
✅ TEST PASSED

...

📊 TEST EXECUTION REPORT
Total Tests: 9
✅ Passed: 7 (77.8%)
❌ Failed: 2 (22.2%)
```

### Task 3: Predictive Analytics

Train and evaluate the machine learning model:

```bash
cd task3_predictive_analytics

# Option 1: Jupyter Notebook (Recommended)
jupyter notebook resource_allocation_model.ipynb

# Option 2: Python Script
python data_preprocessing.py
python model_evaluation.py
```

**Expected Output:**
```
PERFORMANCE METRICS
================================================================================
Testing Set:
  - Accuracy:  0.9649 (96.49%)
  - Precision: 0.9580 (95.80%)
  - Recall:    0.9620 (96.20%)
  - F1-Score:  0.9600 (96.00%)
  - AUC-ROC:   0.9890

✓ Target Achieved (>85% accuracy)
```

---

## 📊 Results

### Overall Performance Summary

| Task | Metric | Target | Achieved | Status |
|------|--------|--------|----------|--------|
| **Task 1** | Development Time | < 5 min | 30 sec | ✅ Exceeded |
| **Task 1** | Code Efficiency | Comparable | +8.5% faster | ✅ Exceeded |
| **Task 2** | Test Coverage | > 5 scenarios | 9 scenarios | ✅ Exceeded |
| **Task 2** | Success Rate | > 70% | 77.8% | ✅ Achieved |
| **Task 3** | Model Accuracy | > 85% | 96.5% | ✅ Exceeded |
| **Task 3** | F1-Score | > 0.80 | 0.96 | ✅ Exceeded |

### Detailed Findings

#### Task 1: Code Completion
- **Manual Implementation**: 
  - Development time: 15-20 minutes
  - Lines of code: 150+ (with tests)
  - Error handling: Comprehensive
  - Documentation: Complete

- **AI Implementation**:
  - Development time: 30 seconds
  - Lines of code: 2-50 (depending on version)
  - Performance: 8.5% faster (using `itemgetter`)
  - Limitation: Requires human review

#### Task 2: Automated Testing
- **9 Test Scenarios**: 
  - Valid login: ✅ PASS
  - Invalid username: ✅ PASS
  - Invalid password: ✅ PASS
  - Both invalid: ✅ PASS
  - Empty username: ✅ PASS
  - Empty password: ✅ PASS
  - Both empty: ✅ PASS
  - SQL injection: ❌ FAIL (expected - site not vulnerable)
  - XSS attempt: ❌ FAIL (expected - site not vulnerable)

- **Execution Time**: 45 seconds total
- **Screenshots Generated**: 9 images
- **Test Reports**: JSON format with detailed logs

#### Task 3: Predictive Analytics
- **Dataset**: 569 samples, 30 features
- **Model**: Random Forest (100 estimators, max_depth=10)
- **Training Time**: 12.3 seconds
- **Cross-Validation**: 5-fold CV score: 0.957 ± 0.018
- **Feature Importance**: Top 3 features identified
- **Deployment Ready**: Model saved and ready for production

#### Ethics Analysis
- **6 Types of Bias** identified in resource allocation
- **IBM AIF360** implementation strategies provided
- **Fairness Metrics**: Disparate Impact, Statistical Parity
- **Mitigation Techniques**: Pre/In/Post-processing approaches

#### Bonus: DocuGenius
- **Problem Solved**: Incomplete/outdated documentation
- **Time Savings**: 80% reduction in documentation time
- **ROI**: 3,000-19,000% depending on team size
- **Market Potential**: $62B annual problem in software industry

---

## 📚 Documentation

### Core Documentation

- **[Installation Guide](docs/installation_guide.md)** - Detailed setup instructions
- **[Execution Guide](docs/execution_guide.md)** - Step-by-step task execution
- **[Troubleshooting](docs/troubleshooting.md)** - Common issues and solutions
- **[API Documentation](docs/api_documentation.md)** - Code reference

### Theoretical Analysis

- **[Q1: AI Code Generation](part1_theory/theoretical_analysis.md#q1)** - Benefits and limitations
- **[Q2: ML in Bug Detection](part1_theory/theoretical_analysis.md#q2)** - Supervised vs unsupervised
- **[Q3: Bias Mitigation](part1_theory/theoretical_analysis.md#q3)** - UX personalization ethics
- **[Case Study: AIOps](part1_theory/case_study_analysis.md)** - Deployment automation

### Task-Specific Guides

- **[Task 1 README](task1_code_completion/README.md)** - Code completion details
- **[Task 2 README](task2_automated_testing/README.md)** - Testing framework guide
- **[Task 3 README](task3_predictive_analytics/README.md)** - ML model documentation

### Reports

- **[Final Report](report/AI_Software_Engineering_Report.pdf)** - Complete assignment submission
- **[Ethical Reflection](part3_ethics/ethical_reflection.md)** - Bias analysis and mitigation
- **[AI Tool Proposal](bonus/ai_tool_proposal.md)** - DocuGenius innovation proposal

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file for configuration (optional):

```bash
# Chrome settings
CHROME_HEADLESS=false
CHROME_WINDOW_SIZE=1920,1080

# Test settings
TEST_TIMEOUT=10
TEST_BASE_URL=https://practicetestautomation.com/practice-test-login/

# Model settings
MODEL_RANDOM_STATE=42
MODEL_N_ESTIMATORS=100
MODEL_MAX_DEPTH=10
```

### Custom Settings

Edit `config.py` to customize behavior:

```python
# config.py
class Config:
    # Task 1 settings
    BENCHMARK_SIZE = 50000
    
    # Task 2 settings
    SELENIUM_TIMEOUT = 10
    SCREENSHOT_ON_FAIL = True
    
    # Task 3 settings
    MODEL_TYPE = "RandomForest"
    TEST_SIZE = 0.2
    RANDOM_STATE = 42
```

---

## 🧪 Testing

Run unit tests to verify functionality:

```bash
# Install pytest
pip install pytest pytest-cov

# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Test Structure

```bash
tests/
├── test_task1.py           # Code completion tests
├── test_task2.py           # Selenium framework tests
├── test_task3.py           # ML model tests
└── conftest.py             # Pytest configuration
```

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Code Standards

- Follow PEP 8 style guide
- Add docstrings to all functions
- Include unit tests for new features
- Update documentation as needed

### Pull Request Checklist

- [ ] Code follows PEP 8 style
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts

---

## 🐛 Known Issues

| Issue | Status | Workaround |
|-------|--------|------------|
| ChromeDriver version mismatch | Open | Use webdriver-manager or download matching version |
| Selenium tests fail on slow connection | Open | Increase TIMEOUT in config |
| Jupyter kernel crashes on large dataset | Open | Reduce n_estimators or use script version |
| Model training slow on CPU | Expected | Use cloud GPU (Colab) or reduce dataset size |

---

## 📈 Future Enhancements

### Planned Features

- [ ] **Task 1**: Integration with GitHub Copilot API
- [ ] **Task 2**: Parallel test execution
- [ ] **Task 3**: Deep learning model comparison
- [ ] **General**: Docker containerization
- [ ] **General**: CI/CD pipeline with GitHub Actions

### Ideas for Extension

1. **Real-time Code Analysis**: Integrate with IDE for live suggestions
2. **Test Generation**: AI-powered test case generation
3. **Model Deployment**: REST API for priority predictions
4. **Dashboard**: Interactive web dashboard for monitoring
5. **Multi-language Support**: Extend beyond Python

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 [Your Team Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

### Tools & Technologies

- **[Selenium](https://www.selenium.dev/)** - Web automation framework
- **[scikit-learn](https://scikit-learn.org/)** - Machine learning library
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation
- **[Matplotlib](https://matplotlib.org/)** & **[Seaborn](https://seaborn.pydata.org/)** - Visualization
- **[Jupyter](https://jupyter.org/)** - Interactive computing

### Data Sources

- **[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/)** - Breast Cancer dataset
- **[Practice Test Automation](https://practicetestautomation.com/)** - Test website

### Inspiration & References

- GitHub Copilot documentation
- IBM AI Fairness 360 toolkit
- Netflix and Google AIOps case studies
- Course materials and lectures

### Special Thanks

- Course instructor for guidance and feedback
- Teaching assistants for technical support
- Team members for collaboration
- Open-source community for excellent tools

---

## 📞 Contact & Support

### Get Help

- **Issues**: [GitHub Issues](https://github.com/Andrez-D/ai-software-engineering/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Andrez-D/ai-software-engineering/discussions)
- **Email**: rutoandrew06@gmail.com
- **PLP LMS Community**: Tag `#AISoftwareAssignment`


---

## 📊 Project Statistics

![GitHub repo size](https://img.shields.io/github/repo-size/Andrez-D/ai-software-engineering)
![GitHub last commit](https://img.shields.io/github/last-commit/Andrez-D/ai-software-engineering)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Andrez-D/ai-software-engineering)

**Project Metrics:**
- **Total Lines of Code**: ~2,500
- **Test Coverage**: 85%
- **Documentation Pages**: 12
- **Code Files**: 15
- **Dependencies**: 20 packages
- **Development Time**: 40 hours (team)

---

## 🎓 Educational Value

This project demonstrates proficiency in:

✅ **AI/ML Engineering**: Model training, evaluation, deployment  
✅ **Software Testing**: Automated testing, test frameworks  
✅ **Data Science**: Data preprocessing, visualization, analysis  
✅ **Ethical AI**: Bias detection, fairness metrics, mitigation  
✅ **Software Engineering**: Code quality, documentation, version control  
✅ **Problem Solving**: Real-world application of AI techniques  
✅ **Communication**: Technical writing, presentation skills  

---

## 🌟 Star History

If you found this project helpful, please consider giving it a ⭐!

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_USERNAME/ai-software-engineering&type=Date)](https://star-history.com/#YOUR_USERNAME/ai-software-engineering&Date)

---

## 📝 Changelog

### Version 1.0.0 (October 2025)
- ✨ Initial release
- ✅ Task 1: Code completion analysis
- ✅ Task 2: Selenium automated testing
- ✅ Task 3: Predictive analytics model
- ✅ Ethics: Bias analysis with IBM AIF360
- ✅ Bonus: DocuGenius AI tool proposal
- 📚 Complete documentation
- 🎥 Video demonstration

---

<div align="center">

**Made with ❤️ by [Kipruto Andrew Kipngetich]**

[⬆ Back to Top](#-ai-in-software-engineering-assignment)

</div>
