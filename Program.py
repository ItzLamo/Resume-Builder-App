import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json

class Resume:
    def __init__(self):
        self.personal_info = {}
        self.education = []
        self.experience = []
        self.skills = []
        self.projects = []
        self.certifications = []

class PersonalInfoFrame(ttk.LabelFrame):
    def __init__(self, parent, resume):
        super().__init__(parent, text="Personal Information", padding=10)
        self.resume = resume
        self.create_widgets()
        
    def create_widgets(self):
        # Name
        ttk.Label(self, text="Full Name:").grid(row=0, column=0, sticky="w", pady=2)
        self.name_entry = ttk.Entry(self, width=40)
        self.name_entry.grid(row=0, column=1, sticky="w", pady=2)
        
        # Email
        ttk.Label(self, text="Email:").grid(row=1, column=0, sticky="w", pady=2)
        self.email_entry = ttk.Entry(self, width=40)
        self.email_entry.grid(row=1, column=1, sticky="w", pady=2)
        
        # Phone
        ttk.Label(self, text="Phone:").grid(row=2, column=0, sticky="w", pady=2)
        self.phone_entry = ttk.Entry(self, width=40)
        self.phone_entry.grid(row=2, column=1, sticky="w", pady=2)
        
        # Address
        ttk.Label(self, text="Address:").grid(row=3, column=0, sticky="w", pady=2)
        self.address_entry = ttk.Entry(self, width=40)
        self.address_entry.grid(row=3, column=1, sticky="w", pady=2)
        
        # Summary
        ttk.Label(self, text="Professional Summary:").grid(row=4, column=0, sticky="w", pady=2)
        self.summary_text = tk.Text(self, width=40, height=4)
        self.summary_text.grid(row=4, column=1, sticky="w", pady=2)
    
    def save_data(self):
        self.resume.personal_info = {
            'name': self.name_entry.get(),
            'email': self.email_entry.get(),
            'phone': self.phone_entry.get(),
            'address': self.address_entry.get(),
            'summary': self.summary_text.get("1.0", tk.END).strip()
        }

class EducationFrame(ttk.LabelFrame):
    def __init__(self, parent, resume):
        super().__init__(parent, text="Education", padding=10)
        self.resume = resume
        self.education_entries = []
        self.create_widgets()
        
    def create_widgets(self):
        self.entries_frame = ttk.Frame(self)
        self.entries_frame.pack(fill="x", expand=True)
        ttk.Button(self, text="Add Education", command=self.add_education_entry).pack(pady=5)
        
    def add_education_entry(self):
        entry_frame = ttk.Frame(self.entries_frame)
        entry_frame.pack(fill="x", pady=5)
        entries = {}
        
        # Degree
        ttk.Label(entry_frame, text="Degree:").grid(row=0, column=0, sticky="w")
        entries['degree'] = ttk.Entry(entry_frame, width=30)
        entries['degree'].grid(row=0, column=1, sticky="w")
        
        # School
        ttk.Label(entry_frame, text="School:").grid(row=1, column=0, sticky="w")
        entries['school'] = ttk.Entry(entry_frame, width=30)
        entries['school'].grid(row=1, column=1, sticky="w")
        
        # Year
        ttk.Label(entry_frame, text="Year:").grid(row=2, column=0, sticky="w")
        entries['year'] = ttk.Entry(entry_frame, width=30)
        entries['year'].grid(row=2, column=1, sticky="w")
        
        # GPA
        ttk.Label(entry_frame, text="GPA:").grid(row=3, column=0, sticky="w")
        entries['gpa'] = ttk.Entry(entry_frame, width=30)
        entries['gpa'].grid(row=3, column=1, sticky="w")
        
        ttk.Button(entry_frame, text="Remove", 
                  command=lambda: self.remove_education_entry(entry_frame)).grid(row=4, column=1, sticky="e")
        
        self.education_entries.append((entry_frame, entries))
        
    def remove_education_entry(self, entry_frame):
        self.education_entries = [(frame, entries) for frame, entries in self.education_entries 
                                if frame != entry_frame]
        entry_frame.destroy()
    
    def save_data(self):
        self.resume.education = []
        for _, entries in self.education_entries:
            education = {
                'degree': entries['degree'].get(),
                'school': entries['school'].get(),
                'year': entries['year'].get(),
                'gpa': entries['gpa'].get()
            }
            self.resume.education.append(education)

