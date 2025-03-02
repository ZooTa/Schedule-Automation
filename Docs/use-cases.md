---
icon: clipboard-list
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---
## **1.1: Sending Schedule Notifications**  

### **Actors**  
- **Administrator** – Manages the schedule data and initiates the messaging process.  
- **Instructor** – Receives schedule notifications.  

### **Preconditions**  
- The administrator has access to the schedule data in a standardized format (CSV or Excel).  
- The system is configured with messaging and email server settings.  

### **Main Success Scenario**  
1. The **administrator logs into the system**.  
2. The **administrator uploads the schedule data file**.  
3. The system **processes the data**, applying alias mapping and standardizing time formats.  
4. The system **prompts the administrator to choose the message format** (text, image, PDF, Excel).  
5. The **administrator selects** the desired format for the message.  
6. The system **prompts the administrator to choose the delivery method** (WhatsApp, email).  
7. The **administrator selects** the desired delivery method.  
8. The system **generates the message** in the selected format.  
9. The system **sends the message** via the chosen platform.  
10. The **administrator receives confirmation** of successful message delivery.  

### **Alternative Scenarios**  

#### **A1. Invalid Data File**  
- 3a. The system detects an **incorrect format or missing fields**.  
- 3b. The system **notifies the administrator** and requests a valid file.  
- 3c. **Use case ends**.  

#### **A2. Unsupported Format or Method**  
- 5a. The administrator selects a **format or method not supported**.  
- 5b. The system **notifies the administrator** and requests a valid option.  
- 5c. **Use case resumes at step 4**.  

#### **A3. Messaging Platform Not Configured**  
- 9a. The system detects that the **chosen platform is not configured**.  
- 9b. The system **prompts the administrator to configure the platform**.  
- 9c. **Use case resumes at step 9**.  

---

## **1.2: Generating Schedule Reports**  

### **Actors**  
- **Administrator** – Manages the schedule data and generates reports.  

### **Preconditions**  
- The administrator has access to the schedule data in a standardized format (CSV or Excel).  

### **Main Success Scenario**  
1. The **administrator logs into the system**.  
2. The **administrator uploads the schedule data file**.  
3. The system **processes the data**, applying alias mapping and standardizing time formats.  
4. The system **prompts the administrator to choose the report format** (PDF, image, Excel, text).  
5. The **administrator selects** the desired format for the report.  
6. The system **generates the schedule report** in the selected format.  
7. The **administrator downloads the report** for further use.  

### **Alternative Scenarios**  

#### **A1. Invalid Data File**  
- 3a. The system detects an **incorrect format or missing fields**.  
- 3b. The system **notifies the administrator** and requests a valid file.  
- 3c. **Use case ends**.  

#### **A2. Report Generation Error**  
- 6a. The system encounters an **error while generating the report**.  
- 6b. The system **logs the error and notifies the administrator**.  
- 6c. **Use case ends**.  

#### **A3. Unsupported Format Selection**  
- 5a. The administrator selects a **format not supported by the system**.  
- 5b. The system **notifies the administrator** and requests a valid format.  
- 5c. **Use case resumes at step 4**.  

---

## **1.3: Automating Instructor Assignment to Sessions**  

### **Actors**  
- **Administrator** – Manages the session data and oversees the assignment process.  
- **System** – Automates the assignment of instructors to sessions.  

### **Preconditions**  
- The administrator has access to the **previous month's session data** and the **current month's availability data**.  
- The session data includes **session codes, locations, and instructor assignments**.  
- The availability data includes **instructor availability for the current month**.  

### **Main Success Scenario**  
1. The **administrator logs into the system**.  
2. The **administrator uploads the previous month's session data and the current month's availability data**.  
3. The system **validates the file structures and data integrity** (e.g., checks for missing fields, correct format).  
4. The system **identifies sessions that remain unchanged** from the previous month.  
5. The system **assigns instructors** to these sessions based on previous assignments and current availability.  
6. The system **generates a new session sheet** with updated instructor assignments.  
7. The **administrator reviews and confirms the assignments**.  
8. The **administrator downloads the updated session sheet** for further use.  

