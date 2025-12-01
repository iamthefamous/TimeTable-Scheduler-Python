"""
Django management command to populate sample data for timetable generation.
This creates instructors, rooms, meeting times, courses, departments, and sections
required to run the timetable scheduler.

The data represents a realistic university scenario with multiple departments,
specialized instructors, varied room types, and comprehensive course offerings.
"""
from django.core.management.base import BaseCommand
from SchedulerApp.models import Instructor, Room, MeetingTime, Course, Department, Section


class Command(BaseCommand):
    help = 'Populate the database with sample data for timetable generation'

    def handle(self, *args, **options):
        self.stdout.write('Populating sample data...')

        # Create Instructors - Diverse faculty with different specializations
        instructors_data = [
            # Computer Science Faculty
            ('I001', 'Dr. Emily Chen'),
            ('I002', 'Prof. James Wilson'),
            ('I003', 'Dr. Sarah Martinez'),
            ('I004', 'Prof. Michael Thompson'),
            # Mathematics Faculty
            ('I005', 'Dr. Robert Anderson'),
            ('I006', 'Prof. Lisa Patel'),
            # Physics Faculty
            ('I007', 'Dr. David Kim'),
            ('I008', 'Prof. Jennifer White'),
            # Electrical Engineering Faculty
            ('I009', 'Dr. Christopher Lee'),
            ('I010', 'Prof. Amanda Garcia'),
            # Business Faculty
            ('I011', 'Dr. William Taylor'),
            ('I012', 'Prof. Michelle Brown'),
        ]

        instructors = {}
        for uid, name in instructors_data:
            instructor, created = Instructor.objects.get_or_create(
                uid=uid,
                defaults={'name': name}
            )
            instructors[uid] = instructor
            if created:
                self.stdout.write(f'  Created instructor: {name}')

        # Create Rooms - Varied room types with different capacities
        rooms_data = [
            # Large Lecture Halls
            ('LH101', 120),
            ('LH102', 100),
            # Medium Classrooms
            ('CR201', 50),
            ('CR202', 45),
            ('CR203', 40),
            # Small Seminar Rooms
            ('SR301', 25),
            ('SR302', 25),
            # Computer Labs
            ('LAB01', 35),
            ('LAB02', 30),
            # Physics/Engineering Labs
            ('LAB03', 25),
        ]

        for r_number, capacity in rooms_data:
            room, created = Room.objects.get_or_create(
                r_number=r_number,
                defaults={'seating_capacity': capacity}
            )
            if created:
                self.stdout.write(f'  Created room: {r_number} (capacity: {capacity})')

        # Create Meeting Times - Standard academic time slots
        time_slots = [
            ('8:45 - 9:45', 'Monday'),
            ('10:00 - 11:00', 'Monday'),
            ('11:00 - 12:00', 'Monday'),
            ('1:00 - 2:00', 'Monday'),
            ('2:15 - 3:15', 'Monday'),
            ('8:45 - 9:45', 'Tuesday'),
            ('10:00 - 11:00', 'Tuesday'),
            ('11:00 - 12:00', 'Tuesday'),
            ('1:00 - 2:00', 'Tuesday'),
            ('2:15 - 3:15', 'Tuesday'),
            ('8:45 - 9:45', 'Wednesday'),
            ('10:00 - 11:00', 'Wednesday'),
            ('11:00 - 12:00', 'Wednesday'),
            ('1:00 - 2:00', 'Wednesday'),
            ('2:15 - 3:15', 'Wednesday'),
            ('8:45 - 9:45', 'Thursday'),
            ('10:00 - 11:00', 'Thursday'),
            ('11:00 - 12:00', 'Thursday'),
            ('1:00 - 2:00', 'Thursday'),
            ('2:15 - 3:15', 'Thursday'),
            ('8:45 - 9:45', 'Friday'),
            ('10:00 - 11:00', 'Friday'),
            ('11:00 - 12:00', 'Friday'),
            ('1:00 - 2:00', 'Friday'),
            ('2:15 - 3:15', 'Friday'),
        ]

        meeting_times = {}
        for i, (time, day) in enumerate(time_slots, 1):
            pid = f'MT{i:02d}'
            mt, created = MeetingTime.objects.get_or_create(
                pid=pid,
                defaults={'time': time, 'day': day}
            )
            meeting_times[pid] = mt
            if created:
                self.stdout.write(f'  Created meeting time: {pid} - {day} {time}')

        # Create Courses - Comprehensive curriculum across departments
        courses_data = [
            # Computer Science Courses
            ('CS101', 'Introduction to Programming', '45', ['I001', 'I002']),
            ('CS102', 'Data Structures', '40', ['I001', 'I003']),
            ('CS201', 'Algorithms', '35', ['I002', 'I003']),
            ('CS202', 'Database Systems', '40', ['I003', 'I004']),
            ('CS301', 'Software Engineering', '30', ['I004', 'I002']),
            ('CS302', 'Computer Networks', '35', ['I001', 'I004']),
            ('CS401', 'Machine Learning', '25', ['I003', 'I001']),
            # Mathematics Courses
            ('MA101', 'Calculus I', '80', ['I005', 'I006']),
            ('MA102', 'Linear Algebra', '60', ['I005', 'I006']),
            ('MA201', 'Differential Equations', '45', ['I006', 'I005']),
            ('MA301', 'Probability & Statistics', '50', ['I005', 'I006']),
            # Physics Courses
            ('PH101', 'Physics I: Mechanics', '90', ['I007', 'I008']),
            ('PH102', 'Physics II: E&M', '70', ['I008', 'I007']),
            ('PH201', 'Modern Physics', '35', ['I007', 'I008']),
            # Electrical Engineering Courses
            ('EE101', 'Circuit Analysis', '50', ['I009', 'I010']),
            ('EE201', 'Electronics', '40', ['I010', 'I009']),
            ('EE301', 'Digital Systems', '35', ['I009', 'I010']),
            # Business Courses
            ('BA101', 'Principles of Management', '80', ['I011', 'I012']),
            ('BA201', 'Marketing Fundamentals', '60', ['I012', 'I011']),
            ('BA301', 'Business Analytics', '40', ['I011', 'I012']),
        ]

        courses = {}
        for course_number, course_name, max_students, instructor_uids in courses_data:
            course, created = Course.objects.get_or_create(
                course_number=course_number,
                defaults={'course_name': course_name, 'max_numb_students': max_students}
            )
            if created:
                for uid in instructor_uids:
                    course.instructors.add(instructors[uid])
                self.stdout.write(f'  Created course: {course_name}')
            elif not course.instructors.exists():
                for uid in instructor_uids:
                    course.instructors.add(instructors[uid])
                self.stdout.write(f'  Updated course instructors: {course_name}')
            courses[course_number] = course

        # Create Departments - Realistic university structure
        departments_data = [
            ('Computer Science', ['CS101', 'CS102', 'CS201', 'CS202', 'CS301', 'CS302', 'CS401']),
            ('Mathematics', ['MA101', 'MA102', 'MA201', 'MA301']),
            ('Physics', ['PH101', 'PH102', 'PH201']),
            ('Electrical Engineering', ['EE101', 'EE201', 'EE301']),
            ('Business Administration', ['BA101', 'BA201', 'BA301']),
        ]

        departments = {}
        for dept_name, course_numbers in departments_data:
            dept, created = Department.objects.get_or_create(
                dept_name=dept_name
            )
            if created:
                for course_num in course_numbers:
                    dept.courses.add(courses[course_num])
                self.stdout.write(f'  Created department: {dept_name}')
            elif not dept.courses.exists():
                for course_num in course_numbers:
                    dept.courses.add(courses[course_num])
                self.stdout.write(f'  Updated department courses: {dept_name}')
            departments[dept_name] = dept

        # Create Sections - Multiple sections per department with varied class loads
        sections_data = [
            # Computer Science Sections
            ('CS-1A', 'Computer Science', 7),
            ('CS-1B', 'Computer Science', 7),
            ('CS-2A', 'Computer Science', 6),
            # Mathematics Sections
            ('MA-1A', 'Mathematics', 4),
            ('MA-1B', 'Mathematics', 4),
            # Physics Sections
            ('PH-1A', 'Physics', 3),
            # Electrical Engineering Sections
            ('EE-1A', 'Electrical Engineering', 3),
            ('EE-2A', 'Electrical Engineering', 3),
            # Business Sections
            ('BA-1A', 'Business Administration', 3),
            ('BA-1B', 'Business Administration', 3),
        ]

        for section_id, dept_name, num_classes in sections_data:
            section, created = Section.objects.get_or_create(
                section_id=section_id,
                defaults={
                    'department': departments[dept_name],
                    'num_class_in_week': num_classes
                }
            )
            if created:
                self.stdout.write(f'  Created section: {section_id} ({dept_name})')

        self.stdout.write(self.style.SUCCESS('\nSample data populated successfully!'))
        self.stdout.write(self.style.SUCCESS('You can now generate a timetable.'))