class ExperienceFrame(ttk.LabelFrame):
    def __init__(self, parent, resume):
        super().__init__(parent, text="Work Experience", padding=10)
        self.resume = resume
        self.experience_entries = []
        self.create_widgets()
        
    def create_widgets(self):
        self.entries_frame = ttk.Frame(self)
        self.entries_frame.pack(fill="x", expand=True)
        ttk.Button(self, text="Add Experience", command=self.add_experience_entry).pack(pady=5)
        
    def add_experience_entry(self):
        entry_frame = ttk.Frame(self.entries_frame)
        entry_frame.pack(fill="x", pady=5)
        entries = {}
        
        # Title
        ttk.Label(entry_frame, text="Job Title:").grid(row=0, column=0, sticky="w")
        entries['title'] = ttk.Entry(entry_frame, width=30)
        entries['title'].grid(row=0, column=1, sticky="w")
        
        # Company
        ttk.Label(entry_frame, text="Company:").grid(row=1, column=0, sticky="w")
        entries['company'] = ttk.Entry(entry_frame, width=30)
        entries['company'].grid(row=1, column=1, sticky="w")
        
        # Location
        ttk.Label(entry_frame, text="Location:").grid(row=2, column=0, sticky="w")
        entries['location'] = ttk.Entry(entry_frame, width=30)
        entries['location'].grid(row=2, column=1, sticky="w")
        
        # Dates
        ttk.Label(entry_frame, text="Start Date:").grid(row=3, column=0, sticky="w")
        entries['start_date'] = ttk.Entry(entry_frame, width=30)
        entries['start_date'].grid(row=3, column=1, sticky="w")
        
        ttk.Label(entry_frame, text="End Date:").grid(row=4, column=0, sticky="w")
        entries['end_date'] = ttk.Entry(entry_frame, width=30)
        entries['end_date'].grid(row=4, column=1, sticky="w")
        
        # Responsibilities
        ttk.Label(entry_frame, text="Responsibilities:").grid(row=5, column=0, sticky="w")
        entries['responsibilities'] = tk.Text(entry_frame, width=30, height=4)
        entries['responsibilities'].grid(row=5, column=1, sticky="w")
        
        ttk.Button(entry_frame, text="Remove", 
                  command=lambda: self.remove_experience_entry(entry_frame)).grid(row=6, column=1, sticky="e")
        
        self.experience_entries.append((entry_frame, entries))
        
    def remove_experience_entry(self, entry_frame):
        self.experience_entries = [(frame, entries) for frame, entries in self.experience_entries 
                                 if frame != entry_frame]
        entry_frame.destroy()
    
    def save_data(self):
        self.resume.experience = []
        for _, entries in self.experience_entries:
            experience = {
                'title': entries['title'].get(),
                'company': entries['company'].get(),
                'location': entries['location'].get(),
                'start_date': entries['start_date'].get(),
                'end_date': entries['end_date'].get(),
                'responsibilities': entries['responsibilities'].get("1.0", tk.END).strip().split('\n')
            }
            self.resume.experience.append(experience)

class SkillsFrame(ttk.LabelFrame):
    def __init__(self, parent, resume):
        super().__init__(parent, text="Skills", padding=10)
        self.resume = resume
        self.create_widgets()
        
    def create_widgets(self):
        ttk.Label(self, text="Enter skills (one per line):").pack(anchor="w")
        self.skills_text = tk.Text(self, width=40, height=6)
        self.skills_text.pack(fill="both", expand=True)
    
    def save_data(self):
        skills = self.skills_text.get("1.0", tk.END).strip().split('\n')
        self.resume.skills = [skill for skill in skills if skill.strip()]

