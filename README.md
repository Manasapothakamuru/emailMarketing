The workflow begins with S3 hosting the campaign assets, followed by EventBridge orchestrating the triggers. AWS Lambda then processes the data and personalizes content, while SES efficiently manages the distribution of emails. Throughout, IAM maintains a secure and controlled environment.

📧 Amazon Simple Email Service (SES): Backbone for sending marketing emails, SES facilitates high deliverability with cost-effectiveness, ensuring messages reach audience's inboxes.

🗃️ Amazon S3 (Simple Storage Service): A robust storage solution, S3 hosts email assets, including templates and contacts, allowing for seamless management and retrieval.

🚀 AWS Lambda: The powerhouse behind email personalization, Lambda executes code to tailor each message based on customer data, ensuring a unique and engaging experience.

🔗 Amazon EventBridge: This event bus triggers workflow, coordinating between services and initiating the Lambda function based on scheduled events or specific conditions.

🔐 AWS Identity & Access Management (IAM): A layer of security that governs access, IAM meticulously manages permissions, ensuring that only authorized entities can interact with services.




![image](https://github.com/Manasapothakamuru/emailMarketing/assets/115751923/0b143c18-d1df-4415-ae44-4e68e722f076)



