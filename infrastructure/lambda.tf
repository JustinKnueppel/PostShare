resource "aws_iam_role" "lambda_role" {
    assume_role_policy    = jsonencode(
        {
            Statement = [
                {
                    Action    = "sts:AssumeRole"
                    Effect    = "Allow"
                    Principal = {
                        Service = "lambda.amazonaws.com"
                    }
                },
            ]
            Version   = "2012-10-17"
        }
    )
    force_detach_policies = false
    max_session_duration  = 3600
    name                  = "Share-Reddit-Role"
    path                  = "/service-role/"
    tags                  = {}
}


data "archive_file" "lambda" {
  type        = "zip"
  output_path = "${path.module}/ShareReddit.zip"

  source_dir = pathexpand("../src")
}

resource "aws_lambda_function" "postshare" {
    filename        = "ShareReddit.zip"
    function_name   = "main"
    role            = aws_iam_role.lambda_role.arn
    handler         = "ShareReddit.main"

    source_code_hash = data.archive_file.lambda.output_base64sha256

    runtime         = "python3.7"
}