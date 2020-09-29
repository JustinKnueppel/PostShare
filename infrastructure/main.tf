provider "aws" {
    region = "us-east-2"
}

terraform {
    backend "s3" {
      bucket = "terraform-state-jpai4rqw7c"
      key    = "Personal/postshare.tfstate"
      region = "us-east-2"
    }
}
