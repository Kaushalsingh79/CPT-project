from flask import Flask, request, render_template, jsonify
import nltk
from collections import Counter
nltk.data.find('tokenizers/punkt')
from nltk.tokenize import word_tokenize

user =''
def process_user_input(user_input):
        
        tokens = word_tokenize(user_input)
        commands = {
        "create_instance": ["create", "make", "launch", "new", "instance"],
        "delete_instance": ["delete", "remove", "terminate", "instance"],
        "list_instances": ["list", "show", "display", "instances"],
        "start_instance": ["start", "run", "activate", "instance"],
        "stop_instance": ["stop", "halt", "deactivate", "instance"],
        "describe_instance": ["describe", "details", "info", "instance"],
        "create_bucket": ["create", "make", "new", "bucket"],
        "delete_bucket": ["delete", "remove", "erase", "bucket"],
        "list_buckets": ["list", "show", "display", "buckets"],
        "upload_file": ["upload", "send", "add", "file"],
        "download_file": ["download", "retrieve", "get", "file"],
        "list_files": ["list", "show", "display", "files"],
        "create_user": ["create", "make", "new", "user"],
        "delete_user": ["delete", "remove", "erase", "user"],
        "list_users": ["list", "show", "display", "users"],
        "grant_permission": ["grant", "allow", "authorize", "permission"],
        "revoke_permission": ["revoke", "deny", "remove", "permission"],
        "list_permissions": ["list", "show", "display", "permissions"],
        "create_database": ["create", "make", "new", "database"],
        "delete_database": ["delete", "remove", "erase", "database"],
        "list_databases": ["list", "show", "display", "databases"],
        "create_table": ["create", "make", "new", "table"],
        "delete_table": ["delete", "remove", "erase", "table"],
        "list_tables": ["list", "show", "display", "tables"],
        "create_lambda_function": ["create", "make", "new", "Lambda", "function"],
        "delete_lambda_function": ["delete", "remove", "erase", "Lambda", "function"],
        "list_lambda_functions": ["list", "show", "display", "Lambda", "functions"],
        "create_api_gateway": ["create", "make", "new", "API", "gateway"],
        "delete_api_gateway": ["delete", "remove", "erase", "API", "gateway"],
        "list_api_gateways": ["list", "show", "display", "API", "gateways"],
        "create_cloudfront_distribution": ["create", "make", "new", "CloudFront", "distribution"],
        "delete_cloudfront_distribution": ["delete", "remove", "erase", "CloudFront", "distribution"],
        "list_cloudfront_distributions": ["list", "show", "display", "CloudFront", "distributions"],
        "create_sqs_queue": ["create", "make", "new", "SQS", "queue"],
        "delete_sqs_queue": ["delete", "remove", "erase", "SQS", "queue"],
        "list_sqs_queues": ["list", "show", "display", "SQS", "queues"],
        "create_sns_topic": ["create", "make", "new", "SNS", "topic"],
        "delete_sns_topic": ["delete", "remove", "erase", "SNS", "topic"],
        "list_sns_topics": ["list", "show", "display", "SNS", "topics"],
        # Add more commands here...
    }
        similarity_scores = {key: sum((Counter(tokens) & Counter(lst)).values()) for key, lst in commands.items()}
        # print(similarity_scores)
        if all(value == next(iter(similarity_scores.values())) for value in similarity_scores.values()):
            return f"w_Input"
        most_common_command = max(similarity_scores, key=similarity_scores.get)
        return most_common_command

def w_Input():
    return f"wrong input"    

# AWS EC2 commands  

def create_instance():
    image_id = get_user_input("<image_id>")
    instance_type = get_user_input("<instance_type>")
    return f"aws ec2 run-instances --image-id {image_id} --instance-type {instance_type}"

def delete_instance():
    instance_id = get_user_input("<instance_id>")
    return f"aws ec2 terminate-instances --instance-ids {instance_id}"

def list_instances():
    return "aws ec2 describe-instances"

def start_instance():
    instance_id = get_user_input("<instance_id>")
    return f"aws ec2 start-instances --instance-ids {instance_id}"

def stop_instance():
    instance_id = get_user_input("<instance_id>")
    return f"aws ec2 stop-instances --instance-ids {instance_id}"

def describe_instance():
    instance_id = get_user_input("<instance_id>")
    return f"aws ec2 describe-instances --instance-ids {instance_id}"

# AWS S3 commands
def create_bucket():
    bucket_name = get_user_input("<bucket_name>")
    return f"aws s3api create-bucket --bucket {bucket_name}"