### **Alternative Scenarios**  

#### **A1. Invalid or Corrupted Data File**  
- 3a. The system detects an **incorrect format, missing fields, or corrupted data**.  
- 3b. The system **notifies the administrator** and requests a valid file.  
- 3c. **Use case ends**.  

#### **A2. Instructor Unavailability**  
- 5a. The system identifies **instructors who are unavailable** for their previous sessions.  
- 5b. The system **flags these sessions for manual review**.  
- 5c. The administrator **manually assigns available instructors** to these sessions.  

#### **A3. New or Terminated Sessions**  
- 4a. The system identifies **new sessions or sessions that have been terminated**.  
- 4b. The system **flags these sessions for manual review**.  
- 4c. The administrator **assigns instructors to new sessions** or confirms terminations.  

---


## **1.4: Notification Scheduling**  

### **Actors**  
- **Administrator** – Schedules notifications for future delivery.  

### **Preconditions**  
- The system supports scheduling of notifications.  

### **Main Success Scenario**  
1. The **administrator logs into the system**.  
2. The **administrator selects the schedule data** and desired notification time.  
3. The system **schedules the notifications** for future delivery.  
4. The system **sends notifications at the scheduled time**.  

### **Alternative Scenarios**  

#### **A1. Scheduling Conflict**  
- 3a. The system detects a **conflict with the scheduled time**.  
- 3b. The system **prompts the administrator to choose a different time**.  
- 3c. **Use case resumes at step 2**.  

---

## **1.5: Custom Report Generation**  

### **Actors**  
- **Administrator** – Generates custom reports based on specific criteria.  

### **Preconditions**  
- The system supports custom report generation.  

### **Main Success Scenario**  
1. The **administrator logs into the system**.  
2. The **administrator selects criteria** for the custom report.  
3. The system **generates the report** based on the selected criteria.  
4. The **administrator downloads the custom report**.  

### **Alternative Scenarios**  

#### **A1. Invalid Criteria**  
- 2a. The system detects **invalid criteria**.  
- 2b. The system **prompts the administrator to correct the criteria**.  
- 2c. **Use case resumes at step 2**.  

---

## **1.6: User Management**  

### **Actors**  
- **Administrator** – Manages user accounts and permissions.  

### **Preconditions**  
- The system supports multiple user accounts with varying permissions.  

### **Main Success Scenario**  
1. The **administrator logs into the system**.  
2. The **administrator navigates to the user management section**.  
3. The **administrator adds, edits, or removes user accounts**.  
4. The **administrator assigns roles and permissions** to each user.  
5. The system **saves the changes** and updates user access accordingly.  

### **Alternative Scenarios**  

#### **A1. Invalid User Data**  
- 3a. The system detects **invalid or incomplete user data**.  
- 3b. The system **prompts the administrator to correct the data**.  
- 3c. **Use case resumes at step 3**.  

---

## **1.7: Data Backup and Recovery**  

### **Actors**  
- **Administrator** – Manages data backup and recovery processes.  

### **Preconditions**  
- The system is configured with backup and recovery settings.  

### **Main Success Scenario**  
1. The **administrator logs into the system**.  
2. The **administrator initiates a data backup process**.  
3. The system **creates a backup** of all critical data and stores it securely.  
4. The **administrator verifies the backup integrity**.  
5. In case of data loss, the **administrator initiates a data recovery process**.  
6. The system **restores data from the latest backup**.  

### **Alternative Scenarios**  

#### **A1. Backup Failure**  
- 3a. The system encounters an **error during the backup process**.  
- 3b. The system **logs the error and notifies the administrator**.  
- 3c. **Use case ends**.  
