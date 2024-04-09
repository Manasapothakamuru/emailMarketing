The workflow begins with S3 hosting the campaign assets, followed by EventBridge orchestrating the triggers. AWS Lambda then processes the data and personalizes content, while SES efficiently manages the distribution of our emails. Throughout, IAM maintains a secure and controlled environment.

📧 Amazon Simple Email Service (SES): Our backbone for sending marketing emails, SES facilitates high deliverability with cost-effectiveness, ensuring our messages reach our audience's inboxes.

🗃️ Amazon S3 (Simple Storage Service): A robust storage solution, S3 hosts our email assets, including templates and images, allowing for seamless management and retrieval.

🚀 AWS Lambda: The powerhouse behind our email personalization, Lambda executes code to tailor each message based on customer data, ensuring a unique and engaging experience.

🔗 Amazon EventBridge: This event bus triggers our workflow, coordinating between services and initiating the Lambda function based on scheduled events or specific conditions.

🔐 AWS Identity & Access Management (IAM): A layer of security that governs access, IAM meticulously manages permissions, ensuring that only authorized entities can interact with our services.




![image](https://github.com/Manasapothakamuru/emailMarketing/assets/115751923/0b143c18-d1df-4415-ae44-4e68e722f076)



