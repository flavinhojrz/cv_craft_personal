// src/types/resume.ts

export interface Basics {
  name: string;
  label: string;
  email: string;
  phone: string;
  location: string;
  website: string;
  summary: string;
}

export interface Education {
  institution: string;
  area: string;
  startDate: string;
  endDate: string;
}

export interface Experience {
  company: string;
  position: string;
  startDate: string;
  endDate: string;
  summary: string;
}

export interface Project {
  name: string;
  position: string;
  startDate: string;
  endDate: string;
  summary: string;
}

export interface Course {
  title: string;
  institution: string;
  hours: number;
  summary: string;
}

export interface Skills {
  technical_support: string[];
  technical_extras: string[];
  soft_skills?: string[];
}

export interface Resume {
  basics: Basics;
  education: Education[];
  experience: Experience[];
  projects: Project[];
  courses: Course[];
  skills: Skills;
}

export interface OptmizeParams {
  data: Resume;
  instructions: string;
  sections?: string[];
}
