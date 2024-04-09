import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def getLinksFromCSV():
    # Open csv
    try:
        # with open('Test.csv', 'r') as file:
        with open('postings.csv', 'r') as file:
            reader = csv.DictReader(file)

            # If job_link column is missing in file return an error
            if 'job_link' not in reader.fieldnames:
                print(f"Error: 'job_link' column not found in the CSV file.")
                return None
            
            # Store all the links in a list
            listOfLinks = []
            for row in reader:
                link = row['job_link']
                listOfLinks.append(link)
            return listOfLinks

    # If file not found return an error    
    except FileNotFoundError:
        print("Error: File not found.")
        return None

'''
def scrapeLinkedin_AI(linkedin_url):
    # Send a GET request to the LinkedIn job page
    response = requests.get(linkedin_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the "About the job" section by its class name or other identifying feature
        about_job_section = soup.find('section', class_='jobs-description__content')  # Example class name, adjust as needed

        # Extract the text from the "About the job" section
        if about_job_section:
            about_job_text = about_job_section.get_text()
            return about_job_text
        else:
            return "About the job section not found on the page."

    else:
        return "Failed to retrieve the LinkedIn page. Status code: {}".format(response.status_code)
''' 

def scrapeLinkedin(url):
    # Send a GET request to the specified URL and store the response in the variable page.
    page = requests.get(url)
    # create a BeautifulSoup object, specifying html to parse contents of page.text
    soup = BeautifulSoup(page.text, 'html.parser')
    # Print parsed HTML document
    print(soup)
    # Specify soup jobs-description__content
    #jobAbout = soup.find_all('table', class_ = 'wikitable')[1]
    jobAbout = soup.find('article', class_='jobs-description__container')
    print(jobAbout)

'''
def LinkedinLogin(Path, Username, Password):
    # Creating a webdriver instance
    driver = webdriver.Chrome(Path)
    # This instance will be used to log into LinkedIn
    
    # Opening linkedIn's login page
    driver.get("https://linkedin.com/uas/login")
    
    # waiting for the page to load
    time.sleep(5)
    
    # entering username
    username = driver.find_element(By.ID, "username")
    
    # In case of an error, try changing the element
    # tag used here.
    
    # Enter Your Email Address
    username.send_keys(Username)  
    
    # entering password
    pword = driver.find_element(By.ID, "password")
    # In case of an error, try changing the element 
    # tag used here.
    
    # Enter Your Password
    pword.send_keys(Password)        
    
    # Clicking on the log in button
    # Format (syntax) of writing XPath --> 
    # //tagname[@attribute='value']
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # In case of an error, try changing the
    # XPath used here.
'''

def main():
    # Create list of Links from the csv file
    listOfLinks = getLinksFromCSV()
    '''
    if listOfLinks is not None:
        print("list of links: ", listOfLinks)
    '''

    print("Number of links: ", len(listOfLinks))

    # Scrape about job section from linkedin link
    linkedin_url = "https://www.linkedin.com/jobs/view/c%23-software-engineer-at-e-tech-group-3780474203/"
    #linkedin_url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
    scrapeLinkedin(linkedin_url)

    #about_job = scrapeLinkedin_AI(linkedin_url)
    #print(about_job)

    PATH = "C:\\Users\\Guill\\Downloads\\chromedriver"
    USERNAME = ""
    PASSWORD = ""
    #LinkedinLogin(PATH, USERNAME, PASSWORD)

if __name__ == "__main__":
    main()





