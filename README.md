# 📅 Timetable Scheduler

An intelligent university timetable generator that uses a **Genetic Algorithm** to create optimized class schedules while satisfying multiple constraints. This project demonstrates practical applications of **discrete mathematics** and **algorithmic optimization** in solving complex combinatorial problems.

## 🔬 Theoretical Foundations & Discrete Mathematics

### The Scheduling Problem as a Discrete Optimization Problem

Timetable scheduling is a classic example of a **Constraint Satisfaction Problem (CSP)** in discrete mathematics. The problem can be formally defined as:

- **Variables**: A finite set of classes that need to be scheduled
- **Domains**: Each variable can take values from a discrete set of (room, time slot, instructor) combinations
- **Constraints**: A set of rules that restrict valid assignments

This maps directly to the mathematical structure of a **combinatorial optimization problem**, where we seek to find an optimal solution from a finite (but exponentially large) set of possibilities.

### Graph Theory Connections

The scheduling problem has deep connections to graph coloring:

| Graph Theory Concept | Scheduling Equivalent |
|---------------------|----------------------|
| **Vertices** | Classes/Courses to be scheduled |
| **Edges** | Conflicts between classes (same instructor, same room, same section at same time) |
| **Graph Coloring** | Assigning time slots (colors) such that no adjacent vertices share the same color |
| **Chromatic Number** | Minimum number of time slots needed |

The timetable scheduling problem is equivalent to the **Graph Coloring Problem**, which is known to be **NP-hard**. This explains why we use heuristic algorithms like genetic algorithms instead of brute-force approaches.

### Computational Complexity

| Aspect | Complexity Analysis |
|--------|---------------------|
| **Problem Class** | NP-hard (no known polynomial-time solution) |
| **Solution Space** | O((R × T × I)^n) where R=rooms, T=time slots, I=instructors, n=classes |
| **Brute Force** | Infeasible for realistic problem sizes |
| **Genetic Algorithm** | Polynomial time per generation, finds near-optimal solutions |

### Set Theory and Relations

The scheduling problem uses fundamental set theory concepts:

```
Let S = {s₁, s₂, ..., sₙ} be the set of sections
Let T = {t₁, t₂, ..., tₘ} be the set of time slots
Let R = {r₁, r₂, ..., rₖ} be the set of rooms
Let I = {i₁, i₂, ..., iₗ} be the set of instructors
Let C = {c₁, c₂, ..., cₚ} be the set of courses

A valid schedule is a function: f: Classes → T × R × I
Subject to: ∀ constraints being satisfied
```

## 🧬 Genetic Algorithm: Discrete Optimization in Action

### Algorithm Overview

Genetic Algorithms (GAs) are **metaheuristic optimization algorithms** inspired by the process of natural selection. They operate on the principle of **survival of the fittest** and are particularly effective for discrete optimization problems.

```
┌─────────────────────────────────────────────────────────────────┐
│                    GENETIC ALGORITHM FLOW                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────────────┐                                          │
│   │ Initialize       │ Create random population of schedules   │
│   │ Population       │ (Each schedule = chromosome)            │
│   └────────┬─────────┘                                          │
│            │                                                    │
│            ▼                                                    │
│   ┌──────────────────┐                                          │
│   │ Fitness          │ Evaluate how well each schedule         │
│   │ Evaluation       │ satisfies constraints                   │
│   └────────┬─────────┘                                          │
│            │                                                    │
│            ▼                                                    │
│   ┌──────────────────┐                                          │
│   │ Selection        │ Tournament selection: choose fittest    │
│   │ (Tournament)     │ from random subset                      │
│   └────────┬─────────┘                                          │
│            │                                                    │
│            ▼                                                    │
│   ┌──────────────────┐                                          │
│   │ Crossover        │ Combine two parent schedules to         │
│   │ (Recombination)  │ create offspring                        │
│   └────────┬─────────┘                                          │
│            │                                                    │
│            ▼                                                    │
│   ┌──────────────────┐                                          │
│   │ Mutation         │ Randomly alter some class assignments   │
│   │                  │ to maintain diversity                   │
│   └────────┬─────────┘                                          │
│            │                                                    │
│            ▼                                                    │
│   ┌──────────────────┐         ┌──────────────────┐             │
│   │ Termination      │───No───►│ New Generation   │─────┐       │
│   │ Condition Met?   │         └──────────────────┘     │       │
│   └────────┬─────────┘                                  │       │
│            │ Yes                                        │       │
│            ▼                          ◄─────────────────┘       │
│   ┌──────────────────┐                                          │
│   │ Return Best      │ Output the schedule with highest        │
│   │ Schedule         │ fitness score                           │
│   └──────────────────┘                                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Mathematical Representation

**Chromosome Encoding**: Each schedule is encoded as a sequence of genes:
```
Schedule = [Gene₁, Gene₂, ..., Geneₙ]
where Geneᵢ = (courseᵢ, roomᵢ, timeᵢ, instructorᵢ)
```

**Fitness Function**:
```
fitness(schedule) = 1 / (1 + number_of_conflicts)
```

This ensures:
- A perfect schedule (0 conflicts) has fitness = 1.0
- More conflicts → lower fitness → less likely to survive

### Key Genetic Operations

| Operation | Mathematical Description | Purpose |
|-----------|-------------------------|---------|
| **Selection** | Tournament of size k: Select max(fitness) from random k individuals | Preferentially choose fitter parents |
| **Crossover** | Uniform crossover with p=0.5: Gene from parent A or B | Combine successful traits from two parents |
| **Mutation** | With probability p=0.05: Replace gene with random valid gene | Introduce diversity, escape local optima |
| **Elitism** | Preserve top 2 schedules unchanged | Prevent loss of best solutions |

### Discrete Mathematics in Genetic Operators

**Tournament Selection** uses concepts from:
- **Combinatorics**: Selecting k individuals from n (C(n,k) possibilities)
- **Probability**: Each individual has p(selection) proportional to relative fitness

**Crossover** applies:
- **Boolean Algebra**: Each gene position uses random boolean to decide parent
- **Permutations**: Creating new arrangements from existing ones

**Mutation** employs:
- **Probability Distributions**: Bernoulli trials with p=0.05 for each gene
- **Random Sampling**: Uniform selection from valid domain values

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

### Constraints as Logical Predicates (Discrete Mathematics)

The constraints can be formally expressed using **predicate logic**, a fundamental concept in discrete mathematics:

**Hard Constraints (must be satisfied for a valid solution):**

```
∀ c₁, c₂ ∈ Classes, c₁ ≠ c₂:
    ¬(section(c₁) = section(c₂) ∧ time(c₁) = time(c₂))
    // A section cannot have two different classes at the same time
    
