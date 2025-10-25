"""
Task 2: Automated Testing with AI
Framework: Selenium WebDriver
Objective: Automate login page testing (valid/invalid credentials)
Author: [Kipruto Andrew Kipngetich]
Date: October 2025
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import json
from datetime import datetime

class LoginTestAutomation:
    """
    Automated testing class for login page functionality.
    Simulates AI-enhanced testing with intelligent wait strategies and error detection.
    """
    
    def __init__(self, base_url="https://practicetestautomation.com/practice-test-login/"):
        """
        Initialize the test automation framework.
        
        Args:
            base_url: URL of the login page to test
        """
        self.base_url = base_url
        self.driver = None
        self.test_results = []
        self.setup_driver()
    
    def setup_driver(self):
        """Configure and initialize Chrome WebDriver with options."""
        print("🔧 Setting up Chrome WebDriver...")
        
        chrome_options = Options()
        # Uncomment for headless mode (no browser window)
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Suppress unnecessary logs
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.implicitly_wait(10)
            print("✅ WebDriver initialized successfully")
        except Exception as e:
            print(f"❌ Error initializing WebDriver: {e}")
            print("💡 Make sure ChromeDriver is installed and in PATH")
            raise
    
    def navigate_to_login(self):
        """Navigate to the login page."""
        print(f"\n🌐 Navigating to: {self.base_url}")
        self.driver.get(self.base_url)
        time.sleep(1)  # Allow page to load
        print("✅ Page loaded successfully")
    
    def find_element_safe(self, by, value, timeout=10):
        """
        Safely find element with explicit wait (AI-enhanced pattern).
        
        Args:
            by: Selenium By locator type
            value: Locator value
            timeout: Maximum wait time in seconds
            
        Returns:
            WebElement or None
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"⚠️  Timeout: Element not found - {value}")
            return None
    
    def test_login(self, username, password, expected_result, test_name):
        """
        Execute a single login test case.
        
        Args:
            username: Username to enter
            password: Password to enter
            expected_result: "success" or "failure"
            test_name: Descriptive name for the test
            
        Returns:
            dict: Test result details
        """
        print(f"\n{'='*70}")
        print(f"🧪 TEST: {test_name}")
        print(f"{'='*70}")
        
        start_time = time.time()
        result = {
            "test_name": test_name,
            "username": username,
            "password": "****" if password else "",
            "expected": expected_result,
            "actual": None,
            "status": "FAIL",
            "duration": 0,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "screenshot": None,
            "error_message": None
        }
        
        try:
            # Navigate to login page
            self.navigate_to_login()
            
            # Find username field (AI would learn these selectors)
            print("🔍 Locating username field...")
            username_field = self.find_element_safe(By.ID, "username")
            if not username_field:
                raise Exception("Username field not found")
            
            # Find password field
            print("🔍 Locating password field...")
            password_field = self.find_element_safe(By.ID, "password")
            if not password_field:
                raise Exception("Password field not found")
            
            # Find submit button
            print("🔍 Locating submit button...")
            submit_button = self.find_element_safe(By.ID, "submit")
            if not submit_button:
                raise Exception("Submit button not found")
            
            # Enter credentials
            print(f"⌨️  Entering username: {username}")
            username_field.clear()
            username_field.send_keys(username)
            
            print(f"⌨️  Entering password: {'*' * len(password) if password else ''}")
            password_field.clear()
            password_field.send_keys(password)
            
            # Click submit
            print("🖱️  Clicking submit button...")
            submit_button.click()
            
            # Wait for response (AI learns optimal wait times)
            time.sleep(2)
            
            # Analyze result
            print("🔍 Analyzing page response...")
            
            # Check for success indicators
            success_detected = self.check_login_success()
            
            # Check for error messages
            error_detected = self.check_login_error()
            
            # Determine actual result
            if success_detected:
                result["actual"] = "success"
                print("✅ Login successful - redirected to dashboard")
            elif error_detected:
                result["actual"] = "failure"
                print("❌ Login failed - error message displayed")
            else:
                result["actual"] = "unknown"
                print("⚠️  Unable to determine login result")
            
            # Compare with expected result
            if result["actual"] == expected_result:
                result["status"] = "PASS"
                print(f"✅ TEST PASSED: Got expected result '{expected_result}'")
            else:
                result["status"] = "FAIL"
                result["error_message"] = f"Expected {expected_result}, got {result['actual']}"
                print(f"❌ TEST FAILED: Expected '{expected_result}', got '{result['actual']}'")
            
            # Take screenshot
            screenshot_name = f"test_{test_name.replace(' ', '_')}_{int(time.time())}.png"
            self.driver.save_screenshot(screenshot_name)
            result["screenshot"] = screenshot_name
            print(f"📸 Screenshot saved: {screenshot_name}")
            
        except Exception as e:
            result["status"] = "ERROR"
            result["error_message"] = str(e)
            print(f"❌ TEST ERROR: {e}")
        
        finally:
            # Calculate duration
            end_time = time.time()
            result["duration"] = round(end_time - start_time, 2)
            print(f"⏱️  Test duration: {result['duration']} seconds")
            
            # Store result
            self.test_results.append(result)
        
        return result
    
    def check_login_success(self):
        """
        Check if login was successful (AI pattern: multiple success indicators).
        
        Returns:
            bool: True if success detected
        """
        try:
            # Method 1: Check for success URL
            current_url = self.driver.current_url
            if "logged-in-successfully" in current_url or "dashboard" in current_url:
                return True
            
            # Method 2: Check for success message element
            success_element = self.driver.find_element(By.CLASS_NAME, "post-title")
            if success_element and "successfully" in success_element.text.lower():
                return True
            
            # Method 3: Check for logout button (indicates logged in)
            logout_button = self.driver.find_elements(By.LINK_TEXT, "Log out")
            if logout_button:
                return True
            
        except NoSuchElementException:
            pass
        
        return False
    
    def check_login_error(self):
        """
        Check if login error occurred (AI pattern: detect various error types).
        
        Returns:
            bool: True if error detected
        """
        try:
            # Method 1: Check for error message element
            error_element = self.driver.find_element(By.ID, "error")
            if error_element and error_element.is_displayed():
                print(f"   Error message: {error_element.text}")
                return True
            
            # Method 2: Check for generic error indicators
            error_classes = ["error", "alert-error", "login-error"]
            for error_class in error_classes:
                elements = self.driver.find_elements(By.CLASS_NAME, error_class)
                if elements and any(e.is_displayed() for e in elements):
                    return True
            
        except NoSuchElementException:
            pass
        
        return False
    
    def run_test_suite(self):
        """
        Execute comprehensive test suite with various scenarios.
        AI would learn these test cases from historical bugs.
        """
        print("\n" + "="*70)
        print("🚀 STARTING AUTOMATED TEST SUITE")
        print("="*70)
        
        # Test cases (AI would generate these based on requirements)
        test_cases = [
            # Valid credentials
            ("student", "Password123", "success", "Valid Login"),
            
            # Invalid username
            ("invaliduser", "Password123", "failure", "Invalid Username"),
            
            # Invalid password
            ("student", "wrongpassword", "failure", "Invalid Password"),
            
            # Both invalid
            ("wronguser", "wrongpass", "failure", "Invalid Credentials"),
            
            # Empty username
            ("", "Password123", "failure", "Empty Username"),
            
            # Empty password
            ("student", "", "failure", "Empty Password"),
            
            # Both empty
            ("", "", "failure", "Empty Credentials"),
            
            # SQL injection attempt (security test)
            ("admin' OR '1'='1", "password", "failure", "SQL Injection Attempt"),
            
            # XSS attempt (security test)
            ("<script>alert('XSS')</script>", "password", "failure", "XSS Attempt"),
        ]
        
        # Run all tests
        for username, password, expected, name in test_cases:
            self.test_login(username, password, expected, name)
            time.sleep(1)  # Brief pause between tests
        
        # Generate test report
        self.generate_report()
    
    def generate_report(self):
        """Generate comprehensive test report with AI-style insights."""
        print("\n" + "="*70)
        print("📊 TEST EXECUTION REPORT")
        print("="*70)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for r in self.test_results if r["status"] == "PASS")
        failed_tests = sum(1 for r in self.test_results if r["status"] == "FAIL")
        error_tests = sum(1 for r in self.test_results if r["status"] == "ERROR")
        
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        print(f"\n📈 Summary:")
        print(f"   Total Tests: {total_tests}")
        print(f"   ✅ Passed: {passed_tests}")
        print(f"   ❌ Failed: {failed_tests}")
        print(f"   ⚠️  Errors: {error_tests}")
        print(f"   📊 Success Rate: {success_rate:.1f}%")
        
        total_duration = sum(r["duration"] for r in self.test_results)
        avg_duration = total_duration / total_tests if total_tests > 0 else 0
        print(f"   ⏱️  Total Duration: {total_duration:.2f}s")
        print(f"   ⏱️  Average Duration: {avg_duration:.2f}s")
        
        # Detailed results
        print(f"\n📋 Detailed Results:")
        print("-" * 70)
        for result in self.test_results:
            status_icon = "✅" if result["status"] == "PASS" else "❌" if result["status"] == "FAIL" else "⚠️"
            print(f"\n{status_icon} {result['test_name']}")
            print(f"   Username: {result['username']}")
            print(f"   Expected: {result['expected']}")
            print(f"   Actual: {result['actual']}")
            print(f"   Duration: {result['duration']}s")
            if result["error_message"]:
                print(f"   Error: {result['error_message']}")
        
        # Save results to JSON
        report_filename = f"test_report_{int(time.time())}.json"
        with open(report_filename, 'w') as f:
            json.dump(self.test_results, f, indent=2)
        print(f"\n💾 Report saved to: {report_filename}")
        
        # AI-style insights
        print(f"\n🤖 AI-Powered Insights:")
        if success_rate == 100:
            print("   ✅ All tests passed! Login functionality is working correctly.")
        elif success_rate >= 80:
            print("   ⚠️  Most tests passed, but some edge cases need attention.")
        else:
            print("   ❌ Multiple failures detected. Critical issues require immediate fix.")
        
        if avg_duration > 5:
            print("   ⚠️  Page load times are slow. Consider performance optimization.")
        else:
            print("   ✅ Page response times are within acceptable range.")
    
    def cleanup(self):
        """Close browser and cleanup resources."""
        if self.driver:
            print("\n🧹 Cleaning up...")
            self.driver.quit()
            print("✅ Browser closed successfully")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*70)
    print("TASK 2: AUTOMATED TESTING WITH SELENIUM")
    print("="*70)
    print("\nThis script demonstrates AI-enhanced automated testing:")
    print("- Intelligent element location")
    print("- Smart wait strategies")
    print("- Comprehensive test coverage")
    print("- Detailed reporting with insights")
    
    tester = None
    
    try:
        # Initialize test framework
        tester = LoginTestAutomation()
        
        # Run full test suite
        tester.run_test_suite()
        
        print("\n" + "="*70)
        print("✅ TEST SUITE COMPLETED SUCCESSFULLY")
        print("="*70)
        
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Always cleanup
        if tester:
            tester.cleanup()
    
    print("\n💡 To run manually:")
    print("   python selenium_login_test.py")
    print("\n📚 Requirements:")
    print("   pip install selenium")
    print("   Download ChromeDriver: https://chromedriver.chromium.org/")