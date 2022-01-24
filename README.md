# Hackfest-EasyAccessPatientRecord

## Introduction
This application that can be used by doctors and patients. The application provides role-based access to doctors, patients, and admin. All the medical records of patients are stored securely. Once a record is created and saved then it can be accessed by both patients and doctors. Doctors can log in to view all the patient’s profiles, and add prescriptions to them. The Doctor can also view all the registered medicines on the portal along with their details. The patients can view all the doctors. A patient's record can only be viewed either by the doctor or the patient itself.

## Project Overview
1. **Home Page** is a page that displays some basic stats about the website and helps in welcoming the user to a universal dashboard that has direct links to various personalized sections of the website.
![image](https://user-images.githubusercontent.com/42884781/150816900-d27f22a8-7d14-4846-a375-c9f34d2a3a26.png)

2. **Doctor Sign** Up is a page that is used by the doctor to register an account by entering some basic
details like his name, email id, contact, selecting his department and choosing a secure password.
![image](https://user-images.githubusercontent.com/42884781/150817031-7d335ba5-6c3d-4bca-b116-10e21230b31e.png)

3. **Common Sign In** is a page that is used by both a doctor and a patient to log in into his account and
access his information and perform various tasks available at hand. The page authenticates the
login credentials and redirects the user who is either a doctor or a patient to their respective
homepages depending on their account type.
![image](https://user-images.githubusercontent.com/42884781/150817901-9bce2c42-9480-4227-8fe0-0a13c84c3c28.png)

4. **Doctor Home Page** serves as a dashboard to the doctor where he has options to perform a bunch
of tasks like viewing all the patients, the list of available medicines that are registered on the
platform, his personal profile as well as an option to go ahead and prescribe his patient.
![image](https://user-images.githubusercontent.com/42884781/150817862-226be167-f501-4de1-95c8-f7f170a1e8bd.png)

5. **All Registered Patients page** is used by a doctor to see a list of all the patients who have registered
themselves on the platform. There are further options available to a doctor to view the patient’s
full profile including his prescription history in details as well as an option to prescribe him if the
need be.
![image](https://user-images.githubusercontent.com/42884781/150817835-aab3274f-b571-4dc1-9ac8-7a4fedf9d647.png)

6. **Patient’s Profile** page is a page that displays all the basic as well as any medical information and the
prescription history of a patient in one single page. The basic details of the patient include his
name, contact, addresses and any medical history, while his medical information includes his
height, weight, allergic conditions and more. The prescription history shows all the list of
prescriptions he may have received on the platform from various doctors and if the need be, there
is an option to take a detailed look at individual prescriptions by clicking on the View button below
each prescription.
![image](https://user-images.githubusercontent.com/42884781/150817804-7a5a0825-f70f-4dcb-a4d2-fa328b54ecef.png)

7. **Add Prescription** page is used by a doctor to prescribe a patient. The doctor has to select some
basic details like date of visit, reason for visit, remarks on the patient’s health and more. The doctor
is also given an option to add multiple medicines by clicking on Add Medicine button. For every
medicine, the doctor needs to detail the dosage data and the duration of intake for the same.
![image](https://user-images.githubusercontent.com/42884781/150817768-94211176-4b14-40de-a4ba-5ee5632dd5b5.png)

8. **View all Medicine** page helps doctor take a look at all the registered medicines on the platform.
There is also an option to look into the details like composition of individual medicines.
![image](https://user-images.githubusercontent.com/42884781/150817740-56fe8163-cae2-43fa-9395-92aed0a33b13.png)

9. **Doctor’s Profile** page shows the doctor his basic information like his name, email, contact and
more. The page also consists of each and every prescription that a particular doctor has ever made
and there’s always an option to look for any of these prescription in full detail by clicking on the
view button at the bottom of each one of them.
![image](https://user-images.githubusercontent.com/42884781/150817630-a2635e07-80f6-403e-9bf3-479a665b7ef0.png)

10. **Patient Sign Up** page is used by a patient to register his account on the platform. In order to do so,
the patient has to first enter his basic details like his name, contact, address, any medical history
and more and choose a password for authentication. Then he moves on to enter medical
information like his height weight, any prevailing allergic conditions and more.
![image](https://user-images.githubusercontent.com/42884781/150817585-4c896cc3-bb33-4e4b-9bbb-c147cc5a44ea.png)

11. **Patient Home** page is like a health dashboard for the patient. Once he is directed to this page, he
has the options in form of buttons to either view his profile or all the doctors registered on the
platform.
![image](https://user-images.githubusercontent.com/42884781/150817467-a55f9742-d625-491a-9ec8-b497f08b8b47.png)

12. **All Registered Doctor** page is used by the patient to view the list of all the registered doctors on the
platform. The basic info of a doctor like his name, contact and email are also provided for further
reference.
![image](https://user-images.githubusercontent.com/42884781/150817334-d01076b6-62ed-4505-8a15-2236aa2d0dc0.png)

13. **Patient’s Profile** page is a page that displays all the basic as well as any medical information and the
prescription history of a patient in one single page. The basic details of the patient include his
name, contact, addresses and any medical history, while his medical information includes his
height, weight, allergic conditions and more. The prescription history shows all the list of
prescriptions he may have received on the platform from various doctors and if the need be, there
is an option to take a detailed look at individual prescriptions by clicking on the View button below
each prescription.
![image](https://user-images.githubusercontent.com/42884781/150817295-780a7d45-2f17-4480-962d-3a4a14f24e35.png)

14. **Update Profile** page is used by a patient to update any of his basic information details including his
phone, email or address as well. This page comes in handy to patients in-case they entered wrong
information while registering their profile on the platform.
![image](https://user-images.githubusercontent.com/42884781/150817279-2d0e0d17-f44c-4a61-aa27-e70bfbe43ec8.png)

15. **Update Medical Information** page is used by a patient to update his medical information like his
height, weight, allergic conditions and more.
![image](https://user-images.githubusercontent.com/42884781/150817249-8d94b412-7903-412c-b8d1-40a3877c0e1a.png)

16. **Admin Panel** of Django Administration is used to enter any pre required information like medicines,
their preparations and various departments for doctors into the database.

17. The application is responsive and **mobile friendly**, so one can take control of their health into their
own hands now.
![image](https://user-images.githubusercontent.com/42884781/150817215-8f0c2b7d-c9dd-4faf-9e94-9332bfb11cd6.png)


## Database Schema

![image](https://user-images.githubusercontent.com/42884781/150818850-468785fc-d47a-43e0-9845-b98b9d3261a8.png)


## Deploying H-EAPR on AWS

1.	Create the yml file which triggers every-time a push or a pull request has been made.
![image](https://user-images.githubusercontent.com/42884781/150818322-fd6f50ed-8638-40f9-89d0-15529d11b962.png)

2.	The yml file when executed runs the docker file.
![image](https://user-images.githubusercontent.com/42884781/150818344-cc9a4f0b-f820-4b54-bb37-766d7ad64ab4.png)

3.	The docker file runs the start script
![image](https://user-images.githubusercontent.com/42884781/150818369-802b9924-2d1a-461e-9ebe-482711077b20.png)

4.	On Amazon AWS Elastic Beanstalk, create a new environment by selecting web server environment tier and entering the application and environment name. Docker is selected as the platform here.
![image](https://user-images.githubusercontent.com/42884781/150818388-d8f1111d-2c30-4563-8925-44d80da8f8ca.png)

5.	Create an IAM user in Amazon AWS.
![image](https://user-images.githubusercontent.com/42884781/150818404-c14231e9-0468-4196-b5bb-d82964b45157.png)

6.	Add the AWS Access Key and Secret Access Key in GitHub action secrets.
![image](https://user-images.githubusercontent.com/42884781/150818424-e8200194-2149-42ec-889a-de8a9325b0d1.png)

7.	Wait for the build to complete.
![image](https://user-images.githubusercontent.com/42884781/150818443-63aa77ad-ab36-4f7f-827a-c53e0aed5f45.png)

8.	The build when successfully completed shows a green tick.
![image](https://user-images.githubusercontent.com/42884781/150818466-2e816c86-43ac-474f-a699-282667e6ff0d.png)

9.	The same can be seen at environment dashboard too.
![image](https://user-images.githubusercontent.com/42884781/150818474-ffd3536e-6faa-425f-b41f-ec2f1f10857d.png)

10.	Go to the deployment link to check if the application is running.
![image](https://user-images.githubusercontent.com/42884781/150818490-30304357-7128-44c2-bc25-2e3eb7cc9d4b.png)

