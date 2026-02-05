# 🛡️AWS Compliance Report Cleaner Via Binary0101Devil

This tool processes **Nessus-exported AWS compliance reports** and automatically cleans and restructures the data for easier analysis, reporting, and automation. It is designed specifically for reports that contain AWS CIS / Security Hub style compliance checks inside the **Description** field.

---

## 📥 Input

Exported CSV report from **Tenable Nessus**.

The report must contain these columns:

| Column Name                      | Purpose                                                                        |
| -------------------------------- | ------------------------------------------------------------------------------ |
| **Description**                  | Contains check details like `"2.13 Ensure access keys are rotated" : [FAILED]` |
| **Amazon AWS Compliance Checks** | Target column where extracted check text will be placed                        |

---

## ⚙️ What This Script Does

The script automatically:

### 1️⃣ Extracts AWS Compliance Check Text

From Description like:

```
"2.13 Ensure access keys are rotated every 90 days or less" : [FAILED]
```

It extracts:

```
2.13 Ensure access keys are rotated every 90 days or less
```

---

### 2️⃣ Moves Text to Proper Column

Extracted text is moved to:

```
Amazon AWS Compliance Checks
```

---

### 3️⃣ Cleans the Description Field

Removes the extracted portion, keeping Description readable and uncluttered.

---

### 4️⃣ Removes Control Numbers

Turns:

```
2.13 Ensure access keys are rotated every 90 days or less
```

Into:

```
Ensure access keys are rotated every 90 days or less
```

Supports formats like:

```
1.2
2.13
1.2.3
```

---

## 📤 Output

A new cleaned CSV file:

```
cleaned_<original_filename>.csv
```

Ready for:

* Reporting
* Compliance dashboards
* GRC tools
* Data analysis
* SIEM ingestion

---

## 🧠 Supported Status Tags

Works automatically for:

```
[FAILED]
[WARNING]
[PASS]
[Any future status inside brackets]
```

---

## 🖥️ Requirements

* Python 3.8+
* pandas

Install dependency:

```bash
pip install pandas
```

---

## ▶ Usage

```bash
python script.py
```

Enter file name when prompted:

```
aws_report.csv
```

Output:

```
cleaned_aws_report.csv
```

---

## ❗ Why This Tool Exists

Nessus exports AWS compliance checks inside long Description strings, which makes:

* Filtering hard
* Reporting messy
* Automation difficult

This tool normalizes the data structure for security engineers, cloud teams, and auditors.

---


