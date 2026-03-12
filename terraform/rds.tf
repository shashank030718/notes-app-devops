# Subnet group for RDS (needs 2 AZs)
resource "aws_db_subnet_group" "main" {
  name       = "${var.project_name}-db-subnet"
  subnet_ids = aws_subnet.private[*].id

  tags = { Name = "${var.project_name}-db-subnet" }
}

# RDS PostgreSQL instance
resource "aws_db_instance" "postgres" {
  identifier        = "${var.project_name}-db"
  engine            = "postgres"
  engine_version    = "15"
  instance_class    = "db.t3.micro"   # free tier eligible
  allocated_storage = 20

  db_name  = "notesdb"
  username = "postgres"
  password = var.db_password

  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.rds.id]

  skip_final_snapshot = true   # for dev/learning — don't keep snapshot on delete
  publicly_accessible = false  # only accessible inside VPC

  tags = { Name = "${var.project_name}-db" }
}

output "rds_endpoint" {
  value = aws_db_instance.postgres.endpoint
}