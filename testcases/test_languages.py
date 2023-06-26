import time
import pytest
from pages.Assessment_page import Assessment
from pages.Carriersummary_page import Carrier
from pages.Cognitiveskills_page import CognitiveSkills
from pages.Languages_page import Language
from pages.SignUp_page import Signup
from pages.Welcome_page import Welcome
from pages.Personal_details_page import Personaldetails
from pages.Jobrole_page import JobRole
from pages.Project_page import Projects
from pages.Education_page import Education
from pages.Certificate_page import Certificate
from pages.Publication_page import Publication
from pages.Patents_page import Patent
from pages.VoluntaryRoles_page import VoluntaryRoles
from pages.HonorAwards_page import HonorAwards
from pages.Causes_page import Causes
from pages.Hobbies_page import Hobbies


# Variables
def variables():
    language = ["kannada", "english", "hindi"]
    proficiency = ["beg", "adv", "inter"]
    location = ["bangalore", "delhi", "561203"]
    companyname = ["IBM", "Google", "Cognizant"]
    jobtype = ["full time", "intern", "part time", "freelanc", "contract"]
    experience = ["Advanced Technologies", "IT Services", "Agri-business"]
    organization = ["startup", "small", "mnc"]
    based = ["product", "service", "both"]
    date = "25041999"
    month = ["jan", "feb", "march", "may", "june", "july"]
    year = ["1900", "1910", "1920", "1930", "1940", "2000", "2001", "2002"]
    designation = ["Developer", "Automation", "Manualtester", "frontend", "backend"]
    managementlevel = ["jun", "sen", "mid"]
    functionalarea = ["development", "human", "marketing"]
    skill = ["java", "python", "c prog", "automation", "php"]
    expertise = ["beg", "skil", "expert"]
    startsalary = ["12", "3213", "214"]
    endsalary = ["21433", "2136832", "812765"]
    degree = ["10th", "12th", "bsc", "mca", "phd"]
    university = ["bangalore", "delhi", "odisha"]
    hobbies = ["Romantic songs", "Cricket", "Cricket highlights", "Hill Climbing"]
    cgpa = ["7.89", "9.65", "5.98"]
    linkdin = "https://www.linkedin.com/in/amith-kulkarni-1326241b4"
    headline = "Automation Developer"
    firstname = "Amith"
    lastname = "talentPlace"
    description = ["Listing projects on your resume allows hiring managers", " It's important to list your most relevant projects on your resume.", "List the skills you want to highlight", "Think of the specific projects you want to include."]


@pytest.mark.usefixtures("setup")
class TestCases:
    # Login happens automatically using fixtures..!!![for all the forms]
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lang = Language(self.driver, self.wait)
        self.cog = CognitiveSkills(self.driver, self.wait)
        self.tass = Assessment(self.driver, self.wait)
        self.cas = Carrier(self.driver, self.wait)
        self.sup = Signup(self.driver, self.wait)
        self.wcl = Welcome(self.driver, self.wait)
        self.per = Personaldetails(self.driver, self.wait)
        self.job = JobRole(self.driver, self.wait)
        self.prj = Projects(self.driver, self.wait)
        self.edu = Education(self.driver, self.wait)
        self.cert = Certificate(self.driver, self.wait)
        self.pub = Publication(self.driver, self.wait)
        self.pat = Patent(self.driver, self.wait)
        self.vol = VoluntaryRoles(self.driver, self.wait)
        self.hon = HonorAwards(self.driver, self.wait)
        self.cau = Causes(self.driver, self.wait)
        self.hob = Hobbies(self.driver, self.wait)
    # def test_signUp(self): BCZ of  Line 25
    #     self.sup.sign_up(firstname, lastname, email, phone_no, dob, gender, location, password, confirm_password)

    def test_welcome_page(self):
        self.wcl.welcomepage()

    @pytest.mark.personaldetails
    def test_personal_details(self):
        for i in range(1):
            self.per.personaldetails(self.firstname, self.lastname, self.date, self.year[i], self.location[i], self.headline, self.linkdin)

    @pytest.mark.jobrole
    def test_jobrole(self):
        for i in range(3):
            self.job.addcompany(i, self.companyname[i], self.jobtype[i], self.experience[i], self.organization[i], self.based[i], self.designation[i], self.managementlevel[i], self.location[i], self.functionalarea[i], self.skill[i], self.expertise[i], self.year[i], self.year[i+1], self.startsalary[i], self.endsalary[i])
            self.job.next()

    @pytest.mark.projects
    def test_projects(self):
        self.prj.edit_profile()
        self.prj.click_projectdashboard()
        for j in range(3):
            self.prj.project(self.firstname, self.year[j], self.year[j+1], self.linkdin, self.description[j], self.skill[j], j, self.description[j])
        self.prj.next()

    @pytest.mark.education
    def test_education(self):
        self.edu.edit_profile()
        self.edu.click_educationdashboard()
        for i in range(3):
            self.edu.education(self.degree[i], self.university[i], self.location[i], self.cgpa[i], self.year[i], self.year[i+1], self.description[i], self.description[i+1])
        self.edu.next()
    @pytest.mark.certificate
    def test_certificate(self):
        self.cert.edit_profile()
        self.cert.click_certificatedashboard()
        for i in range(3):
            self.cert.certificate(self.designation[i], self.university[i], self.year[i], self.year[i+1], self.skill[i], self.description[i])
        self.cert.next()

    @pytest.mark.publication
    def test_publication(self):
        self.pub.edit_profile()
        self.pub.click_publicationdashboard()
        for i in range(3):
            self.pub.publication(self.companyname[i], self.year[i], self.date, self.linkdin, self.firstname, self.linkdin, self.description[i])
        self.pub.next()

    @pytest.mark.patent
    def test_patent(self):
        self.pat.edit_profile()
        self.pat.click_patentdashboard()
        for i in range(3):
            self.pat.patent(i, self.companyname[i], self.year[i], self.date, self.linkdin, self.firstname, self.linkdin, self.description[i])
        self.pub.next()

    @pytest.mark.voluntaryrole
    def test_voluntary_roles(self):
        self.vol.edit_profile()
        self.vol.click_voluntaryrolesdashboard()
        for i in range(3):
            self.vol.voluntaryroles(self.designation[i], self.companyname[i], self.year[i], self.year[i+1], self.description[i], )
        self.vol.next()

    @pytest.mark.honorawards
    def test_honorawards(self):
        self.hon.edit_profile()
        self.hon.click_honorawarddashboard()
        for i in range(3):
            self.hon.honorawards(i, self.designation[i], self.companyname[i], self.year[i], self.description[i])
        self.vol.next()
        self.vol.discrad()

    @pytest.mark.causes
    def test_causes(self):
        self.cau.edit_profile()
        self.cau.click_causesdashboard()
        self.cau.causes()

    @pytest.mark.hobbies
    def test_hobbies(self):
        self.hob.edit_profile()
        self.hob.click_hobbiesdashboard()
        for i in range(1, 4):
            self.hob.hobbies(i, self.hobbies[i])
        self.hob.next()

    @pytest.mark.languages
    def test_languages(self):
        for i in range(len(self.language)):
            self.lang.language(self.language[i], self.proficiency[i])
        self.lang.next()

    @pytest.mark.cognitiveskills
    def test_cognitive_skills(self):
        self.cog.edit_profile()
        self.cog.click_cognitiveskilldashboard()
        self.cog.cognitive()

    @pytest.mark.carriersummary
    def test_carrier(self):
        self.cas.carrier()

    @pytest.mark.assessment
    def test_assessment(self):
        self.tass.assessment()