∀ c₁, c₂ ∈ Classes, c₁ ≠ c₂:
    ¬(room(c₁) = room(c₂) ∧ time(c₁) = time(c₂))
    // A room cannot host two different classes at the same time
    
∀ c₁, c₂ ∈ Classes, c₁ ≠ c₂:
    ¬(instructor(c₁) = instructor(c₂) ∧ time(c₁) = time(c₂))
    // An instructor cannot teach two different classes at the same time

∀ c ∈ Classes:
    capacity(room(c)) ≥ students(course(c))
    // Room capacity must accommodate enrolled students
```

**Conflict Detection as Boolean Satisfiability:**

The fitness function essentially counts **unsatisfied constraints**, transforming this into a weighted MAX-SAT problem:

```
minimize: Σ violation(constraint_i)
subject to: all hard constraints should have violation = 0
```

## 📐 Algorithm Complexity & Performance Analysis

### Time Complexity

| Phase | Complexity | Description |
|-------|------------|-------------|
| Initialization | O(P × n) | Create P random schedules with n classes each |
| Fitness Evaluation | O(n²) | Compare all pairs of classes for conflicts |
| Selection | O(P × k) | Tournament selection of size k, P times |
| Crossover | O(P × n) | Create P offspring with n genes each |
| Mutation | O(P × n) | Potentially mutate each gene |
| **Per Generation** | **O(P × n²)** | Dominated by fitness evaluation |
| **Total Algorithm** | **O(G × P × n²)** | G generations |

### Space Complexity

| Component | Complexity | Description |
|-----------|------------|-------------|
| Population | O(P × n) | Store P schedules with n classes |
| Auxiliary | O(n) | Temporary storage during operations |
| **Total** | **O(P × n)** | Linear in population and problem size |

### Convergence Properties

The genetic algorithm exhibits typical **stochastic optimization** behavior:

- **Exploration vs. Exploitation**: Mutation rate (5%) balances exploring new solutions vs. refining existing ones
- **Elitism**: Preserving 2 best schedules ensures **monotonic improvement** of best fitness
- **Tournament Selection**: Creates **selection pressure** proportional to tournament size

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

## 📚 Further Reading: Discrete Mathematics & Algorithms

For those interested in exploring the theoretical foundations of this project:

### Discrete Mathematics Topics
- **Constraint Satisfaction Problems (CSP)**: The mathematical framework for problems with discrete variables and constraints
- **Graph Theory**: Understanding scheduling as graph coloring problems
- **Combinatorics**: Counting and enumerating possible schedules
- **Predicate Logic**: Formal specification of constraints
- **Set Theory**: Modeling domains, relations, and functions in scheduling

### Algorithm Topics
- **Genetic Algorithms**: Holland's foundational work on evolutionary computation
- **Metaheuristics**: Broader class of optimization algorithms including simulated annealing, tabu search
- **NP-Completeness**: Understanding why certain problems require heuristic approaches
- **Approximation Algorithms**: Theoretical guarantees for near-optimal solutions

### Related Problems
- **Graph Coloring Problem**: Assigning colors to vertices with constraints
- **Bin Packing Problem**: Fitting items into containers optimally
- **Job Shop Scheduling**: Scheduling jobs on machines with precedence constraints
- **Vehicle Routing Problem**: Another classical combinatorial optimization problem

## 🙏 Acknowledgments

- **Genetic Algorithm Theory**: Based on evolutionary computation principles pioneered by John Holland
- **Discrete Mathematics**: Constraint satisfaction and combinatorial optimization foundations
- **Graph Theory**: Connections to graph coloring problems established by researchers in scheduling theory
- Django framework for rapid web development
- Bootstrap for responsive UI design

