

# Campus Admin Pro

**Campus Admin Pro** is a comprehensive management application designed for educational institutions, featuring distinct modules for **Admin**, **Staff**, and **Students**. This application streamlines administrative tasks, enhances communication, and leverages AI technology to provide personalized support to students.

## Features

### Admin Module
- Manage user roles and permissions for staff and students.
- Oversee system operations and monitor usage metrics.

### Staff Module
- **CSV File Management**: Import and export CSV files to/from the SQLite database, facilitating easy data updates and management.
- **Bulk Email Sending**: Effortlessly send bulk emails to students and other staff members for announcements, notifications, and updates.
- **Email Tracking System**: Monitor the status of sent emails, ensuring effective communication and follow-ups.

### Student Module
- **Personalized AI Assistant**: Access a customized GPT-based assistant, fine-tuned with Ollama 3.1, to provide tailored responses to student queries, support for academic work, and enhanced learning resources.

## Technologies Used
- **Backend**: Python with Django
- **Database**: SQLite
- **AI Integration**: Ollama 3.1 for personalized student assistance.
- **Email Service**: [Specify the email service used, e.g., SMTP, SendGrid, etc.]

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Aditharavind/mini-project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd campus-admin-pro
   ```

3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application in your browser at `http://127.0.0.1:8000`.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the Adith License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any sections to better fit your project details or style!
