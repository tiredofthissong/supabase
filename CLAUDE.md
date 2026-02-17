# Supabase LMS Platform

**Project:** Lightweight Learning Management System  
**Stack:** Supabase (PostgreSQL) + Python + Plotly  
**Location:** `~/Desktop/bootcamp/platforms/supabase-lms/`

---

## Supabase Credentials

- **Project URL:** `https://gilvijxmudywgcaslfxz.supabase.co`
- **Public API Key:** `sb_publishable_3QYyHIXrfZJb5s-DBjnrDg_qSDRVBRd`
- **Dashboard:** [supabase.com/dashboard](https://supabase.com/dashboard)

---

## Database Schema

### `courses` Table
```sql
CREATE TABLE courses (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

**Current Data:**
- 1 course: "Python for L&D Automation"

---

## Files

### `test_supabase.py`
Tests database connection by inserting a course record.

**Run:**
```bash
python3 test_supabase.py
```

### `dashboard_test.py`
Fetches all courses from database and generates Plotly bar chart.

**Run:**
```bash
python3 dashboard_test.py
open course_dashboard.html
```

### `course_dashboard.html`
Interactive Plotly visualization (auto-generated, don't edit manually).

---

## Quick Commands

**Insert new course:**
```python
from supabase import create_client

url = "https://gilvijxmudywgcaslfxz.supabase.co"
key = "sb_publishable_3QYyHIXrfZJb5s-DBjnrDg_qSDRVBRd"
supabase = create_client(url, key)

supabase.table("courses").insert({"title": "Course Name Here"}).execute()
```

**Query all courses:**
```python
response = supabase.table("courses").select("*").execute()
courses = response.data
```

---

## Session History

### 2026-02-15: Initial Setup
- Created Supabase account + project
- Built `courses` table
- Installed `pip3 install supabase plotly`
- Tested insert/query round-trip
- Generated first dashboard

---

## Next Steps (Options)

**A) Expand Schema:**
- Add `users` table (email, role, created_at)
- Add `user_progress` table (user_id, course_id, completion_%)
- Add `analytics` table (session_data, quiz_scores)

**B) Build Multi-Page Dashboard:**
- Course catalog view
- Learner progress tracking
- Completion rate analytics

**C) GitHub Actions Integration:**
- Automate nightly dashboard refresh
- Push updated HTML to GitHub Pages

**D) Add Authentication:**
- Supabase Auth setup
- Row-level security (users see only their data)
- Login/logout UI

---

## Troubleshooting

**SSL Warning (harmless):**
```
NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+
```
This is due to macOS LibreSSL version — doesn't affect functionality.

**Command not found: pip**
Use `pip3` instead (Python 3.9.6 installed).