def delete_bucket():
    bucket_name = get_user_input("<bucket_name>")
    return f"aws s3api delete-bucket --bucket {bucket_name}"

def list_buckets():
    return "aws s3api list-buckets"

def upload_file():
    bucket_name = get_user_input("<bucket_name>")
    file_key = get_user_input("<file_key>")
    file_path = get_user_input("<file_path>")
    return f"aws s3api put-object --bucket {bucket_name} --key {file_key} --body {file_path}"

def download_file():
    bucket_name = get_user_input("<bucket_name>")
    file_key = get_user_input("<file_key>")
    file_path = get_user_input("<file_path>")
    return f"aws s3api get-object --bucket {bucket_name} --key {file_key} {file_path}"

def list_files():
    bucket_name = get_user_input("<bucket_name>")
    return f"aws s3api list-objects --bucket {bucket_name}"

# AWS IAM commands
def create_user():
    user_name = get_user_input("<user_name>")
    return f"aws iam create-user --user-name {user_name}"

def delete_user():
    user_name = get_user_input("<user_name>")
    return f"aws iam delete-user --user-name {user_name}"

def list_users():
    return "aws iam list-users"

def grant_permission():
    user_name = get_user_input("<user_name>")
    policy_arn = get_user_input("<policy_arn>")
    return f"aws iam attach-user-policy --user-name {user_name} --policy-arn {policy_arn}"

def revoke_permission():
    user_name = get_user_input("<user_name>")
    policy_arn = get_user_input("<policy_arn>")
    return f"aws iam detach-user-policy --user-name {user_name} --policy-arn {policy_arn}"

def list_permissions():
    user_name = get_user_input("<user_name>")
    return f"aws iam list-attached-user-policies --user-name {user_name}"

# AWS RDS commands
def create_database():
    db_instance_id = get_user_input("<db_instance_id>")
    engine = get_user_input("<engine>")
    return f"aws rds create-db-instance --db-instance-identifier {db_instance_id} --engine {engine}"

def delete_database():
    db_instance_id = get_user_input("<db_instance_id>")
    return f"aws rds delete-db-instance --db-instance-identifier {db_instance_id} --skip-final-snapshot"

def list_databases():
    return "aws rds describe-db-instances"

def create_table():
    resource_arn = get_user_input("<resource_arn>")
    secret_arn = get_user_input("<secret_arn>")
    database_name = get_user_input("<database_name>")
    create_table_sql = get_user_input("<create_table_sql>")
    return f"aws rds-data execute-statement --resource-arn {resource_arn} --secret-arn {secret_arn} --database {database_name} --sql {create_table_sql}"

def delete_table():
    resource_arn = get_user_input("<resource_arn>")
    secret_arn = get_user_input("<secret_arn>")
    database_name = get_user_input("<database_name>")
    delete_table_sql = get_user_input("<delete_table_sql>")
    return f"aws rds-data execute-statement --resource-arn {resource_arn} --secret-arn {secret_arn} --database {database_name} --sql {delete_table_sql}"

def list_tables():
    resource_arn = get_user_input("<resource_arn>")
    secret_arn = get_user_input("<secret_arn>")
    database_name = get_user_input("<database_name>")
    list_tables_sql = get_user_input("<list_tables_sql>")
    return f"aws rds-data execute-statement --resource-arn {resource_arn} --secret-arn {secret_arn} --database {database_name} --sql {list_tables_sql}"

# AWS Lambda commands
def create_lambda_function():
    function_name = get_user_input("<function_name>")
    handler = get_user_input("<handler>")
    role_arn = get_user_input("<role_arn>")
    return f"aws lambda create-function --function-name {function_name} --handler {handler} --role {role_arn}"

def delete_lambda_function():
    function_name = get_user_input("<function_name>")
    return f"aws lambda delete-function --function-name {function_name}"

def list_lambda_functions():
    return "aws lambda list-functions"

# AWS API Gateway commands
def create_api_gateway():
    api_name = get_user_input("<api_name>")
    return f"aws apigateway create-rest-api --name {api_name}"

def delete_api_gateway():
    api_name = get_user_input("<api_name>")
    return f"aws apigateway delete-rest-api --rest-api-id {api_name}"

def list_api_gateways():
    return "aws apigateway get-rest-apis"

# AWS CloudFront commands
def create_cloudfront_distribution():
    origin_domain = get_user_input("<origin_domain>")
    return f"aws cloudfront create-distribution --origin-domain-name {origin_domain}"

