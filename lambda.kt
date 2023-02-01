resource "aws_lambda_function" "moving_service" {
  function_name = "moving_service"
  filename      = "moving_service.zip"
  handler       = "index.handler"
  runtime       = "python3.8"
  role          = "${aws_iam_role.lambda_exec.arn}"
  source_code_hash = "${base64sha256(file("moving_service.py"))}"
}

resource "aws_lambda_function" "processing_service" {
  function_name = "processing_service"
  filename      = "processing_service.zip"
  handler       = "index.handler"
  runtime       = "python3.8"
  role          = "${aws_iam_role.lambda_exec.arn}"
  source_code_hash = "${base64sha256(file("processing_service.py"))}"
}
