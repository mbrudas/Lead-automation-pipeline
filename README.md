# 🚀 Lead Automation Pipeline

**Type**: Independent Project · Self-initiated  
**Author**: María Brudas  
**Tools Used**: Python · Pandas · Google Sheets · Google Forms · Apps Script · HubSpot API  
**Language**: English (standard in IT industry)  
**Status**: MVP - Ready for client use, scalable and customizable  

---

## 💡 Project Overview

This project automates the entire lifecycle of a lead: from form capture to CRM synchronization. It was designed and implemented independently to demonstrate how small businesses and service providers can streamline lead management and scale without increasing manual workload.

The solution is **modular, cloud-based, and scalable**, and it's designed with free or low-cost tools. It's ideal for entrepreneurs, small agencies, or businesses that need automation but lack dedicated tech teams.

---

## 🧠 Problem Solved

Many professionals manually manage their leads, which often results in:

- ⌛ Time wasted copying/pasting contact info.
- ❌ Data inconsistencies or duplicates.
- 📉 Missed follow-ups due to scattered information.

This pipeline solves that by:

✅ Automatically cleaning and validating raw contact data.  
✅ Syncing new and historical leads directly into HubSpot CRM.  
✅ Creating a single source of truth in Google Sheets.  
✅ Capturing new form submissions in real-time.

---

## 📌 Architecture Breakdown

The system follows three main phases:

### Phase 1: Data Preparation

| Step | Tool               | Description                                |
|------|--------------------|--------------------------------------------|
| 1    | CSV Dataset        | 1,000+ raw contacts from a public dataset. |
| 2    | Python + Pandas    | Cleaned, standardized, and validated data. |
| 3    | Clean Sheet        | Ready-to-sync clean contact database.      |

---

### Phase 2: Form Capture Automation

| Step | Tool               | Description                                |
|------|--------------------|--------------------------------------------|
| 1    | Google Forms       | Real-time user input.                      |
| 2    | Apps Script        | Automated triggers, form-to-sheet sync.   |
| 3    | Google Sheets      | Central database, fully updated.          |

---

### Phase 3: CRM Integration

| Step | Tool               | Description                                  |
|------|--------------------|----------------------------------------------|
| 1    | Google Sheets      | Source for HubSpot sync.                     |
| 2    | HubSpot API v3     | REST-based integration using private token. |
| 3    | HubSpot CRM        | Live contact management and segmentation.    |

---

## 📊 Key Metrics (Real)

| Metric                          | Value               |
|----------------------------------|---------------------|
| Time saved in contact entry     | ⏱️ 90%               |
| Data accuracy post-cleaning     | ✅ 95.6%             |
| CRM sync time (end-to-end)      | ⚡ ~28 seconds       |
| System availability             | 🔁 99.9%             |
| Total records processed         | 🗂️ 653 (cleaned + synced) |
| Leads captured via form         | 🆕 41                |

---

## 🔐 Data Note

- Dataset used: [Sample customer data from Datablist](https://www.datablist.com/learn/csv/download-sample-csv-files)  
- No sensitive or real client data was used in this prototype.

---

## 💼 Potential Clients / Use Cases

This system is ideal for:

- 🧠 Independent consultants or coaches  
- 📢 Marketing and ad agencies  
- 🏪 Small businesses without a dedicated IT team  
- 📇 Admins needing a centralized, up-to-date CRM  
- 🛠️ Professionals managing contacts in spreadsheets  

---

## 🌍 Vision & Future

This is an MVP version of what can become a **productized service** or **white-label solution**. The idea is to later:

- Offer setup as a **freelance service** or **subscription model**  
- Create a **licensable/franchise-ready product**  
- Automate additional actions (emails, reminders, segmentation, etc.)

---

## 📂 Files in this Repository

| File           | Purpose                                 |
|----------------|------------------------------------------|
| `README.md`    | Professional summary of the project      |
| `index.html`   | Interactive architecture diagram (visual)|
| (Not included) | Private Python code for data cleaning    |
| (Not included) | Apps Script for form-to-CRM sync         |

---

## 📜 License

This project is for educational and professional portfolio use only. No sensitive data is included. Scripts and tokens are excluded by design.

---

