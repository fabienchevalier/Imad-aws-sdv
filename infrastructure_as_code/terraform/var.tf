variable "instance_name" {
  type        = string
  description = "The name of the EC2 instance."
}

variable "ami" {
  type        = string
  description = "The ID of the AMI to use for the EC2 instance."
}

variable "instance_type" {
  type        = string
  description = "The type of the EC2 instance."
}

variable "ssh_cidr_blocks" {
  type        = list(string)
  description = "The CIDR blocks to allow SSH access to the EC2 instance."
}

variable "http_cidr_blocks" {
  type        = list(string)
  description = "The CIDR blocks to allow HTTP access to the EC2 instance."
}

variable "user_name" {
  type        = string
  description = "The name of the IAM user."
}
