# 📅 Timetable Scheduler

An intelligent university timetable generator that uses a **Genetic Algorithm** to create optimized class schedules while satisfying multiple constraints.

## ✨ Features

- **Genetic Algorithm Optimization**: Automatically generates conflict-free timetables using evolutionary computation
- **Constraint Satisfaction**: Handles both hard and soft scheduling constraints
- **Web-Based Interface**: User-friendly Django web application for managing scheduling data
- **CRUD Operations**: Full management of instructors, rooms, courses, departments, sections, and meeting times
- **Authentication**: Secure login system for administrators
- **Real-time Generation**: Watch the algorithm evolve schedules in real-time

## 🛠️ Technology Stack

- **Backend**: Python 3.6+, Django 3.2
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Algorithm**: Genetic Algorithm with tournament selection, crossover, and mutation

## 📋 Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/iamthefamous/TimeTable-Scheduler-Python.git
   cd TimeTable-Scheduler-Python
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Login with your superuser credentials

## 📖 Usage

### Setting Up Data

Before generating a timetable, you need to configure the following:

1. **Instructors**: Add teachers with their unique IDs and names
2. **Rooms**: Define classrooms with their seating capacities
3. **Meeting Times**: Set up available time slots for each day
4. **Courses**: Create courses and assign instructors
5. **Departments**: Group courses by department
6. **Sections**: Define sections with their weekly class requirements

### Generating a Timetable

1. Log in to the application
2. Ensure all required data is configured
3. Click on "Generate Timetable"
4. The genetic algorithm will run and display the optimized schedule

## 🧬 Algorithm Details

The genetic algorithm uses the following parameters:

| Parameter | Value |
|-----------|-------|
| Population Size | 30 |
| Elite Schedules | 2 |
| Tournament Selection Size | 8 |
| Mutation Rate | 0.05 |
| Max Generations | 100 |

## 📊 Constraints

The algorithm satisfies the following constraints:

### Hard Constraints
| Constraint | Description |
|------------|-------------|
| Unique Class Timing | Each section has only one class at any given time |
| Room Capacity | Room seating capacity must accommodate course enrollment |
| No Room Conflicts | Two classes cannot occupy the same room simultaneously |
| Instructor Availability | Each instructor teaches only one class at a time |
| Course-Instructor Assignment | Teachers are assigned only to their designated courses |

### Soft Constraints
| Constraint | Description |
|------------|-------------|
| Section Requirements | Classes are allocated according to section needs |
| Department Alignment | Courses are scheduled within their respective departments |
| Even Distribution | Courses are evenly distributed throughout the week |

## 📁 Project Structure

```
TimeTable-Scheduler-Python/
├── Scheduler/              # Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI configuration
├── SchedulerApp/           # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View functions & genetic algorithm
│   ├── forms.py            # Form definitions
│   ├── urls.py             # App URL patterns
│   └── admin.py            # Admin configuration
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS)
├── assets/                 # Collected static assets
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 📸 Screenshots

<details>
<summary>Click to view screenshots</summary>

### Home Page
![Home Page](./assets/img/1.png)

### Add Instructor
![Add Instructor](./assets/img/2.png)

### Add Room
![Add Room](./assets/img/3.png)

### Add Course
![Add Course](./assets/img/4.png)

### Add Department
![Add Department](./assets/img/5.png)

### Add Section
![Add Section](./assets/img/6.png)

### Generated Timetable
![Generated Timetable](./assets/img/7.png)

### Timetable View
![Timetable View](./assets/img/8.png)

</details>

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Genetic Algorithm concepts for optimization
- Django framework for rapid web development
- Bootstrap for responsive UI design

