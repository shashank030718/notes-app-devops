variable "aws_region" {
  default = "ap-south-1"
}

variable "project_name" {
  default = "notes-app"
}

variable "db_password" {
  description = "RDS PostgreSQL password"
  sensitive   = true
  default     = "NotesApp2024!"
}