def delete_cloudfront_distribution():
    distribution_id = get_user_input("<distribution_id>")
    return f"aws cloudfront delete-distribution --id {distribution_id}"

def list_cloudfront_distributions():
    return "aws cloudfront list-distributions"

# AWS SQS commands
def create_sqs_queue():
    queue_name = get_user_input("<queue_name>")
    return f"aws sqs create-queue --queue-name {queue_name}"

def delete_sqs_queue():
    queue_url = get_user_input("<queue_url>")
    return f"aws sqs delete-queue --queue-url {queue_url}"

def list_sqs_queues():
    return "aws sqs list-queues"

# AWS SNS commands
def create_sns_topic():
    topic_name = get_user_input("<topic_name>")
    return f"aws sns create-topic --name {topic_name}"

def delete_sns_topic():
    topic_arn = get_user_input("<topic_arn>")
    return f"aws sns delete-topic --topic-arn {topic_arn}"

def list_sns_topics():
    return "aws sns list-topics"

def get_user_input(tag_name):
    
    return f"<{tag_name}>"
# Get user input
com = { "create_instance": create_instance,
    "delete_instance": delete_instance,
    "list_instances": list_instances,
    "start_instance": start_instance,
    "stop_instance": stop_instance,
    "describe_instance": describe_instance,
    "create_bucket": create_bucket,
    "delete_bucket": delete_bucket,
    "list_buckets": list_buckets,
    "upload_file": upload_file,
    "download_file": download_file,
    "list_files": list_files,
    "create_user": create_user,
    "delete_user": delete_user,
    "list_users": list_users,
    "grant_permission": grant_permission,
    "revoke_permission": revoke_permission,
    "list_permissions": list_permissions,
    "create_database": create_database,
    "delete_database": delete_database,
    "list_databases": list_databases,
    "create_table": create_table,
    "delete_table": delete_table,
    "list_tables": list_tables,
    "create_lambda_function": create_lambda_function,
    "delete_lambda_function": delete_lambda_function,
    "list_lambda_functions": list_lambda_functions,
    "create_api_gateway": create_api_gateway,
    "delete_api_gateway": delete_api_gateway,
    "list_api_gateways": list_api_gateways,
    "create_cloudfront_distribution": create_cloudfront_distribution,
    "delete_cloudfront_distribution": delete_cloudfront_distribution,
    "list_cloudfront_distributions": list_cloudfront_distributions,
    "create_sqs_queue": create_sqs_queue,
    "delete_sqs_queue": delete_sqs_queue,
    "list_sqs_queues": list_sqs_queues,
    "create_sns_topic": create_sns_topic,
    "delete_sns_topic": delete_sns_topic,
    "list_sns_topics": list_sns_topics,
    "w_Input":w_Input
    # ... (add more commands as needed)
}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        data = request.get_json()
        user = data["username"]
        if not user:
            return jsonify({"error": "Please enter a username"})
        def append_to_txt(file_path, data):
         
            with open(file_path, 'a') as txtfile:
                
                txtfile.write(data + '\n')

        # Example usage:
        file_path = '/Users/kaushal79/Python codes/cptApp/session.txt'  # Replace with your actual file path
        data_to_append = user  # Replace with your data
        
        append_to_txt(file_path, data_to_append)
        

        return render_template("index.html", username = user)


@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        
        return render_template("index.html")
    elif request.method == "POST":
        
           
        
        data = request.get_json()
        user_message = data["user_message"]
        
        
        bot_responses = [] 
        
        function_name = process_user_input(user_message)
        if function_name in com and callable(com[function_name]):
            func = com[function_name]
            response = func()

            if response is not None:
                bot_responses.append(response)
            else:
                print(f"Function '{function_name}' returned None.")
          
        return jsonify({"bot_messages": (bot_responses)})
    else:
        
        return jsonify({"error": "Unsupported request method"})
@app.route("/close-session", methods=["POST"])
def close_session():
    
    return jsonify({"message": "Session closed successfully"})


@app.route("/close.html")
def render_closed_page():
    def delete_from_text_file(file_path, target_string):
    # Read the content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

    # Remove the target string from the lines
        lines = [line for line in lines if target_string not in line]

    # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)

# Example usage:
    file_path = '/Users/kaushal79/Python codes/cptApp/session.txt'  # Replace with your actual file path
    target_string_to_delete = user  # Replace with the string you want to delete

    delete_from_text_file(file_path, target_string_to_delete)

    return render_template("close.html")
if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=8080)