class ProjectsFrame(ttk.LabelFrame):
    def __init__(self, parent, resume):
        super().__init__(parent, text="Projects", padding=10)
        self.resume = resume
        self.project_entries = []
        self.create_widgets()
        
    def create_widgets(self):
        self.entries_frame = ttk.Frame(self)
        self.entries_frame.pack(fill="x", expand=True)
        ttk.Button(self, text="Add Project", command=self.add_project_entry).pack(pady=5)
        
    def add_project_entry(self):
        entry_frame = ttk.Frame(self.entries_frame)
        entry_frame.pack(fill="x", pady=5)
        entries = {}
        
        # Project Name
        ttk.Label(entry_frame, text="Project Name:").grid(row=0, column=0, sticky="w")
        entries['name'] = ttk.Entry(entry_frame, width=30)
        entries['name'].grid(row=0, column=1, sticky="w")
        
        # Description
        ttk.Label(entry_frame, text="Description:").grid(row=1, column=0, sticky="w")
        entries['description'] = tk.Text(entry_frame, width=30, height=3)
        entries['description'].grid(row=1, column=1, sticky="w")
        
        ttk.Button(entry_frame, text="Remove", 
                  command=lambda: self.remove_project_entry(entry_frame)).grid(row=2, column=1, sticky="e")
        
        self.project_entries.append((entry_frame, entries))
        
    def remove_project_entry(self, entry_frame):
        self.project_entries = [(frame, entries) for frame, entries in self.project_entries 
                              if frame != entry_frame]
        entry_frame.destroy()
    
    def save_data(self):
        self.resume.projects = []
        for _, entries in self.project_entries:
            project = {
                'name': entries['name'].get(),
                'description': entries['description'].get("1.0", tk.END).strip()
            }
            self.resume.projects.append(project)

class CertificationsFrame(ttk.LabelFrame):
    def __init__(self, parent, resume):
        super().__init__(parent, text="Certifications", padding=10)
        self.resume = resume
        self.certification_entries = []
        self.create_widgets()
        
    def create_widgets(self):
        self.entries_frame = ttk.Frame(self)
        self.entries_frame.pack(fill="x", expand=True)
        ttk.Button(self, text="Add Certification", command=self.add_certification_entry).pack(pady=5)
        
    def add_certification_entry(self):
        entry_frame = ttk.Frame(self.entries_frame)
        entry_frame.pack(fill="x", pady=5)
        entries = {}
        
        # Certification Name
        ttk.Label(entry_frame, text="Name:").grid(row=0, column=0, sticky="w")
        entries['name'] = ttk.Entry(entry_frame, width=30)
        entries['name'].grid(row=0, column=1, sticky="w")
        
        # Issuer
        ttk.Label(entry_frame, text="Issuer:").grid(row=1, column=0, sticky="w")
        entries['issuer'] = ttk.Entry(entry_frame, width=30)
        entries['issuer'].grid(row=1, column=1, sticky="w")
        
        # Date
        ttk.Label(entry_frame, text="Date:").grid(row=2, column=0, sticky="w")
        entries['date'] = ttk.Entry(entry_frame, width=30)
        entries['date'].grid(row=2, column=1, sticky="w")
        
        ttk.Button(entry_frame, text="Remove", 
                  command=lambda: self.remove_certification_entry(entry_frame)).grid(row=3, column=1, sticky="e")
        
        self.certification_entries.append((entry_frame, entries))
        
    def remove_certification_entry(self, entry_frame):
        self.certification_entries = [(frame, entries) for frame, entries in self.certification_entries 
                                    if frame != entry_frame]
        entry_frame.destroy()
    
    def save_data(self):
        self.resume.certifications = []
        for _, entries in self.certification_entries:
            certification = {
                'name': entries['name'].get(),
                'issuer': entries['issuer'].get(),
                'date': entries['date'].get()
            }
            self.resume.certifications.append(certification)

class ResumeBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Builder")
        self.root.geometry("800x600")
        
        self.resume = Resume()
        self.create_widgets()
        
    def create_widgets(self):
        # Create main container
        main_container = ttk.Frame(self.root, padding=10)
        main_container.pack(fill="both", expand=True)
        
        # Create notebook for tabs
        notebook = ttk.Notebook(main_container)
        notebook.pack(fill="both", expand=True)
        
        # Personal Info Tab
        self.personal_info_frame = PersonalInfoFrame(notebook, self.resume)
        notebook.add(self.personal_info_frame, text="Personal Info")
        
        # Education Tab
        self.education_frame = EducationFrame(notebook, self.resume)
        notebook.add(self.education_frame, text="Education")
        
        # Experience Tab
        self.experience_frame = ExperienceFrame(notebook, self.resume)
        notebook.add(self.experience_frame, text="Experience")
        
        # Skills Tab
        self.skills_frame = SkillsFrame(notebook, self.resume)
        notebook.add(self.skills_frame, text="Skills")
        
        # Projects Tab
        self.projects_frame = ProjectsFrame(notebook, self.resume)
        notebook.add(self.projects_frame, text="Projects")
        
        # Certifications Tab
        self.certifications_frame = CertificationsFrame(notebook, self.resume)
        notebook.add(self.certifications_frame, text="Certifications")
        
        # Buttons Frame
        buttons_frame = ttk.Frame(main_container)
        buttons_frame.pack(fill="x", pady=10)
        
        ttk.Button(buttons_frame, text="Save as Text", 
                  command=lambda: self.save_resume("txt")).pack(side="left", padx=5)
        ttk.Button(buttons_frame, text="Save as JSON", 
                  command=lambda: self.save_resume("json")).pack(side="left", padx=5)
    
    def save_resume(self, format_type):
        # Save data from all frames
        self.personal_info_frame.save_data()
        self.education_frame.save_data()
        self.experience_frame.save_data()
        self.skills_frame.save_data()
        self.projects_frame.save_data()
        self.certifications_frame.save_data()
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"resume_{timestamp}.{format_type}"
        
        try:
            if format_type == "json":
                with open(filename, 'w') as f:
                    json.dump(self.resume.__dict__, f, indent=4)
            else:
                with open(filename, 'w') as f:
                    f.write(self.format_resume_text())
            
            messagebox.showinfo("Success", f"Resume saved successfully as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save resume: {str(e)}")
    
    def format_resume_text(self):
        text = []
        
        # Personal Information
        text.append("=" * 50)
        text.append(f"{self.resume.personal_info.get('name', '')}")
        text.append(f"Email: {self.resume.personal_info.get('email', '')}")
        text.append(f"Phone: {self.resume.personal_info.get('phone', '')}")
        text.append(f"Address: {self.resume.personal_info.get('address', '')}")
        
        # Summary
        if self.resume.personal_info.get('summary'):
            text.append("\nPROFESSIONAL SUMMARY")
            text.append("-" * 20)
            text.append(self.resume.personal_info['summary'])
        
        # Education
        if self.resume.education:
            text.append("\nEDUCATION")
            text.append("-" * 20)
            for edu in self.resume.education:
                text.append(f"{edu['degree']}")
                text.append(f"{edu['school']}, {edu['year']}")
                if edu.get('gpa'):
                    text.append(f"GPA: {edu['gpa']}")
                text.append("")
        
        # Experience
        if self.resume.experience:
            text.append("WORK EXPERIENCE")
            text.append("-" * 20)
            for exp in self.resume.experience:
                text.append(f"{exp['title']}")
                text.append(f"{exp['company']} - {exp['location']}")
                text.append(f"{exp['start_date']} - {exp['end_date']}")
                for resp in exp.get('responsibilities', []):
                    text.append(f"• {resp}")
                text.append("")
        
        # Projects
        if self.resume.projects:
            text.append("PROJECTS")
            text.append("-" * 20)
            for project in self.resume.projects:
                text.append(f"{project['name']}")
                text.append(f"{project['description']}")
                text.append("")
        
        # Certifications
        if self.resume.certifications:
            text.append("CERTIFICATIONS")
            text.append("-" * 20)
            for cert in self.resume.certifications:
                text.append(f"{cert['name']} - {cert['issuer']}")
                text.append(f"Date: {cert['date']}")
                text.append("")
        
        # Skills
        if self.resume.skills:
            text.append("SKILLS")
            text.append("-" * 20)
            text.append(", ".join(self.resume.skills))
        
        return "\n".join(text)

def main():
    root = tk.Tk()
    app = ResumeBuilderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()