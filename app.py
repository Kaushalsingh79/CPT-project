from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Store login credentials in memory (for demonstration purposes)
credentials = {
    "user1": "password1",
    "user2": "password2",
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]

        # Check if the user is authenticated
        if user not in credentials or credentials[user] != password:
            return jsonify({"error": "Authentication failed"})
        else:
            return render_template("index.html")

    return render_template("login.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    import subprocess
# Check the return code to see if the command was successful
    

    data = request.get_json()
    # user = data["user"]
    user_message = data["user_message"]
    ####
    import spacy

# Load the English language model from spaCy
    nlp = spacy.load("en_core_web_sm")

# Define a mapping of user intents to AWS CLI commands
    intent_commands = {
    "list_instances": "aws ec2 describe-instances",
    "create_instance": "aws ec2 run-instances",
    "start_instance": "aws ec2 start-instances",
    "stop_instance": "aws ec2 stop-instances",
    "list_s3_buckets": "aws s3 ls",
    "create_s3_bucket": "aws s3api create-bucket",
    "list_lambda_functions": "aws lambda list-functions",
    "create_lambda_function": "aws lambda create-function",
    "list_rds_instances": "aws rds describe-db-instances",
    "create_rds_instance": "aws rds create-db-instance",
    "list_dynamodb_tables": "aws dynamodb list-tables",
    "create_dynamodb_table": "aws dynamodb create-table",
    "list_sqs_queues": "aws sqs list-queues",
    "create_sqs_queue": "aws sqs create-queue",
    "list_sns_topics": "aws sns list-topics",
    "create_sns_topic": "aws sns create-topic",
    "list_cloudwatch_alarms": "aws cloudwatch describe-alarms",
    "create_cloudwatch_alarm": "aws cloudwatch put-metric-alarm",
    "list_iam_users": "aws iam list-users",
    "create_iam_user": "aws iam create-user",
    "list_vpc_subnets": "aws ec2 describe-subnets",
    "create_vpc_subnet": "aws ec2 create-subnet",
    "list_security_groups": "aws ec2 describe-security-groups",
    "create_security_group": "aws ec2 create-security-group",
    "list_route53_hosted_zones": "aws route53 list-hosted-zones",
    "create_route53_hosted_zone": "aws route53 create-hosted-zone",
    "list_ecs_clusters": "aws ecs list-clusters",
    "create_ecs_cluster": "aws ecs create-cluster",
    "list_efs_filesystems": "aws efs describe-file-systems",
    "create_efs_filesystem": "aws efs create-file-system",
    "list_elasticsearch_domains": "aws es list-domain-names",
    "create_elasticsearch_domain": "aws es create-elasticsearch-domain",
    "list_ssm_documents": "aws ssm list-documents",
    "create_ssm_document": "aws ssm create-document",
    "list_sqs_queues": "aws sqs list-queues",
    "create_sqs_queue": "aws sqs create-queue",
    "list_sqs_queues": "aws sqs list-queues",
    "create_sqs_queue": "aws sqs create-queue",
    # Add more intents and AWS CLI commands as needed
}

# Function to generate AWS CLI command based on user input
    def generate_aws_command(user_input):
        doc = nlp(user_input.lower())  # Process user input using NLP

    # Define keywords for various intents
        intent_keywords = {
    "list_instances": ["list", "show", "display", "instances"],
    "create_instance": ["create", "launch", "new", "instance"],
    "start_instance": ["start", "run", "activate", "instance"],
    "stop_instance": ["stop", "halt", "deactivate", "instance"],
    "list_s3_buckets": ["list", "show", "display", "S3", "buckets"],
    "create_s3_bucket": ["create", "make", "new", "S3", "bucket"],
    "list_lambda_functions": ["list", "show", "display", "Lambda", "functions"],
    "create_lambda_function": ["create", "make", "new", "Lambda", "function"],
    "list_rds_instances": ["list", "show", "display", "RDS", "instances"],
    "create_rds_instance": ["create", "make", "new", "RDS", "instance"],
    "list_dynamodb_tables": ["list", "show", "display", "DynamoDB", "tables"],
    "create_dynamodb_table": ["create", "make", "new", "DynamoDB", "table"],
    "list_sqs_queues": ["list", "show", "display", "SQS", "queues"],
    "create_sqs_queue": ["create", "make", "new", "SQS", "queue"],
    "list_sns_topics": ["list", "show", "display", "SNS", "topics"],
    "create_sns_topic": ["create", "make", "new", "SNS", "topic"],
    "list_cloudwatch_alarms": ["list", "show", "display", "CloudWatch", "alarms"],
    "create_cloudwatch_alarm": ["create", "make", "new", "CloudWatch", "alarm"],
    "list_iam_users": ["list", "show", "display", "IAM", "users"],"create_iam_user": ["create", "make", "new", "IAM", "user"],
    "list_vpc_subnets": ["list", "show", "display", "VPC", "subnets"],
    "create_vpc_subnet": ["create", "make", "new", "VPC", "subnet"],
    "list_security_groups": ["list", "show", "display", "security", "groups"],
    "create_security_group": ["create", "make", "new", "security", "group"],
    "list_route53_hosted_zones": ["list", "show", "display", "Route 53", "hosted zones"],
    "create_route53_hosted_zone": ["create", "make", "new", "Route 53", "hosted zone"],
    "list_ecs_clusters": ["list", "show", "display", "ECS", "clusters"],
    "create_ecs_cluster": ["create", "make", "new", "ECS", "cluster"],
    "list_efs_filesystems": ["list", "show", "display", "EFS", "filesystems"],
    "create_efs_filesystem": ["create", "make", "new", "EFS", "filesystem"],
    "list_elasticsearch_domains": ["list", "show", "display", "Elasticsearch", "domains"],
    "create_elasticsearch_domain": ["create", "make", "new", "Elasticsearch", "domain"],
    "list_ssm_documents": ["list", "show", "display", "SSM", "documents"],
    "create_ssm_document": ["create", "make", "new", "SSM", "document"],
    "list_sqs_queues": ["list", "show", "display", "SQS", "queues"],
    "create_sqs_queue": ["create", "make", "new", "SQS", "queue"],
    # Add more keywords for other intents
    }


    # Determine the user's intent
        matched_intent = None
        for intent, keywords in intent_keywords.items():
            if any(keyword in user_input for keyword in keywords):
                matched_intent = intent
                break

        if matched_intent:
            return intent_commands.get(matched_intent, "Command not recognized")
        else:
            return "Command not recognized"

# Chatbot loop
    # while True:
    #     user_input = input("Enter a command in English: ")
    #     if user_input.lower() == "exit":
    #         break  # Exit the loop
    #     generated_command = generate_aws_command(user_input)
    #     print("Generated AWS CLI Command:", generated_command)




    ####
    user_input = data["user_message"]
    # result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # # Check if the user is authenticated
    # # if user not in credentials or credentials[user] != data["password"]:
    # #     return jsonify({"error": "Authentication failed"})
    # if result.returncode == 0:
    #     print("Command executed successfully.")
    #     print("Output:")
    #     print(result.stdout)
    # else:
    #    print("Command failed with an error.")
    #    print("Error message:")
    #    print(result.stderr)
    # Simulate a response from the bot (You can replace this with an AI-generated response)
    bot_message = f"cmd: {generate_aws_command(user_input.lower())}"

    return jsonify({"bot_message": bot_message})


if __name__ == "__main__":
    app.run(debug=True)